class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Sliding window is necessary for this problem
        # since you're checking adjacent characters
        s1_count = {}
        window_count = {}

        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1

        for i in range(len(s1)):
            c = s2[i]
            window_count[c] = window_count.get(c, 0) + 1

        if s1_count == window_count:
            return True

        for r in range(len(s1), len(s2)):
            window_count[s2[r]] = window_count.get(s2[r], 0) + 1

            l = r - len(s1)
            window_count[s2[l]] -= 1
            if window_count[s2[l]] == 0:
                del window_count[s2[l]]
            
            if s1_count == window_count:
                return True
        return False