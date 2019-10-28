# coding=utf-8

def solution(num):
    if num == 1:
        return 1

    for i in range(2, num):
        if num % i == 0:
            return solution(num // i)
    return num


if __name__ == '__main__':
    print(solution(600851475143))
