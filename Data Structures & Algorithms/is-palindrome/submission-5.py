class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        p: int = 0
        q: int = len(s)-1

        while p < q:
            char_p = ord(s[p])
            char_q = ord(s[q])
            while p < q and not (97 <= char_p <= 122 or 48 <= char_p <= 57):
                p += 1
                char_p = ord(s[p])
            while q > p and not (97 <= char_q <= 122 or 48 <= char_q <= 57):
                q -= 1
                char_q = ord(s[q])
            if char_p != char_q:
                return False
            p += 1
            q -= 1
        
        return True