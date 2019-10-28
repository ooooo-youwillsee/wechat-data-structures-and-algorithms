# coding=utf-8

def solution():
    num = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            result = i * j
            if result > num and isPalindromeNumber(result):
                num = result

    return num


def isPalindromeNumber(num):
    arr: list[int] = []
    while num / 10 != 0:
        arr.append(num % 10)
        num //= 10

    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] != arr[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    print(solution())
