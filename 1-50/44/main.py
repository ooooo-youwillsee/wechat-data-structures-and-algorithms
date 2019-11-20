# coding=utf-8

import math


class Solution:

    def solution(self):
        res = []
        for i in range(1000, 10000):
            if self.isPrime(i):
                for j in range(i + 1, 10000):
                    k = j - i + j
                    if k < 10000 and sorted(str(i)) == sorted(str(j)) == sorted(str(k)) \
                            and self.isPrime(j) and self.isPrime(k):
                        print(i, j, k)
                        res.append(str(i) + str(j) + str(k))
        return res

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
    print(s.solution()[-1])
