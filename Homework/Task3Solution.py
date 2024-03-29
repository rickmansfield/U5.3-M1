"""
WARNING this code doesn't work in VS Code without defining the nodes. 
and creating a local print function to call here. 
i.e. 
in codeSignal # Singly-linked lists are already defined with this interface:(see class below)
"""
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def printLinkedList(head_node):
    if head_node is None:
        print("Nothing there")
        
    current_node = head_node
    ans = ""
    
    while current_node is not None:
        ans = ans + f"[{current_node.value}]->"
        current_node = current_node.next
    return ans


def insertValueIntoSortedLinkedList(l, value):

    node = ListNode(value)
    
    #EDGE
    if l == None:
        return printLinkedList(node)
    #FRONT
    if value < l.value:
        node.next = l
        return printLinkedList(node)
        
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
        return printLinkedList(l)
    

l1 = ListNode(1)
l2 = ListNode(3)
l3 = ListNode(4)
l4 = ListNode(6)
l1.next = l2
l2.next = l3
l3.next = l4

print(insertValueIntoSortedLinkedList(l1, 5)) # [1, 3, 4, 5, 6]
# print(insertValueIntoSortedLinkedList([1, 3, 4, 6], 10)) # [1, 3, 4, 6, 10]
# print(insertValueIntoSortedLinkedList([1, 3, 4, 6], 0)) # [0, 1, 3, 4, 6]
# print(insertValueIntoSortedLinkedList([], 239)) # [239]
# print(insertValueIntoSortedLinkedList([239], 240)) #[239, 240]
# print(insertValueIntoSortedLinkedList([1, 3, 4], -100)) #[-100, 1, 3, 4]
# print(insertValueIntoSortedLinkedList([1, 3, 6, 7], 4)) # [1, 3, 4, 6, 7]
# print(insertValueIntoSortedLinkedList([-1000000000, 999999999], 1000000000)) #[-1000000000, 999999999, 1000000000]
