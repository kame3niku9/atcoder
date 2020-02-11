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
        input = """3
dwango 2
sixth 5
prelims 25
dwango"""
        output = """30"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1
abcde 1000
abcde"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """15
ypnxn 279
kgjgwx 464
qquhuwq 327
rxing 549
pmuduhznoaqu 832
dagktgdarveusju 595
wunfagppcoi 200
dhavrncwfw 720
jpcmigg 658
wrczqxycivdqn 639
mcmkkbnjfeod 992
htqvkgkbhtytsz 130
twflegsjz 467
dswxxrxuzzfhkp 989
szfwtzfpnscgue 958
pmuduhznoaqu"""
        output = """6348"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()