"""
Solution 1:


BFS

Tricky part is how we handle the visited element, we need to add the new elemenet into visited set
immediately after generating it to prevent the same element from being added to the queue at the same level.

Time Complexity: O(https://leetcode.com/problems/open-the-lock/editorial/)
Space complexity : O()
"""


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        if "0000" == target:
            return 0

        queue = deque([[0, 0, 0, 0]])
        rotations = 0
        visited = set("0000")
        while queue:
            size = len(queue)
            rotations += 1
            for _ in range(size):
                cur_comb = queue.popleft()
                for i in range(4):
                    for d in [-1, 1]:
                        cur = list(cur_comb)
                        cur[i] = (cur[i] + d) % 10
                        combVal = "".join(map(str, cur))
                        if combVal not in visited and combVal not in deadends:
                            queue.append(cur)
                            visited.add(combVal)
                        if combVal == target:
                            return rotations

        return -1


"""
Solution 2:

BFS variant

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        queue = deque([[0, 0, 0, 0]])
        rotations = 0
        visited = set("0000")
        while queue:
            size = len(queue)
            for _ in range(size):
                cur_comb = queue.popleft()
                curVal = "".join(map(str, cur_comb))
                if curVal == target:
                    return rotations
                for i in range(4):
                    for d in [-1, 1]:
                        cur = list(cur_comb)
                        cur[i] = (cur[i] + d) % 10
                        combVal = "".join(map(str, cur))
                        if combVal not in visited and combVal not in deadends:
                            queue.append(cur)
                            visited.add(combVal)
            rotations += 1

        return -1
