class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_after(self, target_data, new_data):
        if not self.head:
            return False
        
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                if current == self.tail:
                    self.tail = new_node
                return True
            current = current.next
        return False  

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False

    def remove_beginning(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return removed_data

    def remove_at_end(self):
        if not self.head:
            return None
        if self.head == self.tail:
            removed_data = self.head.data
            self.head = None
            self.tail = None
            return removed_data
        
        current = self.head
        while current.next != self.tail:
            current = current.next
        removed_data = self.tail.data
        current.next = None
        self.tail = current
        return removed_data
    
    def remove_at(self, data):
        if not self.head:
            return None
        if self.head.data == data:
            return self.remove_beginning()

        current = self.head 
        while current.next and current.next.data != data: 
            current = current.next 
        if not current.next: 
            return None

        if current.next == self.tail: 
            self.tail = current 
        removed = current.next.data 
        current.next = current.next.next 
        return removed

    def display(self):
        if not self.head:
            print("The list does not contain anything.")
            return

        current_node = self.head
        while current_node:
            print(current_node.data, end=" > ")
            current_node = current_node.next
        print("None")

todo_list = LinkedList()
todo_list.insert_at_beginning("Wake up early")
todo_list.insert_at_end("Exercise for 30 minutes")

print("Today's activities:")
todo_list.display()

print("\nInserting another activity:")
todo_list.insert_after("Exercise for 30 minutes", "Eat breakfast")
todo_list.display()

print("\nRemoved the first activity:", todo_list.remove_beginning())
todo_list.display()

print("\nRemoved the last activity:", todo_list.remove_at_end())
todo_list.display()

print("\nRemoved specific activity 'Go to the mall':", todo_list.remove_at("Go to the mall"))
todo_list.display()

print("\nRemoved specific task 'Exercise for 30 minutes':", todo_list.remove_at("Exercise for 30 minutes"))
todo_list.display()