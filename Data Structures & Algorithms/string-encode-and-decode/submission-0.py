class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string: str = ""
        for string in strs:
            encoded_string += f"{len(string)}#{string}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs: List[str] = []

        i = 0
        while i < len(s):
            string_len = ''
            while s[i] != '#':
                string_len += s[i]
                i += 1
            strs.append(s[i+1:i+int(string_len)+1])
            i += int(string_len) + 1
            string_len = ''
        
        return strs