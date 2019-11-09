# coding=utf-8


class Solution:

    def solution(self, n):
        res = '1' + '0' * n

        res = int(res, 2)

        sum = 0
        while res:
            sum += res % 10
            res //= 10

        return sum

    def help(self, x, n):
        if n == 0:
            return 1
        if n & 1:
            return x * self.help(x, n - 1)
        return self.help(x * x, n // 2)


if __name__ == '__main__':
    s = Solution()
    print(s.solution(1000))
