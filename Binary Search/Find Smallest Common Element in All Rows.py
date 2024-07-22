"""
Solution 1:

Iterate all elems to count freqs

Time Complexity: O(mn)
Space complexity : O(mn)
"""


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        freqs = {}
        for row in mat:
            for num in row:
                freqs[num] = freqs.get(num, 0) + 1

        keys = sorted(freqs.keys())
        for key in keys:
            if freqs[key] == len(mat):
                return key

        return -1
