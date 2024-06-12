"""
Solution 1:

There are 4 directions we might go, we will keep going on the current direction until we can't.
We will change direction clockwise.

We will mark the visited cell using None(or we can use a val that is out of the range)

Time Complexity: O(m * n)
Space complexity : O(n)
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        delta_x = [0, 1, 0, -1]
        delta_y = [1, 0, -1, 0]
        d_idx = 0 # represent direction index
        r, c = 0, 0

        result = []
        while True:
            result.append(matrix[r][c])
            matrix[r][c] = None
            new_r, new_c = r + delta_x[d_idx], c + delta_y[d_idx]
            if not self.valid(new_r, new_c, m, n, matrix):
                d_idx = (d_idx + 1) % 4
                new_r, new_c = r + delta_x[d_idx], c + delta_y[d_idx]
            if not self.valid(new_r, new_c, m, n, matrix):
                break
            r, c = new_r, new_c
        
        return result

    def valid(self, r, c, m, n, matrix):
        if r < 0 or r >= m or c < 0 or c >=n :
            return False
        
        if matrix[r][c] == None:
            return False

        return True