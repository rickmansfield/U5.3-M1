"""
WARNING this code doesn't work in VS Code without defining the nodes. 
It was desiged to be used with CodeSignal IDE where they are already defined

Example:
l1 = ListNode(1)
l2 = ListNode(3)
l3 = ListNode(4)
l4 = ListNode(5)
l1.next = l2
l2.next = l3
l1.next.next.next = l4 # same ast l3.next=l4

i.e. 
in codeSignal # Singly-linked lists are already defined with this interface:(see class below)
"""
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def insertValueIntoSortedLinkedList(l, value):

    node = ListNode(value)
    
    #EDGE
    if l == None:
        return node
    #FRONT
    if value < l.value:
        node.next = l
        return node
        
    else: #Middle
        cur = l
        prev = None
        # cur, prev = l, None
        #while the new value > current value being evaluated and cur.next is true(there are other values to follow) ...do something... in this case set prev = cur and cur = prev.next
        while value >= cur.value and cur.next:
            prev = cur
            cur = prev.next
        
        #END if value is bigger than last number
        if value >= cur.value and cur.next == None:
            cur.next = node
        else: 
            node.next = prev.next
            prev.next = node
        return l
    
    


# print(insertValueIntoSortedLinkedList([1, 3, 4, 5, 6], 5)) # [1, 3, 4, 5, 6]
# print(insertValueIntoSortedLinkedList([1, 3, 4, 6], 10)) # [1, 3, 4, 6, 10]
# print(insertValueIntoSortedLinkedList([1, 3, 4, 6], 0)) # [0, 1, 3, 4, 6]
# print(insertValueIntoSortedLinkedList([], 239)) # [239]
# print(insertValueIntoSortedLinkedList([239], 240)) #[239, 240]
# print(insertValueIntoSortedLinkedList([1, 3, 4], -100)) #[-100, 1, 3, 4]
# print(insertValueIntoSortedLinkedList([1, 3, 6, 7], 4)) # [1, 3, 4, 6, 7]
# print(insertValueIntoSortedLinkedList([-1000000000, 999999999], 1000000000)) #[-1000000000, 999999999, 1000000000]
