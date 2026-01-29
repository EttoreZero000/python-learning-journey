#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        signo = -1 if x < 0 else 1
        x = abs(x)

        invertido = 0
        while x != 0:
            digito = x % 10
            x //= 10

            # Detectar overflow ANTES de multiplicar
            if invertido > (INT_MAX - digito) // 10:
                return 0

            invertido = invertido * 10 + digito

        return signo * invertido


# @lc code=end

