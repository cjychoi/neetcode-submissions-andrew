class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        mid = int((l + r) / 2)

        while mid != l:
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid
            else: # target > nums[mid]
                l = mid
            
            mid = int((l + r) / 2)
        
        if target == nums[r]:
            return r
        else:
            return -1