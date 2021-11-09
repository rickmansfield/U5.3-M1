class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def insertValueIntoSortedLinkedList(l, value):
    node = ListNode(value)
    if l == None:
        return node
    else:
        if l.value > value:
            node.next = l
            return node
        else:
            cur, prev = l, None
            while cur.next and cur.value <= value:
                prev = cur
                cur = cur.next
            if cur.next == None and cur.value <= value:
                cur.next = node
            else:
                node.next = prev.next
                prev.next = node
            return l