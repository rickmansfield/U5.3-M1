# Singly-linked lists are already defined with this interface:
"""
WARNING this code doesn't work in VS Code without defining the nodes. 
It was desiged to be used with CodeSignal IDE where they are already defined
"""
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
def insertValueIntoSortedLinkedList(l, value):
    # create a new node with the value
    node = ListNode(value)
    # if there is no list return the new node
    if l == None:
        return node
    else:
        # else if the list.value (first item in the list) > the new value
        if l.value > value:
            # set new values as the first item in the list
            node.next = l
            return node
        else:
            # else create a temp value for the current list item and the previous set to None
            temp, prev = l, None
                    #same as 
                    #temp = 1
                    #prev = None
            # while the there is a next item and current item value is less
            # than the value iterate
            while temp.next and temp.value <= value:
                # set previous to temp and temp to next
                prev = temp
                temp = temp.next
            # check if temp.next is None (last item) and still not larger than the value
            if temp.next == None and temp.value <= value:
                # if so add the value as the last item in the list since it is the largest
                temp.next = node
            else:
                # else if the next item is larger than the value set the next item as the next item of the new value
                node.next = prev.next
                # and set the previous item to point to the new value next
                prev.next = node
            # return the list
            return l