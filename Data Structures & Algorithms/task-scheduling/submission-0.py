class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        if not n:
            return len(tasks)
        hash_map = {}
        for task in tasks:
            hash_map[task] = hash_map.get(task, 0) + 1

        max_heap = [-count for count in hash_map.values()]
        heapq.heapify(max_heap)

        queue = deque() # stores [-count, available_at]
        time = 0

        while max_heap or queue:
            time += 1
            if max_heap:
                count = heapq.heappop(max_heap)
                if count + 1 < 0:
                    queue.append((count + 1, time + n)) 
            if queue and queue[0][1] <= time:
                count, available_at = queue.popleft()
                heapq.heappush(max_heap, count)
        return time