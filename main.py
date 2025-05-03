from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from dialog_2 import  Ui_Dialog_2

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 130, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 130, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 130, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 130, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Position"))
        self.pushButton_2.setText(_translate("MainWindow", "Product_property"))
        self.pushButton_3.setText(_translate("MainWindow", "Warehouse"))
        self.pushButton_4.setText(_translate("MainWindow", "Worker"))
        self.pushButton.clicked.connect(partial(self.tabla,"Position"))
        self.pushButton_2.clicked.connect(partial(self.tabla,"Product_property"))
        self.pushButton_3.clicked.connect(partial(self.tabla,"Warehouse"))
        self.pushButton_4.clicked.connect(partial(self.tabla,"Worker"))


    def tabla(self, table_name):
        ui = Ui_Dialog_2(table_name)
        ui.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.show()
    # MainWindow.show()
    sys.exit(app.exec_())
