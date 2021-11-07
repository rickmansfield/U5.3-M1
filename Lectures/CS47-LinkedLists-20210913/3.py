# [3]->[7]->[2]->None
class LinkedListNode:
    """
    - value => A value held in the node
    - next => A reference to the next node in the chain
    """
def __init__(self, value):
    self.value = value
    self.next = None

def __str__(self):
    return f"[{self.value}]->{self.next}"

l = LinkedListNode(3)
l.next = LinkedListNode(7)
l.next.next = LinkedListNode(2)
t = 7

print(l)
def search_ll(l, target):
    current_node = l
    while current_node is not None:
        if current_node.value == target:
            return current_node

        current_node = current_node.next
    return None

found_node = search_ll(l, t)
# print(found_node.value)
