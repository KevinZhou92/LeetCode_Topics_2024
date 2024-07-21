"""
Solution 1:

Binary Search

Time Complexity: 
If M is the number of set function calls, N is the number of get function calls, and L is average length of key and value strings.
get function complexity should be O(N*(L+logM)), L time to hash the key, logM to search arrary of M elements
Space complexity : O(M * L), m elements of length L
"""


class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        values = self.map[key]
        start, end = 0, len(values) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if values[mid][1] <= timestamp:
                start = mid
            else:
                end = mid

        if values[end][1] <= timestamp:
            return values[end][0]

        if values[start][1] <= timestamp:
            return values[start][0]

        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
