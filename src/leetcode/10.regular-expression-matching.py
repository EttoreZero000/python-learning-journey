#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match(i, j):
            if j == len(p):
                return i == len(s)

            next_is_star = (j + 1 < len(p) and p[j + 1] == "*")

            if next_is_star:
                if match(i, j + 2):
                    return True
                k = i
                while k < len(s) and (p[j] == s[k] or p[j] == "."):
                    k += 1
                    if match(k, j + 2):
                        return True
                return False
            else:
                if i < len(s) and (p[j] == s[i] or p[j] == "."):
                    return match(i + 1, j + 1)
                else:
                    return False

        return match(0, 0)
        
# @lc code=end

