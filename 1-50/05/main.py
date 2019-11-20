# coding=utf-8

import sys, math


def solution(n):
    c = 0
    for i in range(2, sys.maxsize):
        if isPrime(i):
            c += 1
            if c is n:
                return i
    return -1


def isPrime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if not x & 1:
        return False
    max = int(math.sqrt(x))
    for i in range(3, max + 1, 2):
        if not x % i:
            return False
    return True


if __name__ == '__main__':
    print(solution(1001))
