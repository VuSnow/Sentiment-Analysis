import tkinter as tk
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Tkinter Window")
root.geometry("300x200")

# Tạo label trong cửa sổ Tkinter
label_tkinter = tk.Label(root, text="This is a Tkinter label")
label_tkinter.pack()

# Hiển thị cửa sổ Tkinter
root.mainloop()

# Tạo cửa sổ PyQt5
app = QApplication([])
window = QWidget()
window.setWindowTitle("PyQt5 Window")
window.setGeometry(100, 100, 300, 200)

# Tạo label trong cửa sổ PyQt5
label_pyqt5 = QLabel("This is a PyQt5 label", window)
label_pyqt5.move(50, 50)

# Hiển thị cửa sổ PyQt5
window.show()

# Chạy ứng dụng PyQt5
app.exec_()
