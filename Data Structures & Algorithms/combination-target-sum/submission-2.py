class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index: int, current: List[int], total: int) -> None:
            if total == target:
                res.append(current.copy())
                return
            if total > target or index >= len(nums):
                return
            current.append(nums[index])
            dfs(index, current, total + nums[index])
            current.pop()
            dfs(index + 1, current, total)
        dfs(0, [], 0)
        return res