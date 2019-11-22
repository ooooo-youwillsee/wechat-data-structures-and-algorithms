# coding=utf-8

import math


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # res = 0
        # for i in range(0, len(s)):
        #     ss = set()
        #     for j in range(i, len(s)):
        #         if s[j] in ss:
        #             res = max(len(ss), res)
        #             break
        #         elif j == len(s) - 1:
        #             res = max(len(ss) + 1, res)
        #         ss.add(s[j])
        # return res

        map = {}
        i = 0
        res = 0
        for j in range(0, len(s)):
            if s[j] in map:
                i = max(i, map[s[j]])
            res = max(res, j - i + 1)
            map[s[j]] = j + 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))
    print(s.lengthOfLongestSubstring('bbbbb'))
    print(s.lengthOfLongestSubstring('pwwkew'))
    print(s.lengthOfLongestSubstring(' '))
    print(s.lengthOfLongestSubstring('ax'))
    print(s.lengthOfLongestSubstring('aab'))
