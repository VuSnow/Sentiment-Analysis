import tkinter as tk

root = tk.Tk()
root.geometry("600x800")
header_label = tk.Label(root, text="Scraping Data",
                        font=('sans-serif', 10, 'bold'), justify='center')
name_company = tk.Label(
    root, text="Enter the name of company: ", font=('sans-serif', 10, 'normal'))
header_label.grid(row=0, column=1)
name_company.grid(row=1, column=0)
# header_label.grid(row=0, column=1)
root.mainloop()
