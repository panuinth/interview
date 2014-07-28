# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):

        return '({})'.format(self.val)
class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        #stack
        s = []
        node = head
        while node:
            s.append(node)
            node = node.next
        out = None
        while s:
            print s
            if not out:
                out = s.pop(0)
            else:
                out.next = s.pop(0)
                out = out.next
            if s:
                out.next = s.pop()
                out = out.next
        return out


def test():
    l = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l.next = l2
    l2.next = l3
    print l
    print Solution().reorderList(l)


test()
