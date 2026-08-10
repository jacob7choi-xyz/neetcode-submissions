class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col, diag, anti_diag = set(), set(), set()
        def dfs(index: int, current: List[str]) -> None:
            if index == n:
                res.append(current.copy())
                return
            for i in range(n):
                if i in col or (index - i) in diag or (index + i) in anti_diag:
                    continue
                col.add(i)
                diag.add(index - i)
                anti_diag.add(index + i)
                current.append(('.' * i) + 'Q' + ('.' * (n-i-1)))
                dfs(index + 1, current)
                col.remove(i)
                diag.remove(index - i)
                anti_diag.remove(index + i)
                current.pop()
        dfs(0, [])
        return res