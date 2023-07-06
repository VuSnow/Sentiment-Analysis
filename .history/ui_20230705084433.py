import tkinter as tk
from tkcalendar import Calendar
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter import *
from datetime import date

root = tk.Tk()
root.geometry("400x400")

start_date = date.today()
end_date = date.today()


company_nameVar = tk.StringVar()


header_label = tk.Label(root, text="Scraping Data",
                        font=('sans-serif', 10, 'bold'), justify='center')
name_company = tk.Label(
    root, text="Enter the name of company: ", font=('sans-serif', 10, 'normal'))
name_entry = tk.Entry(root, textvariable=company_nameVar, font=(
    'sans-serif', 10, 'normal'), justify='left')

start_date_text = tk.Label(root, text="Choose start date: ",
                           font=('sans-serif', 10, 'normal'))
end_date_text = tk.Label(root, text="Choose end date: ",
                         font=('sans-serif', 10, 'normal'))
cal_start = DateEntry(root, selectmode='day', date_pattern='dd/mm/yyyy')
cal_end = DateEntry(root, selectmode='day', date_pattern='dd/mm/yyyy')


def get_date_start():
    # triggered on Button Click
    l1 = tk.Label(root, text='data', bg='yellow')
    l1.grid(row=2, column=2, sticky='w', padx=(10, 0))
    l1.config(text=cal_start.get_date().strftime("%d/%m/%Y"))


def get_date_end():
    if cal_start.get_date() > cal_end.get_date():
        messagebox.showerror(
            "Error", "End date must be greater than start date.")
        return
    l2 = tk.Label(root, text='data', bg='yellow')
    l2.grid(row=3, column=2, sticky='w', padx=(10, 0))
    l2.config(text=cal_end.get_date().strftime("%d/%m/%Y"))


def update_start_date(event):
    global start_date
    start_date = cal_start.get_date()
    check_date_range()


def update_end_date(event):
    global end_date
    end_date = cal_end.get_date()
    check_date_range()


def check_date_range():
    if start_date and end_date and start_date > end_date:
        messagebox.showerror(
            "Error", "End date must be greater than start date.")


cal_start.bind("<<DateEntrySelected>>", update_start_date)
cal_end.bind("<<DateEntrySelected>>", update_end_date)

# button_start = tk.Button(root, text='Read', command=get_date_start)
# button_end = tk.Button(root, text='Read', command=get_date_end)

header_label.grid(row=0, column=1)
name_company.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
start_date_text.grid(row=2, column=0, sticky='e')
cal_start.grid(row=2, column=1, sticky='w')
# button_start.grid(row=2, column=1, sticky='e')
end_date_text.grid(row=3, column=0, sticky='e')
cal_end.grid(row=3, column=1, sticky='w')
# button_end.grid(row=3, column=1, sticky='e')


root.mainloop()
