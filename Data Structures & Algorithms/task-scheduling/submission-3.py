from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        if not n:
            return len(tasks)
        hash_map = Counter(tasks)
        max_heap = [-x for x in hash_map.values()]
        heapq.heapify(max_heap)
        time = 0
        queue = deque()

        while queue or max_heap:
            time += 1
            if max_heap:
                count = heapq.heappop(max_heap)
                if count + 1 < 0:
                    queue.append((count + 1, time + n))
            if queue and queue[0][1] <= time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time