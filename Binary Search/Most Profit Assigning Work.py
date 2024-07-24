"""
Solution 1:

Binary Search 
Search space is possible profit

Time Complexity: O(NLogP) P is the max profit
Space complexity : O(1)
"""


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        """
        binary search between min profit and max profit
        sort (prof, difficulty) in descending order
        sort work in descending order

        most powerful workder work on high profit job first
        """
        profitWithDiff = list(zip(profit, difficulty))
        profitWithDiff.sort(key=lambda p: (-p[0], -p[1]))
        worker.sort(key=lambda x: -x)
        start, end = 0, len(worker) * max(profit)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.canMakeProfit(profitWithDiff, worker, mid):
                start = mid
            else:
                end = mid

        if self.canMakeProfit(profitWithDiff, worker, end):
            return end

        return start

    def canMakeProfit(self, profitWithDiff, worker, profitNeeded):
        wIndex = 0
        pIndex = 0
        profitMade = 0
        while pIndex < len(profitWithDiff) and wIndex < len(worker):
            # difficulty
            if profitWithDiff[pIndex][1] > worker[wIndex]:
                pIndex += 1
            else:
                profitMade += profitWithDiff[pIndex][0]
                wIndex += 1

        return profitMade >= profitNeeded


"""
Solution 2:

Binary Search

Time Complexity: O(NlogN + mLogN). where N is the lenght of profits and M is the length of worker
Space complexity : O()
"""


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        """
        binary search between min profit and max profit
        sort (prof, difficulty) in descending order
        sort work in descending order

        most powerful workder work on high profit job first
        """
        profitWithDiff = list(zip(difficulty, profit))
        # sort by difficulty for ascending order
        profitWithDiff.sort()
        for i in range(len(profitWithDiff) - 1):
            profitWithDiff[i + 1] = [
                profitWithDiff[i + 1][0],
                max(profitWithDiff[i + 1][1], profitWithDiff[i][1]),
            ]

        maxProfit = 0
        for w in worker:
            maxProfit += self.getMaxProfitForWorker(profitWithDiff, w)

        return maxProfit

    def getMaxProfitForWorker(self, profitWithDiff, worker):
        start, end = 0, len(profitWithDiff) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if profitWithDiff[mid][0] <= worker:
                start = mid
            else:
                end = mid

        if profitWithDiff[end][0] <= worker:
            return profitWithDiff[end][1]

        if profitWithDiff[start][0] <= worker:
            return profitWithDiff[start][1]

        return 0


"""
Solution 3:

Greedy Solution

Sort the profit with difficulty in descending order
Always select the task with the max profit for current worker

Time Complexity: O(nlogN + MlogM)
Space complexity : O(N)
"""


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        """
        binary search between min profit and max profit
        sort (prof, difficulty) in descending order
        sort work in descending order

        most powerful workder work on high profit job first
        """
        profitWithDiff = list(zip(profit, difficulty))
        profitWithDiff.sort(key=lambda p: (-p[0], -p[1]))
        worker.sort(key=lambda x: -x)

        wIndex = 0
        pIndex = 0
        profitMade = 0
        while pIndex < len(profitWithDiff) and wIndex < len(worker):
            if profitWithDiff[pIndex][1] > worker[wIndex]:
                pIndex += 1
            else:
                profitMade += profitWithDiff[pIndex][0]
                wIndex += 1

        return profitMade


"""
Solution 1:

Memorization

Create a array to store the max profit for each possible ability, the max ability is determined
by the max ability from the worker.

Time Complexity: O(N + M + maxAbility)
Space complexity : O(maxAbility)
"""


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        maxAbility = max(worker)
        # 1-indexed array
        profits = [0] * (maxAbility + 1)
        for i in range(len(difficulty)):
            if difficulty[i] > maxAbility:
                continue
            profits[difficulty[i]] = max(profits[difficulty[i]], profit[i])

        for i in range(1, len(profits)):
            profits[i] = max(profits[i], profits[i - 1])

        maxProfit = 0
        for w in worker:
            maxProfit += profits[w]

        return maxProfit
