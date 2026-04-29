class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        out = []

        for i in range(len(nums)):

            diff = target - nums[i]

            if diff in seen:
                out.append(seen[diff])
                out.append(i)
                return out
                
            seen[nums[i]] = i