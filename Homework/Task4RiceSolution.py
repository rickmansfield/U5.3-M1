class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def mergeTwoLinkedLists(l1, l2):
    head = merged = ListNode(0)
    while l1 and l2:
        if l1.value < l2.value:
            merged.next = l1
            l1 = l1.next
        else:
            merged.next = l2
            l2 = l2.next
        merged = merged.next
    merged.next = l1 or l2
    return head.next
