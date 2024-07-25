"""
Solution 1:

Binary Search

Time Complexity: O(logN)
Space complexity : O(N)
"""
class Solution:

    def __init__(self, w: List[int]):
        self.totalSum = sum(w)
        self.prefixSum = []
        for i in range(len(w)):
            if i == 0:
                self.prefixSum.append(w[i])
            else:
                self.prefixSum.append(self.prefixSum[i - 1] + w[i])
        
    def pickIndex(self) -> int:
        target = self.totalSum * random.random()
        index = self.search(self.prefixSum, target)

        return index
    
    def search(self, arr, target):
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid] < target:
                start = mid
            else:
                end = mid
        
        if arr[start] >= target:
            return start
        
        return end

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()