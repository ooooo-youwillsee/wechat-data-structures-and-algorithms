# coding=utf-8

import time


class Solution:

    def solution(self):
        maxCount = 0
        max = 0
        for a in range(-999, 1001):
            for b in range(-999, 1001):
                count = 0
                for n in range(0, 1000):
                    sum = n * n + a * n + b
                    if sum < 0 or not self.isPrime(sum):
                        break
                    count += 1
                if count > maxCount:
                    maxCount = count
                    max = a * b
        return max

    def isPrime(self, n):
        if n == 2:
            return True
        if not n & 1:
            return False
        for i in range(2, n):
            if not n % i:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.solution())
