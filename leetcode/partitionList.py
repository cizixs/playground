# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        small,large,shead,lhead = None,None,None,None
        p = head

        while p:
            if p.val < x:
                if small:
                    shead = p
                    small.next = p
                else:
                    small = p;
            else:
                if large:
                    large.next = p
                else:
                    lhead = p
                    large = p

            p = p.next

        small.next = lhead

        return shead

