"""
Solution 1:

BFS

Time Complexity: O(M * N)
Space complexity : O(M * N)
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m = len(heights)
        n = len(heights[0])
        pacificStart = set()
        altanticStart = set()
        for i in range(m):
            pacificStart.add((i, 0))
            altanticStart.add((i, n - 1))
        for i in range(n):
            pacificStart.add((0, i))
            altanticStart.add((m - 1, i))

        pacificVisited = self.bfs(heights, pacificStart)
        alanticVisited = self.bfs(heights, altanticStart)

        return list(pacificVisited.intersection(alanticVisited))

    def bfs(self, heights, startPoints):
        dirs = [(0, 1), (-1, 0), (1, 0), (0, -1)]
        visited = set()
        queue = deque(startPoints)
        while queue:
            r, c = queue.popleft()
            visited.add((r, c))
            for dr, dc in dirs:
                newR, newC = r + dr, c + dc
                if (newR, newC) in visited:
                    continue
                if (
                    0 <= newR < len(heights)
                    and 0 <= newC < len(heights[0])
                    and heights[newR][newC] >= heights[r][c]
                ):
                    queue.append((newR, newC))

        return visited
