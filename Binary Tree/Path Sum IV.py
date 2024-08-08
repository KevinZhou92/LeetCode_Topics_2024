"""
Solution 1:

Recursion

Convert input into a map, which maps depth to {posistion: value}
Then traverse the tree using the map

Time Complexity: O()
Space complexity : O()
"""
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        """
        d -> p -> v
        """

        if not nums:
            return 0
        
        self.res = 0
        tree = {}
        for num in nums:
            num = str(num)
            d, p, v = int(num[0]), int(num[1]), int(num[2])
            if d not in tree:
                tree[d] = {}
            if p not in tree[d]:
                tree[d][p] = v
        self.search(1, 1, 0, tree)

        return self.res
    
    def search(self, depth, pos, curSum, tree):
        if depth not in tree or pos not in tree[depth]:
            return
        
        curSum += tree[depth][pos]
        if depth + 1 not in tree or (pos * 2 not in tree[depth + 1] and pos * 2 - 1 not in tree[depth + 1]):
            self.res += curSum

        self.search(depth + 1, pos * 2 - 1, curSum, tree)
        self.search(depth + 1, pos * 2, curSum, tree)
        curSum -= tree[depth][pos]


        