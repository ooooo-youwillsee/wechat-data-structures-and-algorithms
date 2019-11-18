# coding=utf-8

import sys


class Solution:

    def solution(self):
        k = 166
        m = 286
        for i in range(144, sys.maxsize):
            h = i * (i << 1) - 1
            p = 0
            match = True
            while p < h:
                p = (k * (3 * k - 1)) >> 1
                if p > h:
                    match = False
                    break
                k += 1
            if match:
                t = 0
                while t < h:
                    t = m * (m << 1 - 1)
                    if t == h:
                        return t
                    m += 1

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.solution())
