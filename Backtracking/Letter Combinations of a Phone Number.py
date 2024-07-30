"""
Solution 1:

Backtracking

Time Complexity: O(4^N * N)
Space complexity : O(N)
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ""

        mappings = {
            "2": set("abc"),
            "3": set("def"),
            "4": set("ghi"),
            "5": set("jkl"),
            "6": set("mno"),
            "7": set("pqrs"),
            "8": set("tuv"),
            "9": set("wxyz"),
        }

        res = []
        self.search(digits, 0, mappings, [], res)

        return res

    def search(self, digits, idx, mappings, cur, res):
        if idx == len(digits):
            res.append("".join(cur))
            return

        for c in mappings[digits[idx]]:
            cur.append(c)
            self.search(digits, idx + 1, mappings, cur, res)
            cur.pop()
