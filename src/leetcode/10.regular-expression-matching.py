#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0  # puntero en s
        j = 0  # puntero en p

        # Función recursiva para manejar '*' de forma clara
        def match(i, j):
            # Si llegamos al final del patrón
            if j == len(p):
                return i == len(s)

            # Verificar si el siguiente carácter es '*'
            next_is_star = (j + 1 < len(p) and p[j + 1] == "*")

            if next_is_star:
                # Probar 0 o más repeticiones del carácter actual
                k = i
                # Primer probar 0 repeticiones
                if match(i, j + 2):
                    return True
                # Luego probar 1 o más repeticiones
                while k < len(s) and (p[j] == s[k] or p[j] == "."):
                    k += 1
                    if match(k, j + 2):
                        return True
                return False
            else:
                # Coincidencia directa o '.'
                if i < len(s) and (p[j] == s[i] or p[j] == "."):
                    return match(i + 1, j + 1)
                else:
                    return False

        return match(0, 0)



        
# @lc code=end

