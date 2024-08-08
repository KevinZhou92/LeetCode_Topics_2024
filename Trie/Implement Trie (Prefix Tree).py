"""
Solution 1:

Implement Trie

Time Complexity: O(N)
Space complexity : O(N)
"""


class Trie:

    def __init__(self):
        self.isWord = False
        self.children = {}

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if not c in node.children:
                node.children[c] = Trie()
            node = node.children[c]

        node.isWord = True

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            if not c in node.children:
                return False
            node = node.children[c]

        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            if not c in node.children:
                return False
            node = node.children[c]

        return len(node.children) > 0 or node.isWord


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
