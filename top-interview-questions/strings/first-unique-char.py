class Solution:
    def firstUniqChar(self, s: str) -> int:

    	counts = {}
    	order = []

    	for i, x in enumerate(s):
    		if x in counts:
    			counts[x] += 1
    		else:
    			counts[x] = 1
    			order.append((x, i))

    	for x in order:
    		if counts[x[0]] == 1:
   				return x[1]

    	return -1



sol = Solution()

t = 'leetcode' # 0
t2 = 'loveleetcode' # 2


print(sol.firstUniqChar(t2))