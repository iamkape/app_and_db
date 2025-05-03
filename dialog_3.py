import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QApplication, QLineEdit, QGridLayout



class Ui_Dialog_3(QtWidgets.QDialog):
    send_to_d2 = pyqtSignal(dict)
    def __init__(self, table, row, parent=None):
        super().__init__(parent)
        self.grid = QGridLayout(self)
        self.con = sqlite3.connect('warehouse.db')
        self.table = table
        self.row = row #str type or None
        self.setObjectName("Dialog_3")
        self.resize(400, 800)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        # self.lineEdit = QtWidgets.QLineEdit(self)
        # self.lineEdit.setGeometry(QtCore.QRect(30, 30, 113, 25))
        # self.lineEdit.setObjectName("lineEdit")
        # self.lineEdit_2 = QtWidgets.QLineEdit(self)
        # self.lineEdit_2.setGeometry(QtCore.QRect(30, 90, 113, 25))
        # self.lineEdit_2.setObjectName("lineEdit_2")
        # self.lineEdit_3 = QtWidgets.QLineEdit(self)
        # self.lineEdit_3.setGeometry(QtCore.QRect(30, 150, 113, 25))
        # self.lineEdit_3.setObjectName("lineEdit_3")
        # self.lineEdit_4 = QtWidgets.QLineEdit(self)
        # self.lineEdit_4.setGeometry(QtCore.QRect(30, 210, 113, 25))
        # self.lineEdit_4.setObjectName("lineEdit_4")
        # self.lineEdit_5 = QtWidgets.QLineEdit(self)
        # self.lineEdit_5.setGeometry(QtCore.QRect(30, 270, 113, 25))
        # self.lineEdit_5.setObjectName("lineEdit_5")
        # self.lineEdit_6 = QtWidgets.QLineEdit(self)
        # self.lineEdit_6.setGeometry(QtCore.QRect(30, 330, 113, 25))
        # self.lineEdit_6.setObjectName("lineEdit_6")
        # self.lineEdit_7 = QtWidgets.QLineEdit(self)
        # self.lineEdit_7.setGeometry(QtCore.QRect(30, 390, 113, 25))
        # self.lineEdit_7.setObjectName("lineEdit_7")
        # self.lineEdit_8 = QtWidgets.QLineEdit(self)
        # self.lineEdit_8.setGeometry(QtCore.QRect(30, 450, 113, 25))
        # self.lineEdit_8.setObjectName("lineEdit_8")
        # self.lineEdit_9 = QtWidgets.QLineEdit(self)
        # self.lineEdit_9.setGeometry(QtCore.QRect(30, 510, 113, 25))
        # self.lineEdit_9.setObjectName("lineEdit_9")
        # self.label_1 = QtWidgets.QLabel(self)
        # self.label_1.setGeometry(QtCore.QRect(160, 30, 67, 17))
        # self.label_1.setObjectName("label_1")
        # self.label_2 = QtWidgets.QLabel(self)
        # self.label_2.setGeometry(QtCore.QRect(160, 80, 67, 17))
        # self.label_2.setObjectName("label_2")
        # self.label_3 = QtWidgets.QLabel(self)
        # self.label_3.setGeometry(QtCore.QRect(170, 120, 67, 17))
        # self.label_3.setObjectName("label_3")
        # self.label_4 = QtWidgets.QLabel(self)
        # self.label_4.setGeometry(QtCore.QRect(160, 190, 67, 17))
        # self.label_4.setObjectName("label_4")
        # self.label_5 = QtWidgets.QLabel(self)
        # self.label_5.setGeometry(QtCore.QRect(160, 250, 67, 17))
        # self.label_5.setObjectName("label_5")
        # self.label_6 = QtWidgets.QLabel(self)
        # self.label_6.setGeometry(QtCore.QRect(180, 300, 67, 17))
        # self.label_6.setObjectName("label_6")
        # self.label_7 = QtWidgets.QLabel(self)
        # self.label_7.setGeometry(QtCore.QRect(190, 370, 67, 17))
        # self.label_7.setObjectName("label_7")
        # self.label_8 = QtWidgets.QLabel(self)
        # self.label_8.setGeometry(QtCore.QRect(190, 420, 67, 17))
        # self.label_8.setObjectName("label_8")
        if row is None:
            self.retranslateUi(self, None, table)
        else:
            self.retranslateUi(self, row, table)

        self.buttonBox.accepted.connect(self.btn_ok)
        self.buttonBox.rejected.connect(self.cancel)

    def retranslateUi(self, Dialog_3,row,table):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog_3", "Dialog 3"))
        if row is None:
            self.data_lineedit = []
            with self.con:
                rows_info = self.con.execute(f'Pragma table_info ("{self.table}")').fetchall()
                name_of_column = [i[1] for i in rows_info]
                for i in range(len(name_of_column)):
                    label_name = f'label_{i}'
                    label = QLabel(f'{name_of_column[i]}')
                    line_name = f'lineedit_{i}'
                    lineedit = QLineEdit(self)
                    setattr(self, label_name, label)
                    setattr(self, line_name, lineedit)
                    self.grid.addWidget(lineedit, i+1, 0)
                    self.grid.setSpacing(1)
                    self.grid.addWidget(label, i+1, 1)
                    self.setLayout(self.grid)
                    self.grid.setSpacing(10)
                    self.grid.setVerticalSpacing(1)
                    self.data_lineedit.append(lineedit)
                self.grid.addWidget(self.buttonBox)
        else:
            self.data_lineedit = []
            with self.con:
                rows_info = self.con.execute(f'Pragma table_info ("{self.table}")').fetchall()
                name_of_column = [i[1] for i in rows_info]
                row_text = self.con.execute(f'SELECT * FROM {table} WHERE id={row}').fetchone()
                for i in range(len(name_of_column)):
                    label_name = f'label_{i}'
                    label = QLabel(f'{name_of_column[i]}')
                    line_name = f'lineedit_{i}'
                    lineedit = QLineEdit(self)
                    lineedit.setText(str(row_text[i]))
                    setattr(self, label_name, label)
                    setattr(self, line_name, lineedit)
                    self.grid.addWidget(lineedit, i+1, 0)
                    self.grid.setSpacing(1)
                    self.grid.addWidget(label, i+1, 1)
                    self.setLayout(self.grid)
                    self.grid.setSpacing(10)
                    self.grid.setVerticalSpacing(1)
                    self.data_lineedit.append(lineedit)
                self.grid.addWidget(self.buttonBox)
                # s = 30
                # for i in range(len(name_of_column)):
                #     lab = QLabel(name_of_column[i], self)
                #     QtWidgets.QLabel.setText(lab, name_of_column[i])
                #     lab.setGeometry(160, s, 67, 17)
                #     line = QtWidgets.QLineEdit(self)
                #     line.setGeometry(30, s, 113, 25)
                #     s += 60
        # else:
        #     with self.con:
        #         rows_info = self.con.execute(f'Pragma table_info ("{self.table}")').fetchall()
        #         row_text = self.con.execute(f'SELECT * FROM {table} WHERE id={row}').fetchone()
        #         name_of_column = [i[1] for i in rows_info]
        #         step_label = 30
        #         step_edit = 30
        #         for i in range(len(name_of_column)):
        #             lab = QLabel(name_of_column[i], self)
        #             QtWidgets.QLabel.setText(lab, name_of_column[i])
        #             lab.setGeometry(160, step_label, 67, 17)
        #             step_label += 60
        #         for i,v in enumerate(row_text):
        #             line = QtWidgets.QLineEdit(self)
        #             # print(line.text())
        #             line.setText(str(v))
        #             line.setGeometry(30, step_edit, 113, 25)
        #             step_edit +=
    def btn_ok(self) -> None:
        new_row = {}
        for i, j in enumerate(self.data_lineedit):
            if j.text() == '':
                new_row[i] = None
            else:
                new_row[i] = j.text()
        self.send_to_d2.emit(new_row)
        QtWidgets.QDialog.close(self)

    def cancel(self):
        QtWidgets.QDialog.close(self)
        print('cancel-----')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dial_2 = Ui_Dialog_3()
    dial_2.show()
    sys.exit(app.exec_())
