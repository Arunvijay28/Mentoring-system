class Node:

    __slots__="item","next"
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class LinkedList:
    __slots__="head","size"
    def __init__(self):
        self.head=Node()
        self.size=0
    
    def append(self,obj):
        s=self.head
        for i in range(self.size):
            s=s.next
        s.next=Node(obj)
        self.size+=1
    
    def search(self,obj):
        s=self.head.next
        for i in range(self.size):
            if s.item==obj:
                return s.item 
            s=s.next
        return False
