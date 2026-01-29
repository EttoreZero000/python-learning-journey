#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # Crear una lista de strings, uno por cada fila
        rows = [""] * numRows

        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char

            # Cambiamos dirección si estamos arriba o abajo
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            current_row += 1 if going_down else -1

        return "".join(rows)


# @lc code=end