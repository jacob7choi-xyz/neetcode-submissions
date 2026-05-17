class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if not operations:
            return 0
        stack = []

        for op in operations:
            if op == '+':
                prev_sum = stack[-1] + stack[-2]
                stack.append(prev_sum)
            elif op == 'D':
                prev_double = stack[-1] * 2
                stack.append(prev_double)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)