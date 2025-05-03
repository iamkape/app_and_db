from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

from dialog_3 import Ui_Dialog_3
from PyQt5.QtCore import pyqtSignal


class Ui_Dialog_2(QtWidgets.QDialog):
    def __init__(self, table):
        super().__init__()
        self.table = table
        self.changed = {}
        self.con = sqlite3.connect('warehouse.db')
        self.setObjectName("Dialog_2")
        self.resize(900, 750)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(50, 200, 541, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(70, 150, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 150, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 150, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 150, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(35, 510, 801, 141))
        self.listWidget.setObjectName("listWidget")
        self.show_table(table)
        self.pushButton_2.clicked.connect(self.delete_row)
        self.pushButton_4.clicked.connect(self.reset_table)
        self.pushButton_3.clicked.connect(self.save)
        self.pushButton.clicked.connect(self.add)
        self.tableWidget.cellDoubleClicked.connect(self.double_click)
        self.retranslateUi(self)
    def retranslateUi(self, Dialog_2):
        _translate = QtCore.QCoreApplication.translate
        Dialog_2.setWindowTitle(_translate("Dialog_2", "Dialog"))
        self.pushButton.setText(_translate("Dialog_2", "+"))
        self.pushButton_2.setText(_translate("Dialog_2", "-"))
        self.pushButton_3.setText(_translate("Dialog_2", "save"))
        self.pushButton_4.setText(_translate("Dialog_2", "reset"))
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)

    def show_table(self, table) -> None:
        """Данный метод выводит таблицу базы данных в tablewidget"""
        with self.con:
            current_text = table
            rows_info = self.con.execute(f'Pragma table_info ("{current_text}")').fetchall()
            self.name_of_column = [i[1] for i in rows_info]
            # print(self.name_of_column)
            self.table_data = self.con.execute(f'SELECT * FROM {current_text}').fetchall()
            # print(self.table_data)
            self.tableWidget.setHorizontalHeaderLabels(self.name_of_column)
            self.tableWidget.setRowCount(len(self.table_data))
            self.tableWidget.setColumnCount(len(self.name_of_column))
            for x in range(len(self.table_data)):
                for y in range(len(self.table_data[x])):
                    item = QtWidgets.QTableWidgetItem(str(self.table_data[x][y]))
                    if y == 0:
                        item.setFlags(item.flags() & ~ Qt.ItemIsEditable)
                    self.tableWidget.setItem(x, y, item)
            # self.changed = {}

    def delete_row(self) -> None:
        """данный метод удаляет выбранную строку из таблицы"""
        row_id = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        self.tableWidget.removeRow(self.tableWidget.currentRow())
        self.changed[row_id] = None
        self.pushButton_3.setDisabled(False)
        self.pushButton_4.setDisabled(False)

    def reset_table(self) -> None:
        """Сброс таблицы"""
        self.show_table(self.table)
        self.changed = {}
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)

    def save(self) -> None:
        """Сохранение таблицы"""
        cur = self.table
        print(self.changed, 'list changed method save')
        try:
            with self.con:
                for i,j in self.changed.items():
                    if len(self.changed.values()) == 1 and j == None:
                        self.con.execute(f"""DELETE FROM {cur} WHERE id={int(i)}""")
                    else:
                        res = [self.name_of_column[i] for i in self.changed.keys()]
                        print(res,'res method save')
                        col = ', '.join(res)
                        print(col, 'col')
                        que = ', '.join('?' * len(self.changed.values()))
                        query = (f"""INSERT OR REPLACE INTO {cur} ({col}) VALUES ({que})""")
                        print(query)
                        self.con.execute(query, list(self.changed.values()))
            self.listWidget.addItem(f"Сохранение прошло успешно для таблицы {cur}")
            self.changed = {}
        except Exception as e:
            self.listWidget.addItem(f"Ошибка сохранения {e}. База данных не изменилась")
            print(e)
        self.show_table(cur)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)

    def add(self) -> None:
        """Данный метод открывает 3е диалоговое при нажатии кнопки +"""
        self.ui = Ui_Dialog_3(self.table,None)
        self.ui.send_to_d2.connect(self.add_row)
        self.ui.exec_()

    def double_click(self) -> None:
        """Данный метод открывает 3е диалоговое при двойном нажатии"""
        row = self.tableWidget.item(self.tableWidget.currentRow(),0).text()
        self.ui = Ui_Dialog_3(self.table,row)
        self.ui.send_to_d2.connect(self.add_row)
        self.ui.exec_()

    def add_row(self, new: dict) -> None:
        """Данный метод получает список изменений из 3го диалогового окна"""
        self.changed = new
        self.pushButton_3.setDisabled(False)
        self.pushButton_4.setDisabled(False)
        row_number = self.tableWidget.rowCount()
        self.tableWidget.insertRow(int(row_number))
        for i, j in new.items():
            print(i, j)
            self.tableWidget.setItem(int(row_number), i, QTableWidgetItem(j))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dial = Ui_Dialog_2()
    dial.show()
    sys.exit(app.exec_())
