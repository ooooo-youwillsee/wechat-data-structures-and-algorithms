# coding=utf-8

class Solution:

    def solution(self, n):
        max = 0
        target = 0
        for i in range(1, n):
            c = self.circulation(1, i)
            if c > max:
                target = i
                max = c
        return target

    def circulation(self, dividend, divisor):
        quotientsList = []
        modList = []
        index = -1
        while True:
            quotientsList.append(dividend // divisor)
            mod = dividend % divisor
            if not mod:
                break
            modCount = modList.count(mod)
            if modCount:
                index = modList.index(mod)
                break
            else:
                modList.append(mod)
            dividend = mod * 10

        return 0 if index < 0 else len(quotientsList) - (index + 1)


if __name__ == '__main__':
    s = Solution()
    print(s.solution(1000))
