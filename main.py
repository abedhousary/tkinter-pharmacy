from tkinter import *
import mysql.connector

class phar:
    def __init__(self):
        self.cn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database = "pharmacy"
        )
        self.cr = self.cn.cursor()
    def clear(self):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
    def upda (self):
        quan = e3.get()
        mon = e4.get()
        id = e1.get()
        self.cr.execute("update meds set soldmoney = soldmoney +  %s , quantity =quantity -  %s  where id = %s",(mon,quan,id))
        self.cn.commit()
    def sell(self):
        name = e2.get()
        price = e4.get()
        quan = e3.get()
        self.cr.execute(
            "insert into sells (name,price,quan) values (%s,%s,%s) ", (name, price,quan))
        self.cn.commit()
        self.upda()
        lis.delete(0, END)
        self.getdata()
        self.clear()

    def getdata(self):
        self.cr.execute("select id,name,quantity,price from pharmacy.meds")
        fd = self.cr.fetchall()
        for row in fd:
            s2 = "{:>25}{:>40}{:>40}{:>38}".format(row[0], row[1], row[2], row[3])
            lis.insert(END, s2)


main = phar()

root = Tk()
root.title('pharmacy')
width = 1200
height = 900
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw / 2) - (width / 2)
y = (sh / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.config(bg="grey")
lbl = Label(root, text="Pharmacy System", fg="white",
            bg="grey", font=("Arial", 19))

lbl.pack()
root.config(bg="grey")
lbl1 = Label(root, text="ID", fg="white",
             bg="grey", font=("Arial", 15))
lbl2 = Label(root, text="Product Name", fg="white",
             bg="grey", font=("Arial", 15))
lbl3 = Label(root, text="Quantity", fg="white",
             bg="grey", font=("Arial", 15))
lbl4 = Label(root, text="Price", fg="white",
             bg="grey", font=("Arial", 15))

e1 = Entry(root, font=12, justify="center")
e2 = Entry(root, font=12)
e3 = Entry(root, font=12)
e4 = Entry(root, font=12)

btn1 = Button(root, text="SELL", borderwidth=10,
              width=48, height=5, font=10,command = main.sell)
# btn2 = Button(root, text="Update details",
#               borderwidth=10, width=12, height=5, font=10)
# btn3 = Button(root, text="Delete medicine",
#               borderwidth=10, width=12, height=5, font=10)

#second frame
def edit (event):
    selecteddata = lis.get(ACTIVE).split()
    e1.insert(0,selecteddata[0])
    e2.insert(0,selecteddata[1])
    e4.insert(0,selecteddata[3])
    e1.config(state = "readonly")
    e2.config(state = "readonly")
    e4.config(state = "readonly")

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
# btn2.place(x=200, y=480)
# btn3.place(x=380, y=480)

frame1.place(x=590,y=190)
root.mainloop()
