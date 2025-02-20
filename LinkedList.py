class Node:
    def __init__(self,data):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtTheEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insertAtTheIndex(self, data, index):
        if index == 0:
            insertAtBeginning(data)
            return

        index_at_the_moment = 0
        current_node = self.head
        while index_at_the_moment > index and current_node is not None:
            index_at_the_moment += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Nie ma takiego Indexu")

    def updateNode(self, val, index):
        current_node = self.head
        index_at_the_moment = 0
        while index_at_the_moment != index:
            current_node = current_node.next
            index_at_the_moment += 1
        if current_node is not None:
            current_node.value = val
        else:
            print("Nie ma takiego Indexu")

    def removeFirstNode(self):
        if self.head is None:
            print("Nie ma pierwszego elemntu Listy Linkowanej")
            return
        self.head = self.head.next

    def removeLastNode(self):
        if self.head is None:
            print("Nie ma pierwszego elemntu Listy Linkowanej")
            return

        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    def size(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    def print(self):
        nice_list = ""
        current_node = self.head
        while current_node is not None:
            nice_list += current_node.data + "-->"
            current_node = current_node.next
        return nice_list



linked_list = Linked_List()
linked_list.insertAtBeginning("5")
linked_list.insertAtTheEnd("2")
linked_list.size()
linked_list.print()


