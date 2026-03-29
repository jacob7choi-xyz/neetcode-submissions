class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = set()

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    res.add(i)
                    res.add(j)
    
        return list(res)