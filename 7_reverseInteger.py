class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        rev = 0
        while num>0:
            rev *= 10
            rev += num % 10
            num = num // 10
        
        ans = rev if x>0 else -rev
        return ans if ans>= -2147483648 and abs(ans) <= 2147483647 else 0
