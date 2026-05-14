class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        length = 0
        for i in nums_set:
            if i - 1 not in nums_set:
                count = 0
                while i in nums_set:
                    i += 1
                    count += 1
                length = max(length, count)
        return length