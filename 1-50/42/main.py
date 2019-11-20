# coding=utf-8

import math
import sys


class Solution:

    def solution(self):
        for i in range(646, sys.maxsize):
            if self.distinctPrimes(i) and self.distinctPrimes(i + 1) \
                    and self.distinctPrimes(i + 2) and self.distinctPrimes(i + 3):
                return i
        return -1

    def distinctPrimes(self, n):
        s = set()
        i = 2
        while not self.isPrime(n):
            if not n % i:
                s.add(i)
                if len(s) > 3:
                    return False
                n //= i
                i = 2
            else:
                i += 1
        s.add(n)
        if len(s) != 4:
            return False
        return True

    def isPrime(self, n):
        if n == 2:
            return True
        if not n & 1 or n == 1:
            return False
        max = int(math.sqrt(n))
        for i in range(3, max + 1):
            if not n % i:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.solution())
