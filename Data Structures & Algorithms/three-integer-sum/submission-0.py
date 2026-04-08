class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []

        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)-1):
                    if nums[i] + nums[j] + nums[k] == 0:
                        out.append([nums[i], nums[j], nums[k]])
        
        return out
