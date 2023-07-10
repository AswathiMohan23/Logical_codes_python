#
# Given a single-digit number k and a singly-linked list whose nodes stores digits of a
# non-negative number, add k to the linked list.
#
# Input: List = 9 —> 9 —> 9 —> 3 —> None, k = 7
# Output: 1 —> 0 —> 0 —> 0 —> 0 —> None
# Explanation: The input linked list represents the number 9993.
# Adding a single-digit number 7 results in linked list corresponding to the number 10000.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Helper function to print a given linked list
def printList(msg, head):
    print(msg, end='')
    while head:
        print(head.data, end=' —> ')
        head = head.next
    print('None')


def reverse(head):
    prev = None
    current = head

    # traverse the list
    while current is not None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev


def addDigit(head, num):
    # empty list
    if head is None:
        return Node(num)

    # reverse the linked list
    head = reverse(head)

    # initialize carry with the given num
    carry = num

    # traverse the reversed list
    curr = head
    while carry > 0:
        total = curr.data + carry  # total =7+3=10
        curr.data = total % 10  # 10%10=0
        carry = total // 10  # 10//10=1

        if curr.next is None:
            break

        curr = curr.next

    # add a new node at the end of the linked list if there is any carry left
    if carry > 0:
        curr.next = Node(carry)

    # reverse the list again to get the original order
    head = reverse(head)
    return head


if __name__ == '__main__':
    # Input: List = 9 — > 9 — > 9 — > 3 — > None, k = 7
    head = Node(9)
    head.next = Node(9)
    head.next.next = Node(9)
    head.next.next.next = Node(9)
    head.next.next.next.next = Node(3)
    printList('Original linked list: ', head)
    head = addDigit(head, 7)
    printList('Resultant linked list: ', head)
