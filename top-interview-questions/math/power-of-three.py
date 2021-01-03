from math import log

class Solution:
    def isPowerOfThree(self, n: int) -> bool:

    	if n == 0:
    		return False

    	return (n > 0) and (1162261467 % n == 0)


solution = Solution()


assert solution.isPowerOfThree(1) == True
assert solution.isPowerOfThree(27) == True
assert solution.isPowerOfThree(0) == False
assert solution.isPowerOfThree(9) == True
assert solution.isPowerOfThree(45) == False
assert solution.isPowerOfThree(243) == True


print("All Tests Passed! :)")