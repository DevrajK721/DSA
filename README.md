# LinkedListsPython
Linked List Implementation consisted of initialising two class objects, LinkedListNode and LinkedList. LinkedListNode contains the proper way of finding value and memory location of next node. LinkedList contains data regarding head and tail of the linked list alongside many functions for the manipulation of linked lists.

## FUNCTIONS AVAILABLE FOR USE ##
## Note: Static Method Functions require call to be of form {Variable (if required) = LinkedList.function(inputs)} as opposed to {LLName.function(inputs)} ##

# print_linked_list
'''
DK_LL = LinkedList()
LinkedList.print_linked_list(DK_LL.head)
'''
# add_to_linked_list
'''
DK_LL.add_to_linked_list(1)
DK_LL.add_to_linked_list(2)
DK_LL.add_to_linked_list(3)
'''
# remove_from_linked_list
'''
DK_LL.remove_from_linked_list()
LinkedList.print_linked_list(DK_LL.head)
'''
# array_to_linked_list
'''
DK_arr = [1, 2, 3, 4, 5]
DK_LL = LinkedList.array_to_linked_list(DK_arr)
LinkedList.print_linked_list(DK_LL.head)
'''
# linked_list_to_array
'''
DK_arr = LinkedList.linked_list_to_array(DK_LL)
print(DK_arr)
'''
# generate_random_linked_list
'''
DK_Random_LL = LinkedList.generate_random_linked_list(20, 0, 100)
LinkedList.print_linked_list(DK_Random_LL.head)
'''
# reverse_linked_list
'''
DK_Random_LL.reverse_linked_list()
LinkedList.print_linked_list(DK_Random_LL.head)
'''
# merge_linked_lists
'''
LL1 = LinkedList()
LL2 = LinkedList()

for i in range(5):
    LL1.add_to_linked_list(i)
    LL2.add_to_linked_list(i + 1)

DK_merged_list = LinkedList.merge_linked_lists(LL1, LL2)
LinkedList.print_linked_list(DK_merged_list.head)
'''
# find_element_in_linked_list
'''
find_val = 3
DK_Random_LL = LinkedList.generate_random_linked_list(20, 0, 10)
location = LinkedList.find_element_in_linked_list(DK_Random_LL, find_val)
LinkedList.print_linked_list(DK_Random_LL.head)
print(location)  # Note: This prints memory location of the node!
'''
