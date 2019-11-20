# coding=utf-8

import sys


class Solution:

    def solution(self):
        for i in range(1, sys.maxsize):
            if self.calc(i) == self.calc(2 * i) == self.calc(3 * i) == self.calc(4 * i) \
                    == self.calc(5 * i) == self.calc(6 * i):
                return i
        return -1

    def calc(self, n):
        s = set()
        while n:
            s.add(n % 10)
            n //= 10

        return s


if __name__ == '__main__':
    s = Solution()
    print(s.solution())
