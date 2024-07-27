class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        start = prices[0]
        length = len(prices)
        for i in range(0 , length):
            if start < prices[i]: 
                maximum += prices[i] - start
            start = prices[i]
        return maximum