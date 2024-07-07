import os
from pathlib import Path
import shutil
import argparse

from filehandler import write_list_to_file, write_dict_to_filenames


def get_xor_of_list(data_list): return [data_list[0] ^ 0] + [
    data_list[i] ^ data_list[i-1] for i in range(1, len(data_list))]


def get_transformed_data(filename: os.PathLike, n: int) -> dict:
    """Create a dictionary containing the first n lines of a binary file.
    Read data and create n chunks of data.
    arguments:
    -----------
        filename: path to the input file
        n: number of chunks to be created

    returns:
    -----------
        dictionary containing the chunk number as key and the chunk data as value.
    """
    filename = Path(filename)
    (filename.parent / filename.stem).mkdir(exist_ok=True, parents=True)
    data = [int(i.strip()) for i in Path(filename).read_text().splitlines()]
    data_xor = get_xor_of_list(data)
    write_list_to_file(data_xor, filename.parent /
                       filename.stem / f"{filename.stem}_c.txt")
    transformed_data_dict = {i: data[i:len(data):n] for i in range(0, n)}
    return transformed_data_dict


def get_sum_of_elements_of_dict(data_dict, idx): return sum(
    [data_dict[k][idx] for k in data_dict.keys()])


def process_binary_data(filename: os.PathLike, n: int, output_filenames_list: list = []) -> None:
    """Create a dictionary containing the first n lines of a binary file.
    Read data and create n chunks of data.
    arguments:
    -----------
        filename: path to the input file
        n: number of chunks to be created

    returns:
    -----------
        dictionary containing the chunk number as key and the chunk data as value.
    """
    # transform data from single column to m x n
    transformed_data_dict = get_transformed_data(filename, n)
    # xor of dict values and shifted by 1 values.
    data_xor_dict = {f'xor_{k}': get_xor_of_list(
        v) for k, v in transformed_data_dict.items()}

    # sum- data_xor_dict[k][i] for k = 0, n-1, sum of values of dict for a given index
    data_xor_sum_list = [get_sum_of_elements_of_dict(
        data_xor_dict, idx) for idx in range(len(list(transformed_data_dict.values())[0]))]

    # transform xor data to single column
    transformed_data_xor_list = [
        val for vlist in data_xor_dict.values() for val in vlist]

    # create files
    output_data_path = filename.parent / filename.stem
    output_data_path.mkdir(exist_ok=True, parents=True)
    _default_output_files_list = [
        output_data_path / f"{filename.stem}_{k}.txt" for k in range(n)]
    output_filenames_list = output_filenames_list if output_filenames_list else _default_output_files_list

    write_dict_to_filenames(
        data_xor_dict, path=output_data_path, filenames_list=output_filenames_list[:n])

    write_list_to_file(data_xor_sum_list,
                       filename=output_data_path / f"{filename.stem}_a.txt")
    write_list_to_file(transformed_data_xor_list,
                       filename=output_data_path / f"{filename.stem}_b.txt")


def main():
    """Get user input
    usecases

    Example 1:
    >> python -m formatbin <filename> <n> <output_filenames_list>

    Example 2
    >> python -m formatbin input.txt 8 output1.txt output2.txt ... output8.txt
    """
    # read arguments- filename, n and n list of filenames for output
    parser = argparse.ArgumentParser('praocess binary data in a file')
    parser.add_argument("-f", "--filename", type=Path,
                        help="Path to the input file")
    parser.add_argument("-n", "--nbit", type=int, default=8,
                        help="Number of chunks to create")
    parser.add_argument("-o", "--outfilenames", type=Path, nargs="+", default=[],
                        help="Paths to output files")
    # help argument
    # parser.add_argument("-h", "--help", action="help",
    #                     help="Show this help message and exit")
    # optional argument- n
    # parser.add_argument("--n", type=int, help="Number of files to create")
    args = parser.parse_args()
    filename = args.filename
    n = args.nbit
    filenames = args.outfilenames
    # process binary file
    shutil.rmtree(filename.parent / filename.stem, ignore_errors=True)
    data = process_binary_data(filename, n)
    # create output files
    # create_files(data, filenames)
    # print success message
    print("Files created successfully")
    print(f"Output files: {filenames}")


# test function
if __name__ == "__main__":
    # import random
    # import tabulate
    # import pandas as pd
    # import shutil

    # n = 8

    # test_data_path = Path(os.getcwd()) / "test_data"
    # # shutil.rmtree(test_data_path, ignore_errors=True)
    # test_data_path.mkdir(exist_ok=True, parents=True)
    # data = '\n'.join([str(random.randint(0, 1)) for i in range(1024)])
    # # data = '\n'.join([str(i) for i in range(1024)])
    # (test_data_path / 'result.txt').write_text(data)
    # # assert list(read_file(test_data_path / 'input.txt')) == data.split('\n')
    # filename = test_data_path / 'result.txt'
    # data_dict = get_transformed_data(filename, 8)

    # # print(tabulate.tabulate(data_dict.values(), headers=list(data_dict.keys()), tablefmt='outer-rounded'))
    # df = pd.DataFrame(data_dict)

    # print(df.columns)
    # process_binary_data(filename, 8)

    main()
