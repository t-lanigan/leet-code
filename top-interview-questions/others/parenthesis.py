class Solution:


    def isValid(self, s: str) -> bool:
        """Tests if the input string is valid for parenthesis
        """
        pMap = {
                   ')': '(',
                   '}': '{',
                   ']': '['
        }

        pStack = []
        for c in s:
            if c in ['(', '{', '[']:
                pStack.append(c)
            else:
                if len(pStack) == 0:
                    return False
                if pMap[c] != pStack.pop():
                    return False

        if len(pStack) != 0:
            return 0

        return True


sol = Solution()

testString = "(){}[]["


print(sol.isValid(testString))