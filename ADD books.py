from tkinter import*
from tkinter import messagebox
import os



def add_book(root):
    #root.destroy()
  
  #-----------------------------------------------------------------------------------------
   # submit function 

    def submit():

        st_var.set("Adding Book Information..")
        status_br.update()
        import time
        time.sleep(3)
        messagebox.showinfo("Information","Book Added Succesfully !")
        

        st_var.set("Books are your biggest friend")
        
        conn=connect('books.db')

        cur=conn.cursor()


        cur.execute('''INSERT INTO books VALUES(:bookInfo1 ,:bookInfo2 ,:bookInfo3, :bookInfo4) ''',
              {
            'bookInfo1':bookInfo1.get(),
            'bookInfo2':bookInfo2.get(),
            'bookInfo3':bookInfo3.get(),
            'bookInfo4' : bookInfo4.get()
              }
        )


add = Tk()
add.title('BOOK MANAGEMENT SYSTEM-ADD BOOK')
add.geometry("925x500+300+200")
add.configure(bg='#fff')


    
headingFrame1 = Frame(add,bg="#FCC981",bd=5)
headingFrame1.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.13)
headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font='Arial 20 bold' )
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
labelFrame = Frame(add,bg='#FCC981')
labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.4)


#Book ID
lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
bookInfo1 = Entry(labelFrame)
bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

        
# Title
lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
bookInfo2 = Entry(labelFrame)
bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

        
# Book Author
lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
bookInfo3 = Entry(labelFrame)
bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

# Book Status
lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
bookInfo4 = Entry(labelFrame)
bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)


       
#Submit Button
SubmitBtn = Button(add,text="SUBMIT",bg='#d1ccc0', fg='black',font="Aharoni 16 bold",borderwidth=10)
SubmitBtn.place(relx=0.28,rely=0.8, relwidth=0.18,relheight=0.08)
    
quitBtn = Button(add,text="Quit",bg='#f7f1e3', fg='black',       command=add.destroy,font="Aharoni 16 bold",borderwidth=10)
quitBtn.place(relx=0.73,rely=0.8, relwidth=0.18,relheight=0.08)
    
st_var=StringVar()
st_var.set("Books are your biggest friend ")
status_br=Label(add,textvariable=st_var,borderwidth=10,font="Aharoni 12 bold",bg='white')
status_br.place(relx=0.0,rely=0.95, relwidth=1.0,relheight=0.05)





add.mainloop()