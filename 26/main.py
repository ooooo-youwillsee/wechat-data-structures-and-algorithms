# coding=utf-8

class Solution:

    def solution(self, a, b):
        s = set()
        for i in range(a, b + 1):
            for j in range(a, b + 1):
                s.add(pow(i, j))
        return len(s)


if __name__ == '__main__':
    s = Solution()
    print(s.solution(2, 100))
