class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        max_profit =0
        for index,item in enumerate(prices[:length-1]):
            for price in prices[index+1:]:
                profit = price- item
                max_profit  = max(max_profit ,profit )
        return max_profit 