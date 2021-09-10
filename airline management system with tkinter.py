import tkinter as tk
from tkinter import ttk
#combobox
from time import strftime
#resizewindow
from tkinter import messagebox
#formessagebox
root=tk.Tk()
root.geometry("380x90")
root.title('ABC Airlines')
root.resizable(0, 0)
root.iconbitmap(r'C:\Users\user\Desktop\python\favicon (1).ico')
root.configure(bg='Black')
board1=tk.Label(root,text="Welcome to ABC Airlines",font=("times new roman", 27),fg="green",bg="black").grid(row=1,column=0,sticky='W')
def pop():
    messagebox.showinfo('Booking Confirmed',"Thank you for booking your ticket in ABC airlines")
def ticket():
    window=tk.Tk()
    window.geometry("500x350")
    window.title('Welcome to ABC Airlines')
    window.resizable(0, 0)
    window.iconbitmap(r'C:\Users\user\Desktop\python\favicon (1).ico')
    n=tk.StringVar()
    window.configure(bg='Black')
    board=tk.Label(window,text="Enter Boarding",font=("times new roman", 17),fg="white",bg="black").grid(row=0,column=0,sticky='W')
    b=ttk.Combobox(window,width=16,textvariable=n)
    b['values']=('Chennai','Mumbai','Goa','Agra','Enter Boarding')
    b.grid(row=0,column=1,columnspan=2,sticky='W')
    b.current(4)
    adhar=tk.Label(window,text="AdharCard number",font=("times new roman", 17),fg="white",bg="black").grid(row=1,column=0,sticky='W')
    adhartb=tk.Entry(window,bd=5,width=18)
    adhartb.grid(row=1,column=1,columnspan=2,sticky='W')
    dest=tk.Label(window,text="Enter your Destination",font=("times new roman", 17),fg="white",bg="Black").grid(row=2,column=0,sticky='W')
    c=ttk.Combobox(window,width=16)
    c['values']=('Chennai','Mumbai','Goa','Agra','Enter Destination')
    c.grid(row=2,column=1,columnspan=2)
    c.current(4)
    date=tk.Label(window,text="Enter your Date of Journey",font=("times new roman", 17),fg="white",bg="Black").grid(row=3,sticky='W')
    dt=ttk.Combobox(window,width=5)
    dt['values']=('Day',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
    dt.grid(row=3,column=1,sticky='W')
    dt.current(0)
    dtm=ttk.Combobox(window,width=5)
    dtm['values']=('Month','Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec')
    dtm.grid(row=3,column=2,sticky='W')
    dtm.current(0)
    npassengers=tk.Label(window,text="Enter the number of Passengers",font=("times new roman", 17),fg="white",bg="black").grid(row=4,sticky='W')
    spin=tk.Spinbox(window,from_=0,to=10,width=4)
    spin.grid(row=4,column=1,columnspan=2)
    npassengerschild=tk.Label(window,text="Passengers below the age of 5",font=("times new roman", 17),fg="white",bg="black").grid(row=5,sticky='W')
    spin1=tk.Spinbox(window,from_=0,to=5,width=4)
    spin1.grid(row=5,column=1,columnspan=2)
    windows=tk.Label(window,text="Do you prefer Window Seat",font=("times new roman", 17),fg="white",bg="Black").grid(sticky='W')
    rad1=tk.Radiobutton(window,text='Yes',font=("times new roman", 13),value=1,bg='black',fg='white',	selectcolor='black').grid(row=6,column=1,sticky='W')
    rad2=tk.Radiobutton(window,text='No',font=("times new roman", 13),value=2,bg='black',fg='white',selectcolor='black').grid(row=6,column=2,sticky='W')
    classs=tk.Label(window,text="Select class",font=("times new roman", 17),fg="white",bg="Black").grid(sticky='W')
    d=ttk.Combobox(window,width=16)
    d['values']=('Premium Economy','Economy','First Class','Select Class')
    d.grid(row=7,column=1,columnspan=2)
    d.current(3)
    meal=tk.Label(window,text="Select your meal option",font=("times new roman", 17),fg="white",bg="black").grid(sticky='W')
    a=ttk.Combobox(window,width=16)
    a['values']=('Non Veg','Veg','Vegan','Enter meal option')
    a.grid(row=8,column=1,columnspan=2)
    a.current(3)
    conform=tk.Button(window,text="Confirm booking",font=("times new roman", 13),fg="white",bg="Black",bd=3,relief='ridge',command=pop)
    conform.grid(sticky='E')
    window.mainloop()
   



conform1=tk.Button(root,text="Book Tickets",font=("times new roman bold", 13),fg="white",bg="Black",bd=3,relief='ridge',command=ticket)
conform2=tk.Button(root,text="Cancel Tickets",font=("times new roman bold", 13),fg="white",bg="Black",bd=3,relief='ridge')
conform1.grid()
conform1.grid()
root.mainloop()


