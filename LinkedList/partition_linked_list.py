from SinglyLinkedList import LinkedList


def partition(linked_list: LinkedList, target: int):
    current_node = linked_list.head
    linked_list.tail = linked_list.head
    
    while current_node:
        next_node = current_node.next
        current_node.next = None
        if current_node < target:
            current_node.next = linked_list.head
            linked_list.head = current_node
        else:
            linked_list.next = current_node
            linked_list.tail = current_node    
        current_node = next_node
    
    if linked_list.tail.next:
        linked_list.tail.next = None
        
            
    
def sum_of_linked_list(linked_list: LinkedList) -> int | float:
    current_node = linked_list.head
    s = 0
    while current_node:
        s += current_node.value
        current_node = current_node.next
    return s


new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)

x = sum_of_linked_list(new_linked_list)
print(x)
