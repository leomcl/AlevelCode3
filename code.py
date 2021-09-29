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


# functions
def raise_frame(frame_name):
    frame_name.tkraise()


def BackLogin():
    raise_frame(loginframe)
    root.geometry('640x600')


def Button1():
    raise_frame(MangerDriverFrame)
    root.geometry('1400x900')


def MangerMenu():
    raise_frame(managermenuframe)
    root.geometry('1400x800')


def ManagerDriver():
    ShowDriverTV()
    ShowDriverPreformaceTV()
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
        messagebox.showinfo('Info', str(TheEmail) + ' Has been deleted')
        ShowDriverTV()
    elif Response == 'No':
        Response.destroy()


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
labelframe = Frame(managermenuframe, bg='white', pady=5, padx=5)
labelframe.grid(row=0, column=0)

photomangermenuscreen = PhotoImage(file='Hannon-Transport Small.png')
photolabelmanager = ttk.Label(labelframe, image=photomangermenuscreen)
photolabelmanager.grid(row=0, column=0, sticky=N)

Button1 = ttk.Button(labelframe, command=ManagerDriver, text='Driver', style='my.TButton').grid(row=0, column=1,
                                                                                                ipady=10, pady=7.5)
Button2 = ttk.Button(labelframe, command=Button1, text='Button2', style='my.TButton').grid(row=0, column=2, ipady=10,
                                                                                           padx=5)
Button3 = ttk.Button(labelframe, command=Button1, text='Button3', style='my.TButton').grid(row=0, column=3, ipady=10,
                                                                                           padx=5)
Button4 = ttk.Button(labelframe, command=Button1, text='Button4', style='my.TButton').grid(row=0, column=4, ipady=10,
                                                                                           padx=5)
Button5 = ttk.Button(labelframe, command=Button1, text='Button5', style='my.TButton').grid(row=0, column=5, ipady=10,
                                                                                           padx=5)
Button6 = ttk.Button(labelframe, command=Button1, text='Button5', style='my.TButton').grid(row=0, column=6, ipady=10,
                                                                                           padx=5)
Button7 = ttk.Button(labelframe, command=MangerMenu, text='Menu', style='my.TButton').grid(row=0, column=7, ipady=10,
                                                                                           padx=5)

# MangerDriverFrame
Driverlabelframe = Frame(MangerDriverFrame, bg='white')
Driverlabelframe.grid(row=0, column=0)

Dphotomangermenuscreen = PhotoImage(file='Hannon-Transport Small.png')
Dphotolabelmanager = Label(Driverlabelframe, image=Dphotomangermenuscreen, bg='white')
Dphotolabelmanager.grid(row=0, column=0, sticky=N)

Button1 = ttk.Button(Driverlabelframe, command=ManagerDriver, text='Driver', style='my.TButton').grid(row=0, column=1,
                                                                                                      ipady=10,
                                                                                                      pady=7.5)
Button2 = ttk.Button(Driverlabelframe, command=Button1, text='Button2', style='my.TButton').grid(row=0, column=2,
                                                                                                 ipady=10, padx=5)
Button3 = ttk.Button(Driverlabelframe, command=Button1, text='Button3', style='my.TButton').grid(row=0, column=3,
                                                                                                 ipady=10, padx=5)
Button4 = ttk.Button(Driverlabelframe, command=Button1, text='Button4', style='my.TButton').grid(row=0, column=4,
                                                                                                 ipady=10, padx=5)
Button5 = ttk.Button(Driverlabelframe, command=Button1, text='Button5', style='my.TButton').grid(row=0, column=5,
                                                                                                 ipady=10, padx=5)
Button6 = ttk.Button(Driverlabelframe, command=Button1, text='Button5', style='my.TButton').grid(row=0, column=6,
                                                                                                 ipady=10, padx=5)
Button7 = ttk.Button(Driverlabelframe, command=MangerMenu, text='Menu', style='my.TButton').grid(row=0, column=7,
                                                                                                 ipady=10, padx=5)

managerTVFrameDriver = Frame(MangerDriverFrame)
managerTVFrameDriver.grid(row=1, column=0, sticky=NW)
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
managerInputsFrameDriver.grid(row=2, column=0, sticky=NW, padx=10)
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

EmailDriverButton = ttk.Button(managerInputsFrameDriver, text='Send Email', command=EmailDriver).grid(row=1, column=4,
                                                                                                      padx=10, pady=10)

# widgits on mangerdriverframe
managerWidgFrameDriver = LabelFrame(MangerDriverFrame, text='Widgets', bg='white', pady=5, padx=5)
managerWidgFrameDriver.grid(row=2, column=0, padx=10, sticky=NE, columnspan=3, ipadx=20, ipady=20)
managerWidgFrameDriver.configure(bg='white')

AvliableDriverwidigitLable = ttk.Label(managerWidgFrameDriver, text='Available Drivers: 0 ', font=40).grid(row=0,
                                                                                                           column=0,
                                                                                                           padx=40,
                                                                                                           pady=20)

UnAvliableDriverwidigitLable = ttk.Label(managerWidgFrameDriver, text='Unavailable Drivers: 0 ', font=40).grid(row=1,
                                                                                                               column=0,
                                                                                                               padx=40,
                                                                                                               pady=20)

NewLatesDriverwidigitLable = ttk.Label(managerWidgFrameDriver, text='New Lates: 0 ', font=40).grid(row=2,
                                                                                                   column=0,
                                                                                                   padx=40,
                                                                                                   pady=20)

managerPreoformacesrameDriver = LabelFrame(MangerDriverFrame, text='Preformaces', bg='white', pady=5, padx=5)
managerPreoformacesrameDriver.grid(row=1, column=0, padx=10, sticky=NE, columnspan=3, ipadx=20, ipady=20)
managerPreoformacesrameDriver.configure(bg='white')

SerTVperformacesLabelD = ttk.Label(managerPreoformacesrameDriver, text='Show:', font=13).grid(row=0, column=0, padx=17)

SearchOptions = [
    "New Lates",
    "All"]

SerTV.set('All')
SerTVDrop = tk.OptionMenu(managerPreoformacesrameDriver, SerTV, *SearchOptions).grid(row=0, column=1, padx=5)

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

raise_frame(loginframe)
root.mainloop()
