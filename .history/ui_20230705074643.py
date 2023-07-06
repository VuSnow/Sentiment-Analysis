import tkinter as tk
from tkcalendar import Calendar

root = tk.Tk()
root.geometry("600x800")


company_nameVar = tk.StringVar()


header_label = tk.Label(root, text="Scraping Data",
                        font=('sans-serif', 10, 'bold'), justify='center')
name_company = tk.Label(
    root, text="Enter the name of company: ", font=('sans-serif', 10, 'normal'))
name_entry = tk.Entry(root, textvariable=company_nameVar, font=(
    'sans-serif', 10, 'normal'), justify='center')
cal = Calendar(root, selectmode='day',
               year=2020, month=5,
               day=22)


header_label.grid(row=0, column=1)
name_company.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
cal.grid(row=2, column=1)


root.mainloop()
