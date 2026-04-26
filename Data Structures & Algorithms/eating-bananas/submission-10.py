class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            hours = 0
            k = (l + r) // 2

            for i in piles:
                hours += math.ceil(i / k)
            
            if hours <= h: # if current k works, check smaller k values
                r = k
            else: # hours > h ; if current k doesn't work, check larger k values
                l = k + 1
            
        return l