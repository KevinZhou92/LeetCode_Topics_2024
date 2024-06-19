"""
Solution 1:

Backtracking.

We either pick or not pick the number at current index and we search in both cases.

Time Complexity: O(2^N * N)
Space complexity : O(N), without considering the space for storing all results
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        self.search(nums, 0, [], res)

        return res

    def search(self, nums, idx, cur, res):
        if idx == len(nums):
            res.append(list(cur))
            return

        self.search(nums, idx + 1, cur, res)
        cur.append(nums[idx])
        self.search(nums, idx + 1, cur, res)
        cur.pop()


"""
Solution 2:

Time Complexity: O(2^N * N)
Space complexity : O(N), without considering the space for storing all results
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        res = []
        self.search(nums, 0, [], res)

        return res

    def search(self, nums, idx, cur, res):
        res.append(list(cur))

        for i in range(idx, len(nums)):
            cur.append(nums[i])
            self.search(nums, i + 1, cur, res)
            cur.pop()
            
"""
Solution 3:

Bit manipulation

Time Complexity: O(2^N)
Space complexity : O(N)
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        for i in range(2**n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            """
            Example:
            Assume there are 3 numbers, we will need binary representation of 3 digits
            so we can use bit representation to indicate which num is selected
            bin(n) will generate a binary representation with 0b as prefix.
            bin(2 ** 3) will generate '0b1000'
            bin(2 ** 3 - 1) generate '0b1111'
            
            This way, we generate bitmask from 000 to 111, which represent all the possible combination
            of subsets.

            """
            bitmask = bin(i)[3:]

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == "1"])

    return output
