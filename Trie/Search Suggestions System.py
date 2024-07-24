"""
Solution 1:

Brute-Force

Time Complexity: O(K * N * K), K is length of search word, N is number of products
Space complexity : O(3 * K)
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
        for c in searchWord:
            prefix += c
            cur = []
            for word in products:
                if word[: len(prefix)] == prefix and len(cur) < 3:
                    cur.append(word)
            res.append(cur)

        return res
