# coding=utf-8

import math


def solution(n):
    sum = 0
    for i in range(2, n + 1):
        if isXX(i):
            sum += i

    return sum


def isXX(n):
    if n < 2:
        return False
    if n is 2:
        return True
    if not n & 1:
        return False
    for i in range(3, int(math.sqrt(n)) + 1):
        if not n % i:
            return False
    return True


if __name__ == '__main__':
    print(solution(10))
