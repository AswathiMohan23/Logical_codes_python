# 1.Given a singly-linked list representation of two positive numbers, calculate and
# store their sum in a new list using constant space.
#
# Input: X = 5 —> 7 —> 3 —> 4 —> None, Y = 9 —> 4 —> 6 —> None
# Output: 6 —> 6 —> 8 —> 0 —> None
# Explanation: 5734 + 946 = 6680

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # inserting a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0

        while first is not None or second is not None:
            first_data = 0 if first is None else first.data
            second_data = 0 if second is None else second.data
            sum = carry + first_data + second_data
            carry = 1 if sum >= 10 else 0
            sum = sum if sum < 10 else sum % 10

            # Creating a new node with sum as data
            temp = Node(sum)

            # if this is the first node then set it as head of resultant list
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
            prev = temp

            # Moving first and second pointers to next nodes
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        if carry > 0:
            temp.next = Node(carry)

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    first = LinkedList()
    second = LinkedList()
    list1 = [5, 7, 3, 4]
    print("First List")
    for i in list1:
        first.push(i)
    print(first.printList())
    list2 = [9, 4, 6]
    print("Second List")
    for i in list2:
        second.push(i)
    print(second.printList())
    print("Resultant list")
    res = LinkedList()
    res.addTwoLists(first.head, second.head)
    print(res.printList())
