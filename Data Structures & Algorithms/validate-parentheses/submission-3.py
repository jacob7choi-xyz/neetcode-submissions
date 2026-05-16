class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        correspondingBracket = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in correspondingBracket:
                stack.append(char)
            elif not stack or correspondingBracket[stack[-1]] != char:
                return False
            else:
                stack.pop()
        return not stack