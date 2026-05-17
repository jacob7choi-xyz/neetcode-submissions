class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        brackets = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in brackets:
                stack.append(char)
            elif not stack or brackets[stack[-1]] != char:
                return False    
            else:
                stack.pop()
        return not stack
