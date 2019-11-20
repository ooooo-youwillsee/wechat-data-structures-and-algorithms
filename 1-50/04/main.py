# coding=utf-8

def solution():
    sum = 0
    list = []
    for i in range(1, 28124):
        if abundant(i):
            list.append(i)

    for i in range(1, 28124):
        isAbundant = False
        k = 0
        j = len(list) - 1
        while k <= j:
            v = list[k] + list[j]
            if i > v:
                k += 1
            elif i < v:
                j -= 1
            else:
                isAbundant = True
                break

        if not isAbundant:
            sum += i
    return sum


def abundant(n):
    sum = 0
    for i in range(1, (n >> 1) + 1):
        if not n % i:
            sum += i
    return sum > n


if __name__ == '__main__':
    print(solution())
