class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class SLL:
    def __init__(self, start=None):
        self.start = start
    
    def isEmpty(self):
        return self.start == None
    
    def insert_at_first(self,data):
        node = Node(data, self.start)
        self.start = node
    
    def insert_at_last(self,data):
        node = Node(data)
        if not self.isEmpty():
            temp=self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        else:
            self.start = node
        
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.data == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            node = Node(data, temp.next)
            temp.next = node
    
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next

# driver code
mylist = SLL()  
mylist.insert_at_first(20)
mylist.insert_at_first(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),88)

mylist.print_list()
