from tkinter import *
from tkinter import messagebox, StringVar , simpledialog
from tkinter import ttk


sim_card_list = []
current_editing_index = -1 # برای نگهداری ایندکس آیتمی که در حال ویرایش است




# 5
def reset_form():
    number.set("")
    owner.set("")
    regester_time.set("")
    oparator.set("")
    charge.set(0)

# 6
def save_click():
    sim_card = {
        "number":number.get(),
        "owner":owner.get(),
        "regester_time":regester_time.get(),
        "oparator":oparator.get(),
        "charge": charge.get()
    }
    sim_card_list.append(sim_card)
    messagebox.showinfo("Save", f"Successfully saved!\n{sim_card}")
    reset_form()
    table.insert("", END, values=tuple(sim_card.values()))

# HomeWork


#8
def edit_click():
    global current_editing_index
    if current_editing_index == -1 :
        messagebox.showwarning("Edit Error")
        return

   # دریافت اطلاعات جدید
    updated_sim_card = {
        "number": number.get(),
        "owner": owner.get(),
        "regester_time": regester_time.get(),
        "oparator": oparator.get(),
        "charge": charge.get()
    }


    sim_card_list[current_editing_index] = updated_sim_card
    messagebox.showwarning('ویرایش با موفقیت انجام شد')

    reset_form()


#9
def remove_click():
    global current_editing_index

    if current_editing_index == -1:
        messagebox.showwarning("Remove Error")
        return
    del sim_card_list[current_editing_index]
    messagebox.showinfo("Remove", "Successfully removed!")
    reset_form()



# 7
def table_select(event):
    try:
        table_row = table.focus()  # I001
        selected = table.item(table_row)["values"]  # مثلاً [1, 'sib', 'sib', '1000', '5']
        number.set(selected[0])
        owner.set(selected[1])
        regester_time.set(selected[2])
        oparator.set(selected[3])
        charge.set(int(selected[4]))

        global current_editing_index
        current_editing_index = (table_row)

    except EXCEPTION as e:
        messagebox.showerror('error')


# 0
window = Tk()
window.title("SimCard")
window.geometry("710x360")
window.resizable(False, False)
# geometry-title

# 1
# number
# owner
# regester_time
# oparator
# charge

number = StringVar()
Label(window,text="number").place(x=20,y=20)
Entry(window, textvariable=number).place(x=100,y=20)

owner = StringVar()
Label(window,text="Owner").place(x=20,y=60)
Entry(window, textvariable=owner).place(x=100,y=60)

regester_time = StringVar()
Label(window,text="Regester_time").place(x=20,y=100)
Entry(window, textvariable=regester_time).place(x=100,y=100)

oparator = StringVar()
Label(window,text="Oparator").place(x=20,y=140)
Entry(window, textvariable=oparator).place(x=100,y=140)

charge = IntVar()
Label(window,text="Charge").place(x=20,y=180)
Entry(window, textvariable=charge).place(x=100,y=180)



# 2
# buttons

Button(window, text="Save", command=save_click, width=7).place(x=20,y=300)
Button(window, text="Edit", command=edit_click, width=7).place(x=95,y=300)
Button(window, text="Remove", command=remove_click, width=7).place(x=170,y=300)



# 3
# search Number
# search Owner

number_search = StringVar()
Label(window,text="Search Number").place(x=250,y=20)
Entry(window, textvariable=number_search).place(x=330,y=20)


owner_search = StringVar()
Label(window,text="Search Owner").place(x=480,y=20)
Entry(window, textvariable=owner_search).place(x=560,y=20)

# 4
# Table
# TreeviewSelect
# bind--> table_select

table = ttk.Treeview(window, height=12,columns=(1,2,3,4,5),show="headings")
table.column(1, width=70)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=80)
table.column(5, width=80)

table.heading(1, text="number")
table.heading(2, text="owner")
table.heading(3, text="regester_time")
table.heading(4, text="oparator")
table.heading(5, text="charge")

table.bind("<<TreeviewSelect>>", table_select)

table.place(x=250, y = 60)


window.mainloop()