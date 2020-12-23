class Solution:
    def reverse(self, x: int) -> int:
        """
        Do not return anything, modify s in-place instead.
        """

        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            s = str(x)
            if x >= 0 :
                revst = s[::-1]
            else:
                temp = s[1:] 
                temp2 = temp[::-1] 
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31:
                return 0
            else: 
                return int(revst)








sol = Solution()

test = -123

print(sol.reverse(test))