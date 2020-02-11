from main import resolve

import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """25"""
        output = """17"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """100"""
        output = """108"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """2020"""
        output = """40812"""
        self.assertIO(input, output)
    def test_入力例_5(self):
        input = """200000"""
        output = """400000008"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()