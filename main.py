from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys
import sqlite3


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.db')
        self.cur = self.con.cursor()
        res = self.cur.execute("""select * from coffee""")
        from PyQt5.QtWidgets import QTableWidgetItem
        self.tableWidget.setColumnCount(6)
        for j, i in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            self.tableWidget.setItem(j, 0, QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(j, 1, QTableWidgetItem(str(i[1])))
            self.tableWidget.setItem(j, 2, QTableWidgetItem(str(i[2])))
            self.tableWidget.setItem(j, 3, QTableWidgetItem(str(i[3])))
            self.tableWidget.setItem(j, 4, QTableWidgetItem(str(i[4])))
            self.tableWidget.setItem(j, 5, QTableWidgetItem(str(i[5])))
            self.tableWidget.setItem(j, 6, QTableWidgetItem(str(i[6])))


app = QApplication(sys.argv)
ex = Example()
ex.show()
app.exit(app.exec())