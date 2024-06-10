"""
Solution 1:
We can rotate from outside to inside, for example, rotate the outside 4 sides, then rotate 
a (n - 1) * (n - 1) square, until we finish rotating the image. Note that in this method,
for each squre, we are only iterating over (N - 1) element, where N = (number of element available each side)
, this is because the last element in the same side is already replaced by the first element in the same side. 

We could also divide the square into 4 cells and rotate cells by iterating over the cells, notice
here we need to be very careful if n is an odd


Time Complexity: O(mn)
Space complexity : O(1)
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        n = len(matrix)
        for i in range(0, n // 2):
            for j in range(0, n - 2 * i - 1):
                tmp = matrix[i][i + j]
                matrix[i][i + j] = matrix[n - i - j - 1][i]
                matrix[n - i - j - 1][i] = matrix[n - i - 1][n - i - j - 1]
                matrix[n - i - 1][n - i - j - 1] = matrix[i + j][n - i - 1]
                matrix[i + j][n - i - 1] = tmp
            
        return