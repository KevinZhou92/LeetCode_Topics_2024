"""
Solution 1:

Hash Map + Traverse

Time Complexity: O(N)
Space complexity : O(N)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head

        dummy = Node(-1)
        newHead = Node(head.val)
        dummy.next = newHead

        seenNodes = {head: newHead}
        queue = deque([head])
        while queue:
            cur = queue.popleft()
            if not cur in seenNodes:
                seenNodes[cur] = Node(cur.val)
            newNode = seenNodes[cur]
            if cur.next and cur.next not in seenNodes:
                seenNodes[cur.next] = Node(cur.next.val)
                queue.append(cur.next)
            newNode.next = seenNodes.get(cur.next, None)
            if cur.random and cur.random not in seenNodes:
                seenNodes[cur.random] = Node(cur.random.val)
                queue.append(cur.random)
            newNode.random = seenNodes.get(cur.random, None)

        return dummy.next


"""
Solution 2:

1. Clone Nodes 
2. Connect Nodes

Time Complexity: O(N)
Space complexity : O(N)
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head

        seenNodes = {}
        cur = head
        while cur:
            seenNodes[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copiedCur = seenNodes.get(cur, None)
            copiedCur.next = seenNodes.get(cur.next, None)
            copiedCur.random = seenNodes.get(cur.random, None)
            cur = cur.next

        return seenNodes.get(head, None)
