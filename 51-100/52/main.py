# coding=utf-8

import sys
import math


class Solution:

    def solution(self, target):
        count = sys.maxsize
        total = 1  ## 1
        n = 1
        while count / total >= target:
            n += 2
            if count == sys.maxsize:
                count = 0
            a, b, c = pow(n - 1, 2) - (n - 2), pow(n - 1, 2) + 1, pow(n - 1, 2) + n
            total += 4
            if self.isPrime(a):
                count += 1
            if self.isPrime(b):
                count += 1
            if self.isPrime(c):
                count += 1
        return n

    def isPrime(self, n):
        if n == 2:
            return True
        if not n & 1 or n == 1:
            return False
        max = int(math.sqrt(n))
        for i in range(3, max + 1, 2):
            if not n % i:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.solution(0.1))
