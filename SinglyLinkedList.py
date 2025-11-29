class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #inserts a new node at the last
    def insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def traverse(self):
        if self.head is not None:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")
    
    def search(self, target):
        a = self.head
        if a.data == target:
            return [True, None, a]
        b = a.next
        while b is not None and b.data != target:
            a = a.next
            b = b.next
        return [b is not None, a, b]
    
    def print_searched(self, target):
        print("Value = ", self.search(target))
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def insAfter(self,x,val):
        found, prev, node = self.search(x)
        if found == True:
            new_node = Node(val)
            new_node.next = node.next
            node.next = new_node
    
    def delNode(self,x):
        found, prev, node = self.search(x)
        if prev is None:
            self.head = node.next
        else:
            prev.next = node.next
        return node
    
    #builds a sigly linked list from a python list
    def buildList(self, val):
        assert len(val) > 0, "No elements"
        a = Node(val[0])
        b = a
        for i in range(1, len(val)):
            newNode = Node(val[i])
            b.next = newNode
            b = newNode
    
    def insTail(self,x):
        newNode = Node(x)
        if self.head is None:
            self.head = newNode
            return
        
        a = self.head
        while a.next:
            a = a.next
        a.next = newNode
    
    def circularize(self):
        a = self.head
        while a.next:
            a = a.next
        a.next = self.head
    
    def traverse_circular(self):
        if self.head is None:
            print('List is empty')
            return
        a = self.head
        while True:
            print(a.data, end=" -> ")
            a = a.next
            if a == self.head:
                break
        print("Back to the head.")

    #to convert a circular LL into Linear
    def linearize(self):
        a = self.head
        while a.next is not self.head:
            a = a.next
        a.next = None
    
        
        

ll = LinkedList()

# Insert nodes
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

print("Normal Linked List:")
ll.traverse()

# Make circular
ll.circularize()

print("\nCircular Linked List Traversal:")
ll.traverse_circular()
        
        
        

        