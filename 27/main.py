# coding=utf-8

class Solution:

    def solution(self):
        sum = 0
        for i in range(2, 5 * pow(9, 5) + 1):
            if self.sum4(i) == i:
                sum += i
        return sum

    def sum4(self, n):
        sum = 0
        while n:
            sum += pow(n % 10, 5)
            n //= 10
        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.solution())
