import os
from pathlib import Path
import shutil
import unittest
import pytest
from formatbin import process_binary, create_files


class TestFormatBin(unittest.TestCase):
    def setUp(self):
        self.n = 8
        self.work_dir = Path(os.getcwd()) / 'test_data'
        self.filename = "input.txt"
        self.filename = Path(os.getcwd()) / 'test_data' / self.filename
        self.results_dir = self.filename.stem

    def tearDown(self):
        if os.path.exists(self.results_dir):
            shutil.rmtree(self.results_dir)

    @pytest.mark.skip(reason="Not testing this yet")
    def test_create_files(self):
        data = process_binary(self.filename, self.n)
        create_files(data, self.results_dir)
        self.assertTrue(self.results_dir.is_dir())
        for i in range(n):
            file_suffix = f'0{i}' if i < 10 else f'{i}'
            self.assertTrue(
                Path(self.results_dir, f"input_{file_suffix}.txt").is_file())
        self.assertTrue(self.results_dir.is_dir())

    def test_process_binary(self):
        filedata = [int(i.strip())
                    for i in self.filename.read_text().strip().split('\n')]
        data = process_binary(self.filename,  self.n)
        self.assertTrue(isinstance(data, dict))
        self.assertTrue(len(data) == self.n)
        self.assertTrue(all([isinstance(v, list) for v in data.values()]))
        self.assertTrue(
            all([len(v) == len(filedata)//self.n for v in data.values()]))
        for k, v in data.items():
            self.assertListEqual(v, filedata[k:len(filedata):self.n])


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
