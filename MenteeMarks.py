import csv
import samplecode
from tkinter import *

username=input("Enter username:")
password=input("Enter password:")
exam=input("Enter CAT-1, CAT-2 or SAT:")

if exam=="CAT-1":

    f=open(r"CAT-1results.txt","r")
    c=csv.reader(f)
    no=next(c)
    l=[]
    for i in c:
        l.append(i)
    f.close()

    marks_tree=samplecode.createBST(l)

elif exam=="CAT-2":
    f=open(r"CAT-2results.txt","r")
    c=csv.reader(f)
    no=next(c)
    l=[]
    for i in c:
        l.append(i)
    f.close()

    marks_tree=samplecode.createBST(l)

elif exam=="SAT":
    f=open()  #inside the parenthesis put the filename containing SAT Marks
    c=csv.reader(f)
    no=next(c)
    l=[]
    for i in c:
        l.append(i)
    f.close()

    marks_tree=samplecode.createBST(l)


samplecode.retrievex(marks_tree,username,1)

marks_details=samplecode.one_mentee_details[3:]
marks_details=[("Maths",marks_details[0]),("BEEE",marks_details[1]),("Physics",marks_details[2]),("PDS",marks_details[3]),
("HSE",marks_details[4]),("EVS",marks_details[5])]

total_rows=len(marks_details)
root=Tk()
for i in range(total_rows):
    for j in range(2):
        e=Entry(root,width=20,fg='blue')
        e.grid(row=i,column=j)
        e.insert(0,marks_details[i][j])  
    

root.mainloop()








