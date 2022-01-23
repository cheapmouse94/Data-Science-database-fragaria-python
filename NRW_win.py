from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np


def window_execute(self, DB, TB):
    self.DB = DB
    self.TB = TB
    self.setObjectName("MainWindow")
    self.resize(500, 300)
    self.setMinimumSize(QtCore.QSize(500, 300))
    self.setMaximumSize(QtCore.QSize(500, 300))
    self.NCW_main = QtWidgets.QWidget(self)
    self.NCW_main.setMinimumSize(QtCore.QSize(500, 300))
    self.NCW_main.setMaximumSize(QtCore.QSize(500, 300))
    self.NCW_main.setObjectName("NCW_main")
    self.verticalLayout = QtWidgets.QVBoxLayout(self.NCW_main)
    self.verticalLayout.setContentsMargins(20, 20, 20, 20)
    self.verticalLayout.setSpacing(10)
    self.verticalLayout.setObjectName("verticalLayout")
    self.Frame_Central = QtWidgets.QFrame(self.NCW_main)
    self.Frame_Central.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.Frame_Central.setFrameShadow(QtWidgets.QFrame.Raised)
    self.Frame_Central.setObjectName("Frame_Central")
    self.LineEdit_sub_2 = QtWidgets.QLineEdit(self.Frame_Central)
    self.LineEdit_sub_2.setGeometry(QtCore.QRect(210, 100, 211, 31))
    self.LineEdit_sub_2.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
    self.LineEdit_sub_2.setObjectName("LineEdit_sub_2")
    self.Label_main = QtWidgets.QLabel(self.Frame_Central)
    self.Label_main.setGeometry(QtCore.QRect(0, 0, 331, 31))
    font = QtGui.QFont()
    font.setPointSize(10)
    font.setBold(False)
    font.setItalic(False)
    font.setUnderline(False)
    font.setWeight(50)
    font.setStrikeOut(False)
    font.setKerning(True)
    self.Label_main.setFont(font)
    self.Label_main.setObjectName("Label_main")
    self.Label_sub_1 = QtWidgets.QLabel(self.Frame_Central)
    self.Label_sub_1.setGeometry(QtCore.QRect(0, 50, 201, 31))
    font = QtGui.QFont()
    font.setPointSize(10)
    font.setBold(False)
    font.setItalic(False)
    font.setUnderline(False)
    font.setWeight(50)
    font.setStrikeOut(False)
    font.setKerning(True)
    self.Label_sub_1.setFont(font)
    self.Label_sub_1.setObjectName("Label_sub_1")
    self.Combo_sub_1 = QtWidgets.QComboBox(self.Frame_Central)
    self.Combo_sub_1.setGeometry(QtCore.QRect(210, 50, 211, 31))
    self.Combo_sub_1.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
    self.Combo_sub_1.setObjectName("Combo_sub_1")
    self.Label_sub_2 = QtWidgets.QLabel(self.Frame_Central)
    self.Label_sub_2.setGeometry(QtCore.QRect(0, 100, 201, 31))
    font = QtGui.QFont()
    font.setPointSize(10)
    font.setBold(False)
    font.setItalic(False)
    font.setUnderline(False)
    font.setWeight(50)
    font.setStrikeOut(False)
    font.setKerning(True)
    self.Label_sub_2.setFont(font)
    self.Label_sub_2.setObjectName("Label_sub_2")
    self.BTN_execute = QtWidgets.QPushButton(self.Frame_Central)
    self.BTN_execute.setGeometry(QtCore.QRect(160, 150, 111, 31))
    font = QtGui.QFont()
    font.setPointSize(10)
    self.BTN_execute.setFont(font)
    self.BTN_execute.setObjectName("BTN_execute")
    self.verticalLayout.addWidget(self.Frame_Central)
    self.setCentralWidget(self.NCW_main)

    _translate = QtCore.QCoreApplication.translate
    self.setWindowTitle(_translate("MainWindow", "MainWindow"))
    self.LineEdit_sub_2.setPlaceholderText(_translate("MainWindow", "None"))
    self.Label_main.setText(_translate("MainWindow", "Tworzenie nowego wiersza"))
    self.Label_sub_1.setText(_translate("MainWindow", "Nowy wiersz o indeksie:"))
    self.Label_sub_2.setText(_translate("MainWindow", "Nazwa wiersza:"))
    self.BTN_execute.setText(_translate("MainWindow", "Wykonaj!"))
    QtCore.QMetaObject.connectSlotsByName(self)

    def refresh_c(a, db):
        dbs = db
        db_row_num = np.arange(len(dbs.index)+1)
        a.clear()

        for x in db_row_num:
            a.addItem("")
            a.setItemText(x, str(x))

    def execute_adding(a, b, db, tb):
        combo_text = a.currentText()
        list_text = b.text()
        
        if list_text not in db.index:
            print(f"Dodano nowy wiersz o nazwie: {list_text}")
            
            arr_temp = np.full((1,len(db.columns)),'LILE')
            db.iloc[int(combo_text)] = arr_temp[0]

            refresh_c(a, db)
            self.refresh_table(db, tb)
        else:
            print("Błąd, nie moża stwożyć dwa wiersze o tych samych nazwach")

    refresh_c(self.Combo_sub_1, self.DB)
    self.BTN_execute.clicked.connect(lambda: execute_adding(self.Combo_sub_1,self.LineEdit_sub_2, self.DB, self.TB))
    