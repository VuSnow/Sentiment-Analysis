import tkinter as tk
from tkcalendar import Calendar
from tkcalendar import DateEntry
from tkinter import *

root = tk.Tk()
root.geometry("400x400")


company_nameVar = tk.StringVar()


header_label = tk.Label(root, text="Scraping Data",
                        font=('sans-serif', 10, 'bold'), justify='center')
name_company = tk.Label(
    root, text="Enter the name of company: ", font=('sans-serif', 10, 'normal'))
name_entry = tk.Entry(root, textvariable=company_nameVar, font=(
    'sans-serif', 10, 'normal'), justify='center')

calendar_name = tk.Label(root, text="Choose start date",
                         font=('sans-serif', 10, 'normal'))
cal = DateEntry(root, selectmode='day')


header_label.grid(row=0, column=1)
name_company.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
calendar_name.grid(row=2, column=0)
cal.grid(row=2, column=1)


root.mainloop()
