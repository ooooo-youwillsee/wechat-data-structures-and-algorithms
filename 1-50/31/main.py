# coding=utf-8

class Solution:

    def solution(self):
        res = 0
        for i in range(10, 999999):
            sum = 0
            mid = i
            while i:
                sum += self.factorial(i % 10)
                i //= 10
            if mid == sum:
                res += mid
        return res

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        sum = 1
        for i in range(2, n + 1):
            sum *= i
        return sum


if __name__ == '__main__':
    s = Solution()
    # print(s.factorial(9))
    print(s.solution())
