class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(current: List[int]) -> None:
            if len(current) == len(nums):
                res.append(current.copy())
                return
            for i in range(len(nums)):
                if nums[i] in current:
                    continue
                current.append(nums[i])
                dfs(current)
                current.pop()
        dfs([])  
        return res