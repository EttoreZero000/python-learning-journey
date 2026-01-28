#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Caso rápido: toda la palabra ya es palíndromo
        if s == s[::-1]:
            return s

        best = ""
        n = len(s)

        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]
                if sub == sub[::-1] and len(sub) > len(best):
                    best = sub

        return best


        
# @lc code=end

