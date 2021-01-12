from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [self.getFizzBuzz(s) for s in range(1, n+1)]

    def getFizzBuzz(self, n: int) -> str:

        fizzBuzz = ""
        if n % 3 == 0:
            fizzBuzz += "Fizz"
        if n % 5 == 0:
            fizzBuzz += "Buzz"
        if fizzBuzz == "":
            fizzBuzz = str(n)

        return fizzBuzz


solution = Solution()

test1 = [
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

assert solution.fizzBuzz(15) == test1

print("All tests passed!")