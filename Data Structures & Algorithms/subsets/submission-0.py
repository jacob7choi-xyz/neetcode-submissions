class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index: int, current: List[int]) -> List[List[int]]:
            if index == len(nums):
                res.append(current)
                return
            backtrack(index + 1, current + [nums[index]])
            backtrack(index + 1, current)
        backtrack(0, [])
        return res
        