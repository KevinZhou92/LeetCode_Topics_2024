"""
Solution 1:

Use a hashmap and for every get, check the previous 300 entries

Time Complexity: O(300) for get
Space complexity : O(N)
"""


class HitCounter:

    def __init__(self):
        self.hits = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        self.hits[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        res = 0
        for ts in range(timestamp, timestamp - 300, -1):
            if ts in self.hits:
                res += self.hits[ts]

        return res


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

"""
Solution 2:

Use a queue and maintain the queue size as 300

Time Complexity: O(1)
Space complexity : O(300)
"""


class HitCounter:

    def __init__(self):
        # store (timestamp, hitCount)
        self.queue = deque([])
        self.count = 0

    def hit(self, timestamp: int) -> None:
        if self.queue and self.queue[-1][0] == timestamp:
            self.queue[-1][1] += 1
        else:
            self.queue.append([timestamp, 1])
        self.count += 1

        return

    def getHits(self, timestamp: int) -> int:
        if not self.queue:
            return 0

        while self.queue and timestamp - self.queue[0][0] >= 300:
            ts, count = self.queue.popleft()
            self.count -= count

        return self.count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
