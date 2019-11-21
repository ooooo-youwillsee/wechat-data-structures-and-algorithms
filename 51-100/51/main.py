# coding=utf-8

class Solution:

    def solution(self, n):
        sum = 0
        a, b = self.help(0, 1, 1, 1)
        c = 0
        while c < n:
            c += 1
            a, b = self.help(1, 1, a, b, True)
            a, b = self.help(1, 1, a, b)
            if self.isValid(a, b):
                sum += 1
        return sum

    def isValid(self, a, b):
        return len(str(a)) > len(str(b))

    def help(self, a1, b1, a2, b2, flag=False):
        a = a1 * b2 + a2 * b1
        b = b1 * b2
        return (b, a) if flag else (a, b)


if __name__ == '__main__':
    s = Solution()
    print(s.help(1, 1, 1, 1))
    print(s.solution(1000))
