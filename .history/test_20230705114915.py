from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

headers = ["title", "date", "content"]
rows = [("Trở thành ngân hàng mẹ của Ngân hàng Xây dựng, Vietcombank được gì?", "2023-06-06", "Classical mechanics"),
        ("Nhận chuyển giao ngân hàng yếu kém: MB, Vietcombank, HDBank và VPBank đã thực hiện đến đâu?",
         "1879-03-14", "Relativity"),
        ("Darwin", "1809-02-12", "Evolution")]


class TableModel(QAbstractTableModel):
    def rowCount(self, parent):
        return len(rows)

    def columnCount(self, parent):
        return len(headers)

    def data(self, index, role):
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()
        return rows[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal:
            return QVariant()
        return headers[section]


app = QApplication([])
model = TableModel()
view = QTableView()
view.setModel(model)

header = view.horizontalHeader()
header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

view.show()
app.exec()

print("lalalalala")
