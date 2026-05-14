class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        longest = 0
        for i in num_set:
            if i - 1 not in num_set:   
                length = 0
                while i in num_set:
                    i += 1
                    length += 1
                longest = max(longest, length)
        return longest