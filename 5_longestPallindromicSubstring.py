class Solution:
    def longestPalindrome(self, s: str) -> str:
        def largestPalindromeAtIndex(s,left,right):
            leftIndex = left
            rightIndex = right
            while leftIndex >=0 and rightIndex < len(s):
                if s[leftIndex] == s[rightIndex]:
                    leftIndex -= 1
                    rightIndex += 1
                else:
                    break
            return (rightIndex - leftIndex + 1)
        
        start = 0
        end = 0
        for i in range(len(s)):    
            lengthOddPalindrome = largestPalindromeAtIndex(s,i,i)
            lengthEvenPalindrome = largestPalindromeAtIndex(s,i,i+1)
            length = max(lengthOddPalindrome,lengthEvenPalindrome)
            if length > (end-start):
                start = i - ((length-1)//2)
                end = i + (length//2)
        return s[start+1:end]
