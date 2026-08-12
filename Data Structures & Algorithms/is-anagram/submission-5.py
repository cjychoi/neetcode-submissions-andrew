class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) == set(t):
            return True
        else:
            return False