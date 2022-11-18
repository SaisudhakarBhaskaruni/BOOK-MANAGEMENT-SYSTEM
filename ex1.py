from msilib.schema import CheckBox
from tkinter import *
from sqlite3 import *


def avlbooks(root):
    # root.destroy()
    avl = Tk()
    avl.title("BOOK MANAGEMENTS SYSTEM-available books")
    avl.geometry("925x500+300+200")
    avl.configure(bg='#fff')

    headingFrame1 = Frame(avl, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.28, rely=0.24, relwidth=0.5, relheight=0.13)



    avl.mainloop()