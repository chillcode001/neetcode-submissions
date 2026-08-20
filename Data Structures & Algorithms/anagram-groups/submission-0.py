class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def create_signature(string: str):
            count = [0]*26
            for char in string:
                count[ord(char) - ord('a')] += 1
            return tuple(count)
        
        map = {}
        for string in strs:
            key = create_signature(string)
            if key not in map.keys():
                map[key] = []
            map[key].append(string)
        
        return [group for key, group in map.items()]