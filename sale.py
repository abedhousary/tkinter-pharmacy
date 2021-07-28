from tkinter import *
import mysql.connector

mon = 0
def sales():
    class db:
        def __init__(self):
            self.cn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pharmacy"
            )
            self.cr = self.cn.cursor()

        def getdata(self):
            global mon
            self.cr.execute("select id,name,price,date from sells")
            fd = self.cr.fetchall()
            for row in fd:
                s2 = "{:^85}{:^40}{:^40}{:^50}".format(row[0], row[1], row[2], str(row[3]))
                mon += float(row[2])
                lis.insert(END, s2)
            e1.insert(0, str(int(mon)))
        def sbyname (self,event):
            mon = 0
            medname = e2.get()
            self.cr.execute("select id,name,price,date from sells where name= %s ",(medname,))
            fd = self.cr.fetchall()
            for row in fd:
                s2 = "{:^85}{:^40}{:^40}{:^50}".format(row[0], row[1], row[2], str(row[3]))
                lis.delete(0,END)
                e1.delete(0,END)
                mon += float(row[2])
                lis.insert(END, s2)
            e1.insert(0, str(int(mon)))

    Db = db()
    root = Tk()
    width = 900
    height = 500
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw / 2) - (width / 2)
    y = (sh / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.config(bg="grey")
    header = "{:^85}{:^40}{:^40}{:^50}".format("Id", "Name", "Price","Date of purchase")
    frame2 = Frame(root, bg = "grey",width = 950 , height = 30)
    frame2.pack()
    lbl = Label(frame2, text="Gains dashboard", bg="grey", font=("fantasy", 18))
    lbl2 = Label(frame2,text = "Search by med name",bg = "grey" )
    e2 = Entry(frame2)
    e2.bind("<Return>",Db.sbyname)
    lbl.place(x=390 , y= 1 )
    lbl2.place(x = 90 , y=5)
    e2.place(x = 220 , y = 5)
    lbl1 = Label(root, text=header, bg="grey")
    sc = Scrollbar(root, orient="vertical")

    lis = Listbox(root, yscrollcommand=sc.set, width=120, height=26)
    sc.config(command=lis.yview)
    frame = Frame(root, height=90, width=850, bg="grey")

    lb = Label(frame,fg="black",bg = "grey",text = "Total Amount",font=(12))
    e1 = Entry(frame)

    lbl1.pack()
    sc.pack(side="right", fill="y")
    lis.pack()
    frame.pack(pady=2)
    lb.place(x=490, y=1)
    e1.place(x=620, y=3)

    Db.getdata()
    root.mainloop()

