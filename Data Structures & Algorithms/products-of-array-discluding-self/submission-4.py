class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return None
        result = []

        prefix, suffix = 1, 1
        for i in range(len(nums)):
            result.append(prefix)
            prefix = prefix * nums[i]
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix = suffix * nums[i]
        return result