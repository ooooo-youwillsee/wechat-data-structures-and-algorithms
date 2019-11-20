# coding=utf-8

class Solution:

    def solution(self, n):
        sum = 0
        for i in range(1, n + 1):
            sum += pow(i, i)
        return sum


if __name__ == '__main__':
    s = Solution()
    res = s.solution(1000)
    print(res)
    print(str(res)[-10:])
