from sqlite3 import connect
from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image,ImageTk
import random
import cv2 as cv
conn=pymysql.connect(host='localhost',user='root',passwd='',db='ab')
a=conn.cursor()
def database():
    #USERID CHECKER
    a.execute("select User_id from account_details")
    userdata = a.fetchall()
    userrows = len(userdata)
    i = 0
    while i < userrows:
        if useridtf.get() == userdata[i][0]:
            messagebox.showerror("Error", "Username already exists")
            return
        i+=1
    
    #PHONE NUMBER CHECKER
    a.execute("select Phone_no from account_details")
    phonedata = a.fetchall()
    phonerows = len(phonedata)
    j = 0
    while j < phonerows:
        if phnotf.get() == phonedata[j][0]:
            messagebox.showerror("Error", "Phone number already exists")
            return
        j+=1

    #EMAIL CHECKER
    a.execute("select Email from account_details")
    emaildata = a.fetchall()
    emailrows = len(emaildata)
    k = 0
    while k < emailrows:
        if emailtf.get() == emaildata[k][0]:
            messagebox.showerror("Error", "Email address already exists")
            return
        k+=1
    
    a.execute("INSERT INTO account_details VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (nametf.get(), acnotf, phnotf.get(), emailtf.get(), addresstf.get(), dobtf.get(), adhaartf.get(),0 , useridtf.get(), passwdtf.get()))
    conn.commit()
    messagebox.showinfo("Registeration Successfull", "Your account has been created please login to add or withraw money.")

def photo():
    cam = cv.VideoCapture(0)
    s, img = cam.read()
    if s:
        cv.namedWindow("cam-test")
        cv.imshow("cam-test",img)
        cv.waitKey(0)
        cv.destroyWindow("cam-test")
        filename = "snapshots/image"+str(random.randint(100000,999999))+".jpg"
        cv.imwrite(filename,img)

def createacfn():
    global ca, nametf, acnotf, phnotf, emailtf, addresstf, dobtf, adhaartf, useridtf, passwdtf
    bm.destroy()
    ca=Tk()
    ca.title("CREATE ACCOUNT")
    ca.geometry("500x500")
    acnotf = str(random.randint(1000000000,9999999999))
    img=PhotoImage(file="registerbg.png")
    img_label=Label(ca, image=img)
    img_label.place(x=0,y=0, relwidth=1, relheight=1)
    name=Label(ca,text="NAME",fg="blue",font=("arial",15,"bold"))
    name.grid(column=0,row=0,padx=20)
    nametf=Entry(ca)
    nametf.grid(column=0,row=1)
    phno=Label(ca,text="PHONE NO",fg="blue",font=("arial",15,"bold"))
    phno.grid(column=0,row=2,padx=20)
    phnotf=Entry(ca)
    phnotf.grid(column=0,row=3)
    email=Label(ca,text="EMAIL",fg="blue",font=("arial",15,"bold"))
    email.grid(column=0,row=6,padx=20)
    emailtf=Entry(ca)
    emailtf.grid(column=0,row=7)
    address=Label(ca,text="ADDRESS",fg="blue",font=("arial",15,"bold"))
    address.grid(column=0,row=8,padx=20)
    addresstf=Entry(ca)
    addresstf.grid(column=0,row=9)
    dob=Label(ca,text="DOB",fg="blue",font=("arial",15,"bold"))
    dob.grid(column=1,row=0,padx=20)
    dobtf=Entry(ca)
    dobtf.grid(column=1,row=1)
    adhaar=Label(ca,text="ADHAAR",fg="blue",font=("arial",15,"bold"))
    adhaar.grid(column=1,row=2,padx=20)
    adhaartf=Entry(ca)
    adhaartf.grid(column=1,row=3)
    userid=Label(ca,text="USER ID",fg="blue",font=("arial",15,"bold"))
    userid.grid(column=1,row=6,padx=20)
    useridtf=Entry(ca)
    useridtf.grid(column=1,row=7)
    passwd=Label(ca,text="PASSWORD",fg="blue",font=("arial",15,"bold"))
    passwd.grid(column=1,row=8,padx=20)
    passwdtf=Entry(ca)
    passwdtf.grid(column=1,row=9)
    regbtn=Button(ca, text="REGISTER", fg="red",font=("arial",15,"bold"), command=database)
    regbtn.grid(column=0,row=11,pady=50)
    homebtn=Button(ca, text="HOME", fg="red",font=("arial",15,"bold"), command=destroyca_openkl)
    homebtn.grid(column=1,row=11,pady=50)
    snapbtn=Button(ca, text="SNAPSHOT", fg="blue",font=("arial",15,"bold"), command=photo)
    snapbtn.grid(column=0,row=10,pady=10)
    ca.mainloop()

def widfn():
    base = int(dataa[7])
    subtract = int(wid_amount_tf.get())
    remaining = base - subtract
    a.execute("Update account_details set Balance = %s where User_id = %s", (remaining, us))
    conn.commit()
    widwn.destroy()
    messagebox.showinfo("Success","Money withdrawn successfully")
    credit = 0
    debit = subtract
    a.execute("insert into transactions values (%s,%s,%s,%s,%s,%s)", (dataa[0], dataa[8], dataa[1], credit, debit, remaining))
    conn.commit()


def widwnfn():
    global widwn, wid_amount_tf
    widwn = Tk()
    widwn.title("Withdraw Money")
    widwn.geometry("300x300")
    amount_label = Label(widwn, text="Amount: ", font=("arial", 11, "bold"))
    wid_amount_tf = Entry(widwn, font=("arial", 11))
    amount_label.grid(row=0, column=0, pady=50)
    wid_amount_tf.grid(row=0, column=1, pady=50)
    wid_btn = Button(widwn, text="WITHDRAW", justify="center", command=widfn)
    wid_btn.grid(row=1, columnspan=2, pady=20)

def addfn():
    base = int(dataa[7])
    surplus = int(amount_tf.get())
    total = base + surplus
    a.execute("Update account_details set Balance = %s where User_id = %s", (total, us))
    conn.commit()
    addwn.destroy()
    messagebox.showinfo("Success","Money deposited successfully")
    debit = 0
    credit = surplus
    a.execute("insert into transactions values (%s,%s,%s,%s,%s,%s)", (dataa[0], dataa[8], dataa[1], credit, debit, total))
    conn.commit()


def addwnfn():
    global addwn, amount_tf
    addwn = Tk()
    addwn.title("ADD MONEY")
    addwn.geometry("300x300")

    amount_label = Label(addwn, text="Amount: ", font=("arial", 11, "bold"))
    amount_tf = Entry(addwn, font=("arial", 11))
    amount_label.grid(row=0, column=0, pady=50)
    amount_tf.grid(row=0, column=1, pady=50)
    add_btn = Button(addwn, text="ADD", justify="center", command=addfn)
    add_btn.grid(row=1, columnspan=2, pady=20)

def login_data_check():
    #USER ID CHECK
    a.execute("select User_id from account_details")
    userdata = a.fetchall()
    userrows = len(userdata)
    i = 0
    userexists = False
    while i < userrows:
        if usertf.get() != userdata[i][0]:
            i+=1
            continue
        else:
            userexists = True
            break
    if userexists == False:
        messagebox.showerror("Error","User doesn't exist")
        return
    #PASSWORD CHECK
    a.execute("select Password from account_details where User_id = %s", (usertf.get()))
    pswdd = a.fetchone()[0]
    if pswdd == pdtf.get():
        acdetailsfn()
    else:
        messagebox.showerror("Error","Incorrect Password")



def acdetailsfn(): 
    global ad, dataa, us
    
    us=usertf.get()
    pa=pdtf.get()
    lp.destroy()
    ad=Tk()
    ad.geometry("500x500")
    ad.title("USER DETAILS")
    img=PhotoImage(file="detailsbg.png")
    img_label=Label(ad, image=img)
    img_label.place(x=0,y=0, relwidth=1, relheight=1)
    a.execute("Select * from account_details where User_id ='"+us+"' and Password='"+pa+"'" )
    dataa= a.fetchone()
    name = "Name: "+dataa[0]
    acno = "Account no.: "+dataa[1]
    phno = "Phone no.: "+dataa[2]
    bal = "Balance: "+str(dataa[7])
    add_btn = Button(ad, text="ADD MONEY", font=("arial", 15, "bold"), command=addwnfn) 
    wid_btn = Button(ad, text="WITHDRAW MONEY", font=("arial", 15, "bold"), command=widwnfn)
    name_label = Label(ad, text=name, font=("arial", 11), bg="white")
    acno_label = Label(ad, text=acno, font=("arial", 11), bg="white")
    phno_label = Label(ad, text=phno, font=("arial", 11), bg="white")
    bal_label = Label(ad, text=bal, font=("arial", 11), bg="white")
    
    name_label.pack(pady=(100,0))
    acno_label.pack()
    phno_label.pack()
    bal_label.pack()
    add_btn.pack()
    wid_btn.pack()
    ad.mainloop()
def loginfn():
    global usertf,pdtf,lp
    bm.destroy()
    lp=Tk()
    lp.title("LOGIN DETAILS")
    lp.geometry("600x500")
    img=PhotoImage(file="loginbg.png")
    img_label=Label(lp, image=img)
    img_label.place(x=0,y=0, relwidth=1, relheight=1)
    user=Label(lp,text="USER ID",fg="blue",font=("arial",15,"bold"))
    user.pack(side="top",pady=(20,0))
    usertf=Entry(lp)
    usertf.pack()
    pswd=Label(lp,text="PASSWORD",fg="blue",font=("arial",15,"bold"))
    pswd.pack(pady=(20,0))
    pdtf=Entry(lp)
    pdtf.pack()
    Submit=Button(lp,text="SUBMIT",justify="center",fg="blue",font=("arial",15,"bold"),command=login_data_check)
    Submit.pack(side="left",padx=20,pady=0)    
    fgpd=Button(lp,text="FORGET PASSWORD",justify="center",fg="blue",font=("arial",15,"bold"), command=forgotfn)
    fgpd.pack(side="left",padx=20,pady=0)
    home=Button(lp,text="HOME",justify="center",fg="blue",font=("arial",15,"bold"), command=destroylp_openkl)
    home.pack(side="left",padx=20,pady=0)
    lp.mainloop()

def forgotfn():
    lp.destroy()
    global fp
    fp=Tk()
    fp.title("FORGOT PASSWORD")
    fp.geometry("400x250")
    reset_label = Label(fp, text="RESET PASSWORD", justify="center", fg="blue",font=("arial",15,"bold"))
    reset_label.grid(row=0,columnspan=2)
    email_label = Label(fp, text="Registered email address: ",font=("arial",11,"bold"))
    email_label.grid(row=1, column=0, pady=(50,0))
    email_tf = Entry(fp, font=("arial",11,"bold"))
    email_tf.grid(row=1, column=1,pady=(50,0))
    send_btn = Button(fp, text="SEND LINK", font=("arial",15,"bold"), fg="white", bg="blue", justify="center")
    send_btn.grid(row=2, columnspan=2, pady=(50,0))
    

def kl():
    global bm
    bm=Tk()
    bm.title("HOME PAGE")
    bm.geometry("500x500")
    bm.wm_attributes("-transparentcolor", "black")
    img=PhotoImage(file="bg.png")
    img_label=Label(bm, image=img)
    img_label.place(x=0,y=0, relwidth=1, relheight=1)
    a=Label(bm,text="ALL CITIZENS BANK",justify="center",fg="white",bg="blue",bd=20,font=("TIMES NEW ROMAN",20,"bold"))
    a.pack(side="top")
    login=Button(bm,text="LOGIN",justify="center",fg="blue",font=("arial",15,"bold"),command=loginfn)
    login.pack(side="left",padx=20,pady=0)
    create=Button(bm,text="CREATE ACCOUNT",justify="center",fg="blue",font=("arial",15,"bold"),command=createacfn)
    create.pack(side="right",padx=20,pady=0)
    bm.mainloop()
def destroylp_openkl():
    lp.destroy()
    kl()
def destroyca_openkl():
    ca.destroy()
    kl()
kl();