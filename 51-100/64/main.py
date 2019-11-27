# coding=utf-8

class Solution:
    def myAtoi(self, s: str) -> int:
        nums, s, ss, = set([str(i) for i in range(10)]), s.strip(' '), ''
        hasNum, hasSymbol, symbol = False, False, ''
        for c in s:
            if c not in nums:
                if c in ['-', '+'] and not hasSymbol and not hasNum:
                    hasSymbol, symbol = True, c
                else:
                    break
            else:
                hasNum = True
                ss += c
        if len(ss) == 0:
            return 0
        res = int(symbol + ss)
        res = pow(2, 31) - 1 if res > pow(2, 31) - 1 else res
        res = pow(-2, 31) if res < pow(-2, 31) else res
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi('42'))
    print(s.myAtoi('     -42'))
    print(s.myAtoi('4193 with words'))
    print(s.myAtoi('words and 987'))
    print(s.myAtoi('-+1'))
    print(s.myAtoi('+'))
    print(s.myAtoi('+abc'))
    print(s.myAtoi('0-1'))
