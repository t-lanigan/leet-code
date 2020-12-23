from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        s.reverse()

    def reverseStringNonBuiltin(self, s: List[str]) -> None:
    	"""
    	Reverses the string using non-builtin methods.
    	"""
    	t = s.copy()

    	for x in range(len(s)):
    		t[x] = s[-(x+1)]

    	s[:] = t



sol = Solution()

test = ['h','e','l','l','o']


sol.reverseStringNonBuiltin(test)
print(test)