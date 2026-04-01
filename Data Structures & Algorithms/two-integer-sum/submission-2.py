class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        out = []

        for i in range(len(nums)): # O(n)
            
            diff = target - nums[i]

            if diff in seen: # O(1)
                out.append(seen[diff]) # get index for remainder
                out.append(i)
                return out

            seen[nums[i]] = i

        