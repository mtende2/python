from tkinter import *
from tkinter import ttk, messagebox
import time
import pymysql
import ttkthemes
def add_student():
 def connect():
 try:
 con = pymysql.connect(host=hostEntry.get(), user=userEntry.get(),
password=passwordEntry.get())
 mycursor = con.cursor()
 mycursor.execute("SELECT 1")
 messagebox.showinfo('Success', 'Database connection is successful',
parent=connectWindow)
 except pymysql.Error:
 messagebox.showerror('Error', 'Invalid details', parent=connectWindow)
 return
 query = 'CREATE DATABASE IF NOT EXISTS studentmanagementsystem'
 mycursor.execute(query)
 query = 'USE studentmanagementsystem'
 mycursor.execute(query)
 query = '''CREATE TABLE IF NOT EXISTS student(id INT NOT NULL PRIMARY KEY,
 name VARCHAR(30), mobile
VARCHAR(10), email VARCHAR(30),
 address VARCHAR(50), gender
VARCHAR(20), dob VARCHAR(20),
 date VARCHAR(50), time
VARCHAR(50))'''
 mycursor.execute(query)
 connectWindow.destroy()
 # Activate buttons after a successful connection
 addstudentButton.config(state=NORMAL)
 searchstudentButton.config(state=NORMAL)
 deletestudentButton.config(state=NORMAL)
 updatestudentButton.config(state=NORMAL)
 showstudentButton.config(state=NORMAL)
 exportstudentButton.config(state=NORMAL)
 exitstudentButton.config(state=NORMAL)
 connectWindow = Toplevel()
 connectWindow.geometry('470x250+730+230')
 connectWindow.title('Database connection')
 connectWindow.resizable(0, 0)
 hostnamelabel = Label(connectWindow, text='Host Name', font=('arial', 20,
'bold'))
 hostnamelabel.grid(row=0, column=0, padx=20)
 hostEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
 hostEntry.grid(row=0, column=1, padx=40, pady=20)
 usernamelabel = Label(connectWindow, text='User Name', font=('arial', 20,
'bold'))
 usernamelabel.grid(row=1, column=0, padx=20)
 userEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
 userEntry.grid(row=1, column=1, padx=40, pady=20)
 passwordlabel = Label(connectWindow, text='Password', font=('arial', 20,
'bold'))
 passwordlabel.grid(row=2, column=0, padx=20)
 passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2, show='*')
 passwordEntry.grid(row=2, column=1, padx=40, pady=20)
 connectButton = ttk.Button(connectWindow, text='CONNECT', command=connect)
 connectButton.grid(row=3, columnspan=2)
# GUI part
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('1774x680+0+0')
root.title('Student Management System')
datetimelabel = Label(root, font=('times new roman', 18, 'bold'))
datetimelabel.place(x=5, y=5)
s = 'Student management system'
sliderlabel = Label(root, text='', font=('times new roman', 28, 'bold'), width=30)
sliderlabel.place(x=200, y=0)
connectButton = ttk.Button(root, text='Connect Database', command=add_student)
connectButton.place(x=980, y=0)
count = 0
text = ''
def slider():
 global text, count
 if count == len(s):
 count = 0
 text = ''
 text = text + s[count]
 sliderlabel.config(text=text)
 count += 1
 sliderlabel.after(300, slider)
def clock():
 date = time.strftime('%d/%m/%Y')
 currenttime = time.strftime('%H:%M:%S')
 datetimelabel.config(text=f' Date: {date}\nTime: {currenttime}')
 datetimelabel.after(1000, clock)
# GUI part
root.geometry('1774x680+0+0')
root.title('Student Management System')
datetimelabel = Label(root, font=('times new roman', 18, 'bold'))
datetimelabel.place(x=5, y=5)
clock()
leftframe = Frame(root)
leftframe.place(x=50, y=80, width=300, height=600)
addstudentButton = ttk.Button(leftframe, text='Add Student', width=25,
state=DISABLED, command=add_student)
addstudentButton.grid(row=1, column=0, pady=20)
searchstudentButton = ttk.Button(leftframe, text='Search Student', width=25,
state=DISABLED)
searchstudentButton.grid(row=2, column=0, pady=20)
deletestudentButton = ttk.Button(leftframe, text='Delete Student', width=25,
state=DISABLED)
deletestudentButton.grid(row=3, column=0, pady=20)
updatestudentButton = ttk.Button(leftframe, text='Update Student', width=25,
state=DISABLED)
updatestudentButton.grid(row=4, column=0, pady=20)
showstudentButton = ttk.Button(leftframe, text='Show Student', width=25,
state=DISABLED)
showstudentButton.grid(row=5, column=0, pady=20)
exportstudentButton = ttk.Button(leftframe, text='Export Data', width=25,
state=DISABLED)
exportstudentButton.grid(row=6, column=0, pady=20)
exitstudentButton = ttk.Button(leftframe, text='Exit', width=25)
exitstudentButton.grid(row=7, column=0, pady=20)
rightframe = Frame(root)
rightframe.place(x=350, y=80, width=820, height=600)
scrollBarX = Scrollbar(rightframe, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightframe, orient=VERTICAL)
studentTable = ttk.Treeview(rightframe, columns=('id', 'name', 'mobile', 'email',
'address', 'gender',
 'dob', 'date', 'time'),
 xscrollcommand=scrollBarX.set,
yscrollcommand=scrollBarY.set)
scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)
scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)
studentTable.pack(fill=BOTH, expand=1)
studentTable.heading('id', text='ID')
studentTable.config(show='headings')
studentTable.heading('name', text='Name')
studentTable.heading('mobile', text='Mobile')
studentTable.heading('email', text='Email')
studentTable.heading('address', text='Address')
studentTable.heading('gender', text='Gender')
studentTable.heading('dob', text='D.O.B', anchor=W)
studentTable.heading('date', text='Added Date')
studentTable.heading('time', text='Added Time')
slider()
clock()
root.mainloop()
