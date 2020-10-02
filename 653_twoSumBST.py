# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        def printInorder(root):   
            if root:              
                return printInorder(root.left) + [root.val] + printInorder(root.right)
            else:
                return []
        
        in_list = printInorder(root)
        
        def twoSum(numbers, target):
            p1 = 0
            p2 = len(numbers)-1
            while p2>p1:
                if numbers[p1] + numbers[p2] == target:
                    return True
                elif numbers[p1] + numbers[p2] < target:
                    p1 += 1
                else:
                    p2 -= 1
                    
        return twoSum(in_list,k)
