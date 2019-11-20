# coding=utf-8


class Solution:

    def solution(self):
        list = [x for x in range(0, 10)]
        return self.help(10, 999999, list)

    def help(self, n, max, list):
        if n > 0:
            res = 1
            if n != 1:
                res = self.recursion(n - 1)
            index = max // res
            mod = max % res
            i = list[index]
            del list[index]
            return str(i) + self.help(n - 1, mod, list)
        return ''

    def recursion(self, n):
        if n == 1 or n == 0:
            return 1
        return n * self.recursion(n - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.solution())
