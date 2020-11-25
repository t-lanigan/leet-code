# Given a sorted array nums, remove the duplicates in-place 
# such that each element appears only once and returns the new length.
# Do not allocate extra space for another array,
# you must do this by modifying the input array in-place withO(1) extra memory.


class Solution:
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 1
        if len(nums) == 0:
            return 0
            
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[x] = nums[i]
                x +=1
        return x

# sorted array
nums = [1, 2, 2, 3, 4, 4]


ans = Solution.removeDuplicates(nums)