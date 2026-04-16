class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        max_length = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
            else:
                seen.discard(s[l])
                l += 1
                continue
            
            max_length = max(max_length, r-l+1)
            r += 1

        return max_length