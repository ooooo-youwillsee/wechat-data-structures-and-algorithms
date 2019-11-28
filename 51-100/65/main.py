# coding=utf-8

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        sum, num = 0, x
        while x:
            sum = sum * 10 + x % 10
            x //= 10
        return sum == num


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-123))
    print(s.isPalindrome(10))
