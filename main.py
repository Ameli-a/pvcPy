from tkinter import *

scrSize = "600x470"

def wlcMsg():
    tk = Tk()
    tk.title("Park Vale Chocolates")
    tk.geometry(scrSize)

    title = Label(tk, bg = "#f1faee",fg = "red", text = "Welcome!", font="50")

    title.pack()
    msg = Message(tk, text = "Welcome to a world of chocolate")
    msg.pack(padx = 20, side = "top")
    btn1 = Button(tk, text = "Enter", command= main_menu).place(relx="0.5", y=150, anchor="center", width=300)
    Button(text="Quit",command=lambda: tk.destroy()).place(relx="0.5", y=200, anchor="center", width=300)
    
    tk.mainloop()

#main menu start

def main_menu():
    tk = Tk()
    tk.geometry(scrSize)
    title = Label(tk, text = "Main menu")
    title.grid(row = 2, column = 2)
    msg = Message(tk, text= "Menu selected")
    msg.grid(row = 2, column = 2)
    btn2 = Button(tk, text = "New Customer", command= add_customer).place(relx="0.5", y=150, anchor="center", width=300)
    btn3 = Button(tk, text = "Log in", command= log_in).place(relx="0.5", y=100, anchor="center", width=300)
    btn4 = Button(tk, text = "Order", command= order).place(relx="0.5", y=200, anchor="center", width=300)
    btn4 = Button(tk, text = "Search Order", command= search_order).place(relx="0.5", y=250, anchor="center", width=300)
    
def add_customer():
    scrSize = "400x300"
    tk = Tk()
    tk.geometry(scrSize)
    title = Label(tk, text= "new_customer")
    command= add_customer_screen

def log_in():
    scrSize = "400x300"
    tk = Tk()
    tk.geometry(scrSize)
    title = Label(tk, text= "log_in")

def order():
    scrSize = "400x300"
    tk = Tk()
    tk.geometry(scrSize)
    title = Label(tk, text= "order")

def search_order():
    scrSize = "400x300"
    tk = Tk()
    tk.geometry(scrSize)
    title = Label(tk, text= "search_order")

#main menu end

#add customer start

def add_customer_screen():
    tk = Tk()
    tk.geometry(scrSize)

wlcMsg()
    
