class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        seen = {} # {num: index}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen: # O(1)
                out.append(seen[diff])
                out.append(i)
                return out
            else:
                seen[num] = i