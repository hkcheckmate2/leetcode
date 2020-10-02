class Solution:
    def isPalindrome(self, x: int) -> bool:
        xRef = x
        xAns = 0
        while xRef>0:
            xAns *= 10
            xAns += xRef % 10
            xRef = xRef // 10
        return True if xAns == x else False
