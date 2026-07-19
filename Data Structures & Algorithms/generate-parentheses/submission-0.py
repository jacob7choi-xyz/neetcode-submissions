class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        open_count = 0
        close_count = 0
        def dfs(open_count: int, close_count: int, current: str) -> None:
            if open_count == close_count == n:
                res.append(current)
                return
            if open_count < n:
                dfs(open_count + 1, close_count, current + "(")
            if close_count < open_count: 
                dfs(open_count, close_count + 1, current + ")")
        dfs(0, 0, "")
        return res
