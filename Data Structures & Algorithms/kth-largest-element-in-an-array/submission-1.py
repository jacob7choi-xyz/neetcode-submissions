class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or not k:
            return 0
        heapq.heapify(nums)

        for i in range(len(nums) - k):
            heapq.heappop(nums)
        return nums[0]