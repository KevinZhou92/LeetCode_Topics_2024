"""
Solution 1:


Time Complexity: O(NlogN)
Space complexity : O(N)
"""
class StockPrice:

    def __init__(self):
        # prices with timestamp
        self.maxPrice = []
        self.minPrice = []
        self.curPrice = 0
        self.curTimeStamp = 0
        self.prices = {}
        

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price

        heapq.heappush(self.maxPrice, [-price, timestamp])
        heapq.heappush(self.minPrice, [price, timestamp])
        if timestamp >= self.curTimeStamp:
            self.curTimeStamp = timestamp
            self.curPrice = price
        
        return

    def current(self) -> int:
        return self.curPrice        

    def maximum(self) -> int:
        price, ts = self.maxPrice[0]
        while ts in self.prices and self.prices[ts] !=  -price:
            heapq.heappop(self.maxPrice)
            price, ts = self.maxPrice[0]
        
        return -self.maxPrice[0][0]
        
    def minimum(self) -> int:
        price, ts = self.minPrice[0]
        while ts in self.prices and self.prices[ts] !=  price:
            heapq.heappop(self.minPrice)
            price, ts = self.minPrice[0]
        
        return self.minPrice[0][0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()