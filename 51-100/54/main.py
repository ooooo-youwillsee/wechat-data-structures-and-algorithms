# coding=utf-8

import sys
import math


class Solution:

    def solution(self):
        list = []
        for i in range(2, sys.maxsize):
            if self.isPrime(i):
                list.append(i)
            if len(list) > 3000:
                break

        sum = sys.maxsize

        for i in range(0, len(list)):
            _i = list[i]
            for j in range(i + 1, len(list)):
                _j = list[j]
                if self.changeBit(_j, _i):
                    continue
                for k in range(j + 1, len(list)):
                    _k = list[k]
                    if self.changeBit(_k, _i) or self.changeBit(_k, _j):
                        continue
                    for l in range(k + 1, len(list)):
                        _l = list[l]
                        if self.changeBit(_l, _i) or self.changeBit(_l, _k) or self.changeBit(_l, _j):
                            continue
                        for m in range(l + 1, len(list)):
                            _m = list[m]
                            if self.changeBit(_m, _l) or self.changeBit(_m, _k) \
                                    or self.changeBit(_m,_i) or self.changeBit(_m, _j):
                                continue
                            else:
                                min = _i + _j + _k + _l + _m
                                if sum > min:
                                    sum = min
        return sum

    def changeBit(self, _i, _j):
        return not self.isPrime(_i + self.fold(_j, self.bitInt(_i))) or not self.isPrime(
            _j + self.fold(_i, self.bitInt(_j)))

    def bitInt(self, n):
        if n == 0:
            return 1
        sum = 0
        while n:
            n //= 10
            sum += 1
        return sum

    def fold(self, num, count):
        while num:
            num *= 10
            count -= 1
        return num

    def isPrime(self, n):
        if n == 2:
            return True
        if not n & 1 or n == 1:
            return False
        max = int(math.sqrt(n))
        for i in range(3, max + 1, 2):
            if not n % i:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.solution())
