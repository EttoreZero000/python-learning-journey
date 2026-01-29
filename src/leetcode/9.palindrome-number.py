#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x //= 10

        return x == reverse or x == reverse // 10

        
# @lc code=end

