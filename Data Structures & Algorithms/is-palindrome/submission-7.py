import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # print(re.sub(r'[^a-zA-Z]', '', s).lower())
        # s_list = list(re.sub(r'[^a-zA-Z0-9]', '', s).lower())
        s_list = list(s)
        # print(s_list)

        if len(s_list) == 1:
            return True

        left = 0
        right = len(s_list) - 1

        while left < right:
            # if s_list[left] != s_list[right]:
            if s_list[left].lower() != s_list[right].lower():
                return False
            left += 1
            right -= 1

        return True