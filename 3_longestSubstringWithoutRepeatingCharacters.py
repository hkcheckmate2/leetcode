class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        chars = set([])
        max_len=j=0
        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[j])
                j += 1
            chars.add(s[i])
            max_len = max(max_len,i-j+1)
            
        return max_len
