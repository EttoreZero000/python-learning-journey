#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (59.35%)
# Likes:    33603
# Dislikes: 2163
# Total Accepted:    5M
# Total Submissions: 8.4M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i^th line are (i, 0) and (i,
# height[i]).
# 
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
# 
# Return the maximum amount of water a container can store.
# 
# Notice that you may not slant the container.
# 
# 
# Example 1:
# 
# 
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
# 
# 
# Example 2:
# 
# 
# Input: height = [1,1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Puntero izquierdo (inicio del arreglo)
        left = 0
        # Puntero derecho (final del arreglo)
        right = len(height) - 1

        # Aquí guardamos el área máxima encontrada
        max_area = 0

        # Mientras los punteros no se crucen
        while left < right:
            # El ancho es la distancia entre los punteros
            width = right - left

            # La altura del contenedor es la menor de las dos líneas
            current_height = min(height[left], height[right])

            # Área actual
            area = width * current_height

            # Actualizamos el máximo si encontramos algo mejor
            if area > max_area:
                max_area = area

            # 🔑 Movimiento clave:
            # Siempre movemos el puntero con la altura menor
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

        # One pront with chatGTP
                
# @lc code=end

