class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return "".join(sorted(s)) == "".join(sorted(t))
        count_s = {}
        count_t = {}
        # count_s, count_t = {}, {}

        for c in s:
            # if c not in count_s:
            #     count_s[c] = 1
            # else:
            #     count_s[c] += 1
            count_s[c] = count_s.get(c, 0) + 1
        for c in t:
            # if c not in count_t:
            #     count_t[c] = 1
            # else:
            #     count_t[c] += 1
            count_t[c] = count_t.get(c, 0) + 1

        return count_s == count_t