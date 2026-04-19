import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute Force
        minK = 999999999
        
        for k in piles:
            print("k = ", k)
            hours = 0
            for i in piles:
                hours = hours + math.ceil(i / k)
                print("hours = ", hours)
            if hours <= h:
                minK = min(minK, k)
                print("minK = ", minK)
        return minK