class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit =0
        
        for index,item in enumerate(prices):
            profit = item-min_price
            min_price = min(min_price,item)
            max_profit = max(profit ,max_profit )
            
        return max_profit