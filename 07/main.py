# coding=utf-8

import math


def solution(max):
    for i in range(1, max):
        for j in range(i + 1, max):
            c = 1000 - i - j
            if pow(i, 2) + pow(j, 2) == pow(c, 2):
                return i * j * c
    return -1


if __name__ == '__main__':
    print(solution(1000))
