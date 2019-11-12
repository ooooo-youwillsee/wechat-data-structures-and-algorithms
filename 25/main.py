# coding=utf-8

class Solution:

    def solution(self, n):
        n = n // 2 + 1
        if n == 1:
            return 1
        sum = 0
        for i in range(2, n + 1):
            sum += pow(2 * (i - 1) + 1, 2)
        x = 0
        for i in range(2, n + 1):
            x += 6 * (i - 1)
        return sum * 4 - x * 2 + 1


if __name__ == '__main__':
    s = Solution()
    print(s.solution(1001))
