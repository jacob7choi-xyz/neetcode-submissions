class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(index: int, current: List[int], total: int) -> None:
            if total == target:
                res.append(current.copy())
                return
            if total > target or index >= len(candidates):
                return
            for i in range(index, len(candidates)): 
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                dfs(i + 1, current, total + candidates[i])
                current.pop()
        dfs(0, [], 0)
        return res