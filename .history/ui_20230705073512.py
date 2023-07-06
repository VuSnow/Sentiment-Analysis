import tkinter as tk

root = tk.Tk()
root.geometry("600x800")
header_label = tk.Label(root, text="Scraping Data",
                        font=('sans-serif', 12, 'bold'), justify='center')
sub_btn = tk.Button(root, text='Submit')
header_label.grid(row=0, column=1)
sub_btn.grid(row=1, column=0)
# header_label.grid(row=0, column=1)
root.mainloop()
