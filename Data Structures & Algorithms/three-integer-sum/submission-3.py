class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        # print(nums)

        for i in range(len(nums)-2):
            # Skip duplicate
            if i>0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            j = i+1
            k = len(nums)-1

            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else: # nums[j] + nums[k] == target
                    # if [nums[i], nums[j], nums[k]] not in out:
                    out.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicates
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return out
