from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import Qt
import sys
from pr import *
app=QtWidgets.QApplication([])
q=uic.loadUi("блюда.ui")
L=Menu()
print("Всего блюд:", len(L.menu_dict))
def updateTable():
    q.tableWidget.setRowCount(len(L.menu_dict))
    row = 0
    for dish in L.menu_dict.values():
        q.tableWidget.setItem(row, 0, QTableWidgetItem(dish.name))
        q.tableWidget.setItem(row, 1, QTableWidgetItem(dish.category))
        q.tableWidget.setItem(row, 2, QTableWidgetItem(str(dish.price)))
        q.tableWidget.setItem(row, 3, QTableWidgetItem(str(dish.weight)))
        for col in range(q.tableWidget.columnCount()):
            q.tableWidget.item(row, col).setTextAlignment(Qt.AlignCenter)
        row += 1
    q.tableWidget.resizeRowsToContents()
    q.tableWidget.resizeColumnsToContents()
    q.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
def btnLoadTable():
    updateTable()
def btnAppendTable():
    str = q.lineEdit.text()
    L.appendDish(str)
    updateTable()
    q.lineEdit.clear()  
def btnDeleteTable():
    selected_row = q.tableWidget.currentRow()
    if selected_row >= 0:
        selected_name = q.tableWidget.item(selected_row, 0).text()
        L.deleteDish(selected_name)
        updateTable()

def btnUpdateTable():
    selected_row = q.tableWidget.currentRow()
    if selected_row >= 0:
        selected_name = q.tableWidget.item(selected_row, 0).text()
        new_name = q.lineEdit_2.text() 
        new_category = q.lineEdit_3.text()  
        new_price = q.lineEdit_4.text()  
        new_weight = q.lineEdit_5.text()  
        L.updateDish(selected_name, new_name, new_category, new_price, new_weight)
        updateTable()
q.pushButton_5.clicked.connect(btnUpdateTable)
q.pushButton.clicked.connect(btnLoadTable)
q.pushButton_3.clicked.connect(btnAppendTable)
q.show()
sys.exit(app.exec())
