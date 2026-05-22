class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points or not k:
            return None
        min_heap = [(x**2 + y**2, x, y) for x, y in points]    
        heapq.heapify(min_heap)    
        res = []

        for i in range(k):
            distance, x, y = heapq.heappop(min_heap)
            res.append([x,y])
        return res