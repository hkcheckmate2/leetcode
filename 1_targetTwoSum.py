class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        def ulta(nums,dest):
            for i in range(len(nums)-1,-1,-1):
                if nums[i] == dest:
                    return i
            
        a = set(nums)
        ele_1 = ele_2 = None
    
        for x in range(len(nums)):
            z = target - nums[x]
            if z in a:
                ele_1 = x
                #ele_2 = nums.index(target - nums[x])
                ele_2 = ulta(nums,z)
                if ele_1 == ele_2:
                    pass
                else:
                    break
        return [ele_1,ele_2]
    
    # [3,2,3]
    # target = 6
