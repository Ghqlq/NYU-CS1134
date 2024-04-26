
#question 4

from DoublyLinkedList import DoublyLinkedList

#a
def copy_linked_list(lnk_lst):
    new = DoublyLinkedList()
    for elem in lnk_lst:
        new.add_last(elem)
    return new

#b
def deep_copy_linked_list(lnk_lst):
    new = DoublyLinkedList()
    for elem in lnk_lst:
        if isinstance(elem, int):
            new.add_last(elem)
        else:
            new.add_last(deep_copy_linked_list(elem))
    return new


