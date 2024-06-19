"""
Solution 1:

Backtracking + Prune

Time Complexity: O(2^N))
Space complexity : O(N)
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        res = []
        candidates.sort()
        self.search_combinations(candidates, 0, 0, target, [], res)

        return res

    def search_combinations(self, candidates, index, cur_sum, target, cur, res):
        if cur_sum == target:
            res.append([e for e in cur])
            return

        for i in range(index, len(candidates)):
            # This is import since nums in input is not UNIQUE
            # Even if we start from un-searched eles we could still
            # end up with the same combination
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] + cur_sum > target:
                continue
            cur_sum += candidates[i]
            cur.append(candidates[i])
            self.search_combinations(candidates, i + 1, cur_sum, target, cur, res)
            cur.pop()
            cur_sum -= candidates[i]
