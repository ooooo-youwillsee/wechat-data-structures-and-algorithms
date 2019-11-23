# coding=utf-8

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums = sorted(nums1 + nums2)
        size = len(nums)
        if size & 1:
            return nums[size // 2]
        else:
            return (nums[size // 2] + nums[size // 2 - 1]) / 2


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([], [2, 3]))
