class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if not operations:
            return 0
        stack = []
        operation_key = {'+', 'D', 'C'}

        for op in operations:
            if op not in operation_key:
                stack.append(int(op))
            elif op == '+':
                prev_sum = stack[-1] + stack[-2]
                stack.append(prev_sum)
            elif op == 'D':
                prev_double = stack[-1] * 2
                stack.append(prev_double)
            elif op == 'C':
                stack.pop()
        return sum(stack)