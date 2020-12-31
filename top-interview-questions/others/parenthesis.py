class Solution:

    def __init__(self):
        self.pMap = {
                   ')': '(',
                   '}': '{',
                   ']': '['
        }

        self.pSwitch = {
                   '(': 0,
                   '{': 0,
                   '[': 0
        }


    def isValid(self, s: str) -> bool:
        """Tests if the input string is valid for parenthesis
        """
        for c in s:
            if c in ['(', '{', '[']:
                self.pSwitch[c] += 1
            else:
                self.pSwitch[self.pMap[c]] -= 1
                if self.pSwitch[self.pMap[c]] > 0:
                    return False

        for key, value in self.pSwitch.items():
            if value != 0:
                return False


        return True


sol = Solution()

failString = "([)]"


print(sol.isValid(testString))