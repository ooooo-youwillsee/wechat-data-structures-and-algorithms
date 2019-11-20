# coding=utf-8


class Solution:

    def solution(self, n):
        sum = 1
        while n:
            sum *= n
            n -= 1
        res = 0
        while sum:
            res += sum % 10
            sum //= 10
        print(res)


if __name__ == '__main__':
    s = Solution()
    s.solution(100)
