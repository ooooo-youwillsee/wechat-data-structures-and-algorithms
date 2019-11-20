# coding=utf-8

import sys


class Solution:

    def solution(self):
        max = 0
        for i in range(1, 10000):
            product = ''
            for j in range(1, 10):
                product += str(i * j)
                if len(product) > 9:
                    break
                if self.repetition(product):
                    continue
                if len(product) == 9:
                    if max < int(product):
                        max = int(product)
        return max

    def repetition(self, str):
        list = []
        for i in str:
            if i == '0' or i in list:
                return True
            list.append(i)
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.solution())
