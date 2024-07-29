"""
Solution 1:

Two Pointers

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return -1

        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                return nums1[p1]

        return -1
