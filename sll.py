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

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
    
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.data == data:
                self.start = None
        else:
            temp = self.start
            if temp.data == data:
                self.start = temp.next
            while temp.next is not None:
                if temp.next.data == data:
                    temp.next = temp.next.next
                    break
                temp = temp.next

    def __iter__(self):
            return SLLIterator(self.start)

class SLLIterator:
    def __init__(self,start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data
        
# driver code
mylist = SLL()  
mylist.insert_at_first(20)
mylist.insert_at_first(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),88)
mylist.print_list()
# mylist.delete_item(88)
# mylist.delete_first()
mylist.delete_last()
print()
for i in mylist:
    print(i, end=' ')
# mylist.print_list()

