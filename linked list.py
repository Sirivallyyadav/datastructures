class Node:
    def __init__(self,data):
       self.data=  data
       self.next = None
class Linkedlist :
    def __init__(self):
        self.head = None
    def add_end(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new 
    def display(self):
        itr = self.head
        while itr:
            print(itr.data,end='-->')
            itr =itr.next
l1 = Linkedlist()
l1.add_end(50)
l1.add_end(150)
l1.add_end(250)
l1.add_end(350)
l1.add_end(450)
l1.add_end(550)
l1.add_end(650)
l1.display()