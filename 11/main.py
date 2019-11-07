# coding=utf-8

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), £2 (200p)
nums = [1, 2, 5, 10, 20, 50, 100, 200]


class Solution:

    def solution(self, n, index):
        c = 0
        for i in range(index, len(nums)):
            if n - nums[i] == 0:
                # self.c += 1
                c += 1
            elif n > i:
                c += self.solution(n - nums[i], i)
        return c


if __name__ == '__main__':
    s = Solution()
    #  创建index才不会乱序，导致重复
    print(s.solution(50, 0))

#    5,
#    1,2,2
#    1,1,1,2
#    1,1,1,1,1
