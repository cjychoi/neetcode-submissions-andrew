class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            hours = 0
            k = (l + r) // 2

            for i in piles:
                hours += math.ceil(i / k)
            
            if hours <= h:
                r = k
            else: # hours > h
                l = k + 1
            
        return l