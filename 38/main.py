# coding=utf-8

import sys


class Solution:

    def solution(self):
        list = []
        minDiff = sys.maxsize
        for i in range(1, 10001):
            list.append(i * (2 * i - 1) >> 1)
        for i in range(0, 10000):
            for j in range(i + 1, 10000):
                min = list[i]
                max = list[j]
                sum = min + max
                if list.count(sum) == 0:
                    continue
                diff = max - min
                if list.count(diff) == 0:
                    continue
                if minDiff > diff:
                    minDiff = diff

        return minDiff


if __name__ == '__main__':
    s = Solution()
    print(s.solution())
