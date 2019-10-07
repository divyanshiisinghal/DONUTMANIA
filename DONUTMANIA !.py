##################
## Project #######
## DONUTMANIA####
## Divyanshi #####
## XII - B  ######
##################
from Tkinter import *
from Tkinter import StringVar, IntVar


import pickle
import os

root=Tk()
list=[]
Blists=[]
s=StringVar()
Bs=StringVar()
Total=IntVar()

class fastfood:
    def _init_(self,itemno,itemdet,category,price):
        self.itemno=0
        self.itemdet=""
        self.category=""
        self.prie=0.0
    def readdata(self,a,b,c,d):
        self.itemno=a
        self.itemdet=b
        self.category=c
        self.price=float(d)
    def display(self):
        print "itemno",self.itemno
        print "item det",self.itemdet
        print "category",self.category
        print "price",self.price

class bill:
    def _init_(self,billno,itemno,itemdet,category,price,quantity,amount):
        self.billno=0
        self.itemno=0
        self.itemdet=""
        self.category=""
        self.price=0.0
        self.quantity=0
        self.amount=0.0
    def readdata(self,bt,a,b,c,d,e):
        self.billno=bt
        self.itemno=a
        self.itemdet=b
        self.category=c
        self.price=float(d)
        self.quantity=int(e)
        self.amount=self.price*self.quantity
    def display(self):
        print "billno",self.billno
        print "itemno",self.itemno
        print "item det",self.itemdet
        print "category",self.category
        print "price",self.price
        print "quantity",self.quantity
        print "amount",self.amount

    
def addfile(E1,E2,E3,E4):
    f=fastfood()
    f.readdata(E1,E2,E3,E4)
    f.display()
    file1=open("menudet.dat","a")
    pickle.dump(f,file1)
    file1.close()

###############################################3
def convert():
    f=fastfood()
    file1=open("menudet.dat","r")
    try:
        while True:
            f=pickle.load(file1)
            s=f.itemdet+"\t"+f.category+"\t"+str(f.price)
            list.append(s)
    except EOFError:
        file1.close()
        return;
       

##########################################
def delfile(E1):
    f=fastfood()
    file1=open("menudet.dat","r")
    file2=open("temp.dat","w")
    try:
        while True:
            f=pickle.load(file1)
            f.display()
            if f.itemno==E1:
                print "deleted"
            else:
                pickle.dump(f,file2)
    except EOFError:
        file1.close()
        file2.close()
        os.remove("menudet.dat")
        os.rename("temp.dat","menudet.dat")
######################################################

def modifyfile(E1,E2,E3,E4):
    f=fastfood()
    file1=open("menudet.dat","r")
    file2=open("temp.dat","w")
    try:
        while True:
            f=pickle.load(file1)
            f.display()
            if f.itemno==E1:
                f=fastfood()
                f.readdata(E1,E2,E3,E4)
                f.display()
                pickle.dump(f,file2)
                print "modified"
            else:
                pickle.dump(f,file2)
    except EOFError:
        file1.close()
        file2.close()
        os.remove("menudet.dat")
        os.rename("temp.dat","menudet.dat")
    
    file1.close()
#####################################################
def clear_file(fileadd):
    fileadd.destroy()
    addmenu()
####################################################
def close_add(fileadd):
    fileadd.destroy()
####################################################
def addmenu():
    fileadd = Toplevel(root,bg='#95056A', height=600, width=600)
    L1 = Label(fileadd, text="Item Number",bg='#E3A9FE' ,justify=LEFT)
    L1.grid(row=0, column=0)
    E1 = Entry(fileadd, width=40)
    E1.grid(row=0,column=1)
    L2 = Label(fileadd, text="Item Description",bg='#E3A9FE' , justify=LEFT)
    L2.grid(row=1,column=0)
    E2 = Entry(fileadd, width=40)
    E2.grid(row=1,column=1)
    L3 = Label(fileadd, text="Item category",bg='#E3A9FE' , justify=LEFT)
    L3.grid(row=2, column=0)
    E3 = Entry(fileadd, width=40)
    E3.grid(row=2, column=1)
    L4 = Label(fileadd, text="Price(in Rs)", bg='#E3A9FE' ,justify=LEFT)
    L4.grid(row=3, column=0)
    E4 = Entry(fileadd,  width=40)
    E4.grid(row=3, column=1)
    button1 = Button(fileadd, text="Save",bg='#E3A9FE' ,activebackground="pink", command=lambda: addfile(E1.get(),E2.get(),E3.get(),E4.get()))
    button1.grid(row=5, column=0)
    button2= Button(fileadd, text="Reset", bg='#E3A9FE' ,activebackground="pink",command= lambda: clear_file(fileadd))
    button2.grid(row=5, column=1)
    button3=Button(fileadd, text="Exit",bg='#E3A9FE' , activebackground='#FF2020',command= lambda: close_add(fileadd))
    button3.grid(row=5,column=2)
           
    #Toplevel.mainloop

##########################################3
def clear_button(fileedirt):
    fileedit.destroy()
    ediemenu()
##########################################
def close_edit(fileedit):
    fileedit.destroy()
############################################
   
def delmenu():
    filewin = Toplevel(root,bg='#95056A')
    L1 = Label(filewin, text="Item Number",bg='#E3A9FE' ,justify=LEFT)
    L1.grid(row=0, column=0)
    E1 = Entry(filewin, width=40)
    E1.grid(row=0,column=1)
    button4 = Button(filewin, text="Check", bg='#E3A9FE',activebackground="pink",command=lambda: delfile(E1.get()))
    button4.grid(row=0, column=2)
    

############################
def editmenu():
    fileadd = Toplevel(root,bg='#95056A', height=600, width=600)
    L1 = Label(fileadd, text="Item Number", bg='#E3A9FE',justify=LEFT)
    L1.grid(row=0, column=0)
    E1 = Entry(fileadd, width=40)
    E1.grid(row=0,column=1)
    L2 = Label(fileadd, text="Item Description", bg='#E3A9FE',justify=LEFT)
    L2.grid(row=1,column=0)
    E2 = Entry(fileadd, width=40)
    E2.grid(row=1,column=1)
    L3 = Label(fileadd, text="Item category", bg='#E3A9FE',justify=LEFT)
    L3.grid(row=2, column=0)
    E3 = Entry(fileadd, width=40)
    E3.grid(row=2, column=1)
    L4 = Label(fileadd, text="Price(in Rs)",bg='#E3A9FE', justify=LEFT)
    L4.grid(row=3, column=0)
    E4 = Entry(fileadd,  width=40)
    E4.grid(row=3, column=1)
    button1 = Button(fileadd, text="Save", bg='#E3A9FE',activebackground="pink",command=lambda: modifyfile(E1.get(),E2.get(),E3.get(),E4.get()))
    button1.grid(row=5, column=0)
    button2= Button(fileadd, text="Reset",bg='#E3A9FE',activebackground="pink", command=lambda: clear_edit(fileadd))
    button2.grid(row=5, column=1)
    button3=Button(fileadd, text="Exit", bg='#E3A9FE',activebackground='#FF2020',command= lambda: close_edit(fileadd))
    button3.grid(row=5,column=2)

##################################
def close_window(filem):
    filem.destroy()

##################################
def close_edit2(fileedit):
    fileedit.destroy()
    
################################
def showmenu():
    lists = []
    s=StringVar()
    a=0
    infile = open('menudet.dat', 'r')
    f=fastfood()
    while 1:
        try:
            f=pickle.load(infile)
            lists.append("     "+f.itemno+"                         "+f.itemdet+"                             "+f.category+"               "+str(f.price))
            
        except EOFError:
            break
    infile.close()
   
    filem = Toplevel(root)
    
    Ls=Listbox(filem, width=55, height=20,bg='#FFF9AA',font="Jokerman")
    
    Ls.pack(side=BOTTOM)
    Ls.insert(END, "                          Menu Card")
    Ls.insert(END," ")
    Ls.insert(END,"ItemNo.          Item Description            Category            Price")
    p="Menu Card\n"
    for i in lists:
       p=p+'\n'+i
       Ls.insert(END,i)

    s.set(p)
    Ls.pack()
    button=Button(filem, text="Click to close",activebackground='#FF2020', command=lambda: close_window(filem))
    button.pack()
    
  
       
    
    
    
      
            
   
 ###########################################################   
    

def showdonut():
    lists = []
    s=StringVar()
    a=0
    infile = open('menudet.dat', 'r')
    f=fastfood()
    while 1:
        try:
            f=pickle.load(infile)
            if f.category=="Donut":
                lists.append("    "+f.itemno+"                     "+f.itemdet+"                              "+f.category+"                  "+str(f.price))
                
                
        except EOFError:
            break
    infile.close()
   
    filem = Toplevel(root)
    
    Ls=Listbox(filem , width=55, height=20,bg='#FFF9AA',font="Jokerman")
    Ls.pack(side=BOTTOM)
    Ls.insert(END, "                      Menu Card(Donut)")
    Ls.insert(END,"  ")
    Ls.insert(END,"ItemNo.          Item Description            Category            Price")
    p="Menu Card\n"
    for i in lists:
       p=p+'\n'+i
       Ls.insert(END,i)

    s.set(p)
    Ls.pack()
    button=Button(filem, text="Click to close",activebackground='#FF2020',  command=lambda: close_window(filem))
    button.pack()
####################################    

def showbeverages():
    lists = []
    s=StringVar()
    a=0
    infile = open('menudet.dat', 'r')
    f=fastfood()
    while 1:
        try:
            f=pickle.load(infile)
            if f.category=="Beverages":
                lists.append("    "+f.itemno+"                       "+f.itemdet+"                                "+f.category+"                      "+str(f.price))
        except EOFError:
            break
    infile.close()
   
    filem = Toplevel(root)
    
    Ls=Listbox(filem, width=55, height=20,bg='#FFF9AA',font="Jokerman")
    Ls.pack(side=BOTTOM)
    Ls.insert(END, "                        Menu Card(Beverages)")
    Ls.insert(END,"  ")
    Ls.insert(END,"Item No.              Item Description               Category                 Price")

    p="Menu Card\n"
    for i in lists:
       p=p+'\n'+i
       Ls.insert(END,i)

    s.set(p)
    Ls.pack()
    button=Button(filem, text="Click to close",activebackground='#FF2020',  command=lambda: close_window(filem))
    button.pack()
####################################################
def insert_bill(fileord,E1,E2,E3):
    fileord.destroy()
    b=bill()
    f=fastfood()
    infile=open("menudet.dat","r")
    idt=" "
    ct=" "
    pr=0.0
    while 1:
        try:
            f=pickle.load(infile)
            if f.itemno==E2:
                idt=f.itemdet
                ct=f.category
                pr=f.price
        except EOFError:
            break
    infile.close()
    b.readdata(E1,E2,idt,ct,pr,E3)
    b.display()
    file2=open("bill.dat","a")
    pickle.dump(b,file2)
    file2.close()
############################################################    

def takeorder():
    fileord = Toplevel(root,bg='#048851', height=400, width=400)
    L1 = Label(fileord, text="Bill Number",bg='#0DE149' ,justify=LEFT)
    L1.grid(row=0, column=0)
    E1 = Entry(fileord, width=40)
    E1.grid(row=0, column=1)
    L2=Label(fileord, text="Item Number", bg='#0DE149' ,justify=LEFT)
    L2.grid(row=1, column=0)
    E2=Entry(fileord,width=40)
    E2.grid(row=1,column=1)
    L3=Label(fileord, text="Quantity ", bg='#0DE149' ,justify=LEFT)
    L3.grid(row=2,column=0)
    E3=Entry(fileord,width=40)
    E3.grid(row=2,column=1)
    button = Button(fileord, text="Add in the Bill",bg='#0DE149' , command=lambda: insert_bill(fileord,E1.get(),E2.get(),E3.get()))
    button.grid(row=4, column=1)

##############################################
def delete_bill(fileord,E1,E2):
    fileord.destroy()
    b=bill()
    file1=open("bill.dat","r")
    file2=open("temp.dat","w")
    try:
        while True:
            b=pickle.load(file1)
            b.display()
            if b.itemno==E2 and b.billno==E1:
                print "deleted"
            else:
                pickle.dump(b,file2)
    except EOFError:
        file1.close()
        file2.close()
        os.remove("bill.dat")
        os.rename("temp.dat","bill.dat")

##################################################

def modify_bill(fileord,E1,E2,E3):
    fileord.destroy()
    b=bill()
    file1=open("bill.dat","r")
    file2=open("temp.dat","w")
    try:
        while True:
            b=pickle.load(file1)
            b.display()
            if b.itemno==E2 and b.billno==E1:
                b1=bill()
                b.readdata(E1,E2,b.itemdet,b.category,b.price,E3)
                b.display()
                pickle.dump(b,file2)
                print "modified"
            else:
                pickle.dump(b,file2)
    except EOFError:
        file1.close()
        file2.close()
        os.remove("bill.dat")
        os.rename("temp.dat","bill.dat")
    
    file1.close()
    
##################################################
def modifyorder():
    fileord = Toplevel(root,bg='#048851', height=400, width=400)
    L1 = Label(fileord, text="Bill Number",bg='#0DE149', justify=LEFT)
    L1.grid(row=0, column=0)
    E1 = Entry(fileord, width=40)
    E1.grid(row=0, column=1)
    L2=Label(fileord, text="Item Number", bg='#0DE149',justify=LEFT)
    L2.grid(row=1, column=0)
    E2=Entry(fileord,width=40)
    E2.grid(row=1,column=1)
    L3=Label(fileord, text="Quantity ", bg='#0DE149',justify=LEFT)
    L3.grid(row=2,column=0)
    E3=Entry(fileord,width=40)
    E3.grid(row=2,column=1)
    button = Button(fileord, text="Modify item in the Bill",bg='#0DE149', command=lambda: modify_bill(fileord,E1.get(),E2.get(),E3.get()))
    button.grid(row=4, column=1)

###################################################################
def cancelorder():
    fileord = Toplevel(root,bg='#048851',  height=400, width=400)
    L1 = Label(fileord, text="Bill Number",bg='#0DE149', justify=LEFT)
    L1.grid(row=0, column=0)
    E1 = Entry(fileord, width=40)
    E1.grid(row=0, column=1)
    L2=Label(fileord, text="Item Number", bg='#0DE149',justify=LEFT)
    L2.grid(row=1, column=0)
    E2=Entry(fileord,width=40)
    E2.grid(row=1,column=1)
    button = Button(fileord, text="Cancel the item from bill", bg='#0DE149',command=lambda: delete_bill(fileord,E1.get(),E2.get()))
    button.grid(row=4, column=1)
    

###############################################

def print_window2(filebp):
    filebp.destroy()

def P_Bill(E1):
    Blists = []
    Bs=StringVar()
    y=0
    billfile = open("bill.dat", "r")
    Bobj=bill()
    Blists.append("Item Number   Item Description                   Price         Quantity         Amount")
    Total=0
    while 1:
        try:
            Bobj=pickle.load(billfile)
            if Bobj.billno==E1:
                Bs="       "+Bobj.itemno
                Bs=Bs+"                "+Bobj.itemdet
                Bs=Bs+"                   "+str(Bobj.price)
                Bs=Bs+"                   "+str(Bobj.quantity)
                Bs=Bs+"                   "+str(Bobj.amount)
                Blists.append(Bs)
                Total=Total+Bobj.amount
        except EOFError:
            break
    billfile.close()
    Blists.append(" ")
    Bs="                               Total Amount :  "+str(Total)
    Blists.append(Bs)
    filebp = Toplevel(root)
    
    Ls=Listbox(filebp, width=70, height=20,bg='#77FFAE',font="Harrington")
    Ls.pack(side=BOTTOM)
    Ls.insert(END, "                                   Bill")
    Ls.insert(END," ")
    Ls.insert(END,"                        Bill Generated By Divyanshi")
    Ls.insert(END," ")
    p=" "
    for i in Blists:
       p=p+'\n'+i
       Ls.insert(END,i)

    s.set(p)
    Ls.pack()
    button=Button(filebp, text="Click to Print", command=lambda: print_window2(filebp))
    button.pack()

##############################################
def Print_bill(filebill,E1):
    filebill.destroy()
    P_Bill(E1)

############################################


def printbill():
    filebill = Toplevel(root,bg='#048851',  height=400, width=400)
    L1 = Label(filebill, text="Bill Number",bg='#0DE149', justify=LEFT)
    L1.grid(row=0, column=0)
    E1 = Entry(filebill, width=40)
    E1.grid(row=0, column=1)
    button = Button(filebill, text="Print the Bill", bg='#0DE149',command=lambda: Print_bill(filebill,E1.get()))
    button.grid(row=0, column=3)
   
###############################################
def close_window2(fileq):
    fileq.destroy()
##############################################
def search(E1):
    lists = []
    s=StringVar()
    a=0
    infile = open('menudet.dat', 'r')
    f=fastfood()
    while 1:
        try:
            f=pickle.load(infile)
            if f.itemno==E1:
                lists.append("Item Number     :          "+f.itemno)
                lists.append("Item Descritpion:          "+f.itemdet)
                lists.append("Item Category   :          "+f.category)
                lists.append("Item Price      :          "+str(f.price))
                lists.append(" ")
                
        except EOFError:
            break
    infile.close()
   
    fileq = Toplevel(root)
    
    Ls=Listbox(fileq, width=50, height=20,bg='#FFC96A',font="Centaur")
    Ls.pack(side=BOTTOM)
    Ls.insert(END, "                Query on Item Number")
    p="Query on Item Number\n"
    for i in lists:
       p=p+'\n'+i
       Ls.insert(END,i)
       

    s.set(p)
    Ls.pack()
    button=Button(fileq, text="Click to close", command=lambda: close_window2(fileq))
    button.pack()

##############################################
def search_item(fileqry,E1):
    fileqry.destroy()
    search(E1)
################################################

def query2(E1):
    lists = []
    s=StringVar()
    a=0
    infile = open('bill.dat', 'r')
    b=bill()
    while 1:
        try:
            b=pickle.load(infile)
            if b.billno==E1:
                lists.append("Item Number     :          "+b.itemno)
                lists.append("Item Descritpion:          "+b.itemdet)
                lists.append("Item Category   :          "+b.category)
                lists.append("Item Price      :          "+str(b.price))
                lists.append("Item Amount     :          "+str(b.amount))
                lists.append(" ")
        except EOFError:
            break
    infile.close()
   
    fileq = Toplevel(root)
    
    Ls=Listbox(fileq, width=50, height=20,bg='#FFC96A',font="Centaur")
    Ls.pack(side=BOTTOM)
    Ls.insert(END, "                Query on Bill Number")
    p="Query on Bill Number\n"
    for i in lists:
       p=p+'\n'+i
       Ls.insert(END,i)
       

    s.set(p)
    Ls.pack()
    button=Button(fileq, text="Click to close", command=lambda: close_window2(fileq))
    button.pack()
    

#######################################################
def search2(fileqry,E1):
    fileqry.destroy()
    query2(E1)
########################################################

def queryb():
    fileqry = Toplevel(root,bg='#E42600', height=400, width=400)
    L1 = Label(fileqry, text="Bill Number",bg='#FF9A51' ,justify=LEFT)
    L1.grid(row=0, column=0)
    E1 = Entry(fileqry, width=40)
    E1.grid(row=0, column=1)
    button = Button(fileqry, text="Search",bg='#FF9A51' , command=lambda: search2(fileqry,E1.get()))
    button.grid(row=0, column=2)
########################################################
def query():
    fileqry = Toplevel(root,bg='#E42600', height=400, width=400)
    L1 = Label(fileqry, text="Item Number",bg='#FF9A51' , justify=LEFT)
    L1.grid(row=0, column=0)
    E1 = Entry(fileqry, width=40)
    E1.grid(row=0, column=1)
    button = Button(fileqry, text="Search",bg='#FF9A51' , command=lambda: search_item(fileqry,E1.get()))
    button.grid(row=0, column=2)
   
########################################

def Exit():
    root.destroy()


#root = Tk()
menubar=Menu(root)
filemenu=Menu(menubar,bg='#B2684D',font="Andalus",tearoff=0)
filemenu.add_command(label="Add Menu",activebackground='#553823',command= addmenu)
filemenu.add_command(label="Delete Menu",activebackground='#553823',command=delmenu)
filemenu.add_command(label="Edit Menu",activebackground='#553823',command=editmenu)
filemenu.add_separator()
filemenu.add_command(label="Exit",activebackground='#CA1025', command=Exit)
menubar.add_cascade(label="Order",menu=filemenu)
fileshow=Menu(menubar,bg='#B2684D',font="Andalus",tearoff=0)
fileshow.add_command(label="Show All",activebackground='#553823',command=showmenu)
fileshow.add_separator()
fileshow.add_command(label="Show DONUTS",activebackground='#553823',command=showdonut)
fileshow.add_command(label="Show BEVERAGES",activebackground='#553823',command=showbeverages)
menubar.add_cascade(label="Menu Card", menu=fileshow)
filebill=Menu(menubar,bg='#B2684D',font="Andalus",tearoff=0)
filebill.add_command(label="Take order",activebackground='#553823',command=takeorder)
filebill.add_command(label="Cancel order",activebackground='#553823',command=cancelorder)
filebill.add_command(label="Modify order",activebackground='#553823',command=modifyorder)
filebill.add_separator()
filebill.add_command(label="Print bill",activebackground='#CA1025',command=printbill)
menubar.add_cascade(label="Bill", menu=filebill)
filereport=Menu(menubar,bg='#B2684D',font="Andalus",tearoff=0)
filereport.add_command(label="Query on item",activebackground='#553823',command=query)
filereport.add_command(label="Query on bill",activebackground='#553823',command=queryb)
menubar.add_cascade(label="Query", menu=filereport)
var1 = StringVar()
label = Message( root, textvariable=var1,font="Algerian",fg='#36210B',bg='#DFB183', bd=275,anchor=CENTER,relief=RAISED )
var1.set("      *^*DonutMANIA*^* \nby !Divyanshi Singhal! \n                ^XII-B^")
label.pack()
root.config(menu=menubar,bg='#894E2F')
root.mainloop()
