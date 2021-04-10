'''
A program that stores the Medicine information
Medicine name, Type
Quantity, Price

User can:

View all records
Search an entry
Add entry
Update entry
Delete
Close
'''

from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(name_text.get(),types_text.get(),quantity_text.get(),price_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(name_text.get(),types_text.get(),quantity_text.get(),price_text.get())
    list1.delete(0,END)
    list1.insert(END,(name_text.get(),types_text.get(),quantity_text.get(),price_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],name_text.get(),types_text.get(),quantity_text.get(),price_text.get())

window=Tk()

window.wm_title("MedicineStore")

l1=Label(window,text="Name")
l1.grid(row=0,column=0)

l2=Label(window,text="Types")
l2.grid(row=0,column=2)

l3=Label(window,text="Quantity")
l3.grid(row=1,column=0)

l4=Label(window,text="Price")
l4.grid(row=1,column=2)

name_text=StringVar()
e1=Entry(window,textvariable=name_text)
e1.grid(row=0,column=1)

types_text=StringVar()
e2=Entry(window,textvariable=types_text)
e2.grid(row=0,column=3)

quantity_text=StringVar()
e3=Entry(window,textvariable=quantity_text)
e3.grid(row=1,column=1)

price_text=StringVar()
e4=Entry(window,textvariable=price_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected", width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()