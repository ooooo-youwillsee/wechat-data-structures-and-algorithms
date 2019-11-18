# coding=utf-8

import sys
import math


class Solution:

    def solution(self):
        for i in range(3, sys.maxsize, 2):
            if not self.composite(i):
                continue
            goldbach = False
            for j in range(2, i - 1):
                if self.isPrime(j) and 1 & (i - j) == 0:
                    square = (i - j) >> 1
                    sqr = int(math.sqrt(square))
                    if sqr * sqr == square:
                        goldbach = True
            if not goldbach:
                return i
        return -1

    def composite(self, n):
        if n == 2:
            return False
        max = int(math.sqrt(n))
        for i in range(3, max + 1, 2):
            if not n % i:
                return True

    def isPrime(self, n):
        if n == 2:
            return True
        if not n & 1 or n == 1:
            return False
        for i in range(3, n):
            if not n % i:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.solution())
