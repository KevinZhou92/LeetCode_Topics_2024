"""
Solution 1:

Use set to track avaiable elements. Loop over the array to find missing eles 

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        seen = set(arr)
        cnt = 0
        val = 1
        res = 0
        while cnt < k:
            if val not in seen:
                cnt += 1
                res = val
            val += 1

        return res


"""
Solution 2:

Brute force with out using hash set
Split it into 3 scenarios
1. number missing before array start
2. number missing in the middle
3. number missing after array ends

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k

        # get how many numbers are missing
        k = k - arr[0] + 1
        for r in range(len(arr) - 1):
            curMissing = arr[i + 1] - arr[i]
            if k <= currMissing:
                return arr[i] + k
            k -= currMissing

        return arr[-1] + k


"""
Solution 3:

Binary Search

Time Complexity: O(logN)
Space complexity : O(1)
"""


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        make use of the characteristic that array is sorted
        do binary search, check diff between element and (index + 1),
        which will tell the count of missing numbers
        """
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            diff = arr[mid] - mid - 1
            if diff >= k:
                end = mid
            else:
                start = mid

        if arr[start] - start - 1 >= k:
            return k

        if arr[end] - end - 1 < k:
            return k + end + 1

        return k + start + 1
