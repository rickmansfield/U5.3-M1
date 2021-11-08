def mergeTwoLinkedLists(l1, l2):
    # create empty node to hold the new merged list
    merged_node = ListNode(0)
    # end will hold the end node
    end = merged_node
    while True:
        # if either list becomes empty join lists
        if l1 is None:
            end.next = l2
            break
        if l2 is None:
            end.next = l1
            break
        # merge the smaller list to the end of the larger and create a head from the merged list
        if l1.value <= l2.value:
            end.next = l1
            l1 = l1.next
        else:
            end.next = l2
            l2 = l2.next
        # iterate the end node
        end = end.next
    return merged_node.next