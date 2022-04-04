from tkinter import *
import tkinter.simpledialog as simpledialog
from tkinter import messagebox, LabelFrame
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
from PIL import Image, ImageTk
import validation
import matplotlib.pyplot as plt

# hello

# functions hi part 2
min_w = 60  # Minimum width of the frame
max_w = 200  # Maximum width of the frame
cur_width = min_w  # Increasing width of the frame
expanded = False  # Check if it is completely exanded


def expand():
    global cur_width, expanded
    cur_width += 100  # Increase the width by 10
    rep = root.after(5, expand)  # Repeat this func every 5 ms
    frame.config(width=cur_width)  # Change the width to new increase width
    if cur_width >= max_w:  # If width is greater than maximum width
        expanded = True  # Frame is expended
        root.after_cancel(rep)  # Stop repeating the func
        fill()


def contract():
    global cur_width, expanded
    cur_width -= 100  # Reduce the width by 10
    rep = root.after(5, contract)  # Call this func every 5 ms
    frame.config(width=cur_width)  # Change the width to new reduced width
    if cur_width <= min_w:  # If it is back to normal width
        expanded = False  # Frame is not expanded
        root.after_cancel(rep)  # Stop repeating the func
        fill()


def fill():
    if expanded:  # If the frame is exanded
        # Show a text, and remove the image
        home_b.config(text='Home', image='', font=(0, 21), fg='white')
        set_b.config(text='Users', image='', font=(0, 21), fg='white')
        ring_b.config(text='Orders', image='', font=(0, 21), fg='white')
    else:
        # Bring the image back
        home_b.config(image=home, font=(0, 21))
        set_b.config(image=settings, font=(0, 21))
        ring_b.config(image=ring, font=(0, 21))


def expand2():
    global cur_width, expanded
    cur_width += 100  # Increase the width by 10
    rep = root.after(5, expand2)  # Repeat this func every 5 ms
    frame2.config(width=cur_width)  # Change the width to new increase width
    if cur_width >= max_w:  # If width is greater than maximum width
        expanded = True  # Frame is expended
        root.after_cancel(rep)  # Stop repeating the func
        fill2()


def contract2():
    global cur_width, expanded
    cur_width -= 100  # Reduce the width by 10
    rep = root.after(5, contract2)  # Call this func every 5 ms
    frame2.config(width=cur_width)  # Change the width to new reduced width
    if cur_width <= min_w:  # If it is back to normal width
        expanded = False  # Frame is not expanded
        root.after_cancel(rep)  # Stop repeating the func
        fill2()


def fill2():
    if expanded:  # If the frame is exanded
        # Show a text, and remove the image
        home_b2.config(text='Driver', image='', font=(0, 21), fg='white')
        set_b2.config(text='Driver', image='', font=(0, 21), fg='white')
        ring_b2.config(text='Orders', image='', font=(0, 21), fg='white')
    else:
        # Bring the image back
        home_b2.config(image=home, font=(0, 21))
        set_b2.config(image=settings, font=(0, 21))
        ring_b2.config(image=ring, font=(0, 21))


def expand3():
    global cur_width, expanded
    cur_width += 100  # Increase the width by 10
    rep = root.after(5, expand3)  # Repeat this func every 5 ms
    frame3.config(width=cur_width)  # Change the width to new increase width
    if cur_width >= max_w:  # If width is greater than maximum width
        expanded = True  # Frame is expended
        root.after_cancel(rep)  # Stop repeating the func
        fill3()


def contract3():
    global cur_width, expanded
    cur_width -= 100  # Reduce the width by 10
    rep = root.after(5, contract3)  # Call this func every 5 ms
    frame3.config(width=cur_width)  # Change the width to new reduced width
    if cur_width <= min_w:  # If it is back to normal width
        expanded = False  # Frame is not expanded
        root.after_cancel(rep)  # Stop repeating the func
        fill3()


def fill3():
    if expanded:  # If the frame is exanded
        # Show a text, and remove the image
        home_b3.config(text='Orders', image='', font=(0, 21), fg='white')
        set_b3.config(text='New', image='', font=(0, 21), fg='white')
        ring_b3.config(text='client', image='', font=(0, 21), fg='white')
    else:
        # Bring the image back
        home_b3.config(image=home, font=(0, 21))
        set_b3.config(image=settings, font=(0, 21))
        ring_b3.config(image=ring, font=(0, 21))


def LogOut():
    raise_frame(loginframe)


def timememberscreen():
    def timemember():
        string = strftime('%H:%M:%S %p')
        adminMemberClockLabel.config(text=string)
        adminMemberClockLabel.after(1000, timemember)

    timemember()


def timedriverscreen():
    def timedriver():
        string = strftime('%H:%M:%S %p')
        driverMemberClockLabel.config(text=string)
        driverMemberClockLabel.after(1000, timedriverscreen)

    timedriver()


def raise_frame(frame_name):
    frame_name.tkraise()
    # "frame" (the side navagation board) must be raised after desired frame, as to keep it in front
    frame.tkraise()


def raise_frameDriver(frame_name):
    frame_name.tkraise()
    # "frame" (the side navagation board) must be raised after desired frame, as to keep it in front
    frame2.tkraise()


def raise_frameClient(frame_name):
    frame_name.tkraise()
    # "frame" (the side navagation board) must be raised after desired frame, as to keep it in front
    frame3.tkraise()


def raise_frameLoader(frame_name):
    frame_name.tkraise()
    # "frame" (the side navagation board) must be raised after desired frame, as to keep it in front
    frame3.tkraise()


def BackLogin():
    raise_frame(loginframe)
    root.geometry('640x600')


def Button1():
    raise_frame(ManagerDriverFrame)
    root.geometry('1400x900')


def MangerMenu():
    timememberscreen()
    raise_frame(managerDashFrame)
    root.geometry('1400x800')


def DriverMenu():
    # timedriverscreen()
    ShowdriverOrderTv()
    raise_frameDriver(drivermenuframe)
    root.geometry('1400x800')


def ClientMenu():
    ShowclientTVOrders()
    raise_frameClient(clientmenuframe)
    root.geometry('1400x800')


def LoaderMenu():
    ShowLoaderTV()
    raise_frameLoader(loadermenuframe)
    root.geometry('1400x800')


def ClientOrders():
    ShowclientTVOrders()
    raise_frameClient(clientOrdersFrame)


def ManagerDriver():
    raise_frame(ManagerDriverFrame)
    ShowDriverTV()
    UpdateDriverMangerWidg()


def MangerOrders():
    raise_frame(ManagerOrderFrame)
    ShowOrderTV()


def ManagerLoader():
    raise_frame(ManagerLoaderFrame)
    ShowLoaderTV()


def ManagerClient():
    raise_frame(ManagerClientFrame)
    ShowClientTV()


def Neworder():
    raise_frameClient(clientNewOrdersFrame)


def usernameandpass():
    conn = sqlite3.connect('data.db')
    mycursor = conn.cursor()

    sql = "INSERT INTO passwords (username, password, type) VALUES (?, ?, ?)"
    val = ("leo", "leo", "customs")
    mycursor.execute(sql, val)

    conn.commit()
    conn.close()
    print('done')


def MangerLogin():
    timememberscreen()
    raise_frame(managermenuframe)
    root.geometry('1400x800')


def login():
    global Finialusername
    Finialusername = username.get()
    Finialpassword = Password.get()
    print(Finialpassword, Finialusername)
    if validation.presenceCheck(Finialusername) is False:
        messagebox.showwarning('', 'Presnce Username')
    elif validation.presenceCheck(Finialpassword) is False:
        messagebox.showwarning('', 'Presnsce password')
    elif validation.emailCheck(Finialusername) is False:
        messagebox.showwarning('', 'email check')
    elif validation.intTypeCheck(Finialusername) is True:
        messagebox.showwarning()
    elif validation.intTypeCheck(Finialpassword) is True:
        messagebox.showwarning()
    else:
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("SELECT rowid, * from passwords WHERE username = (?)", (Finialusername,))
        reader = c.fetchall()
        conn.commit()
        conn.close()
        print(reader)
        for row in reader:
            if row[2] == Finialpassword and row[3] == 'driver':
                DriverMenu()
                print('driver')
            elif row[2] == Finialpassword and row[3] == 'client':
                ClientCompany()
                print('clinent')
            elif row[2] == Finialpassword and row[3] == 'loader':
                LoaderMenu()
                print('driver')
            elif row[2] == Finialpassword and row[3] == 'customs':
                MangerLogin()
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
    conn.commit()
    conn.close()
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

            c.execute("""UPDATE passwords SET password = ? WHERE username = ?""", value)
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
            messagebox.showinfo('Invalid Error', 'Error password does not match confirm password try again')
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
    conn.commit()
    conn.close()


def AddDriver():
    type = 'driver'
    password = 'NotSet'
    Ffirstname = FirstNameD.get()
    Flastname = LastNameD.get()
    Femail = EmailD.get()

    if validation.presenceCheck(Ffirstname) is False:
        messagebox.showwarning()
    elif validation.emailCheck(Femail) is False:
        messagebox.showwarning()
    elif validation.presenceCheck(Flastname) is False:
        messagebox.showwarning()
    elif validation.presenceCheck(Femail) is False:
        messagebox.showwarning()
    elif validation.intTypeCheck(Ffirstname) is True:
        messagebox.showwarning()
    elif validation.intTypeCheck(Flastname) is True:
        messagebox.showwarning()
    elif validation.intTypeCheck(Femail) is True:
        messagebox.showwarning()
    else:
        conn = sqlite3.connect('data.db')
        mycursor = conn.cursor()
        sql = "INSERT INTO drivers (email, firstname, lastname, deliveries, avaliablity) VALUES (?, ?, ?, ?, ?)"
        val = (Femail, Ffirstname, Flastname, 0, "Yes")
        mycursor.execute(sql, val)
        mycursor.execute("INSERT INTO passwords (username, password, type) VALUES (?, ?, ?)", (Femail, password, type))
        conn.commit()
        conn.close()

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
    listvalues = list(dictionary.values())
    TheEmail = listvalues[0]
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
        conn.commit()
        conn.close()
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
        conn.commit()
        conn.close()


def UpdateDriverMangerWidg():
    AmountNo = 0
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM drivers WHERE avaliablity = 'No'")
    for row in c:
        AmountNo += 1
    LableValueNo.set(AmountNo)
    conn.commit()
    conn.close()

    AmountYes = 0
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM drivers WHERE avaliablity = 'Yes'")
    for row in c:
        AmountYes += 1
    LableValueYes.set(AmountYes)
    conn.commit()
    conn.close()

    AmountNew = 0
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM driverPreformace WHERE newLate != 0")
    for row in c:
        AmountNew += 1
    LableValueNew.set(AmountNew)
    conn.commit()
    conn.close()


def CreateScoreBarChart():
    fAmountNo = LableValueNo.get()
    fLableValueNew = LableValueNew.get()
    fLableValueYes = LableValueYes.get()
    fullnames = 'available', 'unavailable', 'new lates'
    scores = int(fLableValueYes), int(fAmountNo), int(fLableValueNew)
    print(int(fAmountNo))
    plt.bar(fullnames, scores, align="center", alpha=0.5, color=['b'])
    plt.xticks(fullnames, fullnames)
    plt.show()


def EmailDriverWarningAll():
    pass


def EmailDriverWarningNew():
    pass


def EmailDriverWarningSel():
    pass


def AddLoader():
    type = 'loader'
    password = 'NotSet'
    Ffirstname = FirstNameL.get()
    Flastname = LastNameL.get()
    Femail = EmailL.get()

    if validation.presenceCheck(Ffirstname) is False:
        messagebox.showwarning()
    elif validation.emailCheck(Femail) is False:
        messagebox.showwarning()
    elif validation.presenceCheck(Flastname) is False:
        messagebox.showwarning()
    elif validation.presenceCheck(Femail) is False:
        messagebox.showwarning()
    elif validation.intTypeCheck(Ffirstname) is True:
        messagebox.showwarning()
    elif validation.intTypeCheck(Flastname) is True:
        messagebox.showwarning()
    elif validation.intTypeCheck(Femail) is True:
        messagebox.showwarning()
    else:
        conn = sqlite3.connect('data.db')
        mycursor = conn.cursor()
        sql = "INSERT INTO loaders (email, firstname, lastname) VALUES (?, ?, ?)"
        val = (Femail, Ffirstname, Flastname)
        mycursor.execute(sql, val)
        mycursor.execute("INSERT INTO passwords (username, password, type) VALUES (?, ?, ?)", (Femail, password, type))
        conn.commit()
        conn.close()

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

    ShowLoaderTV()


def DelLoader():
    curItem = managerTVLoader.focus()
    dictionary = managerTVLoader.item(curItem)
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
        c.execute("DELETE from loaders WHERE email = (?)", (TheEmail,))
        c.execute("DELETE from passwords WHERE username = (?)", (TheEmail,))
        conn.commit()
        conn.close()
        ShowLoaderTV()
    elif Response == 'No':
        Response.destroy()
    ShowLoaderTV()


def ShowLoaderTV():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    managerTVLoader.delete(*managerTVLoader.get_children())
    c.execute("SELECT * FROM loaders")
    for row in c:
        managerTVLoader.insert('', 'end', text=row[0], values=row[1:3])
    print(c)
    conn.commit()
    conn.close()


def AddClient():
    messagebox.showwarning('error', 'Client Added')
    type = 'client'
    password = 'NotSet'
    Ffirstname = FirstNameC.get()
    Flastname = LastNameC.get()
    Femail = EmailC.get()
    Fcompnay = CompanyC.get()
    if validation.presenceCheck(Ffirstname) is False:
        messagebox.showwarning()
    elif validation.emailCheck(Femail) is False:
        messagebox.showwarning()
    elif validation.presenceCheck(Flastname) is False:
        messagebox.showwarning()
    elif validation.presenceCheck(Femail) is False:
        messagebox.showwarning()
    elif validation.intTypeCheck(Ffirstname) is True:
        messagebox.showwarning()
    elif validation.intTypeCheck(Flastname) is True:
        messagebox.showwarning()
    elif validation.intTypeCheck(Femail) is True:
        messagebox.showwarning()
    else:
        conn = sqlite3.connect('data.db')
        mycursor = conn.cursor()

        sql = "INSERT INTO clients (email, firstname, lastname, company) VALUES (?, ?, ?, ?)"
        val = (Femail, Ffirstname, Flastname, Fcompnay)
        mycursor.execute(sql, val)
        mycursor.execute("INSERT INTO passwords (username, password, type) VALUES (?, ?, ?)", (Femail, password, type))
        conn.commit()
        conn.close()

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

        except:
            print('Email not sent')

    ShowClientTV()


def DelClient():
    print('hello')
    ClientcurItem = managerTVClient.focus()
    dictionaryClient = managerTVClient.item(ClientcurItem)
    CLientlistvalues = list(dictionaryClient.values())
    ClientTheEmail = CLientlistvalues[0]
    conn = sqlite3.connect('data.db')
    Response = messagebox.askyesno('Are you sure', 'Are you sure you want to delete this user ')
    if Response:
        c = conn.cursor()
        c.execute("DELETE from clients WHERE email = (?)", (ClientTheEmail,))
        c.execute("DELETE from passwords WHERE username = (?)", (ClientTheEmail,))
        conn.commit()
        conn.close()
        ShowClientTV()
    elif Response == 'No':
        Response.destroy()
    ShowClientTV()


def ShowClientTV():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    managerTVClient.delete(*managerTVClient.get_children())
    c.execute("SELECT * FROM clients")
    for row in c:
        managerTVClient.insert('', 'end', text=row[0], values=row[1:4])
    print(c)
    conn.commit()
    conn.close()


def AddOrder():
    FQuantity = Quantity.get()
    FProductName = ProductName.get()
    LorrieRed = 'None'
    Driver = 'None'
    OrderID = random.randint(1, 1000)
    ProductID = random.randint(1, 1000)
    FCompany = TheCompnay
    FPickUp = PickUp.get()
    FDelivery = Delivery.get()
    FloadID = 'Not Assigned'
    status = 'pending'
    if validation.presenceCheck(FPickUp) is False:
        messagebox.showwarning('', 'pick up')
    elif validation.presenceCheck(FDelivery) is False:
        messagebox.showwarning('', 'delivery')
    else:
        conn = sqlite3.connect('data.db')
        mycursor = conn.cursor()
        sql = "INSERT INTO orders (orderID, company, pickUpAddress, deliveryAddress, loadID, lorrieReg, driverID) VALUES (?, ?, ?, ?, ?, ?, ?)"
        val = (OrderID, FCompany, FPickUp, FDelivery, FloadID, LorrieRed, Driver)
        mycursor.execute(sql, val)
        sql2 = "INSERT INTO orderStatus (orderID, status) VALUES (?, ?)"
        val2 = (OrderID, status)
        mycursor.execute(sql2, val2)
        conn.commit()
        conn.close()

        AddProduct(OrderID)
    ShowclientTVOrders()


def AddProduct(OrderID):
    FProductName = ProductName.get()
    FQuantity = Quantity.get()
    ProductID = random.randint(1, 1000)
    FCompany = TheCompnay
    if validation.presenceCheck(FProductName) is False:
        messagebox.showwarning()
    elif validation.presenceCheck(FQuantity) is False:
        messagebox.showwarning()
    elif validation.intTypeCheck(FProductName) is True:
        messagebox.showwarning()
    elif validation.intTypeCheck(FQuantity) is False:
        messagebox.showwarning()
    else:
        conn = sqlite3.connect('data.db')
        mycursor = conn.cursor()
        sql = "INSERT INTO products (productID, orderID, company, productName, quantity) VALUES (?, ?, ?, ?, ?)"
        val = (ProductID, OrderID, FCompany, FProductName, FQuantity)
        mycursor.execute(sql, val)
        conn.commit()
        conn.close()


def DeleteOrder():
    pass


def ShowOrderTV():
    FinialSerTVOrder = SerTVOrders.get()
    print(FinialSerTVOrder)
    if FinialSerTVOrder == 'All':
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        managerTVOrders.delete(*managerTVOrders.get_children())
        c.execute("SELECT * FROM orders")
        for row in c:
            managerTVOrders.insert('', 'end', text=row[0], values=row[1:7])
        print(c)
        conn.commit()
        conn.close()

    elif FinialSerTVOrder == 'Assigned':
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        managerTVOrders.delete(*managerTVOrders.get_children())
        c.execute("SELECT * FROM orders WHERE lorrieReg != 'None'")
        for row in c:
            managerTVOrders.insert('', 'end', text=row[0], values=row[1:7])
        print(c)
        conn.commit()
        conn.close()

    elif FinialSerTVOrder == 'Not Assigned':
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        managerTVOrders.delete(*managerTVOrders.get_children())
        c.execute("SELECT * FROM orders WHERE lorrieReg = 'None'")
        for row in c:
            managerTVOrders.insert('', 'end', text=row[0], values=row[1:7])
        print(c)
        conn.commit()
        conn.close()


def ShowdriverOrderTv():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    driverTVOrders.delete(*driverTVOrders.get_children())
    c.execute("SELECT * FROM orders WHERE driverID = (?)", (Finialusername,))
    for row in c:
        driverTVOrders.insert('', 'end', text=row[0], values=row[1:6])
    print(c)
    conn.commit()
    conn.close()


def Assign():
    # get order
    ClientcurItem = managerTVOrders.focus()
    dictionaryClient = managerTVOrders.item(ClientcurItem)
    CLientlistvalues = list(dictionaryClient.values())
    global OrderNumber
    OrderNumber = CLientlistvalues[0]

    # top level
    global AssignFrame
    AssignFrame = Toplevel(height=500, width=1000)
    OrderLabel = ttk.Label(AssignFrame, text='order', font=20)
    OrderLabel.grid(row=0, column=0, columnspan=3)

    # driver tv
    global managerTVDriverAssign
    managerTVDriverAssign = ttk.Treeview(AssignFrame, height=10)
    managerTVDriverAssign.grid(row=1, column=0, pady=10, padx=10)
    managerTVDriverAssign.heading('#0', text='Driver')
    managerTVDriverAssign.column('#0', minwidth=0, width=200, anchor='center')

    # lorrie tv
    global managerTVLorrieAssign
    managerTVLorrieAssign = ttk.Treeview(AssignFrame, height=10)
    managerTVLorrieAssign.grid(row=1, column=2)
    managerTVLorrieAssign.heading('#0', text='Lorrie')
    managerTVLorrieAssign.column('#0', minwidth=0, width=200, anchor='center')

    mangerAssignButton = ttk.Button(AssignFrame, text='Assign', command=AssignItems)
    mangerAssignButton.grid(row=2, column=3)

    def PopulateAssign():
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        managerTVDriverAssign.delete(*managerTVDriverAssign.get_children())
        c.execute("SELECT email FROM drivers WHERE avaliablity = 'Yes'")
        for row in c:
            managerTVDriverAssign.insert('', 'end', text=row[0])
        conn.commit()
        conn.close()

        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        managerTVLorrieAssign.delete(*managerTVLorrieAssign.get_children())
        c.execute("SELECT reg FROM lorry WHERE avaliablity = 'Yes'")
        for row in c:
            managerTVLorrieAssign.insert('', 'end', text=row[0])
        conn.commit()
        conn.close()

    PopulateAssign()


def AssignItems():
    # getting data from tv's
    DriverEmail = managerTVDriverAssign.focus()
    dictionaryDriver = managerTVDriverAssign.item(DriverEmail)
    DriverListVAlues = list(dictionaryDriver.values())
    FDriverEmail = DriverListVAlues[0]
    LorryReg = managerTVLorrieAssign.focus()
    dictionaryLorry = managerTVLorrieAssign.item(LorryReg)
    LorryListVAlues = list(dictionaryLorry.values())
    FLorryReg = LorryListVAlues[0]

    if FLorryReg == '':
        messagebox.showerror('error', 'No lorry Selected')
    elif FDriverEmail == '':
        messagebox.showerror('error', 'No Driver Selected')
    else:

        # writing to orders FDriverEmail, FLorryReg
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        sql = "UPDATE orders SET lorrieReg = (?), driverID = (?) WHERE orderID = (?)"
        val = (FLorryReg, FDriverEmail, OrderNumber)
        c.execute(sql, val)
        conn.commit()
        conn.close()

        # writing to drivers
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("UPDATE drivers SET avaliablity = 'No' WHERE email = (?)", (FDriverEmail,))
        conn.commit()
        conn.close()

        # writting to lorry
        # writing to drivers
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("UPDATE lorry SET avaliablity = 'No' WHERE reg = (?)", (FLorryReg,))
        conn.commit()
        conn.close()
        ShowOrderTV()

        AssignFrame.destroy()


def show_status(event):
    OrderNum = driverTVOrders.focus()
    dictionaryOrder = driverTVOrders.item(OrderNum)
    OrderlistValues = list(dictionaryOrder.values())
    FOrderNum = OrderlistValues[0]
    print(FOrderNum)
    status = ''
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT status FROM orderStatus WHERE orderID = (?)", (FOrderNum,))
    for row in c:
        status = row[0]
    conn.commit()
    conn.close()
    TheStatus.set(status)


def show_statusClient(event):
    OrderNum = clientTVOrders.focus()
    dictionaryOrder = clientTVOrders.item(OrderNum)
    OrderlistValues = list(dictionaryOrder.values())
    FOrderNum = OrderlistValues[0]
    print(FOrderNum)
    status = ''
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT status FROM orderStatus WHERE orderID = (?)", (FOrderNum,))
    for row in c:
        status = row[0]
    conn.commit()
    conn.close()
    ClientTheStatus.set(status)


def OutForDelivery():
    OrderNum = driverTVOrders.focus()
    dictionaryOrder = driverTVOrders.item(OrderNum)
    OrderlistValues = list(dictionaryOrder.values())
    FOrderNum = OrderlistValues[0]
    print(FOrderNum)
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("UPDATE orderStatus SET status = 'Out For Delivery' WHERE orderID = (?)", (FOrderNum,))
    conn.commit()
    conn.close()


def Delivered():
    OrderNum = driverTVOrders.focus()
    dictionaryOrder = driverTVOrders.item(OrderNum)
    OrderlistValues = list(dictionaryOrder.values())
    FOrderNum = OrderlistValues[0]
    print(FOrderNum)
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("UPDATE orderStatus SET status = 'Delivered' WHERE orderID = (?)", (FOrderNum,))
    conn.commit()
    conn.close()


def ClientCompany():
    global TheCompnay
    TheCompnay = ''
    print(Finialusername)
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT company FROM clients WHERE email = (?)", (Finialusername,))
    for row in c:
        TheCompnay = row[0]
    conn.commit()
    conn.close()

    print('print', TheCompnay)
    ClientMenu()


def ShowclientTVOrders():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    clientTVOrders.delete(*clientTVOrders.get_children())
    c.execute(
        "SELECT orderID, pickUpAddress, deliveryAddress, loadID, lorrieReg, driverID FROM orders WHERE company = (?)",
        (TheCompnay,))
    for row in c:
        clientTVOrders.insert('', 'end', text=row[0], values=row[1:6])
    conn.commit()
    conn.close()


def ShowLoaderTV():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    LoaderTVProducts.delete(*LoaderTVProducts.get_children())
    c.execute("SELECT * FROM products")
    for row in c:
        LoaderTVProducts.insert('', 'end', text=row[0], values=row[1:4])
    conn.commit()
    conn.close()


def loaded():
    loadID = random.randint(1, 1000)
    OrderNum = LoaderTVProducts.focus()
    print(OrderNum)
    dictionaryOrder = LoaderTVProducts.item(OrderNum)
    print(dictionaryOrder)
    OrderlistValues = list(dictionaryOrder.values())
    print('list', OrderlistValues)
    FOrderNum = OrderlistValues[2]
    FORderID = FOrderNum[0]
    print(FOrderNum)
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("UPDATE orders SET loadID = (?) WHERE orderID = (?)", (loadID, FORderID,))
    conn.commit()
    conn.close()


class UserButtons():
    def __init__(self):
        self.userButtonsFrame = None

    def CreateButtons(self, root):
        self.userButtonsFrame = Frame(root)
        self.userButtonsFrame.place(x=450, y=10)
        self.userButtonsFrame.configure(bg='white')

        userDriverButton = Button(self.userButtonsFrame, text='Driver', command=ManagerDriver)
        userDriverButton.grid(row=0, column=0, ipadx=15, ipady=5)

        userLoaderButton = Button(self.userButtonsFrame, text='Loader', command=ManagerLoader)
        userLoaderButton.grid(row=0, column=2, ipadx=15, ipady=5)

        userClientButton = Button(self.userButtonsFrame, text='Client', command=ManagerClient)
        userClientButton.grid(row=0, column=3, ipadx=15, ipady=5)


root = ThemedTk(theme='yaru')
root.geometry('800x600')
root.title('Logistyics App')
root.configure(background='white')

# ============================================================================
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
UsernmaeLabel = ''

# rest psssword
REpassword1 = StringVar()
REpassword2 = StringVar()
OTPcode = StringVar()

# loader user
MangerTVSerValLoader = StringVar()
FirstNameL = StringVar()
LastNameL = StringVar()
EmailL = StringVar()

# client user
MangerTVSerValClient = StringVar()
FirstNameC = StringVar()
LastNameC = StringVar()
EmailC = StringVar()
CompanyC = StringVar()

# orders
SerTVOrders = StringVar()
ProductName = StringVar()
PickUp = StringVar()
Delivery = StringVar()
Quantity = StringVar()

# driverorders
global TheStatus
TheStatus = StringVar()

# clinetordrs
global ClientTheStatus
ClientTheStatus = StringVar()

# ===========================================================================
# frames
loginframe = Frame(root, bg='white')
create_account_frame = Frame(root, bg='white')
resetpasswordframe = Frame(root, bg='white')
membermenuframe = Frame(root, bg='white')
managermenuframe = Frame(root, bg='white')
# ManagerDriverFrame = Frame(root, bg='white')
ManagerDriverFrameDash = Frame(root, bg='white')
ManagerStaffFrame = Frame(root, bg='light grey')
ManagerClassesFrame = Frame(root, bg='light grey')
drivermenuframe = Frame(root, bg='light grey')
clientmenuframe = Frame(root, bg='light grey')
loadermenuframe = Frame(root, bg='light grey')

for frame in (
        loginframe, create_account_frame, resetpasswordframe, membermenuframe, managermenuframe,
        ManagerStaffFrame, ManagerClassesFrame, ManagerDriverFrameDash, drivermenuframe, clientmenuframe,
        loadermenuframe):
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

# ============================================================================================
# resetpasswordframe
photologinforgotscreen = PhotoImage(file='Hannon-Transport.png')
photolabel2 = Label(resetpasswordframe, image=photologinforgotscreen, bg='white')
photolabel2.grid(row=0, column=0, sticky=NW, columnspan=6)

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

login_button2 = ttk.Button(resetpasswordframe, text='Reset', command=ResetPassword)
login_button2.grid(row=4, column=3)

forgot_password_button = ttk.Button(resetpasswordframe, text='Back', command=BackLogin)
forgot_password_button.grid(row=4, column=2, pady=10)

# ======================================================================================
# managermenuframe frame
managerDashFrame = Frame(managermenuframe, bg='white')
managerDashFrame.place(x=60, y=90, width=1300, height=1000)

managerWidgFrameDriverDash = LabelFrame(managerDashFrame, bg='white', pady=5, padx=5)
managerWidgFrameDriverDash.place(x=20, y=20)
managerWidgFrameDriverDash.configure(bg='white')

# ======================================================================================
# drivers dashboard
# labels
AvliableDriverwidigitLable = ttk.Label(managerWidgFrameDriverDash, text='Available Drivers: ', font=60)
AvliableDriverwidigitLable.grid(row=0, column=0, padx=40, pady=10)

ValueAvliableDriverwidigitLable = ttk.Label(managerWidgFrameDriverDash, textvariable=LableValueYes, font=60)
ValueAvliableDriverwidigitLable.grid(row=0, column=1, padx=40, pady=10)

UnAvliableDriverwidigitLable = ttk.Label(managerWidgFrameDriverDash, text='Unavailable Drivers: ', font=60)
UnAvliableDriverwidigitLable.grid(row=1, column=0, padx=40, pady=10)

ValueNoAvliableDriverwidigitLable = ttk.Label(managerWidgFrameDriverDash, textvariable=LableValueNo, font=60)
ValueNoAvliableDriverwidigitLable.grid(row=1, column=1, padx=40, pady=10)

NewLatesDriverwidigitLable = ttk.Label(managerWidgFrameDriverDash, text='New Lates:', font=60)
NewLatesDriverwidigitLable.grid(row=2, column=0, padx=40, pady=10)

ValueNewAvliableDriverwidigitLable = ttk.Label(managerWidgFrameDriverDash, textvariable=LableValueNew, font=60)
ValueNewAvliableDriverwidigitLable.grid(row=2, column=1, padx=40, pady=10)

ShowGraohButton = ttk.Button(managerWidgFrameDriverDash, text='Show Chart', command=CreateScoreBarChart)
ShowGraohButton.grid(row=3, column=0)
# ==================================================================================
# ManagerDriverFrame
# frames for ManagerDriverFrame
ManagerDriverFrame = Frame(managermenuframe, bg='white')
ManagerDriverFrame.place(x=60, y=90, width=1300, height=1000)

managerTVFrameDriver = LabelFrame(ManagerDriverFrame)
managerTVFrameDriver.place(x=10, y=60)
managerTVFrameDriver.configure(bg='white')

managerInputsFrameDriver = LabelFrame(ManagerDriverFrame, bg='white', pady=5, padx=5)
managerInputsFrameDriver.place(x=10, y=447)
managerInputsFrameDriver.configure(bg='white')

managerWidgFrameDriver = LabelFrame(ManagerDriverFrame, bg='white', pady=5, padx=5)
managerWidgFrameDriver.place(x=750, y=420)
managerWidgFrameDriver.configure(bg='white')

managerPreoformacesrameDriver = LabelFrame(ManagerDriverFrame, bg='white', pady=5, padx=5)
managerPreoformacesrameDriver.place(x=750, y=60)
managerPreoformacesrameDriver.configure(bg='white')

# user buttons driver
ManagerUserButtons = UserButtons()
ManagerUserButtons.CreateButtons(ManagerDriverFrame)

SerachlabelD = ttk.Label(managerTVFrameDriver, text='Search:')
SerachlabelD.grid(row=0, column=0, padx=10, pady=5)

search_entryD = ttk.Entry(managerTVFrameDriver, textvariable=MangerTVSerVal, width=90)
search_entryD.grid(row=0, column=1)

managerTVDriver = ttk.Treeview(managerTVFrameDriver, height=10,
                               columns=('First Name', 'Last Name', 'Column 2 ', 'Coulmn 3'))
managerTVDriver.grid(row=2, column=0, columnspan=30, pady=10, padx=10)

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

FirstNameLabelD = ttk.Label(managerInputsFrameDriver, text='First Name:')
FirstNameLabelD.grid(row=0, column=0, padx=10)

FirstNameentryD = ttk.Entry(managerInputsFrameDriver, textvariable=FirstNameD)
FirstNameentryD.grid(row=0, column=1)

LastNameLabelD = ttk.Label(managerInputsFrameDriver, text='Last Name:')
LastNameLabelD.grid(row=0, column=2, padx=10)
LastNameentryD = ttk.Entry(managerInputsFrameDriver, textvariable=LastNameD)
LastNameentryD.grid(row=0, column=3)

EmailLabelD = ttk.Label(managerInputsFrameDriver, text='Email:')
EmailLabelD.grid(row=0, column=4, padx=10)
EmailentryD = ttk.Entry(managerInputsFrameDriver, textvariable=EmailD)
EmailentryD.grid(row=0, column=5)

AddDriverButton = ttk.Button(managerInputsFrameDriver, text='Add Driver', command=AddDriver)
AddDriverButton.grid(row=1, column=0, padx=10, pady=10)

DelDriverButton = ttk.Button(managerInputsFrameDriver, text='Delete Driver', command=DelDriver)
DelDriverButton.grid(row=1, column=2, padx=10, pady=10)

EmailDriverButton = ttk.Button(managerInputsFrameDriver, text='Send Email', command=UpdateDriverMangerWidg)
EmailDriverButton.grid(row=1, column=4, padx=10, pady=10)

# widgits on ManagerDriverFrame
AvliableDriverwidigitLable = ttk.Label(managerWidgFrameDriver, text='Available Drivers: ', font=60)
AvliableDriverwidigitLable.grid(row=0, column=0, padx=40, pady=10)

ValueAvliableDriverwidigitLable = ttk.Label(managerWidgFrameDriver, textvariable=LableValueYes, font=60)
ValueAvliableDriverwidigitLable.grid(row=0, column=1, padx=40, pady=10)

UnAvliableDriverwidigitLable = ttk.Label(managerWidgFrameDriver, text='Unavailable Drivers: ', font=60)
UnAvliableDriverwidigitLable.grid(row=1, column=0, padx=40, pady=10)

ValueNoAvliableDriverwidigitLable = ttk.Label(managerWidgFrameDriver, textvariable=LableValueNo, font=60)
ValueNoAvliableDriverwidigitLable.grid(row=1, column=1, padx=40, pady=10)

NewLatesDriverwidigitLable = ttk.Label(managerWidgFrameDriver, text='New Lates:', font=60)
NewLatesDriverwidigitLable.grid(row=2, column=0, padx=40, pady=10)

ValueNewAvliableDriverwidigitLable = ttk.Label(managerWidgFrameDriver, textvariable=LableValueNew, font=60)
ValueNewAvliableDriverwidigitLable.grid(row=2, column=1, padx=40, pady=10)

SerTVperformacesLabelD = ttk.Label(managerPreoformacesrameDriver, text='Show:', font=13)
SerTVperformacesLabelD.grid(row=0, column=0, padx=17)

SearchOptions = [
    "New Lates",
    "All",
    "New Lates"]

SerTV.set('All')

SerTVDrop = ttk.OptionMenu(managerPreoformacesrameDriver, SerTV, *SearchOptions)
SerTVDrop.grid(row=0, column=1, padx=5)

SerPreformaTVButton = ttk.Button(managerPreoformacesrameDriver, text='Search', command=ShowDriverPreformaceTV)
SerPreformaTVButton.grid(row=0, column=2, padx=5)

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
                                            command=EmailDriverWarningAll)
EmailDriverPrefromaceAllButton.grid(row=3, column=0, padx=10, pady=5)

EmailDriverPrefromaceNewButton = ttk.Button(managerPreoformacesrameDriver, text='Send Warning New',
                                            command=EmailDriverWarningNew)
EmailDriverPrefromaceNewButton.grid(row=3, column=1, padx=10, pady=5)

EmailDriverPrefromaceSelButton = ttk.Button(managerPreoformacesrameDriver, text='Send Warning Selected',
                                            command=EmailDriverWarningSel)
EmailDriverPrefromaceSelButton.grid(row=3, column=2, padx=10, pady=5)

# ===================================================================================
# managerLoaderFrame
# frames in manager loader frame
ManagerLoaderFrame = Frame(managermenuframe, bg='white')
ManagerLoaderFrame.place(x=60, y=90, width=1300, height=1000)

managerTVFrameLoader = LabelFrame(ManagerLoaderFrame)
managerTVFrameLoader.place(x=10, y=60)
managerTVFrameLoader.configure(bg='white')

managerInputsFrameLoader = LabelFrame(ManagerLoaderFrame, bg='white', pady=5, padx=5)
managerInputsFrameLoader.place(x=10, y=447)
managerInputsFrameLoader.configure(bg='white')

# user buttons in OOP
LoaderUserButtons = UserButtons()
LoaderUserButtons.CreateButtons(ManagerLoaderFrame)

# loader TV
SerachlabelL = ttk.Label(managerTVFrameLoader, text='Search:')
SerachlabelL.grid(row=0, column=0, padx=10, pady=5)

search_entryL = ttk.Entry(managerTVFrameLoader, textvariable=MangerTVSerValLoader, width=90)
search_entryL.grid(row=0, column=1)

managerTVLoader = ttk.Treeview(managerTVFrameLoader, height=10,
                               columns=('First Name', 'Last Name'))
managerTVLoader.grid(row=2, column=0, columnspan=30, pady=10, padx=10)

managerTVLoader.heading('#0', text='Email')
managerTVLoader.column('#0', minwidth=0, width=200, anchor='center')
managerTVLoader.heading('#1', text='First Name')
managerTVLoader.column('#1', minwidth=0, width=110, anchor='center')
managerTVLoader.heading('#2', text='Last Name')
managerTVLoader.column('#2', minwidth=0, width=130, anchor='center')

popupmenustaffLoader = Menu(managerTVFrameLoader, tearoff=0)
popupmenustaffLoader.add_command(label='Delete', command=DelLoader)
popupmenustaffLoader.add_command(label='Send Email', command=EmailDriver)


def do_popup_Loader(event):
    try:
        popupmenustaffLoader.tk_popup(event.x_root, event.y_root)
    finally:
        popupmenustaffLoader.grab_release()


managerTVLoader.bind("<Button-3>", do_popup_Loader)

FirstNameLabelL = ttk.Label(managerInputsFrameLoader, text='First Name:')
FirstNameLabelL.grid(row=0, column=0, padx=10)

FirstNameentryL = ttk.Entry(managerInputsFrameLoader, textvariable=FirstNameL)
FirstNameentryL.grid(row=0, column=1)

LastNameLabelL = ttk.Label(managerInputsFrameLoader, text='Last Name:')
LastNameLabelL.grid(row=0, column=2, padx=10)
LastNameentryL = ttk.Entry(managerInputsFrameLoader, textvariable=LastNameL)
LastNameentryL.grid(row=0, column=3)

EmailLabelL = ttk.Label(managerInputsFrameLoader, text='Email:')
EmailLabelL.grid(row=0, column=4, padx=10)
EmailentryL = ttk.Entry(managerInputsFrameLoader, textvariable=EmailL)
EmailentryL.grid(row=0, column=5)

AddLoaderButton = ttk.Button(managerInputsFrameLoader, text='Add Loader', command=AddLoader)
AddLoaderButton.grid(row=1, column=0, padx=10, pady=10)

DelLoaderButton = ttk.Button(managerInputsFrameLoader, text='Delete Loader', command=DelLoader)
DelLoaderButton.grid(row=1, column=2, padx=10, pady=10)

EmailLoaderButton = ttk.Button(managerInputsFrameLoader, text='Send Email', command=UpdateDriverMangerWidg)
EmailLoaderButton.grid(row=1, column=4, padx=10, pady=10)
# ===================================================================================
# managerClientFrame
# frames in manager client frame
ManagerClientFrame = Frame(managermenuframe, bg='white')
ManagerClientFrame.place(x=60, y=90, width=1300, height=1000)

managerTVFrameClient = LabelFrame(ManagerClientFrame)
managerTVFrameClient.place(x=10, y=60)
managerTVFrameClient.configure(bg='white')

managerInputsFrameClient = LabelFrame(ManagerClientFrame, bg='white', pady=5, padx=5)
managerInputsFrameClient.place(x=10, y=447)
managerInputsFrameClient.configure(bg='white')

managerTVFrameClientOrders = LabelFrame(ManagerClientFrame)
managerTVFrameClientOrders.place(x=750, y=60)
managerTVFrameClientOrders.configure(bg='white')

# user buttons in OOP
ClientUserButtons = UserButtons()
ClientUserButtons.CreateButtons(ManagerClientFrame)

# Client TV
SerachlabelC = ttk.Label(managerTVFrameClient, text='Search:')
SerachlabelC.grid(row=0, column=0, padx=10, pady=5)

search_entryD = ttk.Entry(managerTVFrameClient, textvariable=MangerTVSerValClient, width=90)
search_entryD.grid(row=0, column=1)

managerTVClient = ttk.Treeview(managerTVFrameClient, height=10,
                               columns=('First Name', 'Last Name', 'company'))
managerTVClient.grid(row=2, column=0, columnspan=30, pady=10, padx=10)

managerTVClient.heading('#0', text='Email')
managerTVClient.column('#0', minwidth=0, width=200, anchor='center')
managerTVClient.heading('#1', text='First Name')
managerTVClient.column('#1', minwidth=0, width=110, anchor='center')
managerTVClient.heading('#2', text='Last Name')
managerTVClient.column('#2', minwidth=0, width=130, anchor='center')
managerTVClient.heading('#3', text='Compnay')
managerTVClient.column('#3', minwidth=0, width=130, anchor='center')

popupmenustaffClient = Menu(managerTVFrameClient, tearoff=0)
popupmenustaffClient.add_command(label='Delete', command=DelClient)
popupmenustaffClient.add_command(label='Send Email', command=EmailDriver)


def do_popup_Client(event):
    try:
        popupmenustaffClient.tk_popup(event.x_root, event.y_root)
    finally:
        popupmenustaffClient.grab_release()


managerTVClient.bind("<Button-3>", do_popup_Client)

# inputs client
FirstNameLabelC = ttk.Label(managerInputsFrameClient, text='First Name:')
FirstNameLabelC.grid(row=0, column=0, padx=10)

FirstNameentryC = ttk.Entry(managerInputsFrameClient, textvariable=FirstNameC)
FirstNameentryC.grid(row=0, column=1)

LastNameLabelC = ttk.Label(managerInputsFrameClient, text='Last Name:')
LastNameLabelC.grid(row=0, column=2, padx=10)
LastNameentryC = ttk.Entry(managerInputsFrameClient, textvariable=LastNameC)
LastNameentryC.grid(row=0, column=3)

EmailLabelC = ttk.Label(managerInputsFrameClient, text='Email:')
EmailLabelC.grid(row=0, column=4, padx=10)
EmailentryC = ttk.Entry(managerInputsFrameClient, textvariable=EmailC)
EmailentryC.grid(row=0, column=5)

CompanyLabelC = ttk.Label(managerInputsFrameClient, text='Company:')
CompanyLabelC.grid(row=0, column=6, padx=10)
CompnayentryC = ttk.Entry(managerInputsFrameClient, textvariable=CompanyC)
CompnayentryC.grid(row=0, column=7)

AddClientButton = ttk.Button(managerInputsFrameClient, text='Add Client', command=AddClient)
AddClientButton.grid(row=1, column=0, padx=10, pady=10)

DelClientButton = ttk.Button(managerInputsFrameClient, text='Delete Client', command=DelClient)
DelClientButton.grid(row=1, column=2, padx=10, pady=10)

EmailClientButton = ttk.Button(managerInputsFrameClient, text='Send Email', command=UpdateDriverMangerWidg)
EmailClientButton.grid(row=1, column=4, padx=10, pady=10)

# order TV
managerTVClientOrder = ttk.Treeview(managerTVFrameClientOrders, height=10,
                                    columns='Orders')
managerTVClientOrder.grid(row=2, column=0, columnspan=30, pady=10, padx=10)

managerTVClientOrder.heading('#0', text='Email')
managerTVClientOrder.column('#0', minwidth=0, width=200, anchor='center')
managerTVClientOrder.heading('#1', text='Orders')
managerTVClientOrder.column('#1', minwidth=0, width=110, anchor='center')

popupmenustaffClientOrders = Menu(managerTVFrameClientOrders, tearoff=0)
popupmenustaffClientOrders.add_command(label='Delete', command=DelClient)
popupmenustaffClientOrders.add_command(label='Send Email', command=EmailDriver)


def do_popup_Client_order(event):
    try:
        popupmenustaffClientOrders.tk_popup(event.x_root, event.y_root)
    finally:
        popupmenustaffClientOrders.grab_release()


managerTVClient.bind("<Button-3>", do_popup_Client_order)

# ===================================================================================
# managerOrderFrane
# frames in manager client frame
ManagerOrderFrame = Frame(managermenuframe, bg='white')
ManagerOrderFrame.place(x=60, y=90, width=1300, height=1000)

ManagerOrderTVFrame = Frame(ManagerOrderFrame, bg='white')
ManagerOrderTVFrame.place(x=10, y=20)

ManagerOrderInputsFrame = Frame(ManagerOrderFrame, bg='white')
ManagerOrderInputsFrame.place(x=10, y=447)

# tv frame
# serach tv
SerTVOrdersLabelD = ttk.Label(ManagerOrderTVFrame, text='Show:', font=13)
SerTVOrdersLabelD.grid(row=0, column=0)

SearchOptionsOrders = [
    "Not Assigned",
    "Assigned",
    "All",
    "Not Assigned"]

SerTVDropOrders = ttk.OptionMenu(ManagerOrderTVFrame, SerTVOrders, *SearchOptionsOrders)
SerTVDropOrders.grid(row=0, column=1, padx=5)

SerPreformaTVButton = ttk.Button(ManagerOrderTVFrame, text='Search', command=ShowOrderTV)
SerPreformaTVButton.grid(row=0, column=2, padx=5)

# tv
managerTVOrders = ttk.Treeview(ManagerOrderTVFrame, height=10,
                               columns=('First Name', 'Last Name', 'Column 2 ', 'Coulmn 3', '4', '5'))
managerTVOrders.grid(row=2, column=0, columnspan=30, pady=10, padx=10)

managerTVOrders.heading('#0', text='Order ID')
managerTVOrders.column('#0', minwidth=0, width=130, anchor='center')
managerTVOrders.heading('#1', text='Company')
managerTVOrders.column('#1', minwidth=0, width=130, anchor='center')
managerTVOrders.heading('#2', text='Pick Up')
managerTVOrders.column('#2', minwidth=0, width=130, anchor='center')
managerTVOrders.heading('#3', text='Delivery')
managerTVOrders.column('#3', minwidth=0, width=130, anchor='center')
managerTVOrders.heading('#4', text='Product ID')
managerTVOrders.column('#4', minwidth=0, width=130, anchor='center')
managerTVOrders.heading('#5', text='Lorrie Reg')
managerTVOrders.column('#5', minwidth=0, width=130, anchor='center')
managerTVOrders.heading('#6', text='Driver')
managerTVOrders.column('#6', minwidth=0, width=200, anchor='center')

popupmenuorders = Menu(ManagerOrderTVFrame, tearoff=0)
popupmenuorders.add_command(label='Delete', command=DelDriver)
popupmenuorders.add_command(label='Assign', command=Assign)


def do_popup_orders(event):
    try:
        popupmenuorders.tk_popup(event.x_root, event.y_root)
    finally:
        popupmenuorders.grab_release()


managerTVOrders.bind("<Button-3>", do_popup_orders)

DelDriverButton = ttk.Button(ManagerOrderInputsFrame, text='Delete Order', command=DelDriver)
DelDriverButton.grid(row=1, column=2, padx=10, pady=10)

# ==========================================================================================================
# drivermenuframe
# frames
driverOrdersFrame = Frame(drivermenuframe, bg='white')
driverOrdersFrame.place(x=60, y=90, width=1300, height=1000)

DriverOrderTVFrame = Frame(driverOrdersFrame, bg='white')
DriverOrderTVFrame.place(x=10, y=20)

DriverOrderStatusFrame = Frame(driverOrdersFrame, bg='white')
DriverOrderStatusFrame.place(x=850, y=30)

DriverOrderButtonFrame = Frame(driverOrdersFrame, bg='white')
DriverOrderButtonFrame.place(x=10, y=500)

# tv
driverTVOrders = ttk.Treeview(DriverOrderTVFrame, height=10,
                              columns=('First Name', 'Last Name', 'Column 2 ', 'Coulmn 3', '4'))
driverTVOrders.grid(row=2, column=0, columnspan=30, pady=10, padx=10)

driverTVOrders.heading('#0', text='Order ID')
driverTVOrders.column('#0', minwidth=0, width=130, anchor='center')
driverTVOrders.heading('#1', text='Company')
driverTVOrders.column('#1', minwidth=0, width=130, anchor='center')
driverTVOrders.heading('#2', text='Pick Up')
driverTVOrders.column('#2', minwidth=0, width=130, anchor='center')
driverTVOrders.heading('#3', text='Delivery')
driverTVOrders.column('#3', minwidth=0, width=130, anchor='center')
driverTVOrders.heading('#4', text='Product ID')
driverTVOrders.column('#4', minwidth=0, width=130, anchor='center')
driverTVOrders.heading('#5', text='Lorrie Reg')
driverTVOrders.column('#5', minwidth=0, width=130, anchor='center')

popupmenuordersdriver = Menu(DriverOrderTVFrame, tearoff=0)
popupmenuordersdriver.add_command(label='Status', command=DelDriver)


def do_popup_orders_driver(event):
    try:
        popupmenuordersdriver.tk_popup(event.x_root, event.y_root)
    finally:
        popupmenuordersdriver.grab_release()


driverTVOrders.bind("<Button-3>", do_popup_orders_driver)
driverTVOrders.bind("<Button-1>", show_status)

# status frame
statuslabel = Label(DriverOrderStatusFrame, text='Status:', font=20)
statuslabel.grid(row=0, column=0)
statuslabel2 = ttk.Label(DriverOrderStatusFrame, textvariable=TheStatus, font=20)
statuslabel2.grid(row=0, column=1)

# button frame
OutForDeliveryButton = ttk.Button(DriverOrderButtonFrame, text='Out For Delivery', command=OutForDelivery)
OutForDeliveryButton.grid(row=0, column=0)

DeliveredButton = ttk.Button(DriverOrderButtonFrame, text='Delivered', command=Delivered)
DeliveredButton.grid(row=0, column=1)

# ==========================================================================================================
# clientmenuframe
# frames
clientOrdersFrame = Frame(clientmenuframe, bg='white')
clientOrdersFrame.place(x=60, y=90, width=1300, height=1000)

ClientOrderTVFrame = Frame(clientOrdersFrame, bg='white')
ClientOrderTVFrame.place(x=10, y=20)

ClientOrderStatusFrame = Frame(clientOrdersFrame, bg='white')
ClientOrderStatusFrame.place(x=850, y=30)

ClientOrderInputsFrame = Frame(clientOrdersFrame, bg='white')
ClientOrderInputsFrame.place(x=10, y=447)

# tv
clientTVOrders = ttk.Treeview(ClientOrderTVFrame, height=10,
                              columns=('First Name', 'Last Name', 'Column 2 ', 'Coulmn 3', '4'))
clientTVOrders.grid(row=2, column=0, columnspan=30, pady=10, padx=10)

clientTVOrders.heading('#0', text='Order ID')
clientTVOrders.column('#0', minwidth=0, width=130, anchor='center')
clientTVOrders.heading('#1', text='Pick Up')
clientTVOrders.column('#1', minwidth=0, width=130, anchor='center')
clientTVOrders.heading('#2', text='Delivery')
clientTVOrders.column('#2', minwidth=0, width=130, anchor='center')
clientTVOrders.heading('#3', text='Product ID')
clientTVOrders.column('#3', minwidth=0, width=130, anchor='center')
clientTVOrders.heading('#4', text='Lorrie Reg')
clientTVOrders.column('#4', minwidth=0, width=130, anchor='center')
clientTVOrders.heading('#5', text='Driver')
clientTVOrders.column('#5', minwidth=0, width=130, anchor='center')

clientTVOrders.bind("<Button-1>", show_statusClient)

# status frame
Clientstatuslabel = Label(ClientOrderStatusFrame, text='Status:', font=20)
Clientstatuslabel.grid(row=0, column=0)
Clientstatuslabel2 = ttk.Label(ClientOrderStatusFrame, textvariable=ClientTheStatus, font=20)
Clientstatuslabel2.grid(row=0, column=1)

# new order frame
# clinets inputs
# inputs orders
PickUpLabel = ttk.Label(ClientOrderInputsFrame, text='Pick Up:')
PickUpLabel.grid(row=0, column=0, padx=10)
PickUpEntry = ttk.Entry(ClientOrderInputsFrame, textvariable=PickUp)
PickUpEntry.grid(row=0, column=1)

DeliveryLabel = ttk.Label(ClientOrderInputsFrame, text='Delivery:')
DeliveryLabel.grid(row=0, column=2, padx=10)
DeliveryEntry = ttk.Entry(ClientOrderInputsFrame, textvariable=Delivery)
DeliveryEntry.grid(row=0, column=3)

ProductLabel = ttk.Label(ClientOrderInputsFrame, text='Product Name:')
ProductLabel.grid(row=0, column=4, padx=10)
ProductEntry = ttk.Entry(ClientOrderInputsFrame, textvariable=ProductName)
ProductEntry.grid(row=0, column=5)

QuantityLabel = ttk.Label(ClientOrderInputsFrame, text='Quantity:')
QuantityLabel.grid(row=0, column=6, padx=10)
QuantityEntry = ttk.Entry(ClientOrderInputsFrame, textvariable=Quantity)
QuantityEntry.grid(row=0, column=7)

AddDriverButton = ttk.Button(ClientOrderInputsFrame, text='Add Order', command=AddOrder)
AddDriverButton.grid(row=1, column=0, padx=10, pady=10)

# ========================================================================================================
# new order frame
clientNewOrdersFrame = Frame(clientmenuframe, bg='white')
clientNewOrdersFrame.place(x=60, y=90, width=1300, height=1000)

clientNewOrdersInputsFrame = LabelFrame(clientNewOrdersFrame, text='order', bg='white')
clientNewOrdersInputsFrame.place(x=10, y=447)

ClinetProductTVFrame = Frame(clientNewOrdersFrame, bg='white')
ClinetProductTVFrame.place(x=10, y=20)

# tv
# tv
ClientTVProducts = ttk.Treeview(ClinetProductTVFrame, height=10,
                                columns=('First Name', 'Last Name'))
ClientTVProducts.grid(row=2, column=0, columnspan=30, pady=10, padx=10)

ClientTVProducts.heading('#0', text='Product ID')
ClientTVProducts.column('#0', minwidth=0, width=130, anchor='center')
ClientTVProducts.heading('#1', text='Name')
ClientTVProducts.column('#1', minwidth=0, width=130, anchor='center')
ClientTVProducts.heading('#2', text='Quantity')
ClientTVProducts.column('#2', minwidth=0, width=130, anchor='center')

# ==========================================================================================================
# laodermenuframe
# frames
loaderOrdersFrame = Frame(loadermenuframe, bg='white')
loaderOrdersFrame.place(x=60, y=90, width=1300, height=1000)

OrderProductTVFrame = Frame(loaderOrdersFrame, bg='white')
OrderProductTVFrame.place(x=10, y=20)

# tv
LoaderTVProducts = ttk.Treeview(OrderProductTVFrame, height=10,
                                columns=('First Name', 'Last Name', '2', '3'))
LoaderTVProducts.grid(row=0, column=0, columnspan=30, pady=10, padx=10)

LoaderTVProducts.heading('#0', text='Product ID')
LoaderTVProducts.column('#0', minwidth=0, width=130, anchor='center')
LoaderTVProducts.heading('#1', text='Order ID')
LoaderTVProducts.column('#1', minwidth=0, width=130, anchor='center')
LoaderTVProducts.heading('#2', text='Company')
LoaderTVProducts.column('#2', minwidth=0, width=130, anchor='center')
LoaderTVProducts.heading('#3', text='Product Name')
LoaderTVProducts.column('#3', minwidth=0, width=130, anchor='center')
LoaderTVProducts.heading('#4', text='Quantity')
LoaderTVProducts.column('#4', minwidth=0, width=130, anchor='center')

loadedbutton = ttk.Button(OrderProductTVFrame, text='loaded', command=loaded)
loadedbutton.grid(row=0, column=1)
# ==========================================================================================================
# top menu manager
labelframe2 = Frame(managermenuframe, bg='#0E2B4D')
labelframe2.grid(row=0, column=0, columnspan=3, sticky=NW)

photomangermenuscreen = PhotoImage(file='white-footer-logo.png')
photolabelmanager = Label(labelframe2, image=photomangermenuscreen, bg='#0E2B4D')
photolabelmanager.grid(row=0, column=0, sticky=NW, pady=5)

username_label = Label(labelframe2, text='Manager              ', font=40, fg='white', bg='#0E2B4D')
username_label.grid(row=0, column=2, padx=370)

adminMemberClockLabel = Label(labelframe2, bg='#0E2B4D', fg='white', font='bold')
adminMemberClockLabel.grid(row=0, column=4, padx=10)

LOGoutButton = Button(labelframe2, command=LogOut, text='Log Out', bg='#0E2B4D', fg='white', font=12)
LOGoutButton.grid(row=0, column=5, ipady=30, ipadx=10)

# side menu manager
home = ImageTk.PhotoImage(Image.open('home.png').resize((50, 50), Image.ANTIALIAS))
settings = ImageTk.PhotoImage(Image.open('group.png').resize((50, 50), Image.ANTIALIAS))
ring = ImageTk.PhotoImage(Image.open('speedometer.png').resize((50, 50), Image.ANTIALIAS))

root.update()  # For the width to get updated
frame = Frame(managermenuframe, bg='#0E2B4D', width=60, height=root.winfo_height())
frame.grid(row=1, column=0, sticky=NW, rowspan=4)

# Make the buttons with the icons to be shown
home_b = Button(frame, image=home, bg='#0E2B4D', command=MangerMenu, relief='flat')
set_b = Button(frame, image=settings, bg='#0E2B4D', command=ManagerDriver, relief='flat')
ring_b = Button(frame, image=ring, bg='#0E2B4D', command=MangerOrders, relief='flat')

# Put them on the frame
home_b.grid(row=0, column=0, pady=10)
set_b.grid(row=1, column=0, pady=50)
ring_b.grid(row=2, column=0)

# Bind to the frame, if entered or left
frame.bind('<Enter>', lambda e: expand())
frame.bind('<Leave>', lambda e: contract())

# So that it does not depend on the widgets inside the frame
frame.grid_propagate(False)

# ==========================================================================================================
# top menu driver
labelframe3 = Frame(drivermenuframe, bg='#0E2B4D')
labelframe3.grid(row=0, column=0, columnspan=3, sticky=NW)

photodrivermenuscreen = PhotoImage(file='white-footer-logo.png')
photolabeldriver = Label(labelframe3, image=photodrivermenuscreen, bg='#0E2B4D')
photolabeldriver.grid(row=0, column=0, sticky=NW, pady=5)

username_labeldriver = Label(labelframe3, text='Driver              ', font=40, fg='white', bg='#0E2B4D')
username_labeldriver.grid(row=0, column=2, padx=370)

driverMemberClockLabel = Label(labelframe3, bg='#0E2B4D', fg='white', font='bold')
driverMemberClockLabel.grid(row=0, column=4, padx=10)

LOGoutButtondriver = Button(labelframe3, command=LogOut, text='Log Out', bg='#0E2B4D', fg='white', font=12)
LOGoutButtondriver.grid(row=0, column=5, ipady=30, ipadx=10)

# side menu manager
home2 = ImageTk.PhotoImage(Image.open('home.png').resize((50, 50), Image.ANTIALIAS))
settings2 = ImageTk.PhotoImage(Image.open('group.png').resize((50, 50), Image.ANTIALIAS))
ring2 = ImageTk.PhotoImage(Image.open('speedometer.png').resize((50, 50), Image.ANTIALIAS))

root.update()  # For the width to get updated
frame2 = Frame(drivermenuframe, bg='#0E2B4D', width=60, height=root.winfo_height())
frame2.grid(row=1, column=0, sticky=NW, rowspan=4)

# Make the buttons with the icons to be shown
home_b2 = Button(frame2, image=home, bg='#0E2B4D', command=MangerMenu, relief='flat')
set_b2 = Button(frame2, image=settings, bg='#0E2B4D', command=ManagerDriver, relief='flat')
ring_b2 = Button(frame2, image=ring, bg='#0E2B4D', command=MangerOrders, relief='flat')

# Put them on the frame
home_b2.grid(row=0, column=0, pady=10)
set_b2.grid(row=1, column=0, pady=50)
ring_b2.grid(row=2, column=0)

# Bind to the frame, if entered or left
frame2.bind('<Enter>', lambda e: expand2())
frame2.bind('<Leave>', lambda e: contract2())

# So that it does not depend on the widgets inside the frame
frame2.grid_propagate(False)

# ==========================================================================================================
# top menu client
labelframe4 = Frame(clientmenuframe, bg='#0E2B4D')
labelframe4.grid(row=0, column=0, columnspan=3, sticky=NW)

photoclientmenuscreen = PhotoImage(file='white-footer-logo.png')
photolabelclient = Label(labelframe4, image=photoclientmenuscreen, bg='#0E2B4D')
photolabelclient.grid(row=0, column=0, sticky=NW, pady=5)

username_labelclient = Label(labelframe4, text='Client              ', font=40, fg='white', bg='#0E2B4D')
username_labelclient.grid(row=0, column=2, padx=370)

clientMemberClockLabel = Label(labelframe4, bg='#0E2B4D', fg='white', font='bold')
clientMemberClockLabel.grid(row=0, column=4, padx=10)

LOGoutButtonclient = Button(labelframe4, command=LogOut, text='Log Out', bg='#0E2B4D', fg='white', font=12)
LOGoutButtonclient.grid(row=0, column=5, ipady=30, ipadx=10)

# side menu manager
home3 = ImageTk.PhotoImage(Image.open('home.png').resize((50, 50), Image.ANTIALIAS))
settings3 = ImageTk.PhotoImage(Image.open('group.png').resize((50, 50), Image.ANTIALIAS))
ring3 = ImageTk.PhotoImage(Image.open('speedometer.png').resize((50, 50), Image.ANTIALIAS))

root.update()  # For the width to get updated
frame3 = Frame(clientmenuframe, bg='#0E2B4D', width=60, height=root.winfo_height())
frame3.grid(row=1, column=0, sticky=NW, rowspan=4)

# Make the buttons with the icons to be shown
home_b3 = Button(frame3, image=home3, bg='#0E2B4D', command=ClientOrders, relief='flat')
set_b3 = Button(frame3, image=settings3, bg='#0E2B4D', command=Neworder, relief='flat')
ring_b3 = Button(frame3, image=ring3, bg='#0E2B4D', command=MangerOrders, relief='flat')

# Put them on the frame
home_b3.grid(row=0, column=0, pady=10)
set_b3.grid(row=1, column=0, pady=50)
ring_b3.grid(row=2, column=0)

# Bind to the frame, if entered or left
frame3.bind('<Enter>', lambda e: expand3())
frame3.bind('<Leave>', lambda e: contract3())

# So that it does not depend on the widgets inside the frame
frame3.grid_propagate(False)

# ==========================================================================================================
# top menu loader
labelframe5 = Frame(loadermenuframe, bg='#0E2B4D')
labelframe5.grid(row=0, column=0, columnspan=3, sticky=NW)

photoloadermenuscreen = PhotoImage(file='white-footer-logo.png')
photolabelloader = Label(labelframe5, image=photoclientmenuscreen, bg='#0E2B4D')
photolabelloader.grid(row=0, column=0, sticky=NW, pady=5)

username_labelloader = Label(labelframe5, text='loader              ', font=40, fg='white', bg='#0E2B4D')
username_labelloader.grid(row=0, column=2, padx=370)

loaderMemberClockLabel = Label(labelframe5, bg='#0E2B4D', fg='white', font='bold')
loaderMemberClockLabel.grid(row=0, column=4, padx=10)

LOGoutButtonloader = Button(labelframe5, command=LogOut, text='Log Out', bg='#0E2B4D', fg='white', font=12)
LOGoutButtonloader.grid(row=0, column=5, ipady=30, ipadx=10)

# side menu laoder
home4 = ImageTk.PhotoImage(Image.open('home.png').resize((50, 50), Image.ANTIALIAS))
settings4 = ImageTk.PhotoImage(Image.open('group.png').resize((50, 50), Image.ANTIALIAS))
ring4 = ImageTk.PhotoImage(Image.open('speedometer.png').resize((50, 50), Image.ANTIALIAS))

root.update()  # For the width to get updated
frame4 = Frame(loadermenuframe, bg='#0E2B4D', width=60, height=root.winfo_height())
frame4.grid(row=1, column=0, sticky=NW, rowspan=4)

# Make the buttons with the icons to be shown
home_b4 = Button(frame4, image=home4, bg='#0E2B4D', command=ClientOrders, relief='flat')
set_b4 = Button(frame4, image=settings4, bg='#0E2B4D', command=Neworder, relief='flat')
ring_b4 = Button(frame4, image=ring4, bg='#0E2B4D', command=MangerOrders, relief='flat')

# Put them on the frame
home_b4.grid(row=0, column=0, pady=10)
set_b4.grid(row=1, column=0, pady=50)
ring_b4.grid(row=2, column=0)

# Bind to the frame, if entered or left
frame4.bind('<Enter>', lambda e: expand3())
frame4.bind('<Leave>', lambda e: contract3())

# So that it does not depend on the widgets inside the frame
frame4.grid_propagate(False)

raise_frame(loginframe)
root.mainloop()
