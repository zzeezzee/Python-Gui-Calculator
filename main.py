from tkinter import *

# ===================================================
def button_click(xyz):
    abc = a.get()
    a.delete(0,END)
    a.insert(0,str(abc) + str(xyz))


def clear():
    a.delete(0,END)


def add():
    num_1 = a.get()
    global num
    global work
    num = int(num_1)
    work = "add"
    a.delete(0,END)

def multi():
    num_1 = a.get()
    global num
    global work
    num = int(num_1)
    work = "multi"
    a.delete(0, END)
def divi():
    num_1 = a.get()
    global num
    global work
    num = int(num_1)
    work = "divi"
    a.delete(0, END)

def sub():
    num_1 = a.get()
    global num
    global work
    num = int(num_1)
    work = "sub"
    a.delete(0, END)

def equal():
    num_2 = a.get()
    a.delete(0,END)

    if work == "add":
        a.insert(0,num + int(num_2))

    if work == "multi":
        a.insert(0,num * int(num_2))

    if work == "sub":
        a.insert(0,num - int(num_2))

    if work == "divi":
        a.insert(0,num / int(num_2))



# =======================================================
root = Tk()

root.title("Wrost Calculator")
root.resizable(False,False)
root.configure(bg="gray")

photo = PhotoImage(file="ico.png")
root.iconphoto(False,photo)


a = Entry(root, font=('','30','bold'), bg="lightblue", fg="red", justify="left",bd=40)
a.grid(columnspan=4)


buttton_1 = Button(root, font=('','30','bold'), bg="red", fg="black",text="1",bd=14 , padx=20,pady=10,activebackground="black", activeforeground="red",command=lambda:button_click(1))
buttton_1.grid(row=1,column=0)

buttton_2 = Button(root, font=('','30','bold'), bg="red", fg="black",text="2",bd=14, padx=20,pady=10,activebackground="black", activeforeground="red",command=lambda:button_click(2))
buttton_2.grid(row=1,column=1)

buttton_3 = Button(root, font=('','30','bold'), bg="red", fg="black",text="3",bd=14, padx=20,pady=10,activebackground="black", activeforeground="red",command=lambda:button_click(3))
buttton_3.grid(row=1,column=2)

buttton_4 = Button(root, font=('','30','bold'), bg="red", fg="black",text="4",bd=14, padx=20,pady=10,activebackground="black", activeforeground="red",command=lambda:button_click(4))
buttton_4.grid(row=2,column=0)

buttton_5 = Button(root, font=('','30','bold'), bg="red", fg="black",text="5",bd=14, padx=20,pady=10,activebackground="black", activeforeground="red",command=lambda:button_click(5))
buttton_5.grid(row=2,column=1)

buttton_6 = Button(root, font=('','30','bold'), bg="red", fg="black",text="6",bd=14, padx=20,pady=10,activebackground="black", activeforeground="red",command=lambda:button_click(6))
buttton_6.grid(row=2,column=2)

buttton_7 = Button(root, font=('','30','bold'), bg="red", fg="black",text="7",bd=14, padx=20,pady=10,activebackground="black", activeforeground="red",command=lambda:button_click(7))
buttton_7.grid(row=3,column=0)

buttton_8 = Button(root, font=('','30','bold'), bg="red", fg="black",text="8",bd=14, padx=20,pady=10,activebackground="black", activeforeground="red",command=lambda:button_click(8))
buttton_8.grid(row=3,column=1)

buttton_9 = Button(root, font=('','30','bold'), bg="red", fg="black",text="9",bd=14, padx=20,pady=10,activebackground="black", activeforeground="red",command=lambda:button_click(9))
buttton_9.grid(row=3,column=2)

buttton_0 = Button(root, font=('','30','bold'), bg="red", fg="black",text="0",bd=14, padx=20,pady=10 ,activebackground="black", activeforeground="red",command=lambda:button_click(0))
buttton_0.grid(row=4,column=0)

buttton_add = Button(root, font=('','30','bold'), bg="black", fg="red",text="+",bd=14, padx=20,pady=10,activebackground="red", activeforeground="black", command=lambda:add())
buttton_add.grid(row=1,column=3)

buttton_equal = Button(root, font=('','30','bold'), bg="black", fg="red",text="=",bd=14, padx=20,pady=10,activebackground="red", activeforeground="black",command=lambda:equal())
buttton_equal.grid(row=4,column=2)

buttton_clear = Button(root, font=('','30','bold'), bg="black", fg="red",text="c",bd=14, padx=20,pady=10,activebackground="red", activeforeground="black",command=lambda:clear())
buttton_clear.grid(row=4,column=1)

buttton_multi = Button(root, font=('','30','bold'), bg="black", fg="red",text="x",bd=14, padx=20,pady=10,activebackground="red", activeforeground="black",command=lambda:multi())
buttton_multi.grid(row=3,column=3)

buttton_sub = Button(root, font=('','30','bold'), bg="black", fg="red",text="-",bd=14, padx=25,pady=10,activebackground="red", activeforeground="black",command=lambda:sub())
buttton_sub.grid(row=2,column=3)

buttton_divi = Button(root, font=('','30','bold'), bg="black", fg="red",text="/",bd=14, padx=25,pady=10 , activebackground="red", activeforeground="black",command=lambda:divi())
buttton_divi.grid(row=4,column=3)

root.mainloop()