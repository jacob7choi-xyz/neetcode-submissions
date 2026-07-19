class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(index: int, current: List[int]) -> None:
            res.append(current.copy())
            for i in range(index, len(nums)):
                if nums[i] == nums[i - 1] and i > index:
                    continue
                current.append(nums[i])
                dfs(i + 1, current)
                current.pop()
        dfs(0, [])
        return res