class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

    	ds = self.getCountsDict(s)
    	dt = self.getCountsDict(t)

    	return ds == dt

    def getCountsDict(self, s: str) -> dict:
    	d = {}

    	for x in s:
    		if x in d:
    			d[x] += 1
    		else:
    			d[x] = 1

    	return d


sol = Solution()

s = "anagram"
t = "nagaram"


print(sol.isAnagram(s, t))