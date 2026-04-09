class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0

        l, r = 0, len(heights) - 1

        for l in range(0, len(heights) - 1):
            for r in range (len(heights) - 1, l + 1, -1):
                if (r - l) * min(heights[l], heights[r]) > maxVol:
                    maxVol = (r - l) * min(heights[l], heights[r])
        
        return maxVol