import os
from pathlib import Path

def write_list_to_file(data_list, filename): return filename.write_text(
    "\n".join([str(val) for val in data_list]))


def write_dict_to_filenames(data: dict, path: os.PathLike = None, filenames_list: str = []) -> None:
    """Create output files from the data dictionary.
    arguments:
    -----------
        data: dictionary containing the chunk number as key and the chunk data as value.
        path: path to the output directory. If not provided, the current directory is used.
    """
    path = Path(path) if path is not None else Path()
    # filename = filenames_list[0] if filenames_list is not None else 'input.txt'
    filename = filenames_list[0] if filenames_list else 'input.txt'
    filename_stem = Path(filename).stem if filename is not None else "input"

    for k in data.keys():
        filename = path / f"{filename_stem}_{k}.txt"
        write_list_to_file(data[k], filename=filename)


def create_files(data: dict, path: os.PathLike = None, filename: str = None) -> None:
    """Create output files from the data dictionary.
    arguments:
    -----------
        data: dictionary containing the chunk number as key and the chunk data as value.
        path: path to the output directory. If not provided, the current directory is used.
    """
    filename_stem = Path(filename).stem if filename is not None else "input"
    if path is None:
        path = Path(os.getcwd())
    else:
        path = Path(path)
    path = path / filename_stem
    path.mkdir(parents=True, exist_ok=True)
    for k in data.keys():
        filename = path / f"output_{k}.txt"
        write_list_to_file(data[k], filename=filename)
