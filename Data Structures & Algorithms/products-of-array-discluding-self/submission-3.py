class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return None
        output = []

        prefix, suffix = 1, 1
        for i in range(len(nums)):
            output.append(prefix)
            prefix = nums[i] * prefix
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix
            suffix = nums[i] * suffix
        return output