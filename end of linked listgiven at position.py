class Node:
    def __init__(self, data):
        self.data = data   
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new
    def add_beg(self,data):
        obj=Node(data)
        if self.head is None:
            self.head=obj
            return
        obj.next=self.head
        self.head=obj
    def add_at_position(self, data, position):
        new = Node(data)
        if position <= 0 or self.head is None:
            new.next = self.head
            self.head = new
            return
        itr = self.head
        index = 0
        while itr.next and index < position - 1:
            itr = itr.next
            index += 1
        new.next = itr.next
        itr.next = new
    def remove_two_nodes(self, position):
        if self.head is None:
            print("List is empty")
            return
        if position <= 0:
            first = self.head
            second = first.next
            if second:
                self.head = second.next
            else:
                self.head = None
            return
        prev = self.head
        itr = self.head.next
        index = 1
        while itr and index < position:
            prev = itr
            itr = itr.next
            index += 1
        if itr is None:
            print(f"Position {position} out of range")
            return
        next_node = itr.next.next if itr.next else None
        prev.next = next_node

    def remove(self, data):      
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev = self.head
        itr = self.head.next
        while itr:
            if itr.data == data:
                prev.next = itr.next
                return
            prev = itr
            itr = itr.next
        print(f"Element {data} not found")
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def remove_loop(self):
        if self.head is None:
            return False
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return False
        slow = self.head
        if slow == fast:
            while fast.next != slow:
                fast = fast.next
            fast.next = None
            return True
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None
        return True

    def display(self):
        itr = self.head
        while itr:
            print(itr.data, end="-->")
            itr = itr.next
        print("None")  

ll = LinkedList()
ll.add_end(50)
ll.add_end(150)
ll.add_end(250)
ll.add_end(350)
ll.add_end(450)
ll.add_end(250)
ll.add_beg(10)
ll.display()
ll.add_at_position(200, 2)
print("After adding 200 at position 2:")
ll.display()
ll.remove_two_nodes(3)
print("After removing two nodes starting at position 3:")
ll.display()
print("After reversing the list:")
ll.reverse()
ll.display()