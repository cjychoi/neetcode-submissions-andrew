import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute Force
        minK = max(piles)
        # print("max = ", max(piles))
        
        for k in range(1, max(piles)+1):
            print("k = ", k)
            hours = 0
            for i in piles:
                hours = hours + math.ceil(i / k)
                print("hours = ", hours)
            if hours <= h:
                minK = min(minK, k)
                print("minK = ", minK)
        return minK