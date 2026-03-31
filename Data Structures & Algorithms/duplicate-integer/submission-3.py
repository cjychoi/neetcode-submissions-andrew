class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Brute force solution - O(n^2)
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
        """

        # Hash Set O(n)
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
