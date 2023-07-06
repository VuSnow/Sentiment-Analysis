import tkinter as tk

root = tk.Tk()
root.geometry("600x800")
company_nameVar = tk.StringVar()
header_label = tk.Label(root, text="Scraping Data",
                        font=('sans-serif', 10, 'bold'), justify='center')
name_company = tk.Label(
    root, text="Enter the name of company: ", font=('sans-serif', 10, 'normal'))
name_entry = tk.Entry(root, textvariable=company_nameVar, font=(
    'sans-serif', 10, 'normal'), justify='center')
header_label.grid(row=0, column=1)
name_company.grid(row=1, column=0)
root.mainloop()
