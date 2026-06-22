class Node:
    def __init__(self,data):
        self.data = None
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_end(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
        while itr.next:
            itr = itr.next
        itr.next = new    
    def display(self):
        itr = self.head
        while itr:
            print(itr.data,end ="-->")
ll = LinkedList()
ll.add_end(50)
ll.dispaly()
