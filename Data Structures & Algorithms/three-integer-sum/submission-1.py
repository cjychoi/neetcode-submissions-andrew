class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        print(nums)

        for i in range(0, len(nums)-1):
            target = -nums[i]
            j = i+1
            k = len(nums)-1

            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else: # nums[j] + nums[k] == target
                    out.append([nums[i], nums[j], nums[k]])
                


        # for i in range(0, len(nums)-1):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)-1):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 out.append([nums[i], nums[j], nums[k]])
        
        return out
