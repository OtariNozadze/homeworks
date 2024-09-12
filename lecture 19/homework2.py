class Node:
    def __init__(self, data=None):  
        self.data = data         
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
    
    def remove_value(self, value):
        if self.head is None:
            return

        if value == self.head.data:
            self.head = self.head.next
            return

        current_node = self.head

        while current_node.next and current_node.next.data != value:
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next
        
    def display(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next



linked_list = LinkedList()
linked_list.append("Python")
linked_list.append(10)
linked_list.append(True)
linked_list.append(5.5)
linked_list.append(12)
linked_list.append(66)
# linked_list.display()

linked_list.remove_value("Python")
linked_list.remove_value(True)
linked_list.remove_value(66)


linked_list.display()