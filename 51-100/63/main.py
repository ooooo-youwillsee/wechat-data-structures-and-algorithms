# coding=utf-8

class Solution:
    def reverse(self, x: int) -> int:
        #  True 为正数
        num, flag = x, True
        if x < 0:
            num, flag = -x, False
        res = 0
        while num:
            res = res * 10 + num % 10
            num //= 10
        res = res if flag else -res
        #  −2^31,  2^31 − 1
        return res if pow(-2, 31) <= res <= pow(2, 31) else 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))