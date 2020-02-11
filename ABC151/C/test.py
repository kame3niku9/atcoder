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
        input = """2 5
1 WA
1 AC
2 WA
2 AC
2 WA"""
        output = """2 2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """100000 3
7777 AC
7777 AC
7777 AC"""
        output = """1 0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6 0"""
        output = """0 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()