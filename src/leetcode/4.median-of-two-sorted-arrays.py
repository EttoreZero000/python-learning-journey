#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2:
            nums1.append(num)

        nums1.sort()

        n = len(nums1)
        mid = n // 2

        if n % 2 == 1:
            return float(nums1[mid])
        else:
            return (nums1[mid - 1] + nums1[mid]) / 2

# @lc code=end

