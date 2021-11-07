# memory[34534] = l
# memory[34534] = l.value (5)
# memory[34550] = l.next (767543)
# memory[767543] = l.next.value (6)
# memory[767559] = l.next.next (None)
# [5]->[6]->None
# Linked List Node

class LinkedListNode:
  """
  - value => A value held in the node
  - next => A reference to the next node in the chain
  """
  def __init__(self, value):
    self.value = value
    self.next = None

l = LinkedListNode(5)
l.next = LinkedListNode(6)
