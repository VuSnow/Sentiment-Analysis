import tkinter as tk
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys
import win32gui

# Tạo ứng dụng PyQt
app = QApplication(sys.argv)

# Tạo cửa sổ PyQt
window = QWidget()
layout = QVBoxLayout()
label = QLabel("Hello from PyQt")
layout.addWidget(label)
window.setLayout(layout)
window.show()

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Tkinter with PyQt")
root.geometry("400x300")

# Lấy handle (HWND) của cửa sổ Tkinter
window_handle = root.winfo_id()

# Lấy handle (HWND) của cửa sổ PyQt
pyqt_window = window.winId()

# Nhúng cửa sổ PyQt vào cửa sổ Tkinter
win32gui.SetWindowLong(window_handle, win32gui.GWL_STYLE,
                       win32gui.WS_CHILD | win32gui.WS_VISIBLE)
win32gui.SetParent(pyqt_window, window_handle)

root.mainloop()
