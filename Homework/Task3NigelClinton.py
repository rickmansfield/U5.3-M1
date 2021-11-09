class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def mergeTwoLinkedLists(l1, l2):
    if l1 == None: return l2
    if l2 == None: return l1
    if l1.value < l2.value:
        head_node = l1
        l1 = l1.next
    else:
        head_node = l2
        l2 = l2.next
    current = head_node
    while l1 and l2:
        if l1.value <= l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return head_node