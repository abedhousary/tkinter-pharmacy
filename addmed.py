from tkinter import *
import mysql.connector

def addmed () :
    class phar:
        def __init__(self):
            self.cn = mysql.connector.connect(
                host="localhost",
                user="root",
                password=""
            )
            self.cr = self.cn.cursor()
            self.cr.execute("create database if not exists pharmacy")
            self.cr.execute("""create table if not exists pharmacy.meds (
                        id int primary key auto_increment,
                        name varchar(155),
                        quantity varchar(155),
                        price varchar(155),
                        soldmoney varchar(155)
                        
            ) """)
    
        def clear(self):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
    
        def save(self):
            name = e2.get()
            qua = e3.get()
            price = e4.get()
            self.cr.execute(
                "insert into pharmacy.meds (name,quantity,price,soldmoney) values (%s,%s,%s,%s) ", (name, qua, price, "0"))
            self.cn.commit()
            self.clear()
            lis.delete(0,END)
            self.getdata()
        def update (self):
            self.cr.execute("update pharmacy.meds set name = %s,quantity= %s,price = %s where id = %s ",(e2.get(),e3.get(),e4.get(),e1.get()))
            self.cn.commit()
            self.clear()
            lis.delete(0, END)
            self.getdata()
        def delete(self):
            self.cr.execute("delete from pharmacy.meds where  id = %s ",(e1.get(),))
            self.cn.commit()
            self.clear()
            lis.delete(0, END)
            self.getdata()
        def getdata (self):
            self.cr.execute("select id,name,quantity,price from pharmacy.meds")
            fd = self.cr.fetchall()
            for row in fd:
                s2 ="{:>25}{:>40}{:>40}{:>38}".format(row[0],row[1],row[2],row[3])
                lis.insert(END,s2)
    
    
    main = phar()
    
    root = Tk()
    root.title('Add Med')
    width = 1200
    height = 900
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw / 2) - (width / 2)
    y = (sh / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.config(bg="grey")
    lbl = Label(root, text="Product details", fg="white",
                bg="grey", font=("Arial", 18))
    lbl1 = Label(root, text="ID", fg="white",
                 bg="grey", font=("Arial", 18))
    lbl2 = Label(root, text="Product Name", fg="white",
                 bg="grey", font=("Arial", 18))
    lbl3 = Label(root, text="Quantity", fg="white",
                 bg="grey", font=("Arial", 18))
    lbl4 = Label(root, text="Price", fg="white",
                 bg="grey", font=("Arial", 18))
    
    e1 = Entry(root, font=12, justify="center")
    e2 = Entry(root, font=12)
    e3 = Entry(root, font=12)
    e4 = Entry(root, font=12)
    
    btn1 = Button(root, text="Add medicine", borderwidth=10,
                  width=12, height=5, font=10,command = main.save)
    btn2 = Button(root, text="Update details",
                  borderwidth=10, width=12, height=5, font=10,command = main.update)
    btn3 = Button(root, text="Delete medicine",
                  borderwidth=10, width=12, height=5, font=10,command = main.delete)
    
    #second frame
    def edit (event):
        selecteddata = lis.get(ACTIVE).split()
        e1.insert(0,selecteddata[0])
        e2.insert(0,selecteddata[1])
        e3.insert(0,selecteddata[2])
        e4.insert(0,selecteddata[3])
    
    frame1 = Frame(root,bg="white",height = 435,width=600)
    sc = Scrollbar(frame1,orient = "vertical")
    sc.pack(side= "right",fill = "y")
    lis = Listbox(frame1,width = 95,height = 27,yscrollcommand = sc.set)
    lis.bind('<Double-1>',edit)
    sc.config(command = lis.yview)
    headers = "{:<30}{:<30}{:^30}{:^30}".format("ID","Prodcut name","quantity","Price")
    lb = Label(frame1,text = headers,bg="white")
    lb.pack()
    lis.pack()
    main.getdata()
    
    lbl.place(x=400, y=40)
    lbl1.place(x=40, y=200)
    lbl2.place(x=40, y=270)
    lbl3.place(x=40, y=340)
    lbl4.place(x=40, y=410)
    
    e1.place(x=210, y=200)
    e2.place(x=210, y=275)
    e3.place(x=210, y=340)
    e4.place(x=210, y=410)
    
    btn1.place(x=20, y=480)
    btn2.place(x=200, y=480)
    btn3.place(x=380, y=480)
    
    frame1.place(x=590,y=190)
    root.mainloop()
    