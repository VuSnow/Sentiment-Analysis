import tkinter as tk
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QWindow, QGuiApplication
import sys

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

# Nhúng cửa sổ PyQt vào cửa sổ Tkinter
window_handle = root.winfo_id()
pyqt_window = QWindow.fromWinId(window_handle)
pyqt_window.setFlags(pyqt_window.flags() | Qt.FramelessWindowHint)
pyqt_window.winId()
window.createWinId()

root.mainloop()
