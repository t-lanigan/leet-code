
# Rules:
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900


class Solution:
    def romanToInt(self, s: str) -> int:
        rMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        
        intValue = 0 

        for i in range(len(s)):
            if (i > 0) and (rMap[s[i]] > rMap[s[i-1]]):
                intValue += rMap[s[i]] - 2 * rMap[s[i-1]]

            else:
                intValue += rMap[s[i]]



        return intValue





solution = Solution()

assert solution.romanToInt("III") == 3
assert solution.romanToInt("IV") == 4
assert solution.romanToInt("IX") == 9
assert solution.romanToInt("LVIII") == 58
assert solution.romanToInt("MCMXCIV") == 1994



print("All Tests Passed! :)")