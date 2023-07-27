# 2.Given a singly-linked list of integers, rearrange its nodes to be sorted in
# increasing order.
# Input : 6 —> 3 —> 4 —> 8 —> 2 —> 9 —> None
# Output: 2 —> 3 —> 4 —> 6 —> 8 —> 9 —> None
# Input : 9 —> -3 —> 5 —> -2 —> -8 —> -6 —> None
# Output: -8
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

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    value = LinkedList()
    list1 = [5, 7, 3, 4]
    print("First List")
    for i in list1:
        value.push(i)
    print(value.printList())