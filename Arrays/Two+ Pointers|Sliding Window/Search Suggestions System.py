"""
Solution 1:

Sliding Window, utilize the characteristic of a sorted array

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        if not searchWord or not products:
            return []

        products.sort()
        prefix = ""
        res = []
        l, r = 0, len(products) - 1
        for i in range(len(searchWord)):
            cur = []
            while l <= r and (len(products[l]) <= i or products[l][i] != searchWord[i]):
                l += 1

            while l <= r and (len(products[r]) <= i or products[r][i] != searchWord[i]):
                r -= 1

            for j in range(l, min(l + 3, r + 1)):
                cur.append(products[j])

            res.append(cur)

        return res
