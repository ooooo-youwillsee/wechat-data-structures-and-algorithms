# coding=utf-8

import sys, math


def solution(n):
    sum = 0
    for i in range(1, sys.maxsize):
        sum += i
        c = 0
        for j in range(1, int(math.sqrt(sum)) + 1):
            if not sum % j:
                c += 1
            if c is n:
                return sum
    return -1


if __name__ == '__main__':
    print(solution(500))
