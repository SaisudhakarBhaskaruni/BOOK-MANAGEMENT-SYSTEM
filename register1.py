from tkinter import*
from tkinter import messagebox
import os



def submit():

        st_var.set("Registering User Information..")
        status_br.update()
        import time
        time.sleep(3)
        messagebox.showinfo("Information","Registration Completed !")

        st_var.set("Welcome To LPU Family - THINK BIG")

        conn=connect('users.db')

        cur=conn.cursor()


        cur.execute('''INSERT INTO users VALUES(:nameentry  ,:genderentry,:ageentry, :emailentry ,:passentry) ''',
              {
            'nameentry':nameentry.get(),
            'genderentry':genderentry.get(),
            'ageentry':ageentry.get(),
            'emailentry' : emailentry.get(),
            'passentry' : passentry.get()
              }
        )
        

        conn.commit()
        conn.close()
        os.system('login.py')

        # Reseting the values
        nameentry.delete(0,END)
        ageentry.delete(0,END)
        # ck.delete(0,END)
        passentry.delete(0,END)
        emailentry.delete(0,END)
        genderentry.delete(0,END)

#-----------------------------------root------------------


def sign():
        
    nus=Tk()
    nus.title("NEW USER REGISTRATION")
    nus.geometry("925x500+300+200")
    nus.configure(bg='#fff')
    nus.resizable(False,False)



    l=Label(nus,text=   "                                                welcome to register                                                               ",borderwidth=2,relief=SUNKEN,font="Aharoni 18 bold",fg='#57a1f8', border=0, bg="orange", cursor='hand2').place(x=0,y=50)

    headingFrame1 = Frame(nus,bg="#fdce68",bd=5)
    headingFrame1.place(relx=0.12,rely=0.31,relwidth=0.7,relheight=0.63)
    name=Label(nus,text="Name",font="Aharoni 12 bold").place(relx=0.2,rely=0.33, relwidth=0.2,relheight=0.08)
    gender=Label(nus,text="Gender",font="Aharoni 12 bold").place(relx=0.2,rely=0.43, relwidth=0.2,relheight=0.08)
    Age=Label(nus,text="Age",font="Aharoni 12 bold").place(relx=0.2,rely=0.53, relwidth=0.2,relheight=0.08)
    Password=Label(nus,text="Password ",font="Aharoni 12 bold").place(relx=0.2,rely=0.73, relwidth=0.2,relheight=0.08)
    number=Label(nus,text="Email",font="Aharoni 12 bold").place(relx=0.2,rely=0.63, relwidth=0.2,relheight=0.08)

    namevalue=StringVar()
    gendervalue=StringVar()
    gendervalue.set("M /F /O")
    agevalue=StringVar()
    passvalue=StringVar()
    emailvalue=StringVar()
    agreevalue=IntVar()




    nameentry=Entry(nus,text="Name",borderwidth=5,relief=SUNKEN,font="Aharoni 12 bold",textvariable=namevalue)
    nameentry.place(relx=0.45,rely=0.33, relwidth=0.25,relheight=0.08)
    genderentry=Entry(nus,text="Gender",borderwidth=5,relief=SUNKEN,font="Aharoni 12 bold",textvariable=gendervalue)
    genderentry.place(relx=0.45,rely=0.43, relwidth=0.25,relheight=0.08)

    ageentry=Entry(nus,text="Age",borderwidth=5,relief=SUNKEN,font="Aharoni 12 bold",textvariable=agevalue)
    ageentry.place(relx=0.45,rely=0.53, relwidth=0.25,relheight=0.08)

    passentry=Entry(nus,text="Password",borderwidth=5,relief=SUNKEN,font="Aharoni 12 bold",textvariable=passvalue)
    passentry.place(relx=0.45,rely=0.73, relwidth=0.25,relheight=0.08)

    emailentry=Entry(nus,text="Email",borderwidth=5,relief=SUNKEN,font="Aharoni 12 bold",textvariable=emailvalue)
    emailentry.place(relx=0.45,rely=0.63, relwidth=0.25,relheight=0.08)

    ck=Checkbutton(nus,text="Do you agree with terms and conditions ",variable=agreevalue,).place(relx=0.45,rely=0.8, relwidth=0.34,relheight=0.03)

    Button(nus, width=6, text='sign up', border=5, bg="white", cursor='hand2', fg='#57a1f8').place(relx=0.3,rely=0.85,relwidth=0.2,relheight=0.08)
    st_var=StringVar()
    st_var.set("Welcome To LPU Family - THINK BIG")
    status_br=Label(nus,textvariable=st_var,borderwidth=10,font="Aharoni 12 bold",bg='white')
    status_br.place(relx=0.0,rely=0.95, relwidth=1.0,relheight=0.05)
    nus.mainloop()






