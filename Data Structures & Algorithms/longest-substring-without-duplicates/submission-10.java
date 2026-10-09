class Solution {
    public int lengthOfLongestSubstring(String s) {
        int start = 0, longest = 0;
        Set<Character> hs = new HashSet<>();
        for(int end=0; end<s.length(); end++) {
            while(hs.contains(s.charAt(end))) {
                hs.remove(s.charAt(start++));
            }
            hs.add(s.charAt(end));
            longest = Math.max(longest, end - start + 1);
        }
        return longest;
    }
}
