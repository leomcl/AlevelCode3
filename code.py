from tkinter import *
import tkinter.simpledialog as simpledialog
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import random
import config
import time
from time import strftime


# functions
def LogOut():
    raise_frame(loginframe)




def timememberscreen():
    def timemember():
        string = strftime('%H:%M:%S %p')
        adminMemberClockLabel.config(text=string)
        adminMemberClockLabel.after(1000, timemember)

    timemember()


def raise_frame(frame_name):
    frame_name.tkraise()


def BackLogin():
    raise_frame(loginframe)
    root.geometry('640x600')


def Button1():
    raise_frame(MangerDriverFrame)
    root.geometry('1400x900')


def MangerMenu():
    timememberscreen()
    raise_frame(managermenuframe)
    root.geometry('1400x800')


def ManagerDriver():
    ShowDriverTV()
    ShowDriverPreformaceTV()
    UpdateDriverMangerWidg()
    raise_frame(MangerDriverFrame)
    root.geometry('1400x800')


def usernameandpass():
    conn = sqlite3.connect('data.db')
    mycursor = conn.cursor()

    sql = "INSERT INTO passwords (username, password, type) VALUES (?, ?, ?)"
    val = ("leo", "leo", "customs")
    mycursor.execute(sql, val)

    conn.commit()
    print('done')


def login():
    Finialusername = username.get()

    Finialpassword = Password.get()
    print(Finialpassword, Finialusername)
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * from passwords WHERE username = (?)", (Finialusername,))
    reader = c.fetchall()
    print(reader)
    for row in reader:
        if row[2] == Finialpassword and row[3] == 'driver':
            MangerMenu()
            print('driver')
        elif row[2] == Finialpassword and row[3] == 'client':
            MangerMenu()
            print('driver')
        elif row[2] == Finialpassword and row[3] == 'loader':
            MangerMenu()
            print('driver')
        elif row[2] == Finialpassword and row[3] == 'customs':
            MangerMenu()
            print('customs')
        else:
            messagebox.showinfo("Info", "Incorect password", icon="info")


def forgot_password():
    global number
    number = random.randint(1111, 9999)
    print('OTP:', number)
    global email
    email = simpledialog.askstring("Information", "Enter email:")
    # global forget_email
    # forget_email = email
    subject = 'Reset Password'
    msg = MIMEMultipart()
    msg['From'] = config.emailAddress
    msg['To'] = email
    msg['Subject'] = subject
    body = 'Reset code is: ' + str(number)
    msg.attach(MIMEText(body, 'plain'))

    part = MIMEBase('application', 'octet-stream')
    text = msg.as_string()

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * from passwords WHERE username = (?)", (email,))
    reader = c.fetchall()
    print(reader)

    for row in reader:
        if email != row[1]:
            messagebox.showinfo('Email Error', 'This account does not exist')

        else:
            try:
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.ehlo()
                server.starttls()
                server.login(config.emailAddress, config.password)
                server.sendmail(config.emailAddress, email, text)
                server.quit()
                print('email sent')
                messagebox.showinfo('Email sent', 'Code sent in email.')
                raise_frame(resetpasswordframe)
                resetpasswordframe.geometry('500x500')

            except:
                print('Email not sent')

    conn.commit()
    conn.close()


def ResetPassword():
    FinialNewPassword = REpassword1.get()
    FinialNewPassword2 = REpassword2.get()
    FinialOTPcode = OTPcode.get()

    print(number, FinialOTPcode)
    if len(FinialNewPassword) < 8:
        print('Invalid password')
    else:
        if str(FinialOTPcode) == str(number) and FinialNewPassword2 == FinialNewPassword:
            value = (FinialNewPassword, email)
            conn = sqlite3.connect('data.db')
            c = conn.cursor()

            c.execute("""UPDATE passwords SET password = ?
			WHERE username = ?
			""", value)

            conn.commit()
            conn.close()
            raise_frame(loginframe)
            messagebox.showinfo('Password Reset',
                                'Your password has been reset Successfully. Login with your new password')

        elif str(FinialOTPcode) != str(number) and FinialNewPassword2 == FinialNewPassword:
            messagebox.showinfo('Code', 'Reset password code does match the one sent in the email')

        elif str(FinialOTPcode) == str(number) and FinialNewPassword2 != FinialNewPassword:
            messagebox.showinfo('Invalid password Error', 'New password must match confirm password')

        else:
            messagebox.showinfo('Invalid Error', 'Error password does not match confrm password try again')
            FinialOTPcode.set('')
            FinialNewPassword.set('')
            FinialNewPassword2.set('')


def ShowDriverTV():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    managerTVDriver.delete(*managerTVDriver.get_children())
    c.execute("SELECT * FROM drivers")
    for row in c:
        managerTVDriver.insert('', 'end', text=row[0], values=row[1:5])
    print(c)


def AddDriver():
    type = 'driver'
    password = 'NotSet'
    Ffirstname = FirstNameD.get()
    Flastname = LastNameD.get()
    Femail = EmailD.get()
    conn = sqlite3.connect('data.db')
    mycursor = conn.cursor()

    sql = "INSERT INTO drivers (email, firstname, lastname, deliveries, avaliablity) VALUES (?, ?, ?, ?, ?)"
    val = (Femail, Ffirstname, Flastname, 0, "Yes")
    mycursor.execute(sql, val)
    mycursor.execute("INSERT INTO passwords (username, password, type) VALUES (?, ?, ?)", (Femail, type, password))
    conn.commit()

    subject = 'New Hannon Account'
    msg = MIMEMultipart()
    msg['From'] = config.emailAddress
    msg['To'] = Femail
    msg['Subject'] = subject
    body = 'Welcome to hannon computer system. To set password click "reset password"'
    msg.attach(MIMEText(body, 'plain'))

    part = MIMEBase('application', 'octet-stream')
    text = msg.as_string()
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.emailAddress, config.password)
        server.sendmail(config.emailAddress, Femail, text)
        server.quit()
        print('email sent')
        messagebox.showinfo('Info', 'Added ')
        raise_frame(resetpasswordframe)
        resetpasswordframe.geometry('500x500')

    except:
        print('Email not sent')

    ShowDriverTV()
    UpdateDriverMangerWidg()


def DelDriver():
    curItem = managerTVDriver.focus()
    dictionary = managerTVDriver.item(curItem)
    print(curItem)
    print(dictionary)
    listvalues = list(dictionary.values())
    print(listvalues)
    TheEmail = listvalues[0]
    print(TheEmail)
    conn = sqlite3.connect('data.db')
    Response = messagebox.askyesno('Are you sure', 'Are you sure you want to delete this user ')
    if Response:
        c = conn.cursor()
        c.execute("DELETE from drivers WHERE email = (?)", (TheEmail,))
        c.execute("DELETE from passwords WHERE username = (?)", (TheEmail,))
        conn.commit()
        conn.close()
        ShowDriverTV()
    elif Response == 'No':
        Response.destroy()
    UpdateDriverMangerWidg()


def EmailDriver():
    pass


def ShowDriverPreformaceTV():
    FinialSerTV = SerTV.get()
    print(FinialSerTV)
    if FinialSerTV == 'All':
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        managerDriverPrefTVDriver.delete(*managerDriverPrefTVDriver.get_children())
        c.execute("SELECT * FROM driverPreformace")
        for row in c:
            managerDriverPrefTVDriver.insert('', 'end', text=row[0], values=row[1:3])
        print(c)
    elif FinialSerTV == 'New Lates':
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        managerDriverPrefTVDriver.delete(*managerDriverPrefTVDriver.get_children())
        c.execute("SELECT * FROM driverPreformace WHERE newLAte != 0")
        for row in c:
            managerDriverPrefTVDriver.insert('', 'end', text=row[0], values=row[1:3])
        print(c)


def UpdateDriverMangerWidg():
    AmountNo = 0
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM drivers WHERE avaliablity = 'No'")
    for row in c:
        AmountNo += 1
    LableValueNo.set(AmountNo)

    AmountYes = 0
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM drivers WHERE avaliablity = 'Yes'")
    for row in c:
        AmountYes += 1
    LableValueYes.set(AmountYes)

    AmountNew = 0
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM driverPreformace WHERE newLate != 0")
    for row in c:
        AmountNew += 1
    LableValueNew.set(AmountNew)


def EmailDriverWarningAll():
    pass


def EmailDriverWarningNew():
    pass


def EmailDriverWarningSel():
    pass


root = ThemedTk(theme='yaru')
root.geometry('550x500')
root.title('Logistyics App')
root.configure(background='white')

# variables
# login

username = StringVar()
Password = StringVar()

# manger driver
MangerTVSerVal = StringVar()
FirstNameD = StringVar()
LastNameD = StringVar()
EmailD = StringVar()
SerTV = StringVar()
LableValueYes = StringVar()
LableValueNo = StringVar()
LableValueNew = StringVar()

# rest psssword
REpassword1 = StringVar()
REpassword2 = StringVar()
OTPcode = StringVar()

# frames
loginframe = Frame(root, bg='white')
create_account_frame = Frame(root, bg='white')
resetpasswordframe = Frame(root, bg='white')
membermenuframe = Frame(root, bg='white')
managermenuframe = Frame(root, bg='white')
MangerDriverFrame = Frame(root, bg='white')
ManagerStaffFrame = Frame(root, bg='light grey')
ManagerClassesFrame = Frame(root, bg='light grey')

for frame in (
        loginframe, create_account_frame, resetpasswordframe, membermenuframe, managermenuframe, MangerDriverFrame,
        ManagerStaffFrame, ManagerClassesFrame):
    frame.grid(row=0, column=0, sticky='news')

# styles
s = ttk.Style()
s.configure('my.TButton', font=12)

s2 = ttk.Style()
s2.configure('menu.TButton', font=12, bg='white', fg='blue')

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

forgot_password_button = ttk.Button(loginframe, text='Reset password', command=forgot_password)
forgot_password_button.grid(row=3, column=3, pady=10)

# resetpasswordframe
photologinforgotscreen = PhotoImage(file='Hannon-Transport.png')
photolabel2 = Label(resetpasswordframe, image=photologinforgotscreen, bg='white')
photolabel2.grid(row=0, column=0, sticky=N, columnspan=6)

Code_label1 = ttk.Label(resetpasswordframe, text='Code:', font=18)
Code_label1.grid(row=1, column=2)
Code_entry1 = ttk.Entry(resetpasswordframe, textvariable=OTPcode, font=18)
Code_entry1.grid(row=1, column=3)

Password_label1 = ttk.Label(resetpasswordframe, text='Password:', font=18)
Password_label1.grid(row=2, column=2)
Password_entry1 = ttk.Entry(resetpasswordframe, textvariable=REpassword1, font=18)
Password_entry1.grid(row=2, column=3)

Password_label = ttk.Label(resetpasswordframe, text='Re-enter Password:', font=18)
Password_label.grid(row=3, column=2)
Password_entry = ttk.Entry(resetpasswordframe, textvariable=REpassword2, font=18)
Password_entry.grid(row=3, column=3)

login_button = ttk.Button(resetpasswordframe, text='Reset', command=ResetPassword)
login_button.grid(row=4, column=3)

forgot_password_button = ttk.Button(resetpasswordframe, text='Back', command=BackLogin)
forgot_password_button.grid(row=4, column=2, pady=10)

# managermenuframe frame
labelframe = Frame(managermenuframe, bg='#0E2B4D', pady=5, padx=5)
labelframe.grid(row=1, column=0, sticky=NW)

Button1 = Button(labelframe, command=ManagerDriver, text='Driver', bg='#0E2B4D', fg='white', font=12).grid(row=1,
                                                                                                           column=0,
                                                                                                           ipady=10,
                                                                                                           ipadx=80)
Button2 = Button(labelframe, command=Button1, text='Button2', bg='#0E2B4D', fg='white', font=12).grid(row=2, column=0,
                                                                                                      ipady=10,
                                                                                                      ipadx=73)
Button3 = Button(labelframe, command=Button1, text='Button3', bg='#0E2B4D', fg='white', font=12).grid(row=3, column=0,
                                                                                                      ipady=10,
                                                                                                      ipadx=73)
Button4 = Button(labelframe, command=Button1, text='Button4', bg='#0E2B4D', fg='white', font=12).grid(row=4, column=0,
                                                                                                      ipady=10,
                                                                                                      ipadx=73)
Button5 = Button(labelframe, command=Button1, text='Button5', bg='#0E2B4D', fg='white', font=12).grid(row=5, column=0,
                                                                                                      ipady=10,
                                                                                                      ipadx=73)
Button6 = Button(labelframe, command=Button1, text='Button5', bg='#0E2B4D', fg='white', font=12).grid(row=6, column=0,
                                                                                                      ipady=10,
                                                                                                      ipadx=73)
Button7 = Button(labelframe, command=MangerMenu, text='Menu', bg='#0E2B4D', fg='white', font=12).grid(row=7, column=0,
                                                                                                      ipady=10,
                                                                                                      ipadx=82)

labelframe2 = Frame(managermenuframe, bg='#0E2B4D')
labelframe2.grid(row=0, column=0, columnspan=3, sticky=NW)

photomangermenuscreen = PhotoImage(file='white-footer-logo.png')
photolabelmanager = Label(labelframe2, image=photomangermenuscreen, bg='#0E2B4D')
photolabelmanager.grid(row=0, column=0, sticky=N, pady=5)

username_label = Label(labelframe2, text='Welcome, Leo', font=40, fg='white', bg='#0E2B4D')
username_label.grid(row=0, column=2, padx=150)

adminMemberClockLabel = Label(labelframe2, bg='#0E2B4D', fg='white', font='bold')
adminMemberClockLabel.grid(row=0, column=3, padx=10)

LOGoutButton = Button(labelframe2, command=LogOut, text='Log Out', bg='#0E2B4D', fg='white', font=12).grid(row=0,
                                                                                                               column=4,
                                                                                                               ipady=30,
                                                                                                               ipadx=10)

managerTVFrameDriver = Frame(managermenuframe)
managerTVFrameDriver.grid(row=1, column=1, sticky=NW)
managerTVFrameDriver.configure(bg='white')

SerachlabelD = ttk.Label(managerTVFrameDriver, text='Search:').grid(row=0, column=0, padx=10)
search_entryD = ttk.Entry(managerTVFrameDriver, textvariable=MangerTVSerVal, width=90).grid(row=0, column=1)

managerTVDriver = ttk.Treeview(managerTVFrameDriver, height=15,
                               columns=('First Name', 'Last Name', 'Column 2 ', 'Coulmn 3'))
managerTVDriver.grid(row=2, column=0, columnspan=30, pady=10, padx=30)

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

popupmenustaff = Menu(managerTVFrameDriver, tearoff=0)
popupmenustaff.add_command(label='Delete', command=DelDriver)
popupmenustaff.add_command(label='Send Email', command=EmailDriver)


def do_popup_staff(event):
    try:
        popupmenustaff.tk_popup(event.x_root, event.y_root)
    finally:
        popupmenustaff.grab_release()


managerTVDriver.bind("<Button-3>", do_popup_staff)




# MangerDriverFrame
labelframe = Frame(MangerDriverFrame, bg='#0E2B4D', pady=5, padx=5)
labelframe.grid(row=1, column=0, sticky=NW)

Button1 = Button(labelframe, command=ManagerDriver, text='Driver', bg='#0E2B4D', fg='white', font=12).grid(row=1,
                                                                                                           column=0,
                                                                                                           ipady=10,
                                                                                                           ipadx=80)
Button2 = Button(labelframe, command=Button1, text='Button2', bg='#0E2B4D', fg='white', font=12).grid(row=2, column=0,
                                                                                                      ipady=10,
                                                                                                      ipadx=73)
Button3 = Button(labelframe, command=Button1, text='Button3', bg='#0E2B4D', fg='white', font=12).grid(row=3, column=0,
                                                                                                      ipady=10,
                                                                                                      ipadx=73)
Button4 = Button(labelframe, command=Button1, text='Button4', bg='#0E2B4D', fg='white', font=12).grid(row=4, column=0,
                                                                                                      ipady=10,
                                                                                                      ipadx=73)
Button5 = Button(labelframe, command=Button1, text='Button5', bg='#0E2B4D', fg='white', font=12).grid(row=5, column=0,
                                                                                                      ipady=10,
                                                                                                      ipadx=73)
Button6 = Button(labelframe, command=Button1, text='Button5', bg='#0E2B4D', fg='white', font=12).grid(row=6, column=0,
                                                                                                      ipady=10,
                                                                                                      ipadx=73)
Button7 = Button(labelframe, command=MangerMenu, text='Menu', bg='#0E2B4D', fg='white', font=12).grid(row=7, column=0,
                                                                                                      ipady=10,
                                                                                                      ipadx=82)

labelframe2 = Frame(MangerDriverFrame, bg='#0E2B4D')
labelframe2.grid(row=0, column=0, sticky=NW, columnspan=10)

photomangerdriverscreen = PhotoImage(file='white-footer-logo.png')
photolabelmanagerdriver = Label(labelframe2, image=photomangerdriverscreen, bg='#0E2B4D')
photolabelmanagerdriver.grid(row=0, column=0, sticky=N, pady=5)

username_label = Label(labelframe2, text='Welcome, Leo', font=40, fg='white', bg='#0E2B4D')
username_label.grid(row=0, column=2, padx=342)

adminMemberClockLabel = Label(labelframe2, bg='#0E2B4D', fg='white', font='bold')
adminMemberClockLabel.grid(row=0, column=3, padx=10)

LOGoutButton = Button(labelframe2, command=LogOut, text='Log Out', bg='#0E2B4D', fg='white', font=12).grid(row=0,
                                                                                                               column=4,
                                                                                                               ipady=30,
                                                                                                               ipadx=10)
managerTVFrameDriver = Frame(MangerDriverFrame)
managerTVFrameDriver.grid(row=1, column=1, sticky=NW)
managerTVFrameDriver.configure(bg='white')

SerachlabelD = ttk.Label(managerTVFrameDriver, text='Search:').grid(row=0, column=0, padx=10)
search_entryD = ttk.Entry(managerTVFrameDriver, textvariable=MangerTVSerVal, width=90).grid(row=0, column=1)

managerTVDriver = ttk.Treeview(managerTVFrameDriver, height=15,
                               columns=('First Name', 'Last Name', 'Column 2 ', 'Coulmn 3'))
managerTVDriver.grid(row=2, column=0, columnspan=30, pady=10, padx=30)

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

popupmenustaff = Menu(managerTVFrameDriver, tearoff=0)
popupmenustaff.add_command(label='Delete', command=DelDriver)
popupmenustaff.add_command(label='Send Email', command=EmailDriver)


def do_popup_staff(event):
    try:
        popupmenustaff.tk_popup(event.x_root, event.y_root)
    finally:
        popupmenustaff.grab_release()


managerTVDriver.bind("<Button-3>", do_popup_staff)

managerInputsFrameDriver = LabelFrame(MangerDriverFrame, text='Inputs', bg='white', pady=5, padx=5)
managerInputsFrameDriver.grid(row=2, column=1, sticky=NW, padx=10)
managerInputsFrameDriver.configure(bg='white')

FirstNameLabelD = ttk.Label(managerInputsFrameDriver, text='First Name:').grid(row=0, column=0, padx=10)
FirstNameentryD = ttk.Entry(managerInputsFrameDriver, textvariable=FirstNameD).grid(row=0, column=1)

LastNameLabelD = ttk.Label(managerInputsFrameDriver, text='Last Name:').grid(row=0, column=2, padx=10)
LastNameentryD = ttk.Entry(managerInputsFrameDriver, textvariable=LastNameD).grid(row=0, column=3)

EmailLabelD = ttk.Label(managerInputsFrameDriver, text='Email:').grid(row=0, column=4, padx=10)
EmailentryD = ttk.Entry(managerInputsFrameDriver, textvariable=EmailD).grid(row=0, column=5)

AddDriverButton = ttk.Button(managerInputsFrameDriver, text='Add Driver', command=AddDriver).grid(row=1, column=0,
                                                                                                  padx=10,
                                                                                                  pady=10)

DelDriverButton = ttk.Button(managerInputsFrameDriver, text='Delete Driver', command=DelDriver).grid(row=1, column=2,
                                                                                                     padx=10, pady=10)

EmailDriverButton = ttk.Button(managerInputsFrameDriver, text='Send Email', command=UpdateDriverMangerWidg).grid(row=1,
                                                                                                                 column=4,
                                                                                                                 padx=10,
                                                                                                                 pady=10)

# widgits on mangerdriverframe
managerWidgFrameDriver = LabelFrame(MangerDriverFrame, text='Widgets', bg='white', pady=5, padx=5)
managerWidgFrameDriver.grid(row=2, column=2, padx=10, sticky=NE, columnspan=3, ipadx=20, ipady=5)
managerWidgFrameDriver.configure(bg='white')

AvliableDriverwidigitLable = ttk.Label(managerWidgFrameDriver, text='Available Drivers: ', font=60).grid(row=0,
                                                                                                         column=0,
                                                                                                         padx=40,
                                                                                                         pady=10)

ValueAvliableDriverwidigitLable = ttk.Label(managerWidgFrameDriver, textvariable=LableValueYes, font=60).grid(row=0,
                                                                                                              column=1,
                                                                                                              padx=40,
                                                                                                              pady=10)

UnAvliableDriverwidigitLable = ttk.Label(managerWidgFrameDriver, text='Unavailable Drivers: ', font=60).grid(row=1,
                                                                                                             column=0,
                                                                                                             padx=40,
                                                                                                             pady=10)

ValueNoAvliableDriverwidigitLable = ttk.Label(managerWidgFrameDriver, textvariable=LableValueNo, font=60).grid(row=1,
                                                                                                               column=1,
                                                                                                               padx=40,
                                                                                                               pady=10)

NewLatesDriverwidigitLable = ttk.Label(managerWidgFrameDriver, text='New Lates:', font=60).grid(row=2,
                                                                                                column=0,
                                                                                                padx=40,
                                                                                                pady=10)

ValueNewAvliableDriverwidigitLable = ttk.Label(managerWidgFrameDriver, textvariable=LableValueNew, font=60).grid(row=2,
                                                                                                                 column=1,
                                                                                                                 padx=40,
                                                                                                                 pady=10)

managerPreoformacesrameDriver = LabelFrame(MangerDriverFrame, text='Preformaces', bg='white', pady=5, padx=5)
managerPreoformacesrameDriver.grid(row=1, column=2, padx=10, sticky=NE, columnspan=3, ipadx=20, ipady=20)
managerPreoformacesrameDriver.configure(bg='white')

SerTVperformacesLabelD = ttk.Label(managerPreoformacesrameDriver, text='Show:', font=13).grid(row=0, column=0, padx=17)

SearchOptions = [
    "New Lates",
    "All"]

SerTV.set('All')
SerTVDrop = ttk.OptionMenu(managerPreoformacesrameDriver, SerTV, *SearchOptions).grid(row=0, column=1, padx=5)

SerPreformaTVButton = ttk.Button(managerPreoformacesrameDriver, text='Search', command=ShowDriverPreformaceTV).grid(
    row=0, column=2,
    padx=5)

managerDriverPrefTVDriver = ttk.Treeview(managerPreoformacesrameDriver, height=10,
                                         columns=('New Lates', 'Total Lates'))
managerDriverPrefTVDriver.grid(row=2, column=0, columnspan=30, pady=10, padx=30)

managerDriverPrefTVDriver.heading('#0', text='Email')
managerDriverPrefTVDriver.column('#0', minwidth=0, width=150, anchor='center')
managerDriverPrefTVDriver.heading('#1', text='New lates')
managerDriverPrefTVDriver.column('#1', minwidth=0, width=100, anchor='center')
managerDriverPrefTVDriver.heading('#2', text='Total lates')
managerDriverPrefTVDriver.column('#2', minwidth=0, width=100, anchor='center')

EmailDriverPrefromaceAllButton = ttk.Button(managerPreoformacesrameDriver, text='Send Warning All',
                                            command=EmailDriverWarningAll).grid(row=3,
                                                                                column=0,
                                                                                padx=10,
                                                                                pady=5)

EmailDriverPrefromaceNewButton = ttk.Button(managerPreoformacesrameDriver, text='Send Warning New',
                                            command=EmailDriverWarningNew).grid(row=3,
                                                                                column=1,
                                                                                padx=10,
                                                                                pady=5)

EmailDriverPrefromaceSelButton = ttk.Button(managerPreoformacesrameDriver, text='Send Warning Selected',
                                            command=EmailDriverWarningSel).grid(row=3,
                                                                                column=2,
                                                                                padx=10,
                                                                                pady=5)
raise_frame(loginframe)
root.mainloop()
