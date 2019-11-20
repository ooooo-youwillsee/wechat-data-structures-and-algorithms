# coding=utf-8

import sys

def solution(n):
    num = n * (n - 1)
    s = 0
    for i in range(1, sys.maxsize):
        s = num * i
        for j in range(2, n + 1):
            if s % j:
                break
            if j == n:
                return s

    return s


if __name__ == '__main__':
    print(solution(20))
