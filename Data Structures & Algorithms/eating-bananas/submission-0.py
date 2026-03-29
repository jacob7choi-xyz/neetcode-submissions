class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  
        
        while l < r:
            mid = l + (r-l) // 2
            total_hours = 0

            for i in range(len(piles)):
                total_hours += (piles[i] + mid - 1) // mid # MEMORIZE THIS CEILING DIVISION FORMULA
            if total_hours <= h:
                r = mid
            else:
                l = mid + 1
        return l or r
        