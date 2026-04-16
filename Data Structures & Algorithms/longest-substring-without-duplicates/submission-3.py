class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l, r = 0, 0
        max_length = 0

        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
            else:
                window.discard(s[l])
                l += 1
                continue
            
            max_length = max(max_length, len(window))
            r += 1

        return max_length