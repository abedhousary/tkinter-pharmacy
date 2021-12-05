from tkinter import *
import mysql.connector
from addmed import addmed
from sale import sales


class phar:
    def __init__(self):
        self.cn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pharmacy"
        )
        self.cr = self.cn.cursor()

    def clear(self):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)

    def upda(self):
        quan = e3.get()
        mon = e4.get()
        id = e1.get()
        self.cr.execute(
            "update meds set soldmoney = soldmoney +  %s , quantity =quantity -  %s  where id = %s", (mon, quan, id))
        self.cn.commit()

    def sell(self):
        name = e2.get()
        price = e5.get()
        quan = e3.get()
        receipt = (int(e4.get()) * int(e3.get()))
        self.cr.execute(
            "insert into sells (name,price,quan,beforetax) values (%s,%s,%s,%s * %s ) ", (name, receipt, quan, e4.get(), quan))
        self.cn.commit()
        self.upda()
        lis.delete(0, END)
        self.getdata()
        self.clear()

    def getdata(self):
        self.cr.execute("select id,name,quantity,price from pharmacy.meds")
        fd = self.cr.fetchall()
        for row in fd:
            s2 = "{:>25}{:>40}{:>40}{:>38}".format(
                row[0], row[1], row[2], row[3])
            lis.insert(END, s2)

    def refresh(self):
        lis.delete(0, END)
        self.getdata()


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


root.config(bg="grey")
lbl1 = Label(root, text="ID", fg="white",
             bg="grey", font=("Arial", 15))
lbl2 = Label(root, text="Product Name", fg="white",
             bg="grey", font=("Arial", 15))
lbl3 = Label(root, text="Quantity", fg="white",
             bg="grey", font=("Arial", 15))
lbl4 = Label(root, text="Price", fg="white",
             bg="grey", font=("Arial", 15))
lbl5 = Label(root, text="vat 11%", fg="white",
             bg="grey", font=("Arial", 15))

e1 = Entry(root, font=12, justify="center")
e2 = Entry(root, font=12)
e3 = Entry(root, font=12)
e4 = Entry(root, font=12)
e5 = Entry(root, font=12)

btn1 = Button(root, text="SELL", borderwidth=10,
              width=45, height=5, font=10, command=main.sell)
btn2 = Button(root, text="ADD MED", width=14, font=7, command=addmed)
btn3 = Button(root, text="SALES", width=14, font=7, command=sales)
btn4 = Button(root, text="Refresh", width=14, font=7, command=main.refresh)


def edit(event):
    main.clear()
    selecteddata = lis.get(ACTIVE).split()
    e1.insert(0, selecteddata[0])
    e2.insert(0, selecteddata[1])
    e4.insert(0, selecteddata[3])
    e1.config(state="readonly")
    e2.config(state="readonly")
    e4.config(state="readonly")


def calc(event):
    cal = int(e3.get()) * int(e4.get())
    priceaftertax = cal * 0.025 + cal
    e5.delete(0, END)
    e5.insert(0, priceaftertax)


frame1 = Frame(root, bg="white", height=435, width=600)
sc = Scrollbar(frame1, orient="vertical")
sc.pack(side="right", fill="y")
lis = Listbox(frame1, width=95, height=27, yscrollcommand=sc.set)
lis.bind('<Double-1>', edit)
sc.config(command=lis.yview)
headers = "{:<30}{:<30}{:^30}{:^30}".format(
    "ID", "Prodcut name", "quantity", "Price")
lb = Label(frame1, text=headers, bg="white")
lb.pack()
lis.pack()
main.getdata()

lbl.place(x=430, y=40)
lbl1.place(x=40, y=200)
lbl2.place(x=40, y=270)
lbl3.place(x=40, y=340)
lbl4.place(x=40, y=410)
lbl5.place(x=40, y=470)

e1.place(x=210, y=200)
e2.place(x=210, y=275)
e3.place(x=210, y=340)
e3.bind("<Return>", calc)
e4.place(x=210, y=410)
e5.place(x=210, y=470)

btn1.place(x=20, y=520)
btn2.place(x=1020, y=140)
btn3.place(x=820, y=140)
btn4.place(x=620, y=140)

frame1.place(x=590, y=190)
root.mainloop()
