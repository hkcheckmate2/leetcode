class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start = 0
        while s[start] == " ":
            start += 1
            if start == len(s): return 0
        num = 0
        i = 1+start if s[start]=='-' or s[start]=='+' else start
        digits = {'1','2','3','4','5','6','7','8','9','0'}
        while i<len(s):
            if s[i] in digits:
                num *= 10
                num += int(s[i])
            else: break
            i += 1
        ans = -num if s[start] == '-' else num
        
        if ans<-2147483648:
            return -2147483648
        elif ans>2147483647:
            return 2147483647
        else: return ans
