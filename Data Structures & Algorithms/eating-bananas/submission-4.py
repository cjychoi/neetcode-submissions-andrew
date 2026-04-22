import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        # print("max = ", max(piles))

        while l < r:
            k = (l + r) // 2
            print("k = ", k)

            hours = 0
            for i in piles:
                hours += math.ceil(i / k)
                print("hours = ", hours)
            
            if hours <= h:
                r = k
            else: # hours > h
                l = k + 1
               
        return l