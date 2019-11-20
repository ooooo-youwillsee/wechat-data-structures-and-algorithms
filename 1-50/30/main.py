# coding=utf-8

"""
    no resolve
"""


class Solution:

    def solution(self):
        m = {}
        for i in range(10, 100):
            for j in range(10, 100):
                if i >= j or not j % 10:
                    continue
                # 49/98 = 4/8
                if (i // 10) / (j % 10) == i / j:
                    if i // 10 in m:
                        m[i // 10].append(j % 10)
                    else:
                        m[i // 10] = [j % 10]
        #  分子
        sumU = 1
        #  分母
        sumB = 1
        for (k, v) in m.items():
            for x in v:
                sumU *= k
                sumB *= x
        while True:
            flag = True
            for i in range(sumU, 2, -1):
                if not sumU % i and not sumB % i:
                    flag = False
                    sumU //= i
                    sumB //= i
            if flag:
                break
        return sumB


if __name__ == '__main__':
    s = Solution()
    print(s.solution())
