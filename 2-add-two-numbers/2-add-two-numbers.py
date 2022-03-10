# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        s1 = list(reversed(list(map(str, s1))))
        s2 = list(reversed(list(map(str, s2))))
        s1 = int(''.join(s1))
        s2 = int(''.join(s2))
        res = str(s1 + s2)[::-1]
        
        dummy = ll = ListNode()
        
        for char in res:
            ll.next = ListNode(int(char))
            ll = ll.next
        return dummy.next
        
        
            