# coding=utf-8

class Solution:

    def solution(self, n, target):
        c = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                res = self.help(i) / (self.help(j) * self.help(i - j))
                if res > target:
                    c += 1
        return c

    def help(self, n):
        sum = 1
        while n:
            sum *= n
            n -= 1
        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.solution(100, 1000000))
