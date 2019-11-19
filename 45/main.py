# coding=utf-8

import math
import sys


class Solution:

    def solution(self, n):
        primes = [2]
        for i in range(3, n, 2):
            if self.isPrime(i):
                primes.append(i)
        print('primes: ', primes)

        max, _i = 0, 0
        for i in range(3, n, 2):
            if not self.isPrime(i):
                continue
            num = self.addSum(i, primes, 0, False)
            if max < num:
                max, _i = num, i

        return _i

    def addSum(self, x, list, index, exit):
        if x < 0:
            if exit:
                return -sys.maxsize
            return -self.addSum(-x, list, 0, True)
        digit = list[index]
        if x == digit:
            return 1
        return 1 + self.addSum(x - digit, list, index + 1, exit)

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
    print(s.solution(1000000))
