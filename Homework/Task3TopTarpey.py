"""
WARNING this is a GOOD solution that works. 
But, it does not run in vs code without the class reference below
The class reference below has 

"""
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
        
def insertValueIntoSortedLinkedList(l, value):
    new_node = listNode(value)
    
    #edge
    if not l == None:
        return new_node
    
    #front
    if value < l.value:
        new_node = l
        return new_node
    #middile
    current = l
    while current.next is not None:
        if value < current.next.value:
            new_node.next = current.next
            current.next = new_node
            return l
        
        current = current.next
        
    # end 
    current.next = new_node
    return l