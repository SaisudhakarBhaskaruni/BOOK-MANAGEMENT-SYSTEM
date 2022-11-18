from tkinter import*
from tkinter import messagebox

def issue(root):
    #root.destroy()
    def dedo():
        st_var.set("Applying Changes..")
        status_br.update()
        import time
        time.sleep(3)
        messagebox.showinfo("Information","Book Issued !") 
        st_var.set('''"Librarians are tour-guides for all of knowledge."- Patrick Ness''')
        conn=connect('books.db')

        cur=conn.cursor()


        cur.execute("UPDATE books set status='Issue' where bid=(?)",BIDentry.get())        
        
        

        conn.commit()
        conn.close()

        # Reseting the values
        BIDentry.delete(0,END)
        dateentry.delete(0,END)

isu = Tk()
isu.title("BOOK MANAGEMENT SYSTEM -ISSUE BOOK")
isu.geometry("925x500+300+200")
isu.configure(bg='#fff')



label = Label(text="                                                                                                         ISSUE BOOK                                                                                                                          ", fg="black", bg="orange", font=("Microsoft Yahei UI Light", 9))
label.place(x=0, y=40)


headingFrame1 = Frame(isu,bg="#fdce68",bd=5)
headingFrame1.place(relx=0.15,rely=0.35,relwidth=0.7,relheight=0.55)

head_label=Label(headingFrame1,font="Aharoni 18 bold",text="Enter Book Details").place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.1)

BID=Label(isu,text="Book ID",font="Aharoni 12 bold").place(relx=0.2,rely=0.53, relwidth=0.2,relheight=0.08)
date=Label(isu,text="Date of Issue",font="Aharoni 12 bold").place(relx=0.2,rely=0.63, relwidth=0.2,relheight=0.08)

BIDvalue=StringVar()

datevalue= StringVar()
datevalue.set(" DD/MM/YYYY")


BIDentry=Entry(isu,text="Name",font="Aharoni 12 ",textvariable=BIDvalue)
BIDentry.place(relx=0.45,rely=0.53, relwidth=0.25,relheight=0.08)


dateentry=Entry(isu,font="Aharoni 12 ",textvariable=datevalue)
dateentry.place(relx=0.45,rely=0.63, relwidth=0.25,relheight=0.08)


Issue=Button(isu,text="issue book",borderwidth=2,relief=SUNKEN,font="Aharoni 12 bold ",bg='orange')
Issue.place(relx=0.25,rely=0.77, relwidth=0.2,relheight=0.1)
quitBtn = Button(isu,text="Quit",command=isu.destroy,borderwidth=2,relief=SUNKEN,font="Aharoni 12 bold",bg='orange')
quitBtn.place(relx=0.6,rely=0.77, relwidth=0.18,relheight=0.09)

st_var=StringVar()
st_var.set('''"Librarians are tour-guides for all of knowledge."- Patrick Ness''')
status_br=Label(isu,textvariable=st_var,borderwidth=10,font="Aharoni 12 bold",bg='white')
status_br.place(relx=0.0,rely=0.95, relwidth=1.0,relheight=0.05)





isu.mainloop()