from tkinter import * ###########this for login page##
from tkinter import messagebox
import ast

window = Tk()
window.title("sign up")
window.geometry("925x500+300+200")
window.configure(bg='#fff')
window.resizable(False, False)


def signin():
    Username = user.get()
    Password = code.get()

    if Username == "leelasai" and Password == "1234":
        screen = Toplevel(window)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        
        

    elif Username != 'leelasai' and Password != '1234':
        messagebox.showerror('invalid', "invalid username and password")

    elif Password != '1234':
        messagebox.showerror('invalid', 'invalid password')

    elif Username != 'admin':
        messagebox.showerror('invalid', 'invalid username')


img = PhotoImage(file='LOGO1234.png')
Label(window, image=img, border=0, bg='white').place(x=50, y=50)

frame = Frame(window, width=350, height=390, bg='#fff')
frame.place(x=480, y=50)

heading = Label(frame, text='LOGIN PAGE', bg='white', fg='#57a1f8', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=70, y=5)

############-------USERNAME---------###############


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username:')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


##############--PASSWORD--#############################


def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')


code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password:')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)



######################-------BUTTON FOR LOGIN---##########
Button(frame, width=39, pady=7, text='login', bg='#57a1f8', fg='white', border=0, command=signin).place(x=25, y=200)
label = Label(frame, text="Dont have an account?", fg="black", bg="white", font=("Microsoft Yahei UI Light", 9))
label.place(x=75, y=270)
########################---------BUTTON FOR SIGN UP -------#########
sign_up = Button(frame, width=6, text='sign up', border=0, bg="white", cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)

window.mainloop()
