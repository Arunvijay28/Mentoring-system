from cgitb import text
from tkinter import *       
from tkinter import messagebox
import math
import matplotlib.pyplot as plt
from samplecode import *
import logincred
import csv
import avl
import linkedlist
import main
import smtplib
from tktimepicker import AnalogPicker, AnalogThemes, constants
import os
import acad 
from tkcalendar import Calendar
from ARRAY import *

#from tkcalendar import Calendar
snoe,dide,ree,ssne,gene,dte,se,sne=None,None,None,None,None,None,None,None
ae,be,ce=None,None,None
marks_tree=None
class BST:

	"""This constructor takes 3 arguments: self, key and number. Key-record, number - serial number"""
	def __init__(self,key,number):
		self.key=key
		self.lchild=None
		self.rchild=None
		self.position=number
    
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

	def inorder(self):
		if self.lchild:
			self.lchild.inorder()
		print(self.key,end= "\n")
		if self.rchild:
			self.rchild.inorder()
"""Piece of code which reads the records in the csv file containing mentee details""" 

f=open(r"IT-A details.txt","r")
n=next(csv.reader(f))
l=[]
for i in csv.reader(f):
	l.append(i)
f.close()

"""Insertion of records into the binary search tree start here."""

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

"""Calling .inorder() method to print the records."""
m=Tk()
m.title("SSN Mentoring system")
m.iconbitmap()
m.geometry('1920x1080')
#
img=PhotoImage(file=r'ssnpro1.png')  #importing image of SSN
lab=Label(m,image=img)
lab.place(x=0,y=0,relheight=1,relwidth=1)

myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
myframe.place(relx=0.4,rely=0.4)

f=open(r"credentials1.txt","r")

lis=[]
x=[]
y=[]
no=next(csv.reader(f))
for i in csv.reader(f):
    x.append(i[0])
f.seek(1)
no=next(csv.reader(f))
for j in csv.reader(f):
    y.append(j[1])
lis.append(x)
lis.append(y)
#f=open(r"C:\Users\ashwi\OneDrive\Documents\Ashwin M\New folder\SSN-mentoring-system-project\credentials1.txt","r")
aru=[]
f.seek(0)
a=next(csv.reader(f))
for z in csv.reader(f):
    aru.append(z)
#f.close()
f.close()
s=None
#one_mentee_details=None
def personalinfo(myframe,fno):
    
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.place(relx=0.4,rely=0.4)
    global aru
    T=main.T4
    root=main.root4
    T.retrieve(root,fno)
    record=T.record
    l1=[("DIGITAL ID",record[1]),("ROLL NO",record[2]),
        ("NAME",record[3]),("SECTION",record[4]),("DEPT",record[5]),
        ("EMAIL-ID",record[6]),("GENDER",record[7])]
        
        
    for i in range(len(l1)):
        for j in range(2):
            e=Label(myframe,text=l1[i][j],font=('Helvetica',12),width=20,fg='blue')
            e.grid(row=i,column=j)
            #e.insert(0,l1[i][j])  
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)
    
    

    
def marks(myframe,sno):
    a=clicked.get()
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.place(relx=0.4,rely=0.4)
    #myframe.place(relx=0.4,rely=0.4)
    if a=="CAT-1":
    
        marks=main.cat1[int(sno)][3:]
        mb1=Label(myframe,text='MATHS',font=('Helvetica',12),width=20,fg='blue').grid(row=2,column=2)
        mb1m=Label(myframe,text=marks[0],font=('Helvetica',12),width=20,fg='blue').grid(row=2,column=3)
        mb2=Label(myframe,text='BEEE',font=('Helvetica',12),width=20,fg='blue').grid(row=3,column=2)
        mb2m=Label(myframe,text=marks[1],font=('Helvetica',12),width=20,fg='blue').grid(row=3,column=3)
        mb3=Label(myframe,text='PHYSICS',font=('Helvetica',12),width=20,fg='blue').grid(row=4,column=2)
        mb3m=Label(myframe,text=marks[2],font=('Helvetica',12),width=20,fg='blue').grid(row=4,column=3)
        mb4=Label(myframe,text='PDS',font=('Helvetica',12),width=20,fg='blue').grid(row=5,column=2)
        mb4m=Label(myframe,text=marks[3],font=('Helvetica',12),width=20,fg='blue').grid(row=5,column=3)
        mb5=Label(myframe,text='HSE',font=('Helvetica',12),width=20,fg='blue').grid(row=6,column=2)
        mb5m=Label(myframe,text=marks[4],font=('Helvetica',12),width=20,fg='blue').grid(row=6,column=3)
        mb6=Label(myframe,text='EVS',font=('Helvetica',12),width=20,fg='blue').grid(row=7,column=2)
        mb6m=Label(myframe,text=marks[5],font=('Helvetica',12),width=20,fg='blue').grid(row=7,column=3)
        #print(l)



    elif a=="CAT-2":
        marks=main.cat2[int(sno)][3:]
        mb1=Label(myframe,text='MATHS',font=('Helvetica',12),width=20,fg='blue').grid(row=2,column=2)
        mb1m=Label(myframe,text=marks[0],font=('Helvetica',12),width=20,fg='blue').grid(row=2,column=3)
        mb2=Label(myframe,text='BEEE',font=('Helvetica',12),width=20,fg='blue').grid(row=3,column=2)
        mb2m=Label(myframe,text=marks[1],font=('Helvetica',12),width=20,fg='blue').grid(row=3,column=3)
        mb3=Label(myframe,text='PHYSICS',font=('Helvetica',12),width=20,fg='blue').grid(row=4,column=2)
        mb3m=Label(myframe,text=marks[2],font=('Helvetica',12),width=20,fg='blue').grid(row=4,column=3)
        mb4=Label(myframe,text='PDS',font=('Helvetica',12),width=20,fg='blue').grid(row=5,column=2)
        mb4m=Label(myframe,text=marks[3],font=('Helvetica',12),width=20,fg='blue').grid(row=5,column=3)
        mb5=Label(myframe,text='HSE',font=('Helvetica',12),width=20,fg='blue').grid(row=6,column=2)
        mb5m=Label(myframe,text=marks[4],font=('Helvetica',12),width=20,fg='blue').grid(row=6,column=3)
        mb6=Label(myframe,text='EVS',font=('Helvetica',12),width=20,fg='blue').grid(row=7,column=2)
        mb6m=Label(myframe,text=marks[5],font=('Helvetica',12),width=20,fg='blue').grid(row=7,column=3)
    
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)
    #marks_tree.inorder()

    
        

def academicdetails(myframe):
    global clicked
    
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.place(relx=0.5,rely=0.5)
    #myframe.config(text=clicked.get())
    #label=Label(myframe,text)
    options = [
	"CAT-1",
	"CAT-2"]

# datatype of menu text

    clicked = StringVar()

    # initial menu text
    clicked.set("SELECT EXAM")

    # Create Dropdown menu
    drop = OptionMenu( myframe, clicked , *options )
    drop.pack()
    #print(a)
    # Create button, it will change label text
    button = Button( myframe, text = "SELECT",command=lambda: marks(myframe,d) ).pack()
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)
def mentorship(myframe):
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.place(relx=0.4,rely=0.4)

    return

def login(myframe):   
    global user4
    global passw4,d
    
    # entering details of the user
    user4=entry1.get()
    passw4=entry2.get()
    
    d=logincred.give(user4,passw4,logincred.t)    
    if d=='Invalid username or password':
        messagebox.showinfo("","Invalid Username or Password")
    elif isinstance(d,str):
        myframe.destroy()
        myframe=LabelFrame(m,bg="#A2ACBE",padx=25,pady=40,bd=0)   #importing the frame colour
        myframe.place(relx=0.4,rely=0.4)
        mb=Button(myframe,text='PERSONAL INFO',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :personalinfo(myframe,int(d)))
        mb.grid(row=1,column=1,padx=10,pady=10)
        mb1=Button(myframe,text='ACADEMIC DETAILS',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :academicdetails(myframe))
        mb1.grid(row=1,column=2,padx=10,pady=10)
    #    mb2=Button(myframe,text='MENTORSHIP',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :mentorship(myframe))
    #    mb2.grid(row=1,column=3,padx=10,pady=10)
        b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
        b4.place(relx=0,rely=0)
    else:
        messagebox.showinfo("","Invalid Username or Password")
#d#]ef next(myframe):          #for creating to add update delete
    #myframe.destroy() a page
    #myframe=LabelFrame(m,bg="white")   #importing the frame colour
    #myframe.place(relx=0.4,rely=0.4)
    #mb=Button(myframe,text='PERSONAL INFO',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :personalinfo(myframe))
    #mb.grid(row=1,column=1,padx=10,pady=10)
    #mb1=Button(myframe,text='ACADEMIC DETAILS',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :academicdetails(myframe))
    #mb1.grid(row=1,column=2,padx=10,pady=10)
    #mb2=Button(myframe,text='MENTORSHIP',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :mentorship(myframe))
    #mb2.grid(row=1,column=3,padx=10,pady=10)
def add(myframe,username):
    global snoe,dide,ree,ssne,gene,dte,se,sne,un
    un=username
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.place(relx=0.4,rely=0.4)
    sno=Label(myframe,text='Serial No.').grid(row=1,column=1)
    snoe=Entry(myframe,bd=5)
    snoe.grid(row=1,column=2)
    did=Label(myframe,text='Digital ID').grid(row=2,column=1)
    dide=Entry(myframe,bd=5)
    dide.grid(row=2,column=2)
    re=Label(myframe,text='Register No.').grid(row=3,column=1)
    ree=Entry(myframe,bd=5)
    ree.grid(row=3,column=2)
    sn=Label(myframe,text='Student Name').grid(row=4,column=1)
    sne=Entry(myframe,bd=5)
    sne.grid(row=4,column=2)
    s=Label(myframe,text='Section').grid(row=5,column=1)
    se=Entry(myframe,bd=5)
    se.grid(row=5,column=2)
    dt=Label(myframe,text='Department').grid(row=6,column=1)
    dte=Entry(myframe,bd=5)
    dte.grid(row=6,column=2)
    ssn=Label(myframe,text='SSN Mail ID').grid(row=7,column=1)
    ssne=Entry(myframe,bd=5)
    ssne.grid(row=7,column=2)
    gen=Label(myframe,text='Gender').grid(row=8,column=1)
    gene=Entry(myframe,bd=5)
    gene.grid(row=8,column=2)
    sdj=Button(myframe,text='INSERT',command=lambda: add1(myframe)).grid(row=10,column=1)
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)
def add1(myframe):

    a=snoe.get()
    b=dide.get()
    c=sne.get()
    d=se.get()
    e=ree.get()
    f=dte.get()
    g=ssne.get()
    h=gene.get()
    details=[a,b,e,c,d,f,g,h]
    if un=='divyajohn@ssn.edu.in':
        f=open(r"third20.txt","r")
        l=[]
    # c=0
        c=0
        for i in csv.reader(f):
            if c!=0:
            
                if int(i[0])<int(details[0]):
                    l.append(i)
                elif int(i[0])==int(details[0]):
                    l.append(details)
                    i[0]=str(int(i[0])+1)
                    l.append(i)
                else:
            # c+=1
                    i[0]=str(int(i[0])+1)
                    l.append(i)
            c+=1
        f.close()
        f=open(r"third20.txt","w",newline="")
        w=csv.writer(f)
        w.writerow(['S.No','Digital ID','Register Number','Student Name','Section','Department','SSN Mail / SSN Digital Id','Gender'])
        w.writerows(l)
        f.close()
    elif un=='chandrasekaran@ssn.edu.in':
        f=open(r"first20.txt","r")
        l=[]
    # c=0
        c=0
        for i in csv.reader(f):
            if c!=0:
            
                if int(i[0])<int(details[0]):
                    l.append(i)
                elif int(i[0])==int(details[0]):
                    l.append(details)
                    i[0]=str(int(i[0])+1)
                    l.append(i)
                else:
            # c+=1
                    i[0]=str(int(i[0])+1)
                    l.append(i)
            c+=1
        f.close()
        f=open(r"first20.txt","w",newline="")
        w=csv.writer(f)
        w.writerow(['S.No','Digital ID','Register Number','Student Name','Section','Department','SSN Mail / SSN Digital Id','Gender'])
        w.writerows(l)
        f.close()
    elif un=='rajalakshmitm@ssn.edu.in':
        f=open(r"second20.txt","r")
        l=[]
    # c=0
        c=0
        for i in csv.reader(f):
            if c!=0:
            
                if int(i[0])<int(details[0]):
                    l.append(i)
                elif int(i[0])==int(details[0]):
                    l.append(details)
                    i[0]=str(int(i[0])+1)
                    l.append(i)
                else:
            # c+=1
                    i[0]=str(int(i[0])+1)
                    l.append(i)
            c+=1
        f.close()
        f=open(r"second20.txt","w",newline="")
        w=csv.writer(f)
        w.writerow(['S.No','Digital ID','Register Number','Student Name','Section','Department','SSN Mail / SSN Digital Id','Gender'])
        w.writerows(l)
        f.close()

    f=open(r"third20.txt","w",newline="")
    w=csv.writer(f)
    w.writerow(['S.No','Digital ID','Register Number','Student Name','Section','Department','SSN Mail / SSN Digital Id','Gender'])
    w.writerows(l)
    f.close()
    # root=None
    # Tnew=avl.AVL1()
    # for i in l:
    #     root=Tnew.insert(root,int(i[0]),i)
    # l1=Tnew.inorder(root)
    # print(l1)
    # root=main.root3
    # mentees=main.T3
    # print(details[0],type(details[0]))
    # root=mentees.insert(root,int(details[0]),details)
    
def update(myframe,username):
    global ae,be,ce,unam
    unam=username
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.place(relx=0.4,rely=0.4)
    a=Label(myframe,text='Enter SNO. of the record to be updated').grid(row=2,column=2)
    b=Label(myframe,text='Enter type of data to be updated').grid(row=3,column=2)
    c=Label(myframe,text='Enter the new data to be replaced').grid(row=4,column=2)
    ae=Entry(myframe,bd=5)
    ae.grid(row=2,column=3)
    be=Entry(myframe,bd=5)
    be.grid(row=3,column=3)
    ce=Entry(myframe,bd=5)
    ce.grid(row=4,column=3)
    d=Button(myframe,text='UPDATE THE DETAILS',command=lambda :update1(myframe)).grid(row=5,column=2)
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)
def update1(myframe):
    x=ae.get()
    x=int(x)
    y=be.get()
    z=ce.get()
    if unam=='divyajohn@ssn.edu.in':
        l=[]
        if y.lower()=="digital id":
            number=1
            root=main.root3
            tree=main.T3
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="register number":
            number=2
            root=main.root3
            tree=main.T3
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="student name":
            number=3
            root=main.root3
            tree=main.T3
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="section":
            number=4
            root=main.root3
            tree=main.T3
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="department":
            number=5
            root=main.root3
            tree=main.T3
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        
        f=open(r"third20.txt","w",newline="")
        lh=["S.No","Digital ID","Register Number","Student Name","Section","Department","SSN Mail / SSN Digital Id","Gender"]
        w=csv.writer(f)
        w.writerow(lh)
        w.writerows(l)
        f.close()
    elif unam=='chandrasekaran@ssn.edu.in':
        l=[]
        if y.lower()=="digital id":
            number=1
            root=main.root1
            tree=main.T1
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="register number":
            number=2
            root=main.root1
            tree=main.T1
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="student name":
            number=3
            root=main.root1
            tree=main.T1
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="section":
            number=4
            root=main.root1
            tree=main.T1
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="department":
            number=5
            root=main.root1
            tree=main.T1
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        
        f=open(r"first20.txt","w",newline="")
        lh=["S.No","Digital ID","Register Number","Student Name","Section","Department","SSN Mail / SSN Digital Id","Gender"]
        w=csv.writer(f)
        w.writerow(lh)
        w.writerows(l)
        f.close()
    elif unam=='rajalakshmitm@ssn.edu.in':
        l=[]
        if y.lower()=="digital id":
            number=1
            root=main.root2
            tree=main.T2
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="register number":
            number=2
            root=main.root2
            tree=main.T2
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="student name":
            number=3
            root=main.root2
            tree=main.T2
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="section":
            number=4
            root=main.root2
            tree=main.T2
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        if y.lower()=="department":
            number=5
            root=main.root2
            tree=main.T2
            tree.update(root,x,number,z)
            l=tree.inorder(root)
        
        f=open(r"second20.txt","w",newline="")
        lh=["S.No","Digital ID","Register Number","Student Name","Section","Department","SSN Mail / SSN Digital Id","Gender"]
        w=csv.writer(f)
        w.writerow(lh)
        w.writerows(l)
        f.close()

def delete(myframe,username):
    global unh
    unh=username
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.place(relx=0.4,rely=0.4)
    dele=Label(myframe,text='Do You Want An Entire Record To Be Deleted?').grid(row=2,column=2)
    yese=Button(myframe,text='YES',command=lambda :yes(myframe)).grid(row=2,column=4)
    noe=Button(myframe,text='NO',command=lambda :nono(myframe)).grid(row=2,column=6)
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)
def nono(myframe):
    global xee,yee
    xe=Label(myframe,text='Enter SNO. of the record').grid(row=4,column=2)
    ye=Label(myframe,text='Enter type of data to be deleted').grid(row=5,column=2)
    xee=Entry(myframe,bd=5)
    xee.grid(row=4,column=3)
    yee=Entry(myframe,bd=5)
    yee.grid(row=5,column=3)
    xc=Button(myframe,text='DELETE',command=lambda :nono1(myframe)).grid(row=7,column=2)
def nono1(myframe):
    xec=xee.get()
    xec=int(xec)
    yec=yee.get()
    if unh=='divyajohn@ssn.edu.in':
        l=[]
        if yec.lower()=="digital id":
            number=1
            root=main.root3
            tree=main.T3
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="register number":
            number=2
            root=main.root3
            tree=main.T3
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="student name":
            number=3
            root=main.root3
            tree=main.T3
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="section":
            number=4
            root=main.root3
            tree=main.T3
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="department":
            number=5
            root=main.root3
            tree=main.T3
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        
        f=open(r"third20.txt","w",newline="")
        lh=["S.No","Digital ID","Register Number","Student Name","Section","Department","SSN Mail / SSN Digital Id","Gender"]
        w=csv.writer(f)
        w.writerow(lh)
        w.writerows(l)
        f.close()
    elif unh=='chandrasekaran@ssn.edu.in':
        l=[]
        if yec.lower()=="digital id":
            number=1
            root=main.root1
            tree=main.T1
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="register number":
            number=2
            root=main.root1
            tree=main.T1
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="student name":
            number=3
            root=main.root1
            tree=main.T1
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="section":
            number=4
            root=main.root1
            tree=main.T1
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="department":
            number=5
            root=main.root1
            tree=main.T1
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        
        f=open(r"first20.txt","w",newline="")
        lh=["S.No","Digital ID","Register Number","Student Name","Section","Department","SSN Mail / SSN Digital Id","Gender"]
        w=csv.writer(f)
        w.writerow(lh)
        w.writerows(l)
        f.close()
    elif unh=='rajalakshmitm@ssn.edu.in':
        l=[]
        if yec.lower()=="digital id":
            number=1
            root=main.root2
            tree=main.T2
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="register number":
            number=2
            root=main.root2
            tree=main.T2
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="student name":
            number=3
            root=main.root2
            tree=main.T2
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="section":
            number=4
            root=main.root2
            tree=main.T2
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        if yec.lower()=="department":
            number=5
            root=main.root2
            tree=main.T2
            tree.delete(root,xec,number)
            l=tree.inorder(root)
        
        f=open(r"second20.txt","w",newline="")
        lh=["S.No","Digital ID","Register Number","Student Name","Section","Department","SSN Mail / SSN Digital Id","Gender"]
        w=csv.writer(f)
        w.writerow(lh)
        w.writerows(l)
        f.close()

def yes(myframe):
    global zee
    ze=Label(myframe,text='Enter the SNO. of the record to be deleted').grid(row=4,column=2)
    zee=Entry(myframe,bd=5)
    zee.grid(row=4,column=3)
    cv=Button(myframe,text='DELETE RECORD',command=lambda :yes1(myframe)).grid(row=5,column=2)
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)
def yes1(myframe):
    nb=zee.get()
    if unh=='divyajohn@ssn.edu.in':
        f=open(r"third20.txt","r")
        l=[]
    # c=0
        c=0
        for i in csv.reader(f):
            if c!=0:
            
                if int(i[0])<int(nb):
                    l.append(i)
                elif int(i[0])>int(nb):
                    i[0]=str(int(i[0])-1)
                    l.append(i)
                    
                
            c+=1
        f.close()
        f=open(r"third20.txt","w",newline="")
        w=csv.writer(f)
        w.writerow(['S.No','Digital ID','Register Number','Student Name','Section','Department','SSN Mail / SSN Digital Id','Gender'])
        w.writerows(l)
        f.close()
    if unh=='rajalakshmitm@ssn.edu.in':
        f=open(r"second20.txt","r")
        l=[]
    # c=0
        c=0
        for i in csv.reader(f):
            if c!=0:
            
                if int(i[0])<int(nb):
                    l.append(i)
                elif int(i[0])>int(nb):
                    i[0]=str(int(i[0])-1)
                    l.append(i)
                    
                
            c+=1
        f.close()
        f=open(r"second20.txt","w",newline="")
        w=csv.writer(f)
        w.writerow(['S.No','Digital ID','Register Number','Student Name','Section','Department','SSN Mail / SSN Digital Id','Gender'])
        w.writerows(l)
        f.close()
    if unh=='chandrasekaran@ssn.edu.in':
        f=open(r"first20.txt","r")
        l=[]
    # c=0
        c=0
        for i in csv.reader(f):
            if c!=0:
            
                if int(i[0])<int(nb):
                    l.append(i)
                elif int(i[0])>int(nb):
                    i[0]=str(int(i[0])-1)
                    l.append(i)
                    
                
            c+=1
        f.close()
        f=open(r"first20.txt","w",newline="")
        w=csv.writer(f)
        w.writerow(['S.No','Digital ID','Register Number','Student Name','Section','Department','SSN Mail / SSN Digital Id','Gender'])
        w.writerows(l)
        f.close()
def meeting(myframe,username):
    global xwe,unhe
    unhe=username
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.place(relx=0.4,rely=0.4)
    xw=Label(myframe,text='Enter SNO. of student').grid(row=2,column=2)
    xwe=Entry(myframe,bd=5)
    xwe.grid(row=2,column=3)
    xweb=Button(myframe,text='CHOOSE DATE/TIME',command=lambda :meeting1(myframe)).grid(row=4,column=2)
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)
def timeee():
    # for i in range(0,len(selected_time)):
    #     a=str(selected_time[i])
    #     if i==1:
    #         print(":",end=" ")
    #         print(a,end=" ")
    #     else:
    #         print(a,end=" ") 
    a=str(selected_time[0])+":"+str(selected_time[1])+str(selected_time[2])
    return a
def scheduler(myframe):
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.place(relx=0.4,rely=0.4)
    #ADD 
    
        # theme.setDracula()
        #print(time_picker)
        # Create Object
        # Set geometry
    # Add Calendar
    cal = Calendar(myframe, selectmode = 'day',
                year = 2022, month = 8,
                day = 18)
    cal.pack(pady = 20)
    def grad_date():
        global meeting_date
        meeting_date=str(cal.get_date())
        if unhe=='divyajohn@ssn.edu.in':
            f=open(r"third20.txt","r")
            l=[]
            c=0
            for i in csv.reader(f):
                if c!=0:
                    l.append(i)
                c+=1
            f.close()
            for SNo,DigitalID,RegisterNumber,StudentName,Section,Department,SSNMailSSNDigitalId,Gender in l:
                if str(SNo)==str(xdvjo):
                    EMAIL_ADDRESS = 'ssnmentorshipprojectmailsender@gmail.com'
                    EMAIL_PASS='muanlosmmbtztfzi'
                    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
                        #identifies ourselves with thee mail server
                        #to encrypt traffic
                        
#login now but remember it's always safe to encrypt the login info within "ENVIRONMENT VARIABLES"
                        smtp.login(EMAIL_ADDRESS,EMAIL_PASS)
                        subject = 'Meeting Request'
                        body = f"Hi your mentor wants a meeting to be scheduled with you at\nTIME: {timeee()}\nDATE:{str(meeting_date)}\nKindly join the meeting at the mentioned date and time." 
                        msg =f'Subject:{subject}\n\n{body}'
                        smtp.sendmail(EMAIL_ADDRESS,SSNMailSSNDigitalId,msg)
        elif unhe=='chandrasekaran@ssn.edu.in':
            f=open(r"first20.txt","r")
            l=[]
            c=0
            for i in csv.reader(f):
                if c!=0:
                    l.append(i)
                c+=1
            f.close()
            
            for SNo,DigitalID,RegisterNumber,StudentName,Section,Department,SSNMailSSNDigitalId,Gender in l:
                if str(SNo)==str(xdvjo):
                
                    EMAIL_ADDRESS = 'ssnmentorshipprojectmailsender@gmail.com'
                    EMAIL_PASS='muanlosmmbtztfzi'
                    
                    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
                        smtp.ehlo()#identifies ourselves with thee mail server
                        smtp.starttls()#to encrypt traffic
                        smtp.ehlo()#identifies ourselves with thee mail server
                        #to encrypt traffic
#login now but remember it's always safe to encrypt the login info within "ENVIRONMENT VARIABLES"
                        smtp.login(EMAIL_ADDRESS,EMAIL_PASS)
                        subject = 'Meeting Request'
                        body = f"Hi your mentor wants a meeting to be scheduled with you at\nTIME: {timeee()}\nDATE:{str(meeting_date)}\nKindly join the meeting at the mentioned date and time." 
                        msg =f'Subject:{subject}\n\n{body}'
    
                        smtp.sendmail(EMAIL_ADDRESS,SSNMailSSNDigitalId,msg)

                
        elif unhe=='rajalakshmitm@ssn.edu.in':
            f=open(r"second20.txt","r")
            l=[]
            c=0
            for i in csv.reader(f):
                if c!=0:
                    l.append(i)
                c+=1
            f.close()
            for SNo,DigitalID,RegisterNumber,StudentName,Section,Department,SSNMailSSNDigitalId,Gender in l:
                if str(SNo)==str(xdvjo):
                    EMAIL_ADDRESS = 'ssnmentorshipprojectmailsender@gmail.com'
                    EMAIL_PASS='muanlosmmbtztfzi'
                    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
                        smtp.ehlo()#identifies ourselves with thee mail server
                        smtp.starttls()#to encrypt traffic
                        smtp.ehlo()
#login now but remember it's always safe to encrypt the login info within "ENVIRONMENT VARIABLES"
                        smtp.login(EMAIL_ADDRESS,EMAIL_PASS)
                        subject = 'Meeting Request'
                        body = f"Hi your mentor wants a meeting to be scheduled with you at\nTIME: {timeee()}\nDATE:{str(meeting_date)}\nKindly join the meeting at the mentioned date and time." 
                        msg =f'Subject:{subject}\n\n{body}'
    
                        smtp.sendmail(EMAIL_ADDRESS,SSNMailSSNDigitalId,msg)

    # Add Button and Label
    Button(myframe, text = "SEND MAIL",
        command = grad_date).pack(pady = 10)
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)

def meeting1(myframe):
    global xdvjo
    xdvjo=xwe.get()
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.pack(padx=100,pady=100)
    
    def updateTime(time):
        global selected_time
        time_lbl.configure(text="{}:{} {}".format(*time)) # remove 3rd flower bracket in case of 24 hrs time
        selected_time=list(time)
        myb=Button(myframe,text='Select Date',command=lambda :scheduler(myframe)).pack(padx=20,pady=20)
        
    def get_time():
    
        time_picker = AnalogPicker(myframe, type=constants.HOURS12)
        time_picker.pack(expand=True,fill='both')
        theme = AnalogThemes(time_picker)
    # theme.setDracula()
    # theme.setNavyBlue()
        theme.setNavyBlue()
        ok_btn = Button(myframe, text="OK", command=lambda: updateTime(time_picker.time()),height=2,width=7)
        ok_btn.pack(padx=20,pady=20)
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)

    
    time = ()
    time_lbl = Label(myframe, text="Time:")
    time_lbl.pack()
    time_btn = Button(myframe, text="Select Time Of The Meeting", command=get_time)
    time_btn.pack()
def mu(myframe):
    global clicked1
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.pack(padx=100,pady=100)
    options = ["MATHS","BEEE",'PHYSICS','PDS','HSE','EVS']
    clicked1 = StringVar()
    clicked1.set("SELECT SUBJECT")
    drop = OptionMenu( myframe, clicked1 , *options )
    drop.pack()
    button = Button( myframe, text = "SELECT",command=lambda: mule(myframe) ).pack()
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)
    
def mule(myframe):
    a=clicked.get()
    b=clicked1.get()
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.place(relx=0.2,rely=0.1)
    if unhef=='chandrasekaran@ssn.edu.in':
        if a=='CAT-1':
            if b=='BEEE':

                vf=acad.BEEE(main.cat1)
                
                for i in range(21):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='MATHS':
                vf=acad.MATHS(main.cat1)
                
                for i in range(21):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='PHYSICS':
                vf=acad.PHY(main.cat1)
                
                for i in range(21):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='PDS':
                vf=acad.PDS(main.cat1)
                
                for i in range(21):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='HSE':
                vf=acad.HSE(main.cat1)
                
                for i in range(21):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='EVS':
                vf=acad.EVS(main.cat1)
                
                for i in range(21):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
            b4.place(relx=0,rely=0)
        elif a=='CAT-2':
            if b=='BEEE':

                vf=acad.BEEE(main.cat2)
                
                for i in range(21):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='MATHS':
                vf=acad.MATHS(main.cat2)
                
                for i in range(21):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='PHYSICS':
                vf=acad.PHY(main.cat2)
                
                for i in range(21):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='PDS':
                vf=acad.PDS(main.cat2)
                
                for i in range(21):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='HSE':
                vf=acad.HSE(main.cat2)
                
                for i in range(21):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='EVS':
                vf=acad.EVS(main.cat2)
                
                for i in range(21):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
            b4.place(relx=0,rely=0)
    elif unhef=='rajalakshmitm@ssn.edu.in':
        if a=='CAT-1':
            if b=='BEEE':

                vf=acad.BEEE(main.cat1)
                
                for i in range(21,42):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='MATHS':
                vf=acad.MATHS(main.cat1)
                
                for i in range(21,42):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='PHYSICS':
                vf=acad.PHY(main.cat1)
                
                for i in range(21,42):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='PDS':
                vf=acad.PDS(main.cat1)
                
                for i in range(21,42):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='HSE':
                vf=acad.HSE(main.cat1)
                
                for i in range(21,42):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='EVS':
                vf=acad.EVS(main.cat1)
                
                for i in range(21,42):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
            b4.place(relx=0,rely=0)
        elif a=='CAT-2':
            if b=='BEEE':

                vf=acad.BEEE(main.cat2)
                
                for i in range(21,42):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='MATHS':
                vf=acad.MATHS(main.cat2)
                
                for i in range(21,42):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='PHYSICS':
                vf=acad.PHY(main.cat2)
                
                for i in range(21,42):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='PDS':
                vf=acad.PDS(main.cat2)
                
                for i in range(21,42):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='HSE':
                vf=acad.HSE(main.cat2)
                
                for i in range(21,42):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='EVS':
                vf=acad.EVS(main.cat2)
                
                for i in range(21,42):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
            b4.place(relx=0,rely=0)
    elif unhef=='divyajohn@ssn.edu.in':
        if a=='CAT-1':
            if b=='BEEE':

                vf=acad.BEEE(main.cat1)
                
                for i in range(42,63):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='MATHS':
                vf=acad.MATHS(main.cat1)
                
                for i in range(42,63):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='PHYSICS':
                vf=acad.PHY(main.cat1)
                
                for i in range(42,63):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='PDS':
                vf=acad.PDS(main.cat1)
                
                for i in range(42,63):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='HSE':
                vf=acad.HSE(main.cat1)
                
                for i in range(42,63):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='EVS':
                vf=acad.EVS(main.cat1)
                
                for i in range(42,63):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
            b4.place(relx=0,rely=0)
        elif a=='CAT-2':
            if b=='BEEE':

                vf=acad.BEEE(main.cat2)
                
                for i in range(42,63):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='MATHS':
                vf=acad.MATHS(main.cat2)
                
                for i in range(42,63):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='PHYSICS':
                vf=acad.PHY(main.cat2)
                
                for i in range(42,63):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='PDS':
                vf=acad.PDS(main.cat2)
                
                for i in range(42,63):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='HSE':
                vf=acad.HSE(main.cat2)
                
                for i in range(42,63):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)
            elif b=='EVS':
                vf=acad.EVS(main.cat2)
                
                for i in range(42,63):
                    
                    for j in range(3):
                        e=Label(myframe,width=25,height=2,text=vf[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                        e.grid(row=0,column=0)
                        e.grid(row=i,column=j)       
            b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
            b4.place(relx=0,rely=0)


def cat1cat2(myframe,username):
    global clicked,unhef
    unhef=username
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.pack(padx=100,pady=100)
    options = [
	    "CAT-1",
	    "CAT-2",]

# datatype of menu text

    clicked = StringVar()

    # initial menu text
    clicked.set("SELECT EXAM")

    # Create Dropdown menu
    drop = OptionMenu( myframe, clicked , *options )
    drop.pack()
    #print(a)
    # Create button, it will change label text
    button = Button( myframe, text = "SELECT",command=lambda: mu(myframe) ).pack()
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)


def login1(myframe):            # entering details of the user
    user=entry1.get()
    passw=entry2.get()
    if user=='' and passw=='':
        messagebox.showinfo("","blank invalid")
    elif (user=='chandrasekaran@ssn.edu.in' and passw=='chandru'):
        myframe.destroy()
        myframe=LabelFrame(m,bg="white")   #importing the frame colour
        myframe.grid(row=0,column=0,padx=100,pady=50)
#cal=Calendar(myframe, selectmode = 'day',
         #              year = 2020, month = 5,
         #      day = 22)
        #cal.pack()
        column=len(l[1])
        mentees=main.T1
        records=mentees.inorder(main.root1,[])
        for i in range(len(records)):
            for j in range(column):
                e=Label(myframe,width=25,height=2,text=records[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                e.grid(row=0,column=0)
                e.grid(row=i,column=j)
        f=Button(m,text='ADD',command=lambda: add(myframe,'chandrasekaran@ssn.edu.in'))
        f.place(relx=0,rely=0.05)
        g=Button(m,text='UPDATE',command=lambda: update(myframe,'chandrasekaran@ssn.edu.in'))
        g.place(relx=0,rely=0.1)
        h=Button(m,text='DELETE',command=lambda: delete(myframe,'chandrasekaran@ssn.edu.in'))
        h.place(relx=0,rely=0.15)
        i=Button(m,text='MEETING WITH MENTEE',command=lambda :meeting(myframe,'chandrasekaran@ssn.edu.in'))
        i.place(relx=0,rely=0.2)
        j=Button(m,text='ACADEMIC INFO.',command=lambda :cat1cat2(myframe,'chandrasekaran@ssn.edu.in'))
        j.place(relx=0,rely=0.25)
        
        

        
        
    elif (user=='rajalakshmitm@ssn.edu.in' and passw=='raji'):
        myframe.destroy()
        myframe=LabelFrame(m,bg="white")   #importing the frame colour
        myframe.grid(row=0,column=0,padx=100,pady=50)
        column=len(l[1])
        mentees=main.T2
        records=mentees.inorder(main.root2,[])
        for i in range(len(records)):
            for j in range(column):
                e=Label(myframe,width=25,height=2,text=records[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                e.grid(row=0,column=0)
                e.grid(row=i,column=j)
        f=Button(m,text='ADD',command=lambda: add(myframe,'rajalakshmitm@ssn.edu.in'))
        f.place(relx=0,rely=0.1)
        g=Button(m,text='UPDATE',command=lambda: update(myframe,'rajalakshmitm@ssn.edu.in'))
        g.place(relx=0,rely=0.3)
        h=Button(m,text='DELETE',command=lambda: delete(myframe,'rajalakshmitm@ssn.edu.in'))
        h.place(relx=0,rely=0.5)
        i=Button(m,text='MEETING WITH MENTEE',command=lambda :meeting(myframe,'rajalakshmitm@ssn.edu.in'))
        i.place(relx=0,rely=0.7)
        j=Button(m,text='ACADEMIC INFO.',command=lambda :cat1cat2(myframe,'rajalakshmitm@ssn.edu.in'))
        j.place(relx=0,rely=0.2)
        
        
      
    elif (user=='divyajohn@ssn.edu.in' and passw=='dj'):
        myframe.destroy()
        myframe=LabelFrame(m,bg="white")   #importing the frame colour
        myframe.grid(row=0,column=0,padx=100,pady=50)
        column=len(l[1])
        mentees=main.T3
        records=mentees.inorder(main.root3,[])
        for i in range(len(records)):
            for j in range(column):
                e=Label(myframe,width=25,height=2,text=records[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
                e.grid(row=0,column=0)
                e.grid(row=i,column=j)
        f=Button(m,text='ADD',command=lambda: add(myframe,'divyajohn@ssn.edu.in'))
        f.place(relx=0,rely=0.1)
        g=Button(m,text='UPDATE',command=lambda: update(myframe,'divyajohn@ssn.edu.in'))
        g.place(relx=0,rely=0.2)
        h=Button(m,text='DELETE',command=lambda: delete(myframe,'divyajohn@ssn.edu.in'))
        h.place(relx=0,rely=0.3)
        i=Button(m,text='MEETING WITH MENTEE',command=lambda :meeting(myframe,'divyajohn@ssn.edu.in'))
        i.place(relx=0,rely=0.4)
        j=Button(m,text='ACADEMIC INFO.',command=lambda :cat1cat2(myframe,'divyajohn@ssn.edu.in'))
        j.place(relx=0,rely=0.2)
        
    else:
        messagebox.showinfo("","incorrect")

def raja(myframe):
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.grid(row=0,column=0)
    column=len(l[1])
    mentees=main.T2
    records=mentees.inorder(main.root2,[])
    for i in range(len(records)):
        for j in range(column):
            e=Label(myframe,width=25,height=2,text=records[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
            e.grid(row=0,column=0)
            e.grid(row=i,column=j)
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)
def dj(myframe):
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.grid(row=0,column=0)
    column=len(l[1])
    mentees=main.T3
    records=mentees.inorder(main.root3,[])
    for i in range(len(records)):
        for j in range(column):
            e=Label(myframe,width=25,height=2,text=records[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
            e.grid(row=0,column=0)
            e.grid(row=i,column=j)
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)
def chandra(myframe):
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.grid(row=0,column=0)
    
    column=len(l[1])
    mentees=main.T1
    records=mentees.inorder(main.root1,[])
    for i in range(len(records)):
        for j in range(column):
            e=Label(myframe,width=25,height=2,text=records[i][j],fg='white',bg='#A2ACBE',borderwidth=0)
            e.grid(row=0,column=0)
            e.grid(row=i,column=j)
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)
def muke(myframe):
    arshat=clicked2.get() #cat1 or cat2
    bb=clicked3.get() #subjects
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import avl
# import linkedlist
#file names should be changed
    # f5=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\CAT-1results.txt","r")
    # r5=csv.reader(f5)
    # no=next(csv.reader(f5))
    # cat1=Arr()
    # for i in csv.reader(f5):
    #     cat1.append(i)
    # f5.close()
    # #reading cat2.txt file. lines:77-83
    # f6=open(r"C:\Users\ashwi\OneDrive\Desktop\SSN-mentoring-system-project-1\CAT-2 results.txt","r")
    # r6=csv.reader(f6)
    # no=next(csv.reader(f6))
    # cat2=Arr()
    # for i in csv.reader(f6):
    #     cat2.append(i)
    # f6.close()
    # def math(arr,n=3):
    #     marks=Arr()
    #     for i in arr:
    #         marks.append([i[0],i[1],i[n]])
    #     return marks
    # def beee(arr,n=4):
    #     marks=Arr()
    #     for i in arr:
    #         marks.append([i[0],i[1],i[n]])
    #     return marks
    # def phy(arr,n=5):
    #     marks=Arr()
    #     for i in arr:
    #         marks.append([i[0],i[1],i[n]])
    #     return marks
    # def pds(arr,n=6):
    #     marks=Arr()
    #     for i in arr:
    #         marks.append([i[0],i[1],i[n]])
    #     return marks
    # def hse(arr,n=7):
    #     marks=Arr()
    #     for i in arr:
    #         marks.append([i[0],i[1],i[n]])
    #     return marks
    # def evs(arr,n=8):
    #     marks=Arr()
    #     for i in arr:
    #         marks.append([i[0],i[1],i[n]])
    #     return marks
    # def CAT1(arr=cat1):
    #     marks=Arr()
    #     for i in arr:
    #         marks.append([i[0],i[1],i[3],i[4],i[5],i[6],i[7],i[8]])
    #     return marks
    # def CAT2(arr=cat2):
    #     marks=Arr()
    #     for i in arr:
    #         marks.append([i[0],i[1],i[3],i[4],i[5],i[6],i[7],i[8]])
    #     return marks
    def subject(sub):
        if sub=="MATHS":
            a=acad.MATHS(acad.cat1)
            m=marks(a)
            return m
        elif sub=="BEEE":
            a=acad.BEEE(acad.cat1)
            m=marks(a)
            return m
        elif sub=="PHYSICS":
            a=acad.PHY(acad.cat1)
            m=marks(a)
            return m
        elif sub=="PDS":
            a=acad.PDS(acad.cat1)
            m=marks(a)
            return m
        elif sub=="HSE":
            a=acad.HSE(acad.cat1)
            m=marks(a)
            return m
        elif sub=="EVS":
            a=acad.EVS(acad.cat1)
            m=marks(a)
            return m
        
    #plotting functions and plot creation
    l1=[]
    def marks(arr,l=[]):
        for i in arr:
            l.append(int(i[-1]))
        return l
    markinput=bb
    mark=subject(markinput)
    #print(mark)
    # subject("beee")
    # subject("phy")
    # subject("pds")
    # subject("hse")
    # subject("evs")
    # frequencies
    ages = mark
    # frequencies
    # setting the ranges and no. of intervals
    range = (0, 50)
    bins = 5

    # plotting a histogram
    plt.hist(ages, bins, range, color = 'green',
            histtype = 'bar', rwidth = 0.8)
    # x-axis label
    plt.xlabel('STUDENT MARKS')
    # frequency label
    plt.ylabel('No. of Students')
    # plot title
    plt.title('Students vs Marks')
    # function to show the plot
    plt.show()
    fp=[]
    pp=[]
    ap=[]
    #now we have to take the mark list traverse it and find students who passed the test and failed the test
    def fpp_count(mark):
        for i in mark:
            if 50>=i>=25:
                pp.append(i)
            elif 0<=i<=25:
                fp.append(i)
            else:
                ap.append(i)
        # return f'{len(pp)},{len(fp)},{len(ap)}'
        return len(pp),len(fp),len(ap)
    
    percent_input=fpp_count(mark)
    print(percent_input)
    l=[]
    for j in percent_input:
        j=(j/65)*100
        l.append(j)
    
    def chart():
        
        exp_vals= [int(l[0]),int(l[1])]
        
        #print(l)
        colors=["r","g","b"]
        arshat_labels=["failurepercentage","passpercentage"]
        plt.pie(exp_vals,radius=1.5,autopct='%0.1f%%',shadow=True)
        plt.axis("equal")
        plt.title("Composition of results and Average marks")
        plt.show()
    chart()
    
def muk(myframe):
    global clicked3
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.pack(padx=100,pady=100)
    options = ["MATHS","BEEE",'PHYSICS','PDS','HSE','EVS']
    clicked3 = StringVar()
    clicked3.set("SELECT SUBJECT")
    drop = OptionMenu( myframe, clicked3 , *options )
    drop.pack()
    button = Button( myframe, text = "SELECT",command=lambda: muke(myframe) ).pack()
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)
    #b4=Button(myframe,text='HOME',command=lambda :back(myframe)).pack()

def acadrep(myframe):
    global clicked2
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.pack(padx=100,pady=100)
    options = [
	    "CAT-1",
	    "CAT-2",]

# datatype of menu text

    clicked2= StringVar()

    # initial menu text
    clicked2.set("SELECT EXAM")

    # Create Dropdown menu
    drop = OptionMenu( myframe, clicked2 , *options )
    drop.pack()
    #print(a)
    # Create button, it will change label text
    button = Button( myframe, text = "SELECT",command=lambda: muk(myframe) ).pack()
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)
    #b4=Button(myframe,text='HOME',command=lambda :back(myframe)).pack()

def login2(myframe):
    
    user2=entry1.get()
    passw2=entry2.get()
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.place(relx=0.4,rely=0.4)
    
    if user2=='' and passw2=='':
        messagebox.showinfo("","Invalid Username or Password")
    elif user2=='Manager' and passw2=='123':
        myframe.destroy()
        myframe=LabelFrame(m,bg="#A2ACBE")   #importing the frame colour
        myframe.place(relx=0.4,rely=0.4)
        
        b1=Button(myframe,text='ACADEMIC REPORT',bg="#A2ACBE",font=('Helvetica',14),width=0,command=lambda :acadrep(myframe))
        
        b1.grid(row=4,column=0,padx=10,pady=10)
        b2=Button(myframe,text='Dr. Chandrasekar',bg="#A2ACBE",font=('Helvetica',14),width=0,command=lambda:chandra(myframe))
        b2.grid(row=4,column=1,padx=10,pady=10)
        b=Button(myframe,text='Dr. Rajalakshmi',bg="#A2ACBE",font=('Helvetica',14),width=0,command=lambda:raja(myframe))
        b.grid(row=4,column=2,padx=10,pady=10)
        b3=Button(myframe,text='Dr. Divya John',bg="#A2ACBE",font=('Helvetica',14),width=0,command=lambda:dj(myframe))
        b3.grid(row=4,column=3,padx=10,pady=10)
        #b4=Button(myframe,text='HOME',command=lambda :back(myframe)).grid(row=3,column=3)
        b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
        b4.place(relx=0,rely=0)
def back(myframe):
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.place(relx=0.4,rely=0.4)
    mybutton1=Button(myframe,text="Manager",bg="#A2ACBE",font=('Helvetica',14),command=lambda:open2(myframe))        # creating buttons for manager, mentor , mentee
    mybutton1.grid(row=1,column=0,padx=10,pady=10)
    mybutton2=Button(myframe,text="Mentor",bg="#A2ACBE",font=('Helvetica',14),command=lambda :open1(myframe))
    mybutton2.grid(row=1,column=1,padx=10,pady=10)
    mybutton3=Button(myframe,text="Mentee",bg="#A2ACBE",font=('Helvetica',14),command=lambda :openx(myframe))    
    mybutton3.grid(row=1,column=2,padx=10,pady=10)

def openx(myframe):
    
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",padx=25,pady=40,bd=0)   #importing the frame colour
    myframe.place(relx=0.4,rely=0.3)

    global lf
    global entry1
    global entry2
    b3=Button(myframe,text="BACK",fg='white',bg='#A2ACBE',font=('Helvetica',12),command=lambda :back(myframe)).place(relx=0.3,rely=1)
    la=Label(myframe,text="USERNAME :",font=('Helvetica',14),fg='white',bg='#A2ACBE').grid(row=1,column=0)   #function for creating the username and password button
    la2=Label(myframe,text='PASSWORD :',font=('Helvetica',14),fg='white',bg='#A2ACBE').grid(row=2,column=0)
    entry1=Entry(myframe,bd=5)
    entry1.grid(row=1,column=2)
    entry2=Entry(myframe,bd=5,show='*')
    entry2.grid(row=2,column=2)
    lf=[]
    lf.append(entry1.get())
    lf.append(entry2.get())
    b2=Button(myframe,text="LOGIN",fg='white',bg='#A2ACBE',padx=1,pady=1,font=('Helvetica',12),command=lambda: login(myframe)).place(relx=0.7,rely=1)
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)
def open1(myframe):
    
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",padx=25,pady=40,bd=0)   #importing the frame colour
    myframe.place(relx=0.4,rely=0.3)

   
    global entry1
    global entry2
    b3=Button(myframe,text="BACK",fg='white',bg='#A2ACBE',font=('Helvetica',12),command=lambda :back(myframe)).place(relx=0.3,rely=1)
    la=Label(myframe,text="USERNAME :",font=('Helvetica',14),fg='white',bg='#A2ACBE').grid(row=1,column=0)   #function for creating the username and password button
    la2=Label(myframe,text='PASSWORD :',font=('Helvetica',14),fg='white',bg='#A2ACBE').grid(row=2,column=0)
    entry1=Entry(myframe,bd=5)
    entry1.grid(row=1,column=2)
    entry2=Entry(myframe,bd=5,show='*')
    entry2.grid(row=2,column=2)
    b2=Button(myframe,text="LOGIN",fg='white',bg='#A2ACBE',padx=1,pady=1,font=('Helvetica',12),command=lambda :login1(myframe)).place(relx=0.7,rely=1)
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)   
def open2(myframe):
    
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",padx=25,pady=40,bd=0)   #importing the frame colour
    myframe.place(relx=0.4,rely=0.3)
    global entry1
    global entry2
    b3=Button(myframe,text="BACK",fg='white',bg='#A2ACBE',font=('Helvetica',12),command=lambda :back(myframe)).place(relx=0.3,rely=1)
    la=Label(myframe,text="USERNAME :",font=('Helvetica',14),fg='white',bg='#A2ACBE').grid(row=1,column=0)   #function for creating the username and password button
    la2=Label(myframe,text='PASSWORD :',font=('Helvetica',14),fg='white',bg='#A2ACBE').grid(row=2,column=0)
    entry1=Entry(myframe,bd=5)
    entry1.grid(row=1,column=2)
    entry2=Entry(myframe,bd=5,show='*')
    entry2.grid(row=2,column=2)
    b2=Button(myframe,text="LOGIN",fg='white',bg='#A2ACBE',padx=1,pady=1,font=('Helvetica',12),command=lambda :login2(myframe)).place(relx=0.7,rely=1)
    b4=Button(m,text='HOME',bg="#A2ACBE",font=('Helvetica',14),command=lambda :back(myframe))
    b4.place(relx=0,rely=0)

mybutton1=Button(myframe,text="Manager",bg="#A2ACBE",font=('Helvetica',14),command=lambda :open2(myframe))        # creating buttons for manager, mentor , mentee
mybutton1.grid(row=4,column=0,padx=10,pady=10)
mybutton2=Button(myframe,text="Mentor",bg="#A2ACBE",font=('Helvetica',14),command=lambda :open1(myframe))
mybutton2.grid(row=4,column=1,padx=10,pady=10)
mybutton3=Button(myframe,text="Mentee",bg="#A2ACBE",font=('Helvetica',14),command=lambda :openx(myframe))    
mybutton3.grid(row=4,column=2,padx=10,pady=10)


m.mainloop()
