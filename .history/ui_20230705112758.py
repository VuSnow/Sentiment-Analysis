from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from bs4 import BeautifulSoup
from tkinter import *
from tkcalendar import *
from datetime import *
import csv
import asyncio
import model
import tqdm as notebook_tqdm
import tkinter as tk

root = tk.Tk()
root.geometry("400x200")
root.title("Input Data!")

# creating header
header_label = tk.Label(root, text="Scraping Data",
                        font=('sans-serif', 10, 'bold'), justify='center')
header_label.pack()


def on_button_click():
    root.withdraw()


# creating input form
input_form = tk.Frame(root)
input_form.pack()

# company name
company_name = tk.StringVar()

# input date
start_date = date.today()
end_date = date.today()

# creating components in input form
name_company = tk.Label(
    input_form, text="Enter the name of company: ", font=('sans-serif', 10, 'normal'))
name_entry = tk.Entry(input_form, textvariable=company_name, font=(
    'sans-serif', 10, 'normal'), justify='left')

start_date_text = tk.Label(input_form, text="Choose start date: ",
                           font=('sans-serif', 10, 'normal'))
end_date_text = tk.Label(input_form, text="Choose end date: ",
                         font=('sans-serif', 10, 'normal'))
cal_start = DateEntry(input_form, selectmode='day', date_pattern='dd/mm/yyyy')
cal_end = DateEntry(input_form, selectmode='day', date_pattern='dd/mm/yyyy')

# creating auto update start date function when choose in Date Entry


def update_start_date(event):
    global start_date
    start_date = cal_start.get_date()
    check_date_range()

# creating auto update end date function when choose in Date Entry


def update_end_date(event):
    global end_date
    end_date = cal_end.get_date()
    check_date_range()

# creating check valid date function


def check_date_range():
    if start_date and end_date and start_date > end_date:
        messagebox.showerror(
            "Error", "End date must be greater than start date.")

# creating set start date function when click set button


def get_date_start():
    # triggered on Button Click
    l1 = tk.Label(input_form, text='data', bg='yellow')
    l1.grid(row=2, column=2, sticky='w', padx=(10, 0))
    l1.config(text=cal_start.get_date().strftime("%d/%m/%Y"))

# creating set end date function when click set button


def get_date_end():
    check_date_range()
    l2 = tk.Label(input_form, text='data', bg='yellow')
    l2.grid(row=3, column=2, sticky='w', padx=(10, 0))
    l2.config(text=cal_end.get_date().strftime("%d/%m/%Y"))


# creating button set
button_start = tk.Button(
    input_form, text='Set', command=get_date_start)
button_end = tk.Button(input_form, text='Set', command=get_date_end)
submit = tk.Button(input_form, text='SUBMIT', command=on_button_click)

# auto update when selected date entry
cal_start.bind("<<DateEntrySelected>>", update_start_date)
cal_end.bind("<<DateEntrySelected>>", update_end_date)

# creating all components
name_company.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
start_date_text.grid(row=2, column=0, sticky='e')
cal_start.grid(row=2, column=1, sticky='w')
button_start.grid(row=2, column=1, sticky='e')
end_date_text.grid(row=3, column=0, sticky='e')
cal_end.grid(row=3, column=1, sticky='w')
button_end.grid(row=3, column=1, sticky='e')
submit.grid(row=4, column=1, sticky='w')

root.mainloop()

print("test test")
