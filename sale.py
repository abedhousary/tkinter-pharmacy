from tkinter import  *
import mysql.connector

class db :
    def __init__(self):
        self.cn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "pharmacy"
        )
        self.cr = self.cn.cursor()
    def getdata (self):
        self.cr.execute("select id,name,price from sells")
        fd = self.cr.fetchall()
        for row in fd:
            s2 = "{:^85}{:^40}{:^110}".format(row[0],row[1],row[2])
            lis.insert(END,s2)
Db = db()
root = Tk()
width = 800
height = 500
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw / 2 ) - (width / 2)
y = (sh / 2)- (height /  2)
root.geometry("%dx%d+%d+%d"%(width,height,x,y))
root.config(bg="grey")
header = "{:>10}{:^130}{:^30}".format("Id","Name","Price")
lbl = Label(root,text = "Gains dashboard",bg="grey",font = ("fantasy",18))
lbl1 = Label(root,text = header ,bg="grey")
sc = Scrollbar(root,orient = "vertical")

lis = Listbox(root,yscrollcommand = sc.set,width=120,height = 26)
sc.config(command = lis.yview)
lbl.pack()
lbl1.pack()
sc.pack(side="right",fill = "y")
lis.pack()
Db.getdata()
root.mainloop()