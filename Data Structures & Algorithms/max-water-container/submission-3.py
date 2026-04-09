class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l, r = 0, len(heights) - 1
        # cur_area = (r - l) * min(heights[l], heights[r])

        # Brute Force - O(n^2)
        # for l in range(len(heights) - 1):
        #     for r in range (len(heights) - 1, l, -1):
        #         print("l = ", l, "r = ", r)
        #         print((r - l) * min(heights[l], heights[r]))
        #         if (r - l) * min(heights[l], heights[r]) > maxVol:
        #             maxVol = (r - l) * min(heights[l], heights[r])
        #             print("maxVol = ", maxVol)
        

        while l < r:
            cur_area = (r - l) * min(heights[l], heights[r])

            if cur_area > max_area:
                    max_area = cur_area

            print("l = ", l, "r = ", r)
            print(max_area)


            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else: # heights[l] == heights[r]:
                l += 1
            

        return max_area