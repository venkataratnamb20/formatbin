import os
from pathlib import Path
import glob
import shutil
import unittest
import pytest
from formatbin import get_transformed_data, process_binary_data
from formatbin.filehandler import create_files
import random


class TestFormatBin(unittest.TestCase):
    def setUp(self):
        self.n = 8

        # create test data file
        self.test_data_path = Path(os.getcwd()) / "test_data"
        # shutil.rmtree(self.test_data_path, ignore_errors=True)
        self.test_data_path.mkdir(exist_ok=True, parents=True)
        self.filename = self.test_data_path / "result.txt"
        self.data_length = 1024
        data = "\n".join([str(random.randint(0, 1)) for i in range(self.data_length)])
        # data = '\n'.join([str(i) for i in range(self.data_length)])
        self.filename.write_text(data)

        self.test_data_path = self.filename.stem

    def tearDown(self):
        if os.path.exists(self.test_data_path):
            shutil.rmtree(self.test_data_path)

    @pytest.mark.skip(reason="Not testing this yet")
    def test_create_files(self):
        data = get_transformed_data(self.filename, self.n)
        create_files(data, self.test_data_path)
        self.assertTrue(self.test_data_path.is_dir())
        for i in range(self.n):
            file_suffix = f"0{i}" if i < 10 else f"{i}"
            self.assertTrue(
                Path(self.test_data_path, f"input_{file_suffix}.txt").is_file()
            )
        self.assertTrue(self.test_data_path.is_dir())

    def test_get_transformed_data(self):
        filedata = [
            int(i.strip()) for i in self.filename.read_text().strip().split("\n")
        ]
        data = get_transformed_data(self.filename, self.n)
        self.assertTrue(isinstance(data, dict))
        self.assertTrue(len(data) == self.n)
        self.assertTrue(all([isinstance(v, list) for v in data.values()]))
        self.assertTrue(all([len(v) == len(filedata) // self.n for v in data.values()]))
        for k, v in data.items():
            self.assertListEqual(v, filedata[k : len(filedata) : self.n])

    def test_process_binary_data_file_structure(self):
        results_dir = Path(self.filename.parent / self.filename.stem)
        data = process_binary_data(self.filename, self.n)
        self.assertTrue(data is None)
        # is directory created with filename
        self.assertTrue(results_dir.is_dir())
        # check number of files in the newly created directory is self.n + 3
        self.assertTrue(len(list(results_dir.iterdir())) == self.n + 3)
        # check file names
        for i in range(self.n):
            file_suffix = f"0{i}" if i < 10 else f"{i}"
            self.assertTrue(
                Path(results_dir, f"{self.filename.stem}_{file_suffix}.txt").is_file()
            )
        for suff in list("abc"):
            self.assertTrue(
                Path(results_dir, f"{self.filename.stem}_{suff}.txt").is_file()
            )

    def test_process_binary_data_file_content(self):
        results_dir = Path(self.filename.parent / self.filename.stem)
        data = process_binary_data(self.filename, self.n)
        for file in glob.glob(f"{results_dir}/*"):
            with open(file, "r") as f:
                if file.endswith("_c.txt") or file.endswith("_b.txt"):
                    self.assertEqual(
                        len(f.read().strip().split("\n")), self.data_length
                    )
                else:
                    self.assertEqual(
                        len(f.read().strip().split("\n")), self.data_length // self.n
                    )


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
