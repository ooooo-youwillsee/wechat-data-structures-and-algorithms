# coding=utf-8

class Solution:

    def solution(self, nums, target):
        map = {}
        for i, item in enumerate(nums):
            if target - item in map:
                return [map[target - item], i]
            map[item] = i
        return []


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 9, 10]
    target = 9
    print(s.solution(nums, target))
