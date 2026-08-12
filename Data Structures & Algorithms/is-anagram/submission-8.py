class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (set(s) == set(t)) & (len(s) == len(t)):
            return True
        else:
            return False