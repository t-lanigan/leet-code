class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

    	if haystack == "" and needle == "":
    		return 0

    	if haystack == "":
    		return -1

    	if needle == "":
    		return 0


    	for i, s in enumerate(haystack):
    		if s == needle[0]:
    			if needle == haystack[i:(i+len(needle))]:
    				return i
    			else:
    				continue
    	return -1


sol = Solution()

haystack = "needle"

needle = "dle" # ans: 1

print(sol.strStr(haystack, needle))