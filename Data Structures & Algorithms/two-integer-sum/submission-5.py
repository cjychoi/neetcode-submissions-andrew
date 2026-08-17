class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        seen = {} # dict {num: index}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen: # O(1)
                # out.append(seen[diff])
                # out.append(i)
                # return out 
                return [seen[diff], i]
            
            # else:   # if diff not in seen, add this num and index
            seen[num] = i