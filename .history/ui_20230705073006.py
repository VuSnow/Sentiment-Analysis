import tkinter as tk

root = tk.Tk()
root.geometry("600x800")
header_label = tk.Label(root, text="Scraping Data",
                        font=('sans-serif', 12, 'bold'), justify='center')
header_label.pack()
# header_label.grid(row=0, column=1)
root.mainloop()
