class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
        
def insertValueIntoSortedLinkedList(l, value):
    # Create a new node with a value of "value"
    newNode = ListNode(value)
    # Edge case: Handle node with None type / empty list
    if l == None:
        return newNode
    current_node = l
    # Case: Insert new node at begining of list
    if newNode.value < current_node.value:
        newNode.next = current_node
        return newNode
    # Case: Insert new node somewhere in the middle
    # Traverse through list 
    while current_node.next != None:
        # print(current_node.value)
        if newNode.value > current_node.value and newNode.value < current_node.next.value:
            newNode.next = current_node.next
            current_node.next = newNode
            return l
        current_node = current_node.next
    # Case: Insert new node at end of list
    current_node.next = newNode
    return l