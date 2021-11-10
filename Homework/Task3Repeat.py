"""this block of code preps the solution to run and print in vs code
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

"""
The rest of the code below is the solution to the problem. 
"""
def insertValueIntoSortedLinkedList(l, value):
    # create a new node from the parameter 