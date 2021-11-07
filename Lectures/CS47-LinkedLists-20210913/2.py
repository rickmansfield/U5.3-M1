"""
[3]->[7]->[2]->None

l = LinkedListNode(3)
l.next = LinkedListNode(7)
l.next.next = LinkedListNode(2)
"""
current_node = l
while current_node is not None:
  print(current_node.value)

  current_node = current_node.next