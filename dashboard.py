from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk
import pymysql



def logout_function():
    dashboard_window.destroy()
    messagebox.showinfo("Successful!",'Logged Out Successfully!')
    import signin

dashboard_window=Tk()
dashboard_window.resizable(0,0)
dashboard_window.title('DASHBOARD')

dashbgi=ImageTk.PhotoImage(file='dashboardbg.png')
dashbgilabel=Label(dashboard_window,image=dashbgi)
dashbgilabel.grid()

frame=Frame(dashboard_window,height=80,width=1400,bg='gray40')
frame.place(x=0,y=0)

homeicon=PhotoImage(file='home.png')
homeiconlabel=Label(dashboard_window,image=homeicon).place(x=50,y=25)

homeButton=Button(dashboard_window,text='DASHBOARD',font=("Bahnschrift SemiBold",20,'bold'),bg='gray40',fg='white',cursor='hand2',activebackground='gray',activeforeground='white',bd=0)
homeButton.place(x=100,y=15)

logouticon=PhotoImage(file='logout.png')
logouticonlabel=Label(dashboard_window,image=logouticon).place(x=1150,y=25)

logoutButton=Button(dashboard_window,text='LOGOUT',font=("Bahnschrift SemiBold",20,'bold'),bg='gray40',fg='white',cursor='hand2',activebackground='gray',activeforeground='white',bd=0,command=logout_function)
logoutButton.place(x=1200,y=15)

welcomeLabel=Label(dashboard_window,text='WELCOME TO DASHBOARD!',font=('Arial Black',30,'bold'),fg='gray40',bg='light grey')
welcomeLabel.place(x=30,y=150)

belongLabel=Label(dashboard_window,text='Hello user !!',font=("Open Sans",20,'bold'),fg='gray40',bg='light grey')
belongLabel.place(x=30,y=250)

profile=PhotoImage(file='user.png')
profilelabel=Button(dashboard_window,image=profile,bd=0,cursor='hand2').place(x=30,y=300)

dashboard=PhotoImage(file='dashboard.PNG')
dashlabel=Button(dashboard_window,image=dashboard,bd=0,cursor='hand2').place(x=220,y=300)

search=PhotoImage(file='search.PNG')
searchlabel=Button(dashboard_window,image=search,bd=0,cursor='hand2').place(x=400,y=300)

download=PhotoImage(file='download.PNG')
downloadlabel=Button(dashboard_window,image=download,bd=0,cursor='hand2').place(x=30,y=500)

favourite=PhotoImage(file='favorite.PNG')
favlabel=Button(dashboard_window,image=favourite,bd=0,cursor='hand2').place(x=220,y=500)

settingicon=PhotoImage(file='setting.PNG')
settinglabel=Button(dashboard_window,image=settingicon,bd=0,cursor='hand2').place(x=400,y=500)

homeicon=PhotoImage(file='home.png')
homeiconlabel=Label(dashboard_window,image=homeicon).place(x=50,y=25)

dashboard_window.mainloop()