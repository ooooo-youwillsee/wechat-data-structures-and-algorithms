# coding=utf-8

class Solution:

    def solution(self, n):
        max = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                res = self.help(i, j)
                if res > max:
                    max = res
        return max

    def help(self, a, b):
        n = pow(a, b)
        sum = 0
        while n:
            sum += n % 10
            n //= 10
        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.solution(100))
