class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = {}
        lt = 0
        sl = 0

        for rt, ch in enumerate(s):
            if ch in ls and ls[ch] >= lt:
                lt = ls[ch] + 1
            ls[ch] = rt
            sl = max(sl, rt - lt + 1)
        
        return sl
