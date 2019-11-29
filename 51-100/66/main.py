# coding=utf-8

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = 0, 0
        #  清洗字符 *
        m1 = {}
        res = p
        for c in range(len(p)):
            if p[c] == '*' or p[c] == '.':
                continue
            if p[c] not in s and c < len(p) - 1:
                if p[c + 1] != '*':
                    return False
                else:
                    res = res.replace(p[c] + '*', '')
        p = res
        while i < len(s) or j < len(p):
            if j == len(p):
                return False
            if i == len(s):
                break

            if s[i] == p[j]:
                i, j = i + 1, j + 1
                continue
            else:
                if p[j] == '*' and j >= 1:
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        i, j = i + 1, j + 1
                        continue
                if p[j] == '.':
                    i, j = i + 1, j + 1
                    continue
                if p[j + 1] == '*':
                    j = j + 2
                    continue

        return True


if __name__ == '__main__':
    s = Solution()
    # print(s.isMatch('aa', 'a') == False)
    # print(s.isMatch('aa', 'a*') == True)
    # print(s.isMatch('ab', '.*') == True)
    # print(s.isMatch('aab', 'c*a*b') == True)
    # print(s.isMatch('mississippi', 'mis*is*p*.') == False)
    # print(s.isMatch('ab', '.*c') == False)
    print(s.isMatch('aaa', 'ab*a*c*a') == True)
