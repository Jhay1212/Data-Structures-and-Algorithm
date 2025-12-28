import SinglyLinkedList


def item_from_last(ll, n):
    pointer = ll.head
    tail = ll.head

    for _ in range(n):
        if not tail:
            return None
        tail = tail.next

    while tail:
        pointer = pointer.next
        tail = tail.next
    return pointer


ll1 = SinglyLinkedList.LinkedList()
ll1.append(12)
ll1.append(123)
ll1.append(124)

print(item_from_last(ll1, 2), 2)
