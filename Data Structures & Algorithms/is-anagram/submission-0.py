class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frq = [0]*26
        for char in s.lower():
            frq[ord(char) - ord('a')] += 1
        for char in t.lower():
            frq[ord(char) - ord('a')] -= 1
        return all(f == 0 for f in frq)