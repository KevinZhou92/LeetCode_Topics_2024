"""
Solution 1:

Binary Search on each column

Time Complexity: O(R * logC)
Space complexity : O(1)
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0])
        for row in matrix:
            if row[0] > target:
                continue
            if self.search(row, 0, col - 1, target):
                return True

        return False

    def search(self, array, start, end, target):
        while start + 1 < end:
            mid = start + (end - start) // 2
            if array[mid] > target:
                end = mid
            else:
                start = mid

        if array[start] == target:
            return True

        if array[end] == target:
            return True

        return False


"""
Solution 2:

Start search from Bottom left for top right

Time Complexity: O(R + C)
Space complexity : O(1)
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0])
        r, c = row - 1, 0
        while r >= 0 and c < col:
            if matrix[r][c] < target:
                c += 1
            elif matrix[r][c] > target:
                r -= 1
            else:
                return True

        return False
