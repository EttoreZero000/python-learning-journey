#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        signo = 1
        i = 0

        if s[0] == "-":
            signo = -1
            i+=1
        elif s[0] == "+":
            i+=1

        nS = ""
        while i < len(s) and s[i].isdigit():
            nS += s[i]
            i += 1

        if not nS:
            return 0

        num = signo * int(nS)

        # Manejo de límites int32
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num
        
# @lc code=end