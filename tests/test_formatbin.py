import os
from pathlib import Path
import shutil
import unittest

from formatbin import process_binary, create_files


class TestFormatBin(unittest.TestCase):
    def setUp(self):
        self.n = 8
        self.filename = "input.txt"
        self.filename = Path(self.filename)
        self.results_dir = self.filename.stem

    def tearDown(self):
        if os.path.exists(self.results_dir):
            shutil.rmtree(self.results_dir)

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
        data = process_binary(self.filename,  self.n)
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
