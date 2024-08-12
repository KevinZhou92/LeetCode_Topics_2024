"""
Solution 1:

PriorityQueue
Note that lt function returns a boolean, not a number

Time Complexity: O(nlogK)
Space complexity : O(k)
"""


class NumFreq:
    def __init__(self, num, freq):
        self.num = num
        self.freq = freq

    def __lt__(self, other):
        return self.freq - other.freq < 0


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        numFreqs = defaultdict(int)
        for num in nums:
            numFreqs[num] += 1

        pq = []
        for num, freq in numFreqs.items():
            heapq.heappush(pq, NumFreq(num, freq))
            if len(pq) > k:
                heapq.heappop(pq)
            print(pq[0].num)

        res = []
        while len(pq) > 0:
            res.append(heapq.heappop(pq).num)

        return res
