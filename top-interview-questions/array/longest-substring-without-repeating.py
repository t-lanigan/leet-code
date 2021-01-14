class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        str_list = []
        max_length = 0
        
        for x in s:
            if x in str_list:
                str_list = str_list[str_list.index(x)+1:]
                
            str_list.append(x)    
            max_length = max(max_length, len(str_list))
            
        return max_length




solution = Solution()


assert solution.lengthOfLongestSubstring("abcabcbb") == 3
# assert solution.lengthOfLongestSubstring("bbbbb") == 1
# assert solution.lengthOfLongestSubstring("pwwkew") == 3
# assert solution.lengthOfLongestSubstring("") == 0


print("All tests passed!")