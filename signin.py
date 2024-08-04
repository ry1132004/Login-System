from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#functionality part


def forget_pass():

    def resetpass():
        if usernameEntry.get()=='' or passEntry.get()=='' or confirmEntry.get()=='':
            messagebox.showerror("Error","All fields are required to create new password.",parent=window)
        elif passEntry.get() !=confirmEntry.get():
            messagebox.showerror("Error",'Password did not match.',parent=window)
        else:
            con=pymysql.connect(host='localhost',user='root',password='123456789',database='userdata')
            mycursor=con.cursor()
            query='select * from data where username=%s'
            mycursor.execute(query,(usernameEntry.get()))
            row=mycursor.fetchone
            if row==None:
                messagebox.showwarning("Warning","Username doesn't exist.",parent=window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(passEntry.get(),usernameEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Successful!","Password Changed successfully!Login with New Password",parent=window)
                window.destroy()



    window=Toplevel()
    window.resizable(FALSE,FALSE)
    window.title("Change Password")
    bg=ImageTk.PhotoImage(file='bgi.jpg')
    bgLabel=Label(window,image=bg)
    bgLabel.grid()

    heading_label=Label(window,text='Create a New Password',font=('Ariel',23,'bold'),bg='white',fg='gray')
    heading_label.place(x=650,y=50)
    
    usernameLabel=Label(window,text='Enter Username',font=('Open Sans',11,'bold'),bg='white',fg='gray')
    usernameLabel.place(x=650,y=120)

    usernameEntry=Entry(window,width=25,font=('Open Sans',10,'bold'),bd=0,bg='white',fg='gray')
    usernameEntry.place(x=650,y=150)

    frame=Frame(window,width=300,height=2,bg='gray').place(x=650,y=170)
    
    passLabel=Label(window,text='New Password',font=('Open Sans',11,'bold'),bg='white',fg='gray')
    passLabel.place(x=650,y=200)
    
    passEntry=Entry(window,width=30,font=('Open Sans',10,'bold'),bd=0,bg='white',fg='gray')
    passEntry.place(x=650,y=230)

    frame3=Frame(window,width=300,height=2,bg='gray').place(x=650,y=250)
    
    confirmLabel=Label(window,text='Confirm New Password',font=('Open Sans',11,'bold'),bg='white',fg='gray')
    confirmLabel.place(x=650,y=280)
    
    confirmEntry=Entry(window,width=30,font=('Open Sans',10,'bold'),bd=0,bg='white',fg='gray')
    confirmEntry.place(x=650,y=310)

    frame4=Frame(window,width=300,height=2,bg='gray').place(x=650,y=330)

    submitButton=Button(window,text="Change Password",font=("Ariel",11,'bold'),bg='gray',fg='white',width=35,height=2,cursor='hand2',bd=0,activebackground='gray',activeforeground='white',command=resetpass)
    submitButton.place(x=650,y=400)

    
    window.mainloop()

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required!')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='123456789')
            mycursor=con.cursor()
        except:
            messagebox.showerror("Error",'Connection not established,Try Again!')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror("Error",'User not Registered!')
        else:
            messagebox.showinfo('Message',"Login is successful.")
            root.destroy()
            import dashboard


def register():
    root.destroy()
    import registration

def hide():
    openeye.config(file='hide.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='show.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def pass_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)


#GUI part
root=Tk()
root.resizable(0,0)
root.title('Login Page')

bgImage=ImageTk.PhotoImage(file='bgi.jpg')

bgLabel=Label(root,image=bgImage)
bgLabel.pack()

heading=Label(root,text='USER LOGIN',font=('Ariel',23,'bold'),bg='white',fg='gray')
heading.place(x=700,y=50)

usernameEntry=Entry(root,width=25,font=('Ariel',11),bd=0,fg='gray')
usernameEntry.place(x=675,y=150)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(root,width=250,height=2,bg='gray').place(x=675,y=168)

passwordEntry=Entry(root,width=25,font=('Ariel',11),bd=0,fg='gray')
passwordEntry.place(x=675,y=200)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',pass_enter)

frame2=Frame(root,width=250,height=2,bg='gray').place(x=675,y=220)

openeye=PhotoImage(file='show.png')
eyeButton=Button(root,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=900,y=198)

forgetButton=Button(root,text='Forgot Password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Ariel',9,'bold'),fg='gray',activeforeground='gray',command=forget_pass)
forgetButton.place(x=820,y=250)

loginButton=Button(root,text='LOGIN',font=('Open Sans',16,'bold'),fg='white',bg='gray',cursor='hand2',width=19,bd=0,activeforeground='white',activebackground='gray',command=login_user)
loginButton.place(x=670,y=300)

signupLabel=Label(root,text="Don't have an Account?",font=('Open Sans',9,'bold'),fg='gray',bg='white')
signupLabel.place(x=670,y=400)

newaccButton=Button(root,text='Register Here',font=('Open Sans',9,'bold underline'),fg='blue',cursor='hand2',bd=0,activeforeground='blue',activebackground='white',bg='white',command=register)
newaccButton.place(x=820,y=400)

root.mainloop()