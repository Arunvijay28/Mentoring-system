# SSN-mentoring-system
Creating an Mentoring system for an organization like SSN

## Description 
An organization like SSN College of Engineering wants to develop a mentoring system. A
mentor should be able to view all the mentees assigned to them. On selecting a mentee, the
mentor should be able to add/delete/update the mentee details. The mentor may schedule a
meeting with a mentee and should be able to capture the meeting details later. A mentee
should be able to see only their details, except for the confidential information entered by the
mentor. A mentee should be able to request for a meeting with the mentor through this
system. The manager should be able to generate various reports from these mentee records

## Walkthorugh

### Home Page
<img src="/images/Screenshot 2023-12-14 203540.png" width=50%>

## Tools used
1) Tkinter    - Creating GUI
2) Python     - Implementing Data Structures Algorithms
3) Matplotlib - Visualtion


## Algorithms used

### AVL TREE

As all the Mentees are assigned to a Mentor. if we use linked list searching for a Mentee by a Mentor takes O(n) time complexity.
But by implementing AVL Tree the height of the tree is balanced so that searching takes O(log(n))

### Linked List

All the Mentor and reference of their Mentees are in a linked list . Whereas Mentees are stored as AVL Tree

### Hash Table
To store the login credentials of Mentee,Mentor,Manager . The reason for choosing Hash Table rather than dictionary is because of the time complexity as the average time complexity of Hash Table is O(1)

### Arrays
1-Dimensional Array to store CAT-1 and CAT-2 marks of the students

## Visualization

### Manager side
To show the overall report to the manager we used Matplotlib for visualising the data which is stored in form of text file.
By Clicking a particular Mentor, The Manager could able to see the mark details of the corresponding Mentees in form of pie chart and bar graph
