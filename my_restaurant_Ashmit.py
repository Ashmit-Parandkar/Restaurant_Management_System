from tkinter import *
import random
import time
from tkinter import messagebox
from PIL import ImageTk,Image

login_root = Tk()

login_root.geometry("1366x740+0+0")

login_root.resizable(0,0)

login_root.title("LOGIN PAGE")

login_root.config(bg="firebrick4")

global quan_count_2
quan_count_2 = 0
global num_check
num_check = 1

def check_login():
    flag=1
    f = open("logintxt.txt","r")
    for line in f:
        word = line.split()
        if(word[0]==user_name.get() and word[1]==pass_name.get()):
            flag=1
            messagebox.showinfo("Login", "Login Successful !!")
            login_root.destroy()

            root = Tk()

            root.geometry("1366x740+0+0")

            root.resizable(0, 0)

            # print(root.winfo_screenheight())
            # print(root.winfo_screenwidth())

            root.title("Restaurant Management System - By Ashmit")

            root.config(bg="navy")

            global gross_amount
            gross_amount = 0

            def total():
                global quan_count
                global quan_count_2
                global num_check
                global gross_amount
                global gross_ent
                global tax_amount
                global tax_ent
                global total_amount
                global total_ent

                tot = 0
                quan_count_2=0
                num_check = 1

                for i in range(5):
                    quantity = list_tiffins_frame_entries[i].get()
                    if (quantity == ''):
                        quan_count=0
                        quantity = '0'
                    if(quantity.isnumeric() == False):
                        num_check = 0
                        messagebox.showerror("Wrong Value", "Please enter a number")
                        break
                    if (quantity != '0'):
                        quan_count=1
                        quan_count_2=quan_count
                        tot = tot + (int(list_items_tiffins[i][1][0:-2]) * int(quantity))
                for i in range(5):
                    quantity = list_starters_frame_entries[i].get()
                    if (quantity == ''):
                        quan_count = 0
                        quantity = '0'
                    if (quantity.isnumeric() == False):
                        num_check = 0
                        messagebox.showerror("Wrong Value", "Please enter a number")
                        break
                    if (quantity != '0'):
                        quan_count = 1
                        quan_count_2 = quan_count
                        tot = tot + (int(list_items_starters[i][1][0:-2]) * int(quantity))
                for i in range(5):
                    quantity = list_rotis_frame_entries[i].get()
                    if (quantity == ''):
                        quan_count = 0
                        quantity = '0'
                    if (quantity.isnumeric() == False):
                        num_check = 0
                        messagebox.showerror("Wrong Value", "Please enter a number")
                        break
                    if (quantity != '0'):
                        quan_count = 1
                        quan_count_2 = quan_count
                        tot = tot + (int(list_items_rotis[i][1][0:-2]) * int(quantity))
                for i in range(5):
                    quantity = list_maincourse_frame_entries[i].get()
                    if (quantity == ''):
                        quan_count = 0
                        quantity = '0'
                    if (quantity.isnumeric() == False):
                        num_check = 0
                        messagebox.showerror("Wrong Value", "Please enter a number")
                        break
                    if (quantity != '0'):
                        quan_count = 1
                        quan_count_2 = quan_count
                        tot = tot + (int(list_items_maincourse[i][1][0:-2]) * int(quantity))
                for i in range(5):
                    quantity = list_beverages_frame_entries[i].get()
                    if (quantity == ''):
                        quan_count = 0
                        quantity = '0'
                    if (quantity.isnumeric() == False):
                        num_check = 0
                        messagebox.showerror("Wrong Value", "Please enter a number")
                        break
                    if (quantity != '0'):
                        quan_count = 1
                        quan_count_2 = quan_count
                        tot = tot + (int(list_items_beverages[i][1][0:-2]) * int(quantity))
                for i in range(5):
                    quantity = list_desserts_frame_entries[i].get()
                    if (quantity == ''):
                        quan_count = 0
                        quantity = '0'
                    if (quantity.isnumeric() == False):
                        num_check = 0
                        messagebox.showerror("Wrong Value", "Please enter a number")
                        break
                    if (quantity != '0'):
                        quan_count = 1
                        quan_count_2 = quan_count
                        tot = tot + (int(list_items_desserts[i][1][0:-2]) * int(quantity))
                        # print(tot)

                if(quan_count_2 == 0 or num_check == 0):
                    messagebox.showerror("NO ITEM SELECTED","Please Select any item")
                else:
                    gross_amount = tot

                    gross_ent = Entry(amount_frame, borderwidth=5, relief=SUNKEN, width=12, font=("Tahoma", 13, "bold"),
                                      fg="black")
                    gross_ent.insert(0, "₹ " + str(gross_amount) + " /-")
                    gross_ent.config(state=DISABLED)
                    gross_ent.grid(row=0, column=1, padx=10, pady=10)

                    tax_amount = int((8 / 100) * tot)

                    tax_ent = Entry(amount_frame, borderwidth=5, relief=SUNKEN, width=12, font=("Tahoma", 13, "bold"))
                    tax_ent.insert(0, "₹ " + str(tax_amount) + " /-")
                    tax_ent.config(state=DISABLED)
                    tax_ent.grid(row=1, column=1, padx=15, pady=10)

                    total_amount = gross_amount + tax_amount

                    total_ent = Entry(amount_frame, borderwidth=5, relief=SUNKEN, width=12, font=("Tahoma", 13, "bold"))
                    total_ent.insert(0, "₹ " + str(total_amount) + " /-")
                    total_ent.config(state=DISABLED)
                    total_ent.grid(row=2, column=1, padx=15, pady=10)

            def invoice():

                global quan_count
                global quan_count_2
                global num_check
                global gross_amount
                global gross_ent
                global tax_amount
                global tax_ent
                global total_amount
                global total_ent
                global bill_text

                tot = 0
                quan_count_2 = 0
                num_check = 1

                for i in range(5):
                    quantity = list_tiffins_frame_entries[i].get()
                    if (quantity == ''):
                        quan_count = 0
                        quantity = '0'
                    if (quantity.isnumeric() == False):
                        num_check = 0
                        messagebox.showerror("Wrong Value", "Please enter a number")
                        break
                    if (quantity != '0'):
                        quan_count = 1
                        quan_count_2 = quan_count
                        tot = tot + (int(list_items_tiffins[i][1][0:-2]) * int(quantity))
                for i in range(5):
                    quantity = list_starters_frame_entries[i].get()
                    if (quantity == ''):
                        quan_count = 0
                        quantity = '0'
                    if (quantity.isnumeric() == False):
                        num_check = 0
                        messagebox.showerror("Wrong Value", "Please enter a number")
                        break
                    if (quantity != '0'):
                        quan_count = 1
                        quan_count_2 = quan_count
                        tot = tot + (int(list_items_starters[i][1][0:-2]) * int(quantity))
                for i in range(5):
                    quantity = list_rotis_frame_entries[i].get()
                    if (quantity == ''):
                        quan_count = 0
                        quantity = '0'
                    if (quantity.isnumeric() == False):
                        num_check = 0
                        messagebox.showerror("Wrong Value", "Please enter a number")
                        break
                    if (quantity != '0'):
                        quan_count = 1
                        quan_count_2 = quan_count
                        tot = tot + (int(list_items_rotis[i][1][0:-2]) * int(quantity))
                for i in range(5):
                    quantity = list_maincourse_frame_entries[i].get()
                    if (quantity == ''):
                        quan_count = 0
                        quantity = '0'
                    if (quantity.isnumeric() == False):
                        num_check = 0
                        messagebox.showerror("Wrong Value", "Please enter a number")
                        break
                    if (quantity != '0'):
                        quan_count = 1
                        quan_count_2 = quan_count
                        tot = tot + (int(list_items_maincourse[i][1][0:-2]) * int(quantity))
                for i in range(5):
                    quantity = list_beverages_frame_entries[i].get()
                    if (quantity == ''):
                        quan_count = 0
                        quantity = '0'
                    if (quantity.isnumeric() == False):
                        num_check = 0
                        messagebox.showerror("Wrong Value", "Please enter a number")
                        break
                    if (quantity != '0'):
                        quan_count = 1
                        quan_count_2 = quan_count
                        tot = tot + (int(list_items_beverages[i][1][0:-2]) * int(quantity))
                for i in range(5):
                    quantity = list_desserts_frame_entries[i].get()
                    if (quantity == ''):
                        quan_count = 0
                        quantity = '0'
                    if (quantity.isnumeric() == False):
                        num_check = 0
                        messagebox.showerror("Wrong Value", "Please enter a number")
                        break
                    if (quantity != '0'):
                        quan_count = 1
                        quan_count_2 = quan_count
                        tot = tot + (int(list_items_desserts[i][1][0:-2]) * int(quantity))
                        # print(tot)

                if(quan_count_2 == 0 or num_check ==0):
                    messagebox.showerror("NO ITEM SELECTED", "Please Select any item")
                else:
                    gross_amount = tot

                    gross_ent = Entry(amount_frame, borderwidth=5, relief=SUNKEN, width=12, font=("Tahoma", 13, "bold"),
                                      fg="black")
                    gross_ent.insert(0, "₹ " + str(gross_amount) + " /-")
                    gross_ent.config(state=DISABLED)
                    gross_ent.grid(row=0, column=1, padx=10, pady=10)

                    tax_amount = int((8 / 100) * tot)

                    tax_ent = Entry(amount_frame, borderwidth=5, relief=SUNKEN, width=12, font=("Tahoma", 13, "bold"))
                    tax_ent.insert(0, "₹ " + str(tax_amount) + " /-")
                    tax_ent.config(state=DISABLED)
                    tax_ent.grid(row=1, column=1, padx=15, pady=10)

                    total_amount = gross_amount + tax_amount

                    total_ent = Entry(amount_frame, borderwidth=5, relief=SUNKEN, width=12, font=("Tahoma", 13, "bold"))
                    total_ent.insert(0, "₹ " + str(total_amount) + " /-")
                    total_ent.config(state=DISABLED)
                    total_ent.grid(row=2, column=1, padx=15, pady=10)

                    bill_text = Text(bill_frame, borderwidth=2, relief=SUNKEN, width=42, height=19, padx=6)
                    # bill_text.insert(END, "₹ " + str(total_amount) + " /-")
                    bill_text.insert(END,
                                     (" Bill Number - " + str(random.randint(1000, 9999)) + " ").center(42, "*") + "\n\n")
                    bill_text.insert(END, " Date - " + time.ctime().split()[1] + " " + time.ctime().split()[2] + " " +
                                     time.ctime().split()[4] + " \t\t\t  Time - " + time.ctime().split()[3])
                    bill_text.insert(END, '''
******************************************
                       \t\t\t\t\t\t       ITEM     \t  AMOUNT \t QTY.  \tPRICE \n\n''')
                    for i in range(5):
                        quantity = list_tiffins_frame_entries[i].get()
                        if (quantity == ''):
                            quantity = '0'
                        if (quantity != '0'):
                            bill_text.insert(END, list_items_tiffins[i][0].center(19) + " ₹" + list_items_tiffins[i][
                                1] + quantity.center(9) + ("₹" + str(
                                int(quantity) * int(list_items_tiffins[i][1][0:-2])) + "/-").center(8) + "\n")
                    for i in range(5):
                        quantity = list_starters_frame_entries[i].get()
                        if (quantity == ''):
                            quantity = '0'
                        if (quantity != '0'):
                            bill_text.insert(END, list_items_starters[i][0].center(19) + " ₹" + list_items_starters[i][
                                1] + quantity.center(8) + ("₹" + str(
                                int(quantity) * int(list_items_starters[i][1][0:-2])) + "/-").center(8) + "\n")
                    for i in range(5):
                        quantity = list_rotis_frame_entries[i].get()
                        if (quantity == ''):
                            quantity = '0'
                        if (quantity != '0'):
                            bill_text.insert(END, list_items_rotis[i][0].center(19) + " ₹" + list_items_rotis[i][
                                1] + quantity.center(9) + ("₹" + str(
                                int(quantity) * int(list_items_rotis[i][1][0:-2])) + "/-").center(8) + "\n")
                    for i in range(5):
                        quantity = list_maincourse_frame_entries[i].get()
                        if (quantity == ''):
                            quantity = '0'
                        if (quantity != '0'):
                            bill_text.insert(END, list_items_maincourse[i][0].center(19) + " ₹" + list_items_maincourse[i][
                                1] + quantity.center(8) + ("₹" + str(
                                int(quantity) * int(list_items_maincourse[i][1][0:-2])) + "/-").center(8) + "\n")
                    for i in range(5):
                        quantity = list_beverages_frame_entries[i].get()
                        if (quantity == ''):
                            quantity = '0'
                        if (quantity != '0'):
                            bill_text.insert(END, list_items_beverages[i][0].center(19) + " ₹" + list_items_beverages[i][
                                1] + quantity.center(9) + ("₹" + str(
                                int(quantity) * int(list_items_beverages[i][1][0:-2])) + "/-").center(8) + "\n")
                    for i in range(5):
                        quantity = list_desserts_frame_entries[i].get()
                        if (quantity == ''):
                            quantity = '0'
                        if (quantity != '0'):
                            bill_text.insert(END, list_items_desserts[i][0].center(19) + " ₹" + list_items_desserts[i][
                                1] + quantity.center(9) + ("₹" + str(
                                int(quantity) * int(list_items_desserts[i][1][0:-2])) + "/-").center(8) + "\n")
                    bill_text.insert(END, "\n******************************************\n")
                    bill_text.insert(END, "\n  Gross Amount  -   ₹" + str(gross_amount) + "/-\n  Tax     \t\t-   ₹" + str(
                        tax_amount) + "/-\n\t\t  ----------\n  Total Amount  -   ₹" + str(
                        total_amount) + "/-\n\t\t  ----------\n")
                    bill_text.insert(END, "\n******************************************")

                    bill_text.config(state=DISABLED, bg="white")
                    bill_text.place(x=0, y=0)

            def save():

                global bill_text
                global quan_count_2
                if(quan_count_2 == 0):
                    messagebox.showerror("NO ITEM SELECTED", "Please Select any item")
                else:
                    save_text = bill_text.get("1.0", END)
                    file = open("bill_details.txt", "a", encoding="utf-8")
                    file.write(save_text)
                    file.close()

            def reset():

                global gross_ent
                global tax_ent
                global total_ent
                global bill_text

                for i in range(5):
                    list_tiffins_frame_entries[i].delete(0, END)
                    list_starters_frame_entries[i].delete(0, END)
                    list_rotis_frame_entries[i].delete(0, END)
                    list_maincourse_frame_entries[i].delete(0, END)
                    list_beverages_frame_entries[i].delete(0, END)
                    list_desserts_frame_entries[i].delete(0, END)

                gross_ent = Entry(amount_frame, borderwidth=5, relief=SUNKEN, width=12, font=("Tahoma", 13, "bold"),
                                  fg="black")
                gross_ent.insert(0, "")
                gross_ent.config(state=DISABLED)
                gross_ent.grid(row=0, column=1, padx=10, pady=10)

                tax_ent = Entry(amount_frame, borderwidth=5, relief=SUNKEN, width=12, font=("Tahoma", 13, "bold"))
                tax_ent.insert(0, "")
                tax_ent.config(state=DISABLED)
                tax_ent.grid(row=1, column=1, padx=15, pady=10)

                total_ent = Entry(amount_frame, borderwidth=5, relief=SUNKEN, width=12, font=("Tahoma", 13, "bold"))
                total_ent.insert(0, "")
                total_ent.config(state=DISABLED)
                total_ent.grid(row=2, column=1, padx=15, pady=10)

                bill_text = Text(bill_frame, borderwidth=2, relief=SUNKEN, width=42, height=19, padx=6)
                bill_text.config(state=DISABLED, bg="white")
                bill_text.place(x=0, y=0)

            def calculator():
                root2 = Tk()

                root2.title("Calculator")
                # root2.geometry("300x300")
                root2.config(bg="firebrick4")

                e = Entry(root2, width=20, borderwidth=5, font=("", 14))
                e.grid(row=0, column=0, columnspan=3, padx=5, pady=10, ipady=5, ipadx=10)

                def button_click(number):
                    current = e.get()
                    e.delete(0, END)
                    e.insert(0, str(current) + str(number))

                def button_clear():
                    e.delete(0, END)

                def button_eq():
                    try:
                        if (oper == '+'):
                            current = e.get()
                            e.delete(0, END)
                            e.insert(0, int(prev) + int(current))
                        elif (oper == '-'):
                            current = e.get()
                            e.delete(0, END)
                            e.insert(0, int(prev) - int(current))
                        elif (oper == '*'):
                            current = e.get()
                            e.delete(0, END)
                            e.insert(0, int(prev) * int(current))
                        elif (oper == '/'):
                            current = e.get()
                            e.delete(0, END)
                            e.insert(0, int(prev) / float(current))
                    except:
                        pass

                def button_add():
                    # previous = e.get()
                    global prev
                    global oper
                    oper = '+'
                    prev = e.get()
                    e.delete(0, END)

                def button_sub():
                    # previous = e.get()
                    global prev
                    global oper
                    oper = '-'
                    prev = e.get()
                    e.delete(0, END)

                def button_mul():
                    # previous = e.get()
                    global prev
                    global oper
                    oper = '*'
                    prev = e.get()
                    e.delete(0, END)

                def button_div():
                    # previous = e.get()
                    global prev
                    global oper
                    oper = '/'
                    prev = e.get()
                    e.delete(0, END)

                but_7 = Button(root2, text="7", padx=34, pady=13, command=lambda: button_click(7), bg="firebrick3",
                               fg="white",
                               font=("", 15)).grid(row=1, column=0, columnspan=1)
                but_8 = Button(root2, text="8", padx=34, pady=13, command=lambda: button_click(8), bg="firebrick3",
                               fg="white",
                               font=("", 15)).grid(row=1, column=1, columnspan=1)
                but_9 = Button(root2, text="9", padx=34, pady=13, command=lambda: button_click(9), bg="firebrick3",
                               fg="white",
                               font=("", 15)).grid(row=1, column=2, columnspan=1)

                but_4 = Button(root2, text="4", padx=34, pady=13, command=lambda: button_click(4), bg="firebrick3",
                               fg="white",
                               font=("", 15)).grid(row=2, column=0, columnspan=1)
                but_5 = Button(root2, text="5", padx=34, pady=13, command=lambda: button_click(5), bg="firebrick3",
                               fg="white",
                               font=("", 15)).grid(row=2, column=1, columnspan=1)
                but_6 = Button(root2, text="6", padx=34, pady=13, command=lambda: button_click(6), bg="firebrick3",
                               fg="white",
                               font=("", 15)).grid(row=2, column=2, columnspan=1)

                but_1 = Button(root2, text="1", padx=34, pady=13, command=lambda: button_click(1), bg="firebrick3",
                               fg="white",
                               font=("", 15)).grid(row=3, column=0, columnspan=1)
                but_2 = Button(root2, text="2", padx=34, pady=13, command=lambda: button_click(2), bg="firebrick3",
                               fg="white",
                               font=("", 15)).grid(row=3, column=1, columnspan=1)
                but_3 = Button(root2, text="3", padx=34, pady=13, command=lambda: button_click(3), bg="firebrick3",
                               fg="white",
                               font=("", 15)).grid(row=3, column=2, columnspan=1)

                but_0 = Button(root2, text="0", padx=34, pady=13, command=lambda: button_click(0), bg="firebrick3",
                               fg="white",
                               font=("", 15)).grid(row=4, column=0, columnspan=1)
                but_add = Button(root2, text="+", padx=33, pady=13, command=lambda: button_add(), bg="firebrick4",
                                 fg="white",
                                 font=("", 15)).grid(row=5, column=0, columnspan=1)
                but_eq = Button(root2, text="=", padx=81, pady=13, command=lambda: button_eq(), bg="firebrick3",
                                fg="white",
                                font=("", 15)).grid(row=4, column=1, columnspan=2)
                but_clear = Button(root2, text="CLEAR", padx=73, pady=20, command=lambda: button_clear(),
                                   bg="firebrick3",
                                   fg="white").grid(row=5, column=1, columnspan=2)
                but_sub = Button(root2, text="-", padx=35, pady=12, command=lambda: button_sub(), bg="firebrick4",
                                 fg="white",
                                 font=("", 15)).grid(row=6, column=0, columnspan=1)
                but_mul = Button(root2, text="X", padx=35, pady=12, command=lambda: button_mul(), bg="firebrick4",
                                 fg="white",
                                 font=("", 15)).grid(row=6, column=1, columnspan=1)
                but_div = Button(root2, text="/", padx=35, pady=12, command=lambda: button_div(), bg="firebrick4",
                                 fg="white",
                                 font=("", 15)).grid(row=6, column=2, columnspan=1)

                root2.mainloop()

            top_frame = Frame(root, height=100, borderwidth=10, relief=RIDGE, bg="blue4")
            top_frame.pack(side=TOP, fill=X, anchor="ne")

            lab_top = Label(top_frame, text="RESTAURANT MANAGEMENT SYSTEM", bg="blue4", fg="firebrick1",
                            font=("Tahoma", 25, "bold"), pady=10)
            lab_top.pack()

            menu_frame = Frame(root, borderwidth=10, relief=RIDGE, bg="blue4", width=930)
            menu_frame.pack(side=LEFT, anchor="nw", fill=Y)

            recipt_frame = Frame(root, borderwidth=10, relief=RIDGE, bg="blue4", width=445)
            recipt_frame.pack(side=RIGHT, anchor="ne", fill=Y)

            tiffins_frame = LabelFrame(menu_frame, borderwidth=5, relief=RIDGE, text="TIFFINS", width=300, height=314,
                                       font=("Tahoma", 15, ""), bg="grey10", fg="yellow")
            starters_frame = LabelFrame(menu_frame, borderwidth=5, relief=RIDGE, text="STARTERS", width=300, height=314,
                                        font=("Tahoma", 15, ""), bg="grey10", fg="yellow")
            rotis_frame = LabelFrame(menu_frame, borderwidth=5, relief=RIDGE, text="ROTIS", width=300, height=314,
                                     font=("Tahoma", 15, ""), bg="grey10", fg="yellow")
            maincourse_frame = LabelFrame(menu_frame, borderwidth=5, relief=RIDGE, text="MAIN COURSE", width=300,
                                          height=314, font=("Tahoma", 15, ""), bg="grey10", fg="yellow")
            beverages_frame = LabelFrame(menu_frame, borderwidth=5, relief=RIDGE, text="BEVERAGES", width=300,
                                         height=314, font=("Tahoma", 15, ""), bg="grey10", fg="yellow")
            desserts_frame = LabelFrame(menu_frame, borderwidth=5, relief=RIDGE, text="DESSERTS", width=300, height=314,
                                        font=("Tahoma", 15, ""), bg="grey10", fg="yellow")

            list_menuframes = [tiffins_frame, starters_frame, rotis_frame, maincourse_frame, beverages_frame,
                               desserts_frame]

            for i in range(2):
                for j in range(3):
                    list_menuframes[3 * (i) + j].grid(row=i, column=j, columnspan=1, rowspan=1, pady=2, padx=2)

            q_idly = StringVar()
            q_plaindosa = StringVar()
            q_masaladosa = StringVar()
            q_poori = StringVar()
            q_vada = StringVar()

            list_items_tiffins = [["Idly (2 Pieces)", "30/-"], ["Plain Dosa", "50/-"], ["Masala Dosa", "70/-"],
                                  ["Poori", "60/-"], ["Vada (2 Pieces)", "40/-"]]

            e_idly = Entry(tiffins_frame, textvariable=q_idly, width=5, borderwidth=4, relief=SUNKEN, bg="lightblue1",
                           fg="firebrick1", font=("", 13, "bold"))
            e_plaindosa = Entry(tiffins_frame, textvariable=q_plaindosa, width=5, borderwidth=4, relief=SUNKEN,
                                bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_masaladosa = Entry(tiffins_frame, textvariable=q_masaladosa, width=5, borderwidth=4, relief=SUNKEN,
                                 bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_poori = Entry(tiffins_frame, textvariable=q_poori, width=5, borderwidth=4, relief=SUNKEN, bg="lightblue1",
                            fg="firebrick1", font=("", 13, "bold"))
            e_vada = Entry(tiffins_frame, textvariable=q_vada, width=5, borderwidth=4, relief=SUNKEN, bg="lightblue1",
                           fg="firebrick1", font=("", 13, "bold"))

            list_tiffins_frame_entries = [e_idly, e_plaindosa, e_masaladosa, e_poori, e_vada]

            for i in range(5):
                for j in range(2):
                    lab = Label(tiffins_frame, text=list_items_tiffins[i][j], padx=8, pady=10, font=("Tahoma", 14, ""),
                                bg="grey10", fg="light cyan")
                    lab.grid(row=i, column=j)
                    list_tiffins_frame_entries[i].grid(row=i, column=2, pady=14, padx=25)

            q_vegmanchuria = StringVar()
            q_gobi65 = StringVar()
            q_eggmanchuria = StringVar()
            q_chicken65 = StringVar()
            q_springroll = StringVar()

            list_items_starters = [["Veg Manchuria", "150/-"], ["Gobi 65", "160/-"], ["Egg Manchuria", "180/-"],
                                   ["Chicken Manchuria", "200/-"], ["Spring Rolls", "170/-"]]

            e_vegmanchuria = Entry(starters_frame, textvariable=q_vegmanchuria, width=5, borderwidth=4, relief=SUNKEN,
                                   bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_gobi65 = Entry(starters_frame, textvariable=q_gobi65, width=5, borderwidth=4, relief=SUNKEN,
                             bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_eggmanchuria = Entry(starters_frame, textvariable=q_eggmanchuria, width=5, borderwidth=4, relief=SUNKEN,
                                   bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_chicken65 = Entry(starters_frame, textvariable=q_chicken65, width=5, borderwidth=4, relief=SUNKEN,
                                bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_springroll = Entry(starters_frame, textvariable=q_springroll, width=5, borderwidth=4, relief=SUNKEN,
                                 bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))

            list_starters_frame_entries = [e_vegmanchuria, e_gobi65, e_eggmanchuria, e_chicken65, e_springroll]

            for i in range(5):
                for j in range(2):
                    lab = Label(starters_frame, text=list_items_starters[i][j], padx=8, pady=8, font=("Tahoma", 14, ""),
                                bg="grey10", fg="light cyan")
                    lab.grid(row=i, column=j)
                    list_starters_frame_entries[i].grid(row=i, column=2, pady=14, padx=10)

            q_roti = StringVar()
            q_garlicroti = StringVar()
            q_plainnaan = StringVar()
            q_butternaan = StringVar()
            q_aluparatha = StringVar()

            list_items_rotis = [["Roti", "40/-"], ["Garlic Roti", "50/-"], ["Plain Naan", "55/-"],
                                ["Butter Naan", "65/-"], ["Alu Paratha", "70/-"]]

            e_roti = Entry(rotis_frame, textvariable=q_roti, width=5, borderwidth=4, relief=SUNKEN, bg="lightblue1",
                           fg="firebrick1", font=("", 13, "bold"))
            e_garlicroti = Entry(rotis_frame, textvariable=q_garlicroti, width=5, borderwidth=4, relief=SUNKEN,
                                 bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_plainnaan = Entry(rotis_frame, textvariable=q_plainnaan, width=5, borderwidth=4, relief=SUNKEN,
                                bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_butternaan = Entry(rotis_frame, textvariable=q_butternaan, width=5, borderwidth=4, relief=SUNKEN,
                                 bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_aluparatha = Entry(rotis_frame, textvariable=q_aluparatha, width=5, borderwidth=4, relief=SUNKEN,
                                 bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))

            list_rotis_frame_entries = [e_roti, e_garlicroti, e_plainnaan, e_butternaan, e_aluparatha]

            for i in range(5):
                for j in range(2):
                    lab = Label(rotis_frame, text=list_items_rotis[i][j], padx=8, pady=8, font=("Tahoma", 14, ""),
                                bg="grey10", fg="light cyan")
                    lab.grid(row=i, column=j)
                    list_rotis_frame_entries[i].grid(row=i, column=2, pady=14, padx=30)

            q_potatocurry = StringVar()
            q_paneercurry = StringVar()
            q_eggcurry = StringVar()
            q_butterchicken = StringVar()
            q_fishcurry = StringVar()

            list_items_maincourse = [["Potato Curry", "150/-"], ["Paneer Curry", "170/-"], ["Egg Curry", "200/-"],
                                     ["Butter Chicken", "240/-"], ["Fish Curry", "280/-"]]

            e_potatocurry = Entry(maincourse_frame, textvariable=q_potatocurry, width=5, borderwidth=4, relief=SUNKEN,
                                  bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_paneercurry = Entry(maincourse_frame, textvariable=q_paneercurry, width=5, borderwidth=4, relief=SUNKEN,
                                  bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_eggcurry = Entry(maincourse_frame, textvariable=q_eggcurry, width=5, borderwidth=4, relief=SUNKEN,
                               bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_butterchicken = Entry(maincourse_frame, textvariable=q_butterchicken, width=5, borderwidth=4,
                                    relief=SUNKEN, bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_fishcurry = Entry(maincourse_frame, textvariable=q_fishcurry, width=5, borderwidth=4, relief=SUNKEN,
                                bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))

            list_maincourse_frame_entries = [e_potatocurry, e_paneercurry, e_eggcurry, e_butterchicken, e_fishcurry]

            for i in range(5):
                for j in range(2):
                    lab = Label(maincourse_frame, text=list_items_maincourse[i][j], padx=11, pady=8,
                                font=("Tahoma", 14, ""), bg="grey10", fg="light cyan")
                    lab.grid(row=i, column=j)
                    list_maincourse_frame_entries[i].grid(row=i, column=2, pady=14, padx=18)

            q_masalatea = StringVar()
            q_lemontea = StringVar()
            q_coffee = StringVar()
            q_lemonsoda = StringVar()
            q_coke = StringVar()

            list_items_beverages = [["Masala Tea", "30/-"], ["Lemon Tea", "40/-"], ["Coffee", "45/-"],
                                    ["Lemon Soda", "50/-"], ["Coke", "60/-"]]

            e_masalatea = Entry(beverages_frame, textvariable=q_masalatea, width=5, borderwidth=4, relief=SUNKEN,
                                bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_masalatea.icursor(END)
            e_lemontea = Entry(beverages_frame, textvariable=q_lemontea, width=5, borderwidth=4, relief=SUNKEN,
                               bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_coffee = Entry(beverages_frame, textvariable=q_coffee, width=5, borderwidth=4, relief=SUNKEN,
                             bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_lemonsoda = Entry(beverages_frame, textvariable=q_lemonsoda, width=5, borderwidth=4, relief=SUNKEN,
                                bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_coke = Entry(beverages_frame, textvariable=q_coke, width=5, borderwidth=4, relief=SUNKEN, bg="lightblue1",
                           fg="firebrick1", font=("", 13, "bold"))

            list_beverages_frame_entries = [e_masalatea, e_lemontea, e_coffee, e_lemonsoda, e_coke]

            for i in range(5):
                for j in range(2):
                    lab = Label(beverages_frame, text=list_items_beverages[i][j], padx=15, pady=8,
                                font=("Tahoma", 14, ""), bg="grey10", fg="light cyan")
                    lab.grid(row=i, column=j)
                    list_beverages_frame_entries[i].grid(row=i, column=2, pady=14, padx=30)

            q_chocolatecake = StringVar()
            q_oreomilkshake = StringVar()
            q_vanillaicecream = StringVar()
            q_gulabjamun = StringVar()
            q_fruitsalad = StringVar()

            list_items_desserts = [["Chocolate Cake", "60/-"], ["Oreo Milkshake", "80/-"], ["Vanilla Icecream", "40/-"],
                                   ["Gulab Jamun", "50/-"], ["Fruit Salad", "55/-"]]

            e_chocolatecake = Entry(desserts_frame, textvariable=q_chocolatecake, width=5, borderwidth=4, relief=SUNKEN,
                                    bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_oreomilkshake = Entry(desserts_frame, textvariable=q_oreomilkshake, width=5, borderwidth=4, relief=SUNKEN,
                                    bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_vanillaicecream = Entry(desserts_frame, textvariable=q_vanillaicecream, width=5, borderwidth=4,
                                      relief=SUNKEN, bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_gulabjamun = Entry(desserts_frame, textvariable=q_gulabjamun, width=5, borderwidth=4, relief=SUNKEN,
                                 bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))
            e_fruitsalad = Entry(desserts_frame, textvariable=q_fruitsalad, width=5, borderwidth=4, relief=SUNKEN,
                                 bg="lightblue1", fg="firebrick1", font=("", 13, "bold"))

            list_desserts_frame_entries = [e_chocolatecake, e_oreomilkshake, e_vanillaicecream, e_gulabjamun,
                                           e_fruitsalad]

            for i in range(5):
                for j in range(2):
                    lab = Label(desserts_frame, text=list_items_desserts[i][j], padx=6, pady=8, font=("Tahoma", 14, ""),
                                bg="grey10", fg="light cyan")
                    lab.grid(row=i, column=j)
                    list_desserts_frame_entries[i].grid(row=i, column=2, pady=14, padx=14)

            bill_frame = Frame(recipt_frame, borderwidth=5, relief=RIDGE, width=365, height=316, bg="snow")
            bill_frame.pack(side=TOP, fill=Y, anchor="nw")

            global bill_text
            bill_text = Text(bill_frame, borderwidth=2, relief=SUNKEN, width=44, height=19, state=DISABLED)
            bill_text.pack(side=TOP)

            amount_frame = Frame(recipt_frame, borderwidth=5, relief=RIDGE, width=365, height=160, bg="red4")
            amount_frame.pack(fill=X)

            global gross_ent
            gross_lab = Label(amount_frame, text="Gross amount", padx=25, font=("Tahoma", 14, "bold"), bg="red4",
                              fg="yellow")
            gross_lab.grid(row=0, column=0)
            gross_ent = Entry(amount_frame, borderwidth=5, relief=SUNKEN, state=DISABLED, width=12,
                              font=("Tahoma", 13, "bold"))
            gross_ent.grid(row=0, column=1, padx=10, pady=10)

            global tax_ent
            tax_lab = Label(amount_frame, text="Tax", padx=25, font=("Tahoma", 14, "bold"), bg="red4", fg="yellow")
            tax_lab.grid(row=1, column=0)
            tax_ent = Entry(amount_frame, borderwidth=5, relief=SUNKEN, state=DISABLED, width=12,
                            font=("Tahoma", 13, "bold"))
            tax_ent.grid(row=1, column=1, padx=15, pady=10)

            global total_ent
            total_lab = Label(amount_frame, text="Total Amount", padx=25, font=("Tahoma", 14, "bold"), bg="red4",
                              fg="yellow")
            total_lab.grid(row=2, column=0)
            total_ent = Entry(amount_frame, borderwidth=5, relief=SUNKEN, state=DISABLED, width=12,
                              font=("Tahoma", 13, "bold"))
            total_ent.grid(row=2, column=1, padx=15, pady=10)

            buttons_frame = Frame(recipt_frame, borderwidth=5, relief=RIDGE, width=365, height=300)
            buttons_frame.pack()
            buttons_frame.config(bg="navy")

            total_but = Button(buttons_frame, text="Total", font=("Tahoma", 13, "bold"), padx=58, pady=3, borderwidth=5,
                               relief=RAISED, bg="firebrick2", fg="white", cursor="hand2", command=total)
            total_but.grid(row=0, column=0)

            invoice_but = Button(buttons_frame, text="Invoice", font=("Tahoma", 13, "bold"), padx=46, pady=3,
                                 borderwidth=5, relief=RAISED, bg="firebrick2", fg="white", cursor="hand2",
                                 command=invoice)
            invoice_but.grid(row=0, column=1)

            save_but = Button(buttons_frame, text="Save", font=("Tahoma", 13, "bold"), padx=59, pady=3, borderwidth=5,
                              relief=RAISED, bg="firebrick2", fg="white", cursor="hand2", command=save)
            save_but.grid(row=1, column=0)

            reset_but = Button(buttons_frame, text="Reset", font=("Tahoma", 13, "bold"), padx=54, pady=3, borderwidth=5,
                               relief=RAISED, bg="firebrick2", fg="white", cursor="hand2", command=reset)
            reset_but.grid(row=1, column=1)

            quit_but = Button(buttons_frame, text="Quit", font=("Tahoma", 13, "bold"), command=root.quit, padx=127,
                              pady=4, borderwidth=5, relief=RAISED, bg="firebrick2", fg="white", cursor="hand2")
            quit_but.grid(row=2, column=0, columnspan=2, sticky="W")

            calc_icon = Image.open('img/Calculator_icon.ico')
            calc_icon = calc_icon.resize((35, 35))
            calc_icon = ImageTk.PhotoImage(calc_icon)
            but_calc = Button(buttons_frame, image=calc_icon, borderwidth=5, relief=RAISED, bg="firebrick2", fg="white",
                              cursor="hand2", command=calculator)
            but_calc.grid(row=2, column=1, sticky="E")

            # root.attributes("-fullscreen",True)

            root.mainloop()
            break
        else:
            flag=0
    if(flag==0):
        messagebox.showerror("Login","Login Not Successful")

login_root_bg = Image.open("img/Login_page_img.jpg")
resized = login_root_bg.resize((1366,740),Image.Resampling.LANCZOS)
login_root_bg_resized = ImageTk.PhotoImage(resized)
login_root_bg_image = Label(login_root,image=login_root_bg_resized).place(x=0,y=0,relwidth=1,relheight=1)

main_lab = Label(login_root,text="Welcome to \nRestaurant Management System !!",font=("Tahoma",35),padx=50,pady=50,fg="yellow",bg="black",borderwidth=6,relief=RIDGE)
main_lab.place(x=284,y=106)

f = Frame(login_root,borderwidth=4,width=800,height=100,bg="black",relief=RIDGE)
f.place(x=220,y=405)

l1 = Label(f,text="Username : ",padx=3,pady=10,font=("Tahoma",25),bg="black",fg="yellow")
l1.grid(row=1,column=0,padx=5,pady=10)

l2 = Label(f,text="Password : ",padx=3,pady=10,font=("Tahoma",25),bg="black",fg="yellow")
l2.grid(row=2,column=0,padx=5,pady=10)

user_name = StringVar()
pass_name = StringVar()

e1 = Entry(f,textvariable=user_name,width=48,font=("",20),borderwidth=4,relief=RIDGE)
e1.grid(row=1,column=1,ipady=10,padx=10)

e2 = Entry(f,textvariable=pass_name,width=48,font=("",20),borderwidth=4,relief=RIDGE)
e2.grid(row=2,column=1,ipady=10,padx=10)

submit = Button(login_root,text="SUBMIT",command=check_login,font=("",20),bg="grey8",fg="gold",borderwidth=6,cursor="hand2")
# submit.grid(row=3,column=1,padx=60,pady=20)
submit.place(x=614,y=595)

login_root.mainloop()

