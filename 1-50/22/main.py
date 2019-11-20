# coding=utf-8

class Solution:

    def solution(self, num):
        n1 = n2 = 1
        n = 0
        i = 2
        while len(str(n)) < num:
            i += 1
            n = n1 + n2
            n1, n2 = n2, n
        return i


if __name__ == '__main__':
    s = Solution()
    print(s.solution(1000))
