# Description: This file contains the implementation of a singly linked list in Python.

# Functionality: print, add, remove, convert array to linked list, convert linked list to array, generate random
# linked list, reverse linked list, merge two linked lists, find specific element
# within linked list

# This contains value and next node
class LinkedListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node


# This contains just the head and tail and key functions to operate on the chain
class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    @staticmethod
    def print_linked_list(start_node):
        while start_node:
            print(str(start_node.val) + " -> ", end="")
            start_node = start_node.next_node

        print("None")

    def add_to_linked_list(self, val):
        if self.head:
            self.tail.next_node = LinkedListNode(val)
            self.tail = self.tail.next_node
        else:
            self.head = LinkedListNode(val)
            self.tail = self.head

    # Removes last element from linked list
    def remove_from_linked_list(self):
        if not self.head:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        prev, curr = None, self.head
        while curr.next_node:
            prev = curr
            curr = curr.next_node

        prev.next_node = None
        self.tail = prev

    @staticmethod
    def array_to_linked_list(arr):
        # Initialize the linked list
        linked_list = LinkedList()

        # Add each element to the linked list
        for i in range(len(arr)):
            linked_list.add_to_linked_list(arr[i])

        return linked_list

    def linked_list_to_array(self):
        array = []
        curr = self.head
        while curr:
            array.append(curr.val)
            curr = curr.next_node

        return array

    @staticmethod
    def generate_random_linked_list(length, min_val=0, max_val=10):
        import random as r
        linked_list = LinkedList()
        for i in range(length):
            linked_list.add_to_linked_list(r.randint(min_val, max_val))

        return linked_list

    # Reverse a linked list
    def reverse_linked_list(self):
        prev, curr = None, self.head
        while curr:
            nxt = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = nxt

        self.head = prev

    # Merging two sorted linked lists in sorted order
    @staticmethod
    def merge_linked_lists(l1, l2):
        merged_linked_list = LinkedList()

        curr1, curr2 = l1.head, l2.head
        if not curr1:
            return l2
        elif not curr2:
            return l1

        while curr1 and curr2:
            if curr1.val < curr2.val:
                merged_linked_list.add_to_linked_list(curr1.val)
                curr1 = curr1.next_node
            else:
                merged_linked_list.add_to_linked_list(curr2.val)
                curr2 = curr2.next_node

        if not curr1:
            while curr2:
                merged_linked_list.add_to_linked_list(curr2.val)
                curr2 = curr2.next_node

        elif not curr2:
            while curr1:
                merged_linked_list.add_to_linked_list(curr1.val)
                curr1 = curr1.next_node

        return merged_linked_list

    @staticmethod
    def find_element_in_linked_list(ll, val):
        prev = None
        curr = ll.head
        pos = None
        while not pos:
            if curr.val == val:
                return prev.next_node
            else:
                prev = curr
                curr = curr.next_node

            if not curr:
                return "Element not found"

#
# # Testing Implementation of Linked List Functions
#
# DK_LL = LinkedList()
# DK_LL.add_to_linked_list(1)
# DK_LL.add_to_linked_list(2)
# DK_LL.add_to_linked_list(3)
#
# LinkedList.print_linked_list(DK_LL.head)
#
# DK_LL.remove_from_linked_list()
#
# LinkedList.print_linked_list(DK_LL.head)
#
# DK_arr = [1, 2, 3, 4, 5]
# DK_LL = LinkedList.array_to_linked_list(DK_arr)
# LinkedList.print_linked_list(DK_LL.head)
# DK_arr = LinkedList.linked_list_to_array(DK_LL)
# print(DK_arr)
#
# DK_Random_LL = LinkedList.generate_random_linked_list(20, 0, 100)
# LinkedList.print_linked_list(DK_Random_LL.head)
#
# # Reversing randomly generated linked list
# DK_Random_LL.reverse_linked_list()
# LinkedList.print_linked_list(DK_Random_LL.head)
#
# # Merging two sorted linked lists
# LL1 = LinkedList()
# LL2 = LinkedList()
#
# for i in range(5):
#     LL1.add_to_linked_list(i)
#     LL2.add_to_linked_list(i + 1)
#
# DK_merged_list = LinkedList.merge_linked_lists(LL1, LL2)
# LinkedList.print_linked_list(DK_merged_list.head)
#
# # Implement random linked list then try find a value within that
# find_val = 3
# DK_Random_LL = LinkedList.generate_random_linked_list(20, 0, 10)
# location = LinkedList.find_element_in_linked_list(DK_Random_LL, find_val)
# LinkedList.print_linked_list(DK_Random_LL.head)
# print(location)  # Note: This prints memory location of the node!
