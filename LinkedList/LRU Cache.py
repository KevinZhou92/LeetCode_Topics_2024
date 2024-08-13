"""
Solution 1:

HashMap + Doubly-Linkedlist

Time Complexity: O(1)
Space complexity : O(1)
"""


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodes = {}

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self.removeNode(node)
        self.addNodeToHead(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            oldNode = self.nodes[key]
            self.removeNode(oldNode)
        node = Node(key, value)
        self.nodes[key] = node
        self.addNodeToHead(node)

        if self.capacity < len(self.nodes):
            nodeToRemove = self.tail.prev
            self.removeNode(nodeToRemove)
            self.nodes.pop(nodeToRemove.key)

        return

    def addNodeToHead(self, node):
        curHead = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = curHead
        curHead.prev = node

    def removeNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        node.prev = None
        node.next = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
