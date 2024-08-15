"""
Solution 1:

Two pointers from left and right, we should only move the shorter side, since move the higher side 
will only make the result smaller

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        res = min(height[0], height[-1]) * (r - l)
        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            if l >= r:
                break
            res = max(res, min(height[l], height[r]) * (r - l))

        return res
