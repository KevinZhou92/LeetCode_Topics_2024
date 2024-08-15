"""
Solution 1:

BFS

Check if we can visit all nodes

Time Complexity: O(E)
Space complexity : O(N)
"""


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        outDegrees = defaultdict(set)
        for e in edges:
            outDegrees[e[0]].add(e[1])
            outDegrees[e[1]].add(e[0])

        visited = set()
        queue = deque([0])
        while queue:
            cur = queue.popleft()
            visited.add(cur)
            for neighbor in outDegrees[cur]:
                if neighbor in visited:
                    continue
                queue.append(neighbor)

        return len(visited) == n
