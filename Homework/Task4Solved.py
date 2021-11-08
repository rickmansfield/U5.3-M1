# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    mergedList = ListNode(0)
    end = mergedList
    
    # while True:
    #     if l1 is None:
    #         end.next = l2
    #         break
    #     if l2 is None:
    #         end.next = l1
    #         break
    while l1 and l2:
        if l1.value <= l2.value:
            mergedList.next = l1
            l1 = l1.next
        else: 
            mergedList.next = l2
            l2 = l2.next
    mergedList = mergedList.next
    return end.next

"""
tests
"""
print(mergeTwoLinkedLists([1, 2, 3], [4, 5, 6])) # [1, 2, 3, 4, 5, 6]
print(mergeTwoLinkedLists([1, 1, 2, 4], [0, 3, 5])) # [0, 1, 1, 2, 3, 4, 5]
print(mergeTwoLinkedLists([5, 10, 15, 40], [2, 3, 20])) # [2, 3, 5, 10, 15, 20, 40]
print(mergeTwoLinkedLists([1, 1], [2, 4])) # [1, 1, 2, 4]
print(mergeTwoLinkedLists([], [1, 1, 2, 2, 4, 7, 7, 8] )) # [1, 1, 2, 2, 4, 7, 7, 8]
print(mergeTwoLinkedLists([], [])) # []
print(mergeTwoLinkedLists( [1, 1, 4], [])) # [1, 1, 4]
print(mergeTwoLinkedLists([1, 1] [0])) # [0, 1, 1] 
print(mergeTwoLinkedLists([0], [2])) # [0,2] 
print(mergeTwoLinkedLists([1], [-1000000000, 1000000000])) # [-1000000000, 1, 1000000000]
print(mergeTwoLinkedLists([-1, -1, 0, 1], [-1, 0, 0, 1, 1])) # [-1, -1, -1, 0, 0, 0, 1, 1, 1]
print(mergeTwoLinkedLists([-780990573, -670826849, -404817961, 242026249, 731519938], [-815817641, -426491047, 437929670, 520408640])) # [-815817641, -780990573, -670826849, -426491047, -404817961, 242026249, 437929670, 520408640, 731519938]
