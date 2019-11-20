# coding=utf-8

class Solution:

    def solution(self):
        sum = 0
        for i in range(1, 1000000):
            if self.isPalindrome(i) and self.isPalindrome(int(bin(i).replace('0b', ''))):
                # print(i)
                sum += i
        return sum

    def isPalindrome(self, n):
        sum = 0
        tmp = n
        while n:
            sum = sum * 10 + n % 10
            n //= 10

        return tmp == sum


if __name__ == '__main__':
    s = Solution()
    # print(s.isPalindrome(585))
    print(s.solution())
