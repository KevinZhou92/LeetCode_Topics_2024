"""
Solution 1:

Binary Search

Time Complexity: O(NlogN + k)
Space complexity : O(N)
"""
class SnapshotArray:

    def __init__(self, length: int):
        self.array = {}
        self.size = length
        self.id = 0

    def set(self, index: int, val: int) -> None:
        if index not in self.array:
            self.array[index] = [[self.id, val]]
        else:
            if self.array[index][-1] and self.array[index][-1][0] == self.id:
                self.array[index].pop()
            self.array[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1

        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        if index not in self.array:
            return 0

        return self.binarySearch(self.array[index], snap_id)

    def binarySearch(self, array, id):
        start, end = 0, len(array) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if array[mid][0] <= id:
                start = mid
            else:
                end = mid

        if array[end][0] <= id:
            return array[end][1]

        if array[start][0] > id:
            return 0

        return array[start][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
