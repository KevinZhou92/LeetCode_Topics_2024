"""
Solution 1:

Backtracking

To implement the algorithm, one could literally follow the steps in the Intuition section.
However, we would like to highlight a key trick that we employed, in order to ensure the non-redundancy among the digits within a single combination, as well as the non-redundancy among the combinations.

The trick is that we pick the candidates in order.
We treat the candidate digits as a list with order, i.e. [1, 2, 3, 4, 5, 6, 7, 8. 9].
At any given step, once we pick a digit, e.g. 6, we will not consider any digits before the chosen digit for the following steps, e.g. the candidates are reduced down to [7, 8, 9]

Time Complexity: O()
Space complexity : O(n)
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.search(k, n, [], 0, res)

        return res

    def search(self, count, remain, cur, idx, res):
        if remain == 0 and len(cur) == count:
            res.append(list(cur))
            return

        for i in range(idx, 9):
            if remain - (i + 1) < 0 or len(cur) == count:
                return
            remain -= i + 1
            cur.append(i + 1)
            self.search(count, remain, cur, i + 1, res)
            remain += i + 1
            cur.pop()
