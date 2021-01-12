from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()





solution = Solution()


test1 = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(test1))


print("All tests passed!")