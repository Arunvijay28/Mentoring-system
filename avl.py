class Node(object):
    def __init__(self,val,data=None):
        self.data=data
        self.val=val
        self.left=None
        self.right=None
        self.height=1
class AVL1(object):
    __slots__="record"
    def __init__(self):  #here key is supposeedly the S.no
         self.record=None            #if unwanted comment it becuz this ain't given in the book
    def insert(self,root,key,data):
        #how does insertion work in a AVL tree?
        #it works like the insertion binary but also follows some more height criteria
        if not root:
            return Node(key,data)
        #it is checking if there is a root node already and if not creating one with the node class
        elif key<root.val:
            root.left=self.insert(root.left,key,data)
            #checking for leftchild and recursively calling the insert function
        else:
            root.right=self.insert(root.right,key,data)
             #checking for rightchild and recursively calling the insert function
#height getting updated after insertion
        root.height=1+max(self.getheight(root.left),self.getheight(root.right))
        #now comes the height balance part
        balance=self.getbalance(root)
        if balance>1 and key<root.left.val:   #left imbalance so right rotation
            return self.rightrotate(root)
        if balance<-1 and key>root.right.val:   #bal<-1 right imbalance so do left rotate
            return self.leftrotate(root)
        if balance>1 and key>root.left.val:     #bal>1 so insertion occurred at the right subtree of leftchild of alpha node
            root.left= self.leftrotate(root.left)             #so double rotaation is used first we rotate left and the right
            return self.rightrotate(root)
        if balance<-1 and key<root.right.val:
            root.right=self.rightrotate(root.right)
            return self.leftrotate(root)
        return root                               #atlast the root is returned after rotations
        #well..we're done with insertion now comes deletion of a root from the AVL tree
    def delete(self,root,Sno,number):
        if root.val==Sno:
            root.data[number]="-"
        elif root.val<Sno:
            self.delete(root.right,Sno,number)
        elif root.val>Sno:
            self.delete(root.left,Sno,number)
        else:
            return "Record not found"

    def retrieve(self,root,Sno,r=""):
        if root.val==Sno:
            self.record=root.data
        elif root.val<Sno:
            self.retrieve(root.right,Sno,r)
        elif root.val>Sno:
            self.retrieve(root.left,Sno,r)
        else:
            return "Record not found"

    def update(self,root,Sno,number,data):
        if root.val==Sno:
            root.data[number]=data
        elif root.val<Sno:
            self.update(root.right,Sno,number,data)
        elif root.val>Sno:
            self.update(root.left,Sno,number,data)
        else:
            return "Record not found"

    def leftrotate(self,z):
            y=z.right   
            T2=y.left   #T2(subtree) temproarily storing the y.left 
            y.left=z     #z is rotated to the y 
            z.right=T2   #right of the z are re assigned to T2(subtree)
            z.height=1+max(self.getheight(z.left),self.getheight(z.right))
            y.height=1+max(self.getheight(y.left),self.getheight(y.right))
            return y
    def rightrotate(self,z):
            y=z.left
            T3=y.right
            y.right=z
            z.left=T3
            z.height=1+max(self.getheight(z.left),self.getheight(z.right))
            y.height=1+max(self.getheight(y.left),self.getheight(y.right))
            return y
    def getheight(self,root):
            if not root:
                return 0
            return root.height
    def getbalance(self,root):
            if not root:
                return 0
            return self.getheight(root.left)-self.getheight(root.right)
    
    def getMinvalueNode(self,node,l=[]):
        if node.left:
            self.getMinvalueNode(node.left,l)
        l.append(node)
        if node.right:
            self.getMinvalueNode(node.right,l)
        return [Node(None)] if len(l) ==0 else l

    def inorder(self,root,l=[]):
        if root.left:
            self.inorder(root.left,l)
        l.append(root.data)
        if root.right:
            self.inorder(root.right,l)
        return l



#driver code
# TreeMain = AVL1()    #calling the class
# root=None
# root=TreeMain.insert(root,0,["a,b"])
# root=TreeMain.insert(root,2,["c,s"])
# root=TreeMain.insert(root,4,["f","g"])
# root=TreeMain.insert(root,61,["k","l"])
# root=TreeMain.insert(root,8,["a","b"])
# root=TreeMain.insert(root,10,["f","g"])
# root=TreeMain.insert(root,12,["c","s"])
# # root=TreeMain.insert(root,13)
# # root=TreeMain.insert(root,11)
# #print(root.val)
# TreeMain.inorder(root)
