class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            if x == y:
                continue
            else:
                x = x - y
                heapq.heappush(max_heap, -x) 

        return -max_heap[0] if len(max_heap) == 1 else 0

