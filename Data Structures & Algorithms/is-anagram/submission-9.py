class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        count_s = {}
        count_t = {}

        for c in s:
            count_s[c] = count_s.get(c,0) + 1
        
        for c in t:
            count_t[c] = count_t.get(c,0) + 1
        
        print(count_s)
        print(count_t)

        if (set(s) != set(t)) or (len(s) != len(t)) or (count_s != count_t):
            return False
        
        else: 
            return True
        
        