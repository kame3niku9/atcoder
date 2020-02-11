import sys
from io import StringIO
import unittest

from main import resolve

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
        input = """9 45000"""
        output = """0 9 0"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """20 196000"""
        output = """-1 -1 -1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1000 1234000"""
        output = """2 54 944"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """2000 20000000"""
        output = """2000 0 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()