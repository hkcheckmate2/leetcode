class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def jugaad(nums,x):
            try:
                return nums[x]
            except:
                return float('inf')
            
        top = None
        top_ka_beta = None
        
        n = len(nums1)
        m = len(nums2)
        tot = (n+m)//2
        x=y=0
        
        for i in range(tot+1):
            top_ka_beta = top
            if jugaad(nums1,x) < jugaad(nums2,y):
                top = nums1[x]
                x += 1
            else:
                top = nums2[y]
                y += 1
        
        return top if (n+m)&1 else (top + top_ka_beta)/2
