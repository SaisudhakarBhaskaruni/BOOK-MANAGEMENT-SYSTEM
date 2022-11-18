from msilib.schema import CheckBox
from tkinter import *
from sqlite3 import *




def avlbooks(root):
    #root.destroy()
    avl =Tk()
    avl.title("BOOK MANAGEMENTS SYSTEM-available books")
    avl.geometry("925x500+300+200")
    avl.configure(bg='#fff')


    


    headingFrame1 = Frame(avl,bg="#FFBB00",bd=5) 
    headingFrame1.place(relx=0.28,rely=0.24,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Available Books", bg='black', fg='white', font = "Courier 18 bold")
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(avl,bg='#fbd5b1')
    labelFrame.place(relx=0.13,rely=0.39,relwidth=0.8,relheight=0.5)
    y = 0.25
    Label(labelFrame, text="%-15s%-60s%-90s%-20s"%('BID','Title','Author','Status'),
    bg='orange',fg='white').place(relx=0.07,rely=0.1)

    status_br=Label(avl,text='''"The only thing that you absolutely have to know, is the location of the library." - Alfred Nobel''',borderwidth=10,font="Aharoni 12 bold",bg='white')
    status_br.place(relx=0.0,rely=0.95, relwidth=1.0,relheight=0.05)

   
    
    conn = connect('books.db')
      
    cur = conn.execute('''SELECT * from books where status="Avail" ''')

    for i in cur:
        Label(labelFrame,text="%-15s%-50s%-80s%-10s"%(i[0],i[1],i[2],i[3]) ,bg='#fbd5b1', fg='black').place(relx=0.07,rely=y)
        y += 0.1


    conn.commit()
    conn.close()

    #-------------------------------------------------------------------------------
    quitBtn = Button(avl,text="Quit",bg='#f7f1e3', fg='black',command=avl.destroy,font="Aharoni 16 bold",borderwidth=10)
    quitBtn.place(relx=0.73,rely=0.87, relwidth=0.18,relheight=0.08)
    
   
    avl.mainloop()