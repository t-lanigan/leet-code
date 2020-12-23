from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    	return len(set(nums)) == len(nums)




sol = Solution()

test = [1,2,3,4,4]

print(sol.containsDuplicate(test))