"""
Solution 1:

Topological Sort

Time Complexity: O(V + E)
Space complexity : O(V + E)
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses or not prerequisites:
            return True

        inDegrees = {}
        outDegrees = {}

        for course in range(numCourses):
            inDegrees[course] = 0
            outDegrees[course] = set()

        for pre in prerequisites:
            courseToTake, courseMustTake = pre
            inDegrees[courseToTake] = inDegrees.get(courseToTake, 0) + 1
            outDegrees[courseMustTake].add(courseToTake)

        queue = deque([])
        for course in inDegrees:
            if inDegrees[course] != 0:
                continue
            queue.append(course)

        res = []
        while queue:
            size = len(queue)
            for _ in range(size):
                course = queue.popleft()
                res.append(course)
                for c in outDegrees[course]:
                    inDegrees[c] -= 1
                    if inDegrees[c] == 0:
                        queue.append(c)

        return len(res) == numCourses
