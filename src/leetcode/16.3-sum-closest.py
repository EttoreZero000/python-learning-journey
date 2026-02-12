#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (47.89%)
# Likes:    11518
# Dislikes: 616
# Total Accepted:    1.7M
# Total Submissions: 3.6M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an integer array nums of length n and an integer target, find three
# integers at distinct indices in nums such that the sum is closest to target.
# 
# Return the sum of the three integers.
# 
# You may assume that each input would have exactly one solution.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        
        closest = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Si encontramos exacto, ya ganamos
                if current_sum == target:
                    return current_sum
                
                # Actualizar si es más cercano
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum
                
                # Mover punteros
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest

        
# @lc code=end

