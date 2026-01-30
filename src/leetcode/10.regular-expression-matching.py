#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        size = len(s)
        ch = ""

        for i in range(size):

            if p[i] == "*":
                while ch == s[i]:
                    i+=1
                continue

            if not(s[i] == p[i] or "." == p[i]):
                return False
            ch = s[i]

        
# @lc code=end

