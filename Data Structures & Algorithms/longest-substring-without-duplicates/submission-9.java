class Solution {
    public int lengthOfLongestSubstring(String s) {
        int start = 0, end = start + 1, longest = 0;
        Set<Character> hs = new HashSet<Character>();
        if(s.length() > 0) {
            hs.add(s.charAt(start));
            while(end < s.length()) {
                if(hs.contains(s.charAt(end))) {
                    start++; end = start;
                    if(longest < hs.size()){ longest = hs.size();}
                    hs.clear();
                    hs.add(s.charAt(start));
                } else {
                    hs.add(s.charAt(end));
                }
                end++;
            }
        }
        return longest > hs.size() ? longest : hs.size();
    }
}
