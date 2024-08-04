from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All fields are required!')
    elif passEntry.get() != confirmEntry.get():
        messagebox.showerror('Error',"Password didn't match!")
    elif check.get()==0:
        messagebox.showerror('Error','Terms and Conditions not accepted.')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='123456789')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue,Try Again')
            return
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute("use userdata")

        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror("Warning","User already exists.")
        else:
            query='insert into data(email,username,password) values (%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Message',"Registration Successful!")
            clear()
            login_page()


def login_page():
    signup_window.destroy()
    import signin



signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)

bgimage=ImageTk.PhotoImage(file='bgi.jpg')
bgLabel=Label(signup_window,image=bgimage)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=630,y=50)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Ariel',20,'bold'),bg='white',fg='gray')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Enter Your Email',font=('Open Sans',11,'bold'),bg='white',fg='gray')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=30,font=('Open Sans',10,'bold'),bd=0,bg='gray',fg='white')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Enter Username',font=('Open Sans',11,'bold'),bg='white',fg='gray')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry=Entry(frame,width=30,font=('Open Sans',10,'bold'),bd=0,bg='gray',fg='white')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passLabel=Label(frame,text='Enter A Password',font=('Open Sans',11,'bold'),bg='white',fg='gray')
passLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passEntry=Entry(frame,width=30,font=('Open Sans',10,'bold'),bd=0,bg='gray',fg='white')
passEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmLabel=Label(frame,text='Confirm Password',font=('Open Sans',11,'bold'),bg='white',fg='gray')
confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmEntry=Entry(frame,width=30,font=('Open Sans',10,'bold'),bd=0,bg='gray',fg='white')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
tacCheckButton=Checkbutton(frame,text='I agree to the terms & conditions.',font=("Open Sans",10),cursor='hand2',bg='white',variable=check)
tacCheckButton.grid(row=9,column=0,sticky='w',padx=25,pady=10)

registerButton=Button(frame,text='REGISTER',font=("Open Sans",20,'bold'),bd=0,fg='white',bg='gray',width=17,activebackground='white',activeforeground='gray',command=connect_database)
registerButton.grid(row=10,column=0,pady=10)

noaccLabel=Label(frame,text="Already have an Account?",font=("Open Sans",11),bg='white',fg='gray')
noaccLabel.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginbutton=Button(frame,text='Login Here',font=("Open Sans",11,'underline'),fg='blue',bg='white',bd=0,activebackground='white',activeforeground='blue',command=login_page)                  
loginbutton.place(x=200,y=392)

signup_window.mainloop()
