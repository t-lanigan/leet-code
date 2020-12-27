from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0 for x in range(n)] 
        def climb(i: int, n: int, memo: List[int]) -> int:
            if i > n:
                return 0
            if i == n:
                return 1
            if memo[i] != 0:
            	return memo[i]
            memo[i] = climb(i+1, n, memo) + climb(i+2, n, memo)
            return memo[i]
        
        return climb(0, n, memo)


sol = Solution()
n = 5



print(sol.climbStairs(n))



