# coding=utf-8

import sys


class Solution:

    def solution(self):

        sum = 0
        c = 0
        for i in range(10, sys.maxsize):
            for num in self.getCheckNums(i):
                if not self.isPrime(num):
                    break
            else:
                c += 1
                sum += i
                if c == 11:
                    return sum

        return sum

    def getCheckNums(self, n):
        s = set()
        num = len(str(n)) - 1
        while num:
            s.add(n % pow(10, num))
            s.add(n // pow(10, num))
            num -= 1
        s.add(n)
        return s

    def isPrime(self, n):
        if n == 2:
            return True
        # 确保1不是素数
        if not n & 1 or n == 1:
            return False
        for i in range(3, n):
            if not n % i:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    # print(s.getCheckNums(3797))
    print(s.solution())
