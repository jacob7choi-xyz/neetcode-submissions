class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return []
        hash_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def dfs(index: int, current: str) -> None:
            if index == len(digits):
                res.append(current)
                return
            for i in hash_map[digits[index]]:
                dfs(index+1, current+i)
        dfs(0,"")
        return res