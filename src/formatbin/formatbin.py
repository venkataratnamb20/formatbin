import os
from pathlib import Path
import argparse


def process_binary(filename: os.PathLike, n: int) -> dict:
    """Create a dictionary containing the first n lines of a binary file.
    Read data and create n chunks of data.
    arguments:
    -----------
        filename: path to the input file
        n: number of chunks to create

    returns:
    -----------
        dictionary containing the chunk number as key and the chunk data as value.
    """
    data = [int(i.strip()) for i in Path(filename).read_text().splitlines()]
    data_dict = {i: data[i:len(data):n] for i in range(0, n)}
    return data_dict


def create_files(data: dict, path: os.PathLike = None) -> None:
    """Create output files from the data dictionary.
    arguments:
    -----------
        data: dictionary containing the chunk number as key and the chunk data as value.
        path: path to the output directory. If not provided, the current directory is used.
    """
    if path is None:
        path = Path(os.getcwd())
    else:
        path = Path(path)
    for i in range(len(data)):
        with open(path / f"output_{i}.txt", "w") as f:
            f.writelines(data[i])


def main():
    # read arguments- filename, n and n list of filenames for output
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=Path, help="Path to the binary file")
    parser.add_argument("n", type=int, help="Number of files to create")
    parser.add_argument("filenames", type=Path, nargs="+",
                        help="Paths to output files")
    args = parser.parse_args()
    filename = args.filename
    n = args.n
    filenames = args.filenames
    # process binary file
    data = process_binary(filename, n)
    # create output files
    create_files(data, filenames)
    # print success message
    print("Files created successfully")
    print(f"Output files: {filenames}")


if __name__ == "__main__":
    main()
