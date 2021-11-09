def mergeTwoLinkedLists(l1, l2):
    cur1, cur2 = l1, l2
    new_head, prev = None, None
    while cur1 is not None or cur2 is not None:
        if cur1 is None:
            if prev:
                prev.next = cur2
            if new_head is None:
                new_head = cur2
            prev = cur2
            cur2 = cur2.next
            break
        elif cur2 is None:
            if prev:
                prev.next= cur1
            if new_head is None:
                new_head = cur1
            prev = cur1
            cur1 = cur1.next
            break
        else:
            if cur1.value <= cur2.value:
                if prev:
                    prev.next = cur1
                if new_head is None:
                    new_head = cur1
                prev = cur1
                cur1 = cur1.next
            else:
                if prev:
                    prev.next = cur2
                if new_head is None:
                    new_head = cur2
                prev = cur2
                cur2 = cur2.next
    return new_head