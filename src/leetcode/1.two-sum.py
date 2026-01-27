#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not (len(nums) >= 2 and len(nums) <= 10**4):
            raise ValueError("The size is incorrect")
    
        for num in nums:
            if not(-10**9 <= num and 10**9 >= num):
                raise ValueError("The numbers is very big or very less")

        if not(-10**9 <= target and target <= 10**9):
            raise ValueError("The target is very big or very less")

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j] == target and not(i==j):
                    return [i,j]
# @lc code=end

