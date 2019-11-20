# coding=utf-8

import sys


class Solution:

    def solution(self):
        res = 1
        c = 0
        s = ''
        nums = [1, 10, 100, 1000, 10000, 100000, 1000000]
        for i in range(1, sys.maxsize):
            ss = str(i)
            c += len(ss)
            s += ss
            if c > 1000000:
                break
        for i in nums:
            res *= int(s[i - 1])

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.solution())
