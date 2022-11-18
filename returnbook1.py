from tkinter import*
from tkinter import messagebox



    

def ret():    
    def lelo():
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
    
    rt = Tk()
    rt.title("BOOK MANAGEMENT SYSTEM -RETURN BOOK")
    rt.geometry("925x500+300+200")
    rt.configure(bg='#fff')



    label = Label(text="                                                                                                         RETURN BOOK                                                                                                                          ", fg="black", bg="orange", font=("Microsoft Yahei UI Light", 9))
    label.place(x=0, y=40)


    headingFrame1 = Frame(rt,bg="#fdce68",bd=5)
    headingFrame1.place(relx=0.15,rely=0.35,relwidth=0.7,relheight=0.55)

    head_label=Label(headingFrame1,font="Aharoni 18 bold",text="Enter Book Details").place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.1)


    gender=Label(rt,text="Book ID",font="Aharoni 12 bold").place(relx=0.2,rely=0.53, relwidth=0.2,relheight=0.08)
    Age=Label(rt,text="Fine (if any)",font="Aharoni 12 bold").place(relx=0.2,rely=0.63, relwidth=0.2,relheight=0.08)

    BIDvalue=StringVar()
    finevalue=IntVar()


    BIDentry=Entry(rt,text="Name",font="Aharoni 12 ",textvariable=BIDvalue)
    BIDentry.place(relx=0.45,rely=0.53, relwidth=0.25,relheight=0.08)


    fineentry=Entry(rt,text="Name",font="Aharoni 12 bold",textvariable=finevalue)
    fineentry.place(relx=0.45,rely=0.63, relwidth=0.25,relheight=0.08)

    Return = Button(rt, text="Return",borderwidth=4,relief=SUNKEN,font="Aharoni 12 bold",bg='orange',command=lelo)
    Return.place(relx=0.25,rely=0.77, relwidth=0.2,relheight=0.1)
    quitBtn = Button(rt,text="Quit",borderwidth=4,relief=SUNKEN,font="Aharoni 12 bold",bg='orange',command=rt.destroy)
    quitBtn.place(relx=0.6,rely=0.77, relwidth=0.18,relheight=0.09)

        
    status_br=Label(rt,text='''"When in doubt go to the library." - J.K Rowling''',borderwidth=10,font="Aharoni 12 bold",bg='white')
    status_br.place(relx=0.0,rely=0.95, relwidth=1.0,relheight=0.05)

    st_var=StringVar()
    st_var.set('''"When in doubt go to the library." - J.K Rowling''')
    status_br=Label(rt,textvariable=st_var,borderwidth=10,font="Aharoni 12 bold",bg='white')
    status_br.place(relx=0.0,rely=0.95, relwidth=1.0,relheight=0.05)




    rt.mainloop()

    