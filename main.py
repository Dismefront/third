from PyQt5.QtWidgets import QApplication, QMainWindow
from addEditCoffeeForm import Ui_MainWindow as SEcond
from MainWidget import Ui_MainWindow as FIrst
import sys
import sqlite3


con = sqlite3.connect('data/coffee.db')
cur = con.cursor()


class Example(QMainWindow, FIrst):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.edit)
        self.pushButton_2.clicked.connect(self.refresh)
        res = cur.execute("""select * from coffee""")
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

    def edit(self):
        ex = AddWindow(self)
        ex.show()

    def refresh(self):
        self.tableWidget.clear()
        res = cur.execute("""select * from coffee""")
        from PyQt5.QtWidgets import QTableWidgetItem
        self.tableWidget.setColumnCount(6)
        for j, i in enumerate(res):
            self.tableWidget.setRowCount(j + 1)
            self.tableWidget.setItem(j, 0, QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(j, 1, QTableWidgetItem(str(i[1])))
            self.tableWidget.setItem(j, 2, QTableWidgetItem(str(i[2])))
            self.tableWidget.setItem(j, 3, QTableWidgetItem(str(i[3])))
            self.tableWidget.setItem(j, 4, QTableWidgetItem(str(i[4])))
            self.tableWidget.setItem(j, 5, QTableWidgetItem(str(i[5])))
            self.tableWidget.setItem(j, 6, QTableWidgetItem(str(i[6])))


class AddWindow(QMainWindow, SEcond):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.dl)

    def add(self):
        sort = self.lineEdit.text()
        roast = self.lineEdit_2.text()
        type = self.lineEdit_3.text()
        desc = self.lineEdit_4.text()
        pr = self.lineEdit_5.text()
        cap = self.lineEdit_6.text()
        cur.execute(f"""insert into coffee(sort, roast, type, 
                    description, price, capacity)
                    values('{sort}', {roast}, '{type}', 
                    '{desc}', {pr}, {cap})""")
        con.commit()

    def dl(self):
        id = self.lineEdit_7.text()
        cur.execute(f"""delete from coffee where id = {id}""")
        con.commit()


app = QApplication(sys.argv)
ex = Example()
ex.show()
app.exit(app.exec())