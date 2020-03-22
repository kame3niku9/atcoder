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
        input = """3 5 4
11100
10001
00111"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 5 8
11100
10001
00111"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """4 10 4
1110010010
1000101110
0011101001
1101000111"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()