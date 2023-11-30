import ctypes
class Arr:
    __slots__="size","capacity","array"
    def __init__(self):
        self.capacity=2
        self.array=(ctypes.py_object*self.capacity)()
        self.size=0

    def append(self,data):
        if self.size==self.capacity:
            self.resize(2*self.capacity)
        self.array[self.size]=data
        self.size+=1
    
    def __len__(self):
        return self.size

    def resize(self,newcap):
        newarray=(ctypes.py_object*newcap)()
        for i in range(self.size):
            newarray[i]=self.array[i]
        self.array=newarray
        self.capacity=newcap
    
    def is_empty(self):
        return self.size==0

    def __getitem__(self,index):
        if not self.is_empty():
            if 0<=index<self.size:
                return self.array[index]
            raise IndexError('invalis index')
        return "Array is empty"
    
    def __str__(self):
        s="["
        for i in range(self.size):
            s+=str(self.array[i])+","
        s=s.rstrip(",")+"]"
        return s
    
    def __iter__(self):
        for i in range(1,self.size):
            yield self.array[i]