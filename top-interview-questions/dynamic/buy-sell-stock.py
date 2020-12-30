from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if prices == []:
            return 0
        
        buy = prices[0]
        maxProfit = 0
        
        
        for price in prices:
            profit = price - buy
            if profit > maxProfit:
                maxProfit = profit
            if buy > price:
                buy = price
                
        
        return maxProfit


test = Solution()

prices = [7,2,6,1,2,2]

print("The max profit is: {}".format(test.maxProfit(prices)))