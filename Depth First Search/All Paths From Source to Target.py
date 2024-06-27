"""
Solution 1:

DFS

Time Complexity: O(2^N * N)
Space complexity : O(N)
"""


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # we can use BFS to find the path to the target
        if not graph:
            return []

        res = []
        target = len(graph) - 1
        self.search(graph, 0, target, [0], res)

        return res

    def search(self, graph, cur_val, target, cur_path, res):
        if cur_val == target:
            res.append(list(cur_path))
            return

        for neighbor in graph[cur_val]:
            cur_path.append(neighbor)
            self.search(graph, neighbor, target, cur_path, res)
            cur_path.pop()


"""
Solution 1:

DFS #2 Traverse

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # we can use BFS to find the path to the target
        if not graph:
            return []

        res = []
        target = len(graph) - 1
        self.search(graph, 0, target, [], res)

        return res

    def search(self, graph, cur_val, target, cur_path, res):
        cur_path.append(cur_val)
        if cur_val == target:
            res.append(list(cur_path))
            # This is very important!
            cur_path.pop()
            return

        for neighbor in graph[cur_val]:
            self.search(graph, neighbor, target, cur_path, res)
        cur_path.pop()
