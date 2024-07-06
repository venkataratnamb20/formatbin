import os
from pathlib import Path
import argparse


def process_binary(filename: os.PathLike, n: int) -> dict:
    raise NotImplementedError("process_binary function is not implemented")
    return dict()


def create_files(data: dict, path: os.PathLike = None) -> None:
    raise NotImplementedError("create_files function is not implemented")


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
