import tkinter as tk
from tkinter import messagebox
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


def show_pyqt_window():
    app = QApplication([])
    window = QMainWindow()
    label = QLabel("Hello from PyQt!")
    window.setCentralWidget(label)
    window.show()
    app.exec_()


def show_pyqt_window_from_tkinter():
    # messagebox.showinfo("Message", "Button clicked!")
    show_pyqt_window()


root = tk.Tk()

button = tk.Button(root, text="Click Me",
                   command=show_pyqt_window_from_tkinter)
button.pack()

root.mainloop()
