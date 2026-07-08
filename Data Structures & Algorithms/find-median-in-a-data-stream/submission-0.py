class MedianFinder:

    def __init__(self):
        self.bottom_half = []
        self.upper_half = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.bottom_half, -num)
        if self.upper_half and -self.bottom_half[0] > self.upper_half[0]:
            heapq.heappush(self.upper_half, -heapq.heappop(self.bottom_half))
        if (len(self.bottom_half) - len(self.upper_half)) > 1:
            heapq.heappush(self.upper_half, -heapq.heappop(self.bottom_half))
        if (len(self.upper_half) - len(self.bottom_half) > 1):
            heapq.heappush(self.bottom_half, -heapq.heappop(self.upper_half))            

    def findMedian(self) -> float:
        if (len(self.bottom_half) + len(self.upper_half)) % 2 == 0:
            val = (-self.bottom_half[0] + self.upper_half[0]) / 2
        else: 
            if len(self.bottom_half) > len(self.upper_half):
                val = -self.bottom_half[0]
            elif len(self.bottom_half) < len(self.upper_half):
                val = self.upper_half[0]
        return val


        