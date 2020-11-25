from typing import List

class Solution(object):
	"""docstring for Solution"""
	def maxProfit(self, prices: List[int]) -> int:

		maxProfit = 0

		for i in range(1, len(prices)):
			if prices[i] > prices[i-1]:
				maxProfit += prices[i] - prices[i-1]
				
		return "The max profit is: {}".format(maxProfit)


test = Solution()

prices = [7,1,5,3,6,4]

print(test.maxProfit(prices))