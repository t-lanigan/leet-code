from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0:
            return 0
        
        profit = []
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                profit.append(prices[j] - prices[i])
                
        
        return max(profit)


test = Solution()

prices = [7,1,5,3,6,4]

print("The max profit is: {}".format(test.maxProfit(prices)))