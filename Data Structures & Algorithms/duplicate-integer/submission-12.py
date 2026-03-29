class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_nums = {}

        for i in range(len(nums)):
            hash_nums[nums[i]] = hash_nums.get(nums[i], 0) + 1
            if hash_nums[nums[i]] > 1:
                return True
        return False