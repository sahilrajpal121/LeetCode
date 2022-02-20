# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        res = ans
        curr = 0
        head = head.next
        while head != None:
            if head.val == 0 :
                print(curr)
                if res is None:
                    first = curr
                    res = ListNode(curr)
                else:
                    res.next = ListNode(curr)
                    res = res.next
                curr = 0
            else:
                curr += head.val
            head = head.next
        return ans.next