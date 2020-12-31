from typing import List
import random
from abc import ABC, abstractmethod

class SolutionBase(ABC):
    """An Array shuffler interface."""
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    @abstractmethod
    def shuffle(self) -> List[int]:
        pass


class Solution(SolutionBase):
    """
    Implements the SolutionBase Class for the shuffle method.
    """
    def __init__(self, nums: List[int]):
        super(Solution, self).__init__(nums)
            
    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array using the random.shuffle method.
        """
        shuffled = self.nums.copy()
        random.shuffle(shuffled)
        return shuffled


nums = [1,2,3]

# Your Solution object will be instantiated and called as such:
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()

print(param_1)
print(param_2)