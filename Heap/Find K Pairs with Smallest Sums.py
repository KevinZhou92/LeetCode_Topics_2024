"""
Solution 1:

Generate all pairs and store in heap

Memory limit exceeded

Time Complexity: O(mnlogmn)
Space complexity : O(mn)
"""
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        size1 = len(nums1)
        size2 = len(nums2)

        pq = []
        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(pq, (num1 + num2, (num1, num2)))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(pq)[1])
        
        return res

"""
Solution 2:

"Merge K sorted list"

Time Complexity: O(nlogn), where n is the size of the smaller list
Space complexity : O(n)
"""
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        size1 = len(nums1)
        size2 = len(nums2)

        pq = []
        for i in range(size1):
            heapq.heappush(pq, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
        
        res = []
        for _ in range(k):
            _, num1, num2, idx2 = heapq.heappop(pq)
            res.append([num1, num2])
            if idx2 + 1 >= size2:
                continue
            heapq.heappush(pq, (num1 + nums2[idx2 + 1], num1, nums2[idx2 + 1], idx2 + 1))

        return res