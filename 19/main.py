# coding=utf-8

class Solution:

    def solution(self):
        sum = 0
        for i in range(1, 10000):
            n = self.calc(i)
            m = self.calc(n)
            if m == i and i != n:
                sum += i
                print('%d,%d' % (i, n))

        return sum

    def calc(self, n):
        sum = 0
        for i in range(1, n):
            if not n % i:
                sum += i
        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.solution())
