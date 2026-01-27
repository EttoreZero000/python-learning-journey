#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        size = len(s)
        if size == 0:
            return 0

        listaInt = []

        for i in range(size):
            newString = ""
            for j in range(i, size):
                if s[j] in newString:
                    break
                newString += s[j]
            listaInt.append(len(newString))

        return max(listaInt)


# @lc code=end

