from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
def login():
 if usernameEntry.get() == '' or passwordEntry.get() == '':
 messagebox.showerror('Error', 'Fields cannot be empty')
 else:
 if usernameEntry.get() == "Mtende" and passwordEntry.get() == "1234":
 messagebox.showinfo('Success', 'Welcome')
 window.destroy()
 import sms
 else:
 messagebox.showinfo('Detail', 'Not much')
# Create the main window
window = Tk()
window.geometry('1280x700+0+0')
window.title('log in system of the student management system')
# Load background image
#backgroundimage = ImageTk.PhotoImage(file='logo.jpg')
# Create a label to display the background image
#bgLabel = Label(window, image=backgroundimage)
#bgLabel.place(x=0, y=0)
# Create a login frame
loginFrame = Frame(window)
loginFrame.place(x=400, y=150)
# Load logo image
#logoImage = ImageTk.PhotoImage(file='mt.png')
# Create a label to display the logo image
#logoLabel = Label(loginFrame, image=logoImage)
#logoLabel.grid(row=0, column=0, columnspan=2, pady=10, padx=20)
# Load username image
usernameImage = ImageTk.PhotoImage(file='user.png')
# Create a label for username with an image
usernameLabel = Label(loginFrame, image=usernameImage, text="username",
compound=LEFT,
 font=('times new roman', 20, 'bold'), bg='white')
usernameLabel.grid(row=1, column=0)
# Create an entry widget for username
usernameEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5,
fg='royalblue')
usernameEntry.grid(row=1, column=1, pady=10, padx=20)
# Load password image
passwordImage = ImageTk.PhotoImage(file='password.png')
# Create a label for password with an image
passwordLabel = Label(loginFrame, image=passwordImage, text="password",
compound=LEFT,
 font=('times new roman', 20, 'bold'), bg='white')
passwordLabel.grid(row=2, column=0)
# Create an entry widget for password
passwordEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5,
fg='royalblue')
passwordEntry.grid(row=2, column=1, pady=10, padx=20)
# Create a login button
loginButton = Button(loginFrame, text='login', font=('times new roman', 14, 'bold'),
width=15,
 bg='blue', cursor='hand2', command=login)
loginButton.grid(row=3, column=1, pady=10)
# Start the main event loop
window.mainloop()
