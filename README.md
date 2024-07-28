# LinkedListsPython
Linked List Implementation consisted of initialising two class objects, LinkedListNode and LinkedList. LinkedListNode contains the proper way of finding value and memory location of next node. LinkedList contains data regarding head and tail of the linked list alongside many functions for the manipulation of linked lists.

## FUNCTIONS AVAILABLE FOR USE ##
# Note: Static Method Functions require call to be of form {Variable (if required) = LinkedList.function(inputs)} as opposed to {LLName.function(inputs)}
- print_linked_list
- add_to_linked_list
- remove_from_linked_list
- array_to_linked_list
- linked_list_to_array
- generate_random_linked_list
- reverse_linked_list`` 



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

