"""
Solution 1:

Left-most and right-most eles are -∞. So we can find a subarray with a peak by comparing the value of
mid ele and mid+1 ele

Time Complexity: O(logN)
Space complexity : O(1)
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid
        
        if nums[start] < nums[end]:
            return end
        
        return start
        