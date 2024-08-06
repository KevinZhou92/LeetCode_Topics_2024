"""
Solution 1:

Backtracking

Left parenthese count should always >= right parenthese count

Time Complexity: O(4^n)
Space complexity : O(n)
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        res = []
        self.search(n, n, [], res)

        return res

    def search(self, left, right, cur, res):
        if left == 0 and right == 0:
            res.append("".join(cur))
            return

        if left > 0:
            cur.append("(")
            self.search(left - 1, right, cur, res)
            cur.pop()

        if left < right:
            cur.append(")")
            self.search(left, right - 1, cur, res)
            cur.pop()

"""
Solution 2:

BFS

Time Complexity: O()
Space complexity : O()
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []

        res = []
        # cur, leftRemains, rightRemains
        queue = deque([["", n, n]])
        while queue:
            size = len(queue)
            for _ in range(size):
                cur, leftRemains, rightRemains = queue.popleft()
                if leftRemains == 0 and rightRemains == 0:
                    res.append(cur)
                    continue
                if leftRemains > 0:
                    queue.append([cur + "(", leftRemains - 1, rightRemains])
                if leftRemains < rightRemains:
                    queue.append([cur + ")", leftRemains, rightRemains - 1])
        
        return res