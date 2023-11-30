"""This file is a sample of how we are going to store data of mentees in
binary search trees. BST is a non-linear data structure. It is useful in retrieving data faster,
since its time complexity is O(logn). This file also contains classes for Binary Search Trees.
This file deals with 63 records of a CSV file. Those records are of mentees. """

import math
import csv
from tkinter import *
class BST:

	"""This constructor takes 3 arguments: self, key and number. Key-record, number - serial number"""
	def __init__(self,key,number):
		self.key=key
		self.lchild=None
		self.rchild=None
		self.position=number
		self._elements=[]
    
	# This method inserts the records in the binary search tree. It compares the number 
	# passed as an argument, compares the number with the numbers of previously inserted nodes,
	#  and places the record in the tree accordingly.

	def insert(self,data,number):
		if self.position is None:
			self.key=data
			return
		elif self.position>number:
			if self.lchild is None:
				self.lchild= BST(data,number)
			else:
				self.lchild.insert(data,number)
		else:
			if self.rchild:
				self.rchild.insert(data,number)
			else:
				self.rchild= BST(data,number)

	"""This method traverses and prints the records in the ascending order of serial number of records."""
	def get_items(self):
		self.inorder()


	def inorder(self):
		if self.lchild:
			self.lchild.inorder()
		print(self.key,end= "\n")
		self._elements.append(self.key)
		if self.rchild:
			self.rchild.inorder()

def createBST(l,a=0):
    """This function creates BST """
    obj=BST(l[31][a:],32)
    n=16
    p=n
    i=1
    q=n
    c=0
    while c<5:
        
        for j in range(2**i):
            obj.insert(l[int(p-1)][a:],p)
            p= p + 2**((math.log(q,2))+1)
        i+=1
        o = n/(2**(i-1))
        p=o
        q=o
        c+=1
    return obj
one_mentee_details=None	
def retrievex(tree,username,b):

	"""un-username,
	a-the coulumn of username"""
	
	global one_mentee_details
	if tree.key[b]==username:
		
		one_mentee_details=tree.key
		return tree.key
	elif username<tree.key[b]:
		if tree.lchild:
			retrievex(tree.lchild,username,b)
		else:
			return False
	elif username>tree.key[b]:
		if tree.rchild:
			retrievex(tree.rchild,username,b)
		else:
		    return False


	
#Piece of code which reads the records in the csv file containing mentee details
f=open(r"IT-A details.txt","r")
n=next(csv.reader(f))
l=[]
for i in csv.reader(f):
	l.append(i)
f.close()

mentee_details_tree=createBST(l)

"""Insertion of records into the binary search tree start here.
obj=BST(l[31],32)
n=16
p=n
i=1
q=n
c=0
while c<5:
    for j in range(2**i):
        obj.insert(l[int(p-1)],p)
        p= p + 2**((math.log(q,2))+1)
    i+=1
    o = n/(2**(i-1))
    p=o
    q=o
    c+=1
Calling .inorder() method to print the records.
#obj.inorder()

"""




