# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = l1.val + l2.val
        carry = temp//10
        data = temp%10
        head = ListNode(data)
        curr = head
        
        l1 = l1.next
        l2 = l2.next
            
        while l1 and l2:
            temp = carry + l1.val + l2.val
            carry = temp//10
            data = temp%10
            
            l1 = l1.next
            l2 = l2.next
                                       
            curr.next = ListNode(data)
            curr = curr.next
        
        while l1:
            temp = carry + l1.val
            carry = temp//10
            data = temp%10
            
            l1 = l1.next
                                       
            curr.next = ListNode(data)
            curr = curr.next
        
        while l2:
            temp = carry + l2.val
            carry = temp//10
            data = temp%10
            
            l2 = l2.next
                                       
            curr.next = ListNode(data)
            curr = curr.next
        
        while carry:
            temp = carry
            carry = temp//10
            data = temp%10
                                       
            curr.next = ListNode(data)
            curr = curr.next
        
        
        return head
