from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
            
        nums[:] = a



sol = Solution()

nums = [1,2,3,4,5,6]

print(sol.rotate(nums, 2))
print(nums)