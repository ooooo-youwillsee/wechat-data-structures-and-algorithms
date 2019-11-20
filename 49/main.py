# coding=utf-8

class Solution:

    def solution(self):
        c = 0
        for i in range(1, 10000):
            n = 0
            res = i
            while n < 50:
                res = self.reverseNum(res) + res
                n += 1
                if res == self.reverseNum(res):
                    break
            else:
                c+=1
        return c

    def reverseNum(self, n):
        sum = 0
        while n:
            sum = sum * 10 + n % 10
            n //= 10
        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.solution())
