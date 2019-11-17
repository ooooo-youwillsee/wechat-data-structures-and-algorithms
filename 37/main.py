# coding=utf-8

class Solution:

    def solution(self):
        for i in range(987654321, 1, -1):
            s = str(i)
            if len(set(list(s))) == len(s) and self.isPrime(i):
                return i

        return 0

    def isFullNum(self, n):
        s = sorted(str(n))
        if '0' in s:
            return False
        for i in range(0, len(s)):
            if i != int(s[i]) - 1:
                return False
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
    # print(s.isFullNum(12345))
    print(s.solution())
