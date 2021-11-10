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
    new_node = ListNode(value)
    
    #edge
    if l == None:
        return new_node
    
    #front
    if value < l.value:
        new_node = l
        return new_node
    #middile
    current_node = l
    while current_node.next is not None:
        if value < current_node.next.value:
            new_node.next = current_node.next
            current_node.next = new_node
            return l
        
        current_node = current_node.next
        
    # end 
    current_node.next = new_node
    return l