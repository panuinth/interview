# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return '({})'.format(str(self.val))

    def printl(self):
        if self.next:
            return '{} -> {}'.format(self, self.next.printl())
        else:
            return self

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    # 1 -> 2 -> 3 -> 4 -> 5
    #     (s)       (e)
    def reverseLL(self, head, n):
        prev = None
        nxt = None
        index = head
        print 'xx'
        while index and n >= 0:
            nxt = index.next
            index.next = prev
            prev = index
            index = nxt
            n -= 1

        head.next = index
        print prev.printl()
        return prev

    def reverseBetween(self, head, m, n):
        if not head:
            return head
        index = head
        for i in range(m-1):
                index = index.next


        index = self.reverseLL(index, n - m)
        return head

def test():
    root = ListNode(1)
    node = root
    for i in range(2, 6):
        l = ListNode(i)
        node.next = l
        node = node.next

    print root.printl()
#    print Solution().reverseLL(root, 3).printl()
    print Solution().reverseBetween(root, 2, 4).printl()

test()
