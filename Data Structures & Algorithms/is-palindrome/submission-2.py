import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # print(re.sub(r'[^a-zA-Z]', '', s).lower())
        s_list = list(re.sub(r'[^a-zA-Z]', '', s).lower())
        # print(s_list)

        left = 0
        right = len(s_list) - 1

        while left < right and left != right:
            if s_list[left] != s_list[right]:
                return False
            left += 1
            right -= 1

        return True