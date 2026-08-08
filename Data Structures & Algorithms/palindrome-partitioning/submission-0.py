class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(index: int, current: List) -> None:
            if index == len(s):
                res.append(current.copy())
                return 
            for i in range(index, len(s)):
                if s[index: i+1] == s[index: i+1][::-1]:
                    current.append(s[index:i+1])
                    dfs(i + 1, current)
                    current.pop()
        dfs(0, [])
        return res