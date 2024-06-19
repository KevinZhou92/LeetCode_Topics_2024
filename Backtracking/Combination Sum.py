"""
Solution 1:

Backtracking.

Note that same element can be used multiple times, so we should always start searching from current
elements and onward.

Once a candidate is added into the current combination, we will not look back to all the previous candidates in the next explorations.

Time Complexity: O(N^(T/M + 1))
Space complexity : O(n)
"""
class Solution:
     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
          if not candidates:
               return []
          
          res = []
          self.search_combinations(candidates, 0, 0, target, [], res)

          return res

     def search_combinations(self, candidates, index, cur_sum, target, cur, res):
          if cur_sum == target:
               res.append([e for e in cur])
               return
          
          for i in range(index, len(candidates)):
               if candidates[i] + cur_sum > target:
                    continue
               cur_sum += candidates[i]
               cur.append(candidates[i])
               self.search_combinations(candidates, i, cur_sum, target, cur, res)
               cur.pop()
               cur_sum -= candidates[i]
        