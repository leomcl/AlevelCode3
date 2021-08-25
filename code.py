from tkinter import *
import tkinter.simpledialog as simpledialog
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk



# functions  
def raise_frame(frame_name):
    frame_name.tkraise()


def login():
    raise_frame(managermenuframe)
    root.geometry('590x600')


def forgot_password():
    pass


def Button1():
    raise_frame(MangerDriverFrame)
    root.geometry('640x600')


def MangerMenu():
    raise_frame(managermenuframe)
    root.geometry('640x600')


def ManagerDriver():
    raise_frame(MangerDriverFrame)
    root.geometry('640x600')


def AddDriver():
    pass


def DelDriver():
    pass


def EmailDriver():
    pass


# variables
username = ''
Password = ''
MangerTVSerVal = ''
FirstNameD = ''
LastNameD = ''
EmailD = ''

# root
root = ThemedTk(theme='yaru')
root.geometry('550x500')
root.title('Logistyics App')
root.configure(background='white')

# frames
loginframe = Frame(root, bg='white')
create_account_frame = Frame(root, bg='light grey')
resetpasswordframe = Frame(root, bg='light grey')
membermenuframe = Frame(root, bg='white')
managermenuframe = Frame(root, bg='white')
MangerDriverFrame = Frame(root, bg='white')
ManagerStaffFrame = Frame(root, bg='light grey')
ManagerClassesFrame = Frame(root, bg='light grey')

for frame in (
loginframe, create_account_frame, resetpasswordframe, membermenuframe, managermenuframe, MangerDriverFrame,
ManagerStaffFrame, ManagerClassesFrame):
    frame.grid(row=0, column=0, sticky='news')

# compoents
# log in frame
photologinscreen = PhotoImage(file='Hannon-Transport.png')
photolabel = Label(loginframe, image=photologinscreen, bg='white')
photolabel.grid(row=0, column=0, sticky=N, columnspan=6)

username_label = ttk.Label(loginframe, text='Username:', font=18)
username_label.grid(row=1, column=2)
username_entry = ttk.Entry(loginframe, textvariable=username, font=18)
username_entry.grid(row=1, column=3)

Password_label = ttk.Label(loginframe, text='Password:', font=18)
Password_label.grid(row=2, column=2)
Password_entry = ttk.Entry(loginframe, textvariable=Password, font=18)
Password_entry.grid(row=2, column=3)

login_button = ttk.Button(loginframe, text='Login', command=login)
login_button.grid(row=3, column=2)

forgot_password_button = ttk.Button(loginframe, text='Forgot password', command=forgot_password)
forgot_password_button.grid(row=3, column=3, pady=10)

# managermenuframe frame
labelframe = LabelFrame(managermenuframe, text='', bg='white', pady=5, padx=5)
labelframe.grid(row=0, column=0)

photomangermenuscreen = PhotoImage(file='Hannon-Transport Small.png')
photolabelmanager = ttk.Label(labelframe, image=photomangermenuscreen)
photolabelmanager.grid(row=0, column=0, sticky=N)

Button1 = ttk.Button(labelframe, command=ManagerDriver, text='Driver').grid(
    row=0, column=1)
Button2 = ttk.Button(labelframe, command=Button1, text='Button2').grid(
    row=0, column=2)
Button3 = ttk.Button(labelframe, command=Button1, text='Button3').grid(
    row=0, column=3)
Button4 = ttk.Button(labelframe, command=Button1, text='Button4').grid(
    row=0, column=4)
Button5 = ttk.Button(labelframe, command=Button1, text='Button5').grid(
    row=0, column=5)
Button6 = ttk.Button(labelframe, command=Button1, text='Button5').grid(
    row=0, column=6)
Button7 = ttk.Button(labelframe, command=MangerMenu, text='Menu').grid(
    row=0, column=7)

# MangerDriverFrame
Driverlabelframe = Frame(MangerDriverFrame, bg='white')
Driverlabelframe.grid(row=0, column=0)

Dphotomangermenuscreen = PhotoImage(file='Hannon-Transport Small.png')
Dphotolabelmanager = Label(Driverlabelframe, image=Dphotomangermenuscreen, bg='white')
Dphotolabelmanager.grid(row=0, column=0, sticky=N)

Button1 = ttk.Button(Driverlabelframe, command=ManagerDriver, text='Driver').grid(row=0, column=1)
Button2 = ttk.Button(Driverlabelframe, command=Button1, text='Button2').grid(row=0, column=2)
Button3 = ttk.Button(Driverlabelframe, command=Button1, text='Button3').grid(row=0, column=3)
Button4 = ttk.Button(Driverlabelframe, command=Button1, text='Button4').grid(row=0, column=4)
Button5 = ttk.Button(Driverlabelframe, command=Button1, text='Button5').grid(row=0, column=5)
Button6 = ttk.Button(Driverlabelframe, command=Button1, text='Button5').grid(row=0, column=6)
Button7 = ttk.Button(Driverlabelframe, command=MangerMenu, text='Menu').grid(row=0, column=7)

managerTVFrameDriver = Frame(MangerDriverFrame)
managerTVFrameDriver.grid(row=1, column=0)
managerTVFrameDriver.configure(bg='white')

SerachlabelD = ttk.Label(managerTVFrameDriver, text='Search:').grid(row=0, column=0, padx=10)
search_entryD = ttk.Entry(managerTVFrameDriver, textvariable=MangerTVSerVal, width=90).grid(row=0, column=1)

managerTVDriver = ttk.Treeview(managerTVFrameDriver, height=10,
                               columns=('First Name', 'Last Name', 'Column 2 ', 'Coulmn 3'))
managerTVDriver.grid(row=2, column=0, columnspan=30, pady=10)

managerTVDriver.heading('#0', text='Email')
managerTVDriver.column('#0', minwidth=0, width=200, anchor='center')
managerTVDriver.heading('#1', text='First Name')
managerTVDriver.column('#1', minwidth=0, width=110, anchor='center')
managerTVDriver.heading('#2', text='Last Name')
managerTVDriver.column('#2', minwidth=0, width=130, anchor='center')
managerTVDriver.heading('#3', text='Deliveries')
managerTVDriver.column('#3', minwidth=0, width=120, anchor='center')
managerTVDriver.heading('#4', text='Avaliabilty')
managerTVDriver.column('#4', minwidth=0, width=70, anchor='center')

managerInputsFrameDriver = LabelFrame(MangerDriverFrame, text='Inputs', bg='white', pady=5, padx=5)
managerInputsFrameDriver.grid(row=2, column=0)
managerInputsFrameDriver.configure(bg='white')

FirstNameLabelD = ttk.Label(managerInputsFrameDriver, text='First Name:').grid(row=0, column=0, padx=10)
FirstNameentryD = ttk.Entry(managerInputsFrameDriver, textvariable=FirstNameD).grid(row=0, column=1)

LastNameLabelD = ttk.Label(managerInputsFrameDriver, text='Last Name:').grid(row=0, column=2, padx=10)
LastNameentryD = ttk.Entry(managerInputsFrameDriver, textvariable=LastNameD).grid(row=0, column=3)

EmailLabelD = ttk.Label(managerInputsFrameDriver, text='Email:').grid(row=0, column=4, padx=10)
EmailentryD = ttk.Entry(managerInputsFrameDriver, textvariable=EmailD).grid(row=0, column=5)

AddDriverButton = ttk.Button(managerInputsFrameDriver, text='Add Driver', command=AddDriver).grid(row=1, column=0, padx=10,
                                                                                              pady=10)

DelDriverButton = ttk.Button(managerInputsFrameDriver, text='Delete Driver', command=DelDriver).grid(row=1, column=2,
                                                                                                 padx=10, pady=10)

EmailDriverButton = ttk.Button(managerInputsFrameDriver, text='Send Email', command=EmailDriver).grid(row=1, column=4,
                                                                                                  padx=10, pady=10)

raise_frame(loginframe)
root.mainloop()
