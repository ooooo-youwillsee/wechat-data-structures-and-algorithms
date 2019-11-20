# coding=utf-8

class Solution:

    def solution(self, p):
        m = {}
        for a in range(1, 500):
            for b in range(1, 500):
                for c in range(1, 500):
                    if a * a + b * b == c * c and a + b + c <= p:
                        num = a + b + c
                        m[num] = m[num] + 1 if num in m else 1
        maxC = 0
        max = 0
        for (k, v) in m.items():
            if v > maxC:
                maxC = v
                max = k
        return max


if __name__ == '__main__':
    s = Solution()
    print(s.solution(1000))
