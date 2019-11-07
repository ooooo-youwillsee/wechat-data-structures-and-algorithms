# coding=utf-8

class Solution:

    def solution(self, n):
        maxLen = 0
        max = 0
        for i in range(n, 100000, -1):
            c = 1
            j = i
            while j > 1:
                if j & 1:
                    j = 3 * j + 1
                else:
                    j >>= 1
                c += 1
            if c > maxLen:
                maxLen = c
                max = i
        return maxLen, max


if __name__ == '__main__':
    print(Solution().solution(1000000))
