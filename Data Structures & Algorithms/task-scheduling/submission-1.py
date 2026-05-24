from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        if not n:
            return len(tasks)
        count = Counter(tasks)
        max_heap = [-x for x in count.values()]
        heapq.heapify(max_heap)

        queue = deque()

        time = 0

        while queue or max_heap:
            time += 1
            if max_heap:
                val = heapq.heappop(max_heap)          
                if val + 1 < 0:
                    queue.append((val + 1, time + n))      
            if queue and queue[0][1] <= time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time

