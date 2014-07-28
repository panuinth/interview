# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add_node(self, node):
        if not node:
            return
        if self.next:
            self.next.add_node(node)
        else:
            self.next = node
        return self
    def __repr__(self):
        return str(self.val)

    def print_list(self):
        out = ''
        node = self
        while node:
            out += '{} ->'.format(node)
            node = node.next
        return out

def middle(head):
    # return midle element of the linked list
    node2 = head
    node1 = head
    while (node2 and node2.next):
        node1 = node1.next
        node2 = node2.next.next if node2.next else node2.next
    return node1

def add_node(head, node):
    if not node:
        return head
    if not head:
        return node
    if head.next:
        add_node(head.next, node)
    else:
        head.next = node
    return head

class Solution:



    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        # merge sort
        if not head or not head.next:
            return head
        mid = middle(head)
        print mid
        node = head
        left = None # value < mid
        equal = None # value == mid
        right = None # value > mid
        while node:
            tmp = node.next
            node.next = None

            if node.val < mid.val:
                if not left:
                    left = node
                else:
                    add_node(left,node)
            elif node.val == mid.val:
                if not equal:
                    equal = node
                else:
                    add_node(equal, node)
            else:
                if not right:
                    right = node
                else:
                    add_node(right, node)
            node = tmp
        head = add_node(self.sortList(left), equal)
        head = add_node(head, self.sortList(right))
        return head


def test_append(root):
    for i in range(10):
        add_node(root, ListNode(99-i))
    return root

def test_middle(root):
    print middle(root)

def test_sort(root):
    print Solution().sortList(root)



root = ListNode(3)
add_node(root, ListNode(2))
add_node(root, ListNode(4))
#test_append(root)
test_middle(root)

print root.print_list()
test_sort(root)

print root.print_list()
