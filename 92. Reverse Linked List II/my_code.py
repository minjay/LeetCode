# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n:
            return head
        # create origin
        origin = ListNode(0)
        # make origin point to head
        origin.next = head
        # init left_pointer
        left_pointer = origin
        # move left_pointer to the (m-1)-th node
        for i in range(m-1):
            left_pointer = left_pointer.next
        # init curr as the m-th node
        curr = left_pointer.next
        prev = None
        # reverse the direction of the links n-m+1 times
        for i in range(n-m+1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        # make the m-th node point to the (n+1)-th node or None
        left_pointer.next.next = curr
        # make the (m-1)-th node point to the n-th node
        left_pointer.next = prev
        return origin.next
        