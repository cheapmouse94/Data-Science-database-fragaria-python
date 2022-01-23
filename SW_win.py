from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np

def window_execute(self, DB, TB):
    self.DB = DB
    self.TB = TB
    self.setObjectName("MainWindow")
    self.resize(500, 500)
    self.setMinimumSize(QtCore.QSize(500, 500))
    self.setMaximumSize(QtCore.QSize(500, 600))
    self.FW_main = QtWidgets.QWidget(self)
    self.FW_main.setMinimumSize(QtCore.QSize(500, 500))
    self.FW_main.setMaximumSize(QtCore.QSize(500, 600))
    self.FW_main.setObjectName("FW_main")
    self.verticalLayout = QtWidgets.QVBoxLayout(self.FW_main)
    self.verticalLayout.setContentsMargins(20, 20, 20, 20)
    self.verticalLayout.setSpacing(10)
    self.verticalLayout.setObjectName("verticalLayout")
    self.Frame_Central = QtWidgets.QFrame(self.FW_main)
    self.Frame_Central.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.Frame_Central.setFrameShadow(QtWidgets.QFrame.Raised)
    self.Frame_Central.setObjectName("Frame_Central")
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
    self.Label_sub_1.setGeometry(QtCore.QRect(100, 50, 81, 31))
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
    self.Combo_sub_1.setGeometry(QtCore.QRect(190, 50, 171, 31))
    self.Combo_sub_1.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
    self.Combo_sub_1.setObjectName("Combo_sub_1")
    self.Combo_sub_1.addItem("")
    self.Combo_sub_1.addItem("")
    self.Label_sub_2 = QtWidgets.QLabel(self.Frame_Central)
    self.Label_sub_2.setGeometry(QtCore.QRect(100, 100, 81, 31))
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
    self.BTN_execute.setGeometry(QtCore.QRect(180, 350, 111, 31))
    font = QtGui.QFont()
    font.setPointSize(10)
    self.BTN_execute.setFont(font)
    self.BTN_execute.setObjectName("BTN_execute")
    self.Combo_sub_2 = QtWidgets.QComboBox(self.Frame_Central)
    self.Combo_sub_2.setGeometry(QtCore.QRect(190, 100, 171, 31))
    self.Combo_sub_2.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
    self.Combo_sub_2.setObjectName("Combo_sub_2")
    self.listWidget = QtWidgets.QListWidget(self.Frame_Central)
    self.listWidget.setGeometry(QtCore.QRect(80, 250, 301, 81))
    self.listWidget.setObjectName("listWidget")
    self.BTN_add_cond_1 = QtWidgets.QPushButton(self.Frame_Central)
    self.BTN_add_cond_1.setGeometry(QtCore.QRect(120, 200, 101, 31))
    font = QtGui.QFont()
    font.setPointSize(10)
    self.BTN_add_cond_1.setFont(font)
    self.BTN_add_cond_1.setObjectName("BTN_add_cond_1")
    self.BTN_clear_cond_1 = QtWidgets.QPushButton(self.Frame_Central)
    self.BTN_clear_cond_1.setGeometry(QtCore.QRect(250, 200, 101, 31))
    font = QtGui.QFont()
    font.setPointSize(10)
    self.BTN_clear_cond_1.setFont(font)
    self.BTN_clear_cond_1.setObjectName("BTN_clear_cond_1")
    self.Combo_sub_3 = QtWidgets.QComboBox(self.Frame_Central)
    self.Combo_sub_3.setGeometry(QtCore.QRect(190, 150, 171, 31))
    self.Combo_sub_3.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
    self.Combo_sub_3.setObjectName("Combo_sub_3")
    self.Combo_sub_3.addItem("")
    self.Combo_sub_3.addItem("")
    self.Label_sub_3 = QtWidgets.QLabel(self.Frame_Central)
    self.Label_sub_3.setGeometry(QtCore.QRect(100, 150, 81, 31))
    font = QtGui.QFont()
    font.setPointSize(10)
    font.setBold(False)
    font.setItalic(False)
    font.setUnderline(False)
    font.setWeight(50)
    font.setStrikeOut(False)
    font.setKerning(True)
    self.Label_sub_3.setFont(font)
    self.Label_sub_3.setObjectName("Label_sub_3")
    self.verticalLayout.addWidget(self.Frame_Central)
    self.setCentralWidget(self.FW_main)
    QtCore.QMetaObject.connectSlotsByName(self)
    _translate = QtCore.QCoreApplication.translate
    self.setWindowTitle(_translate("MainWindow", "MainWindow"))
    self.Label_main.setText(_translate("MainWindow", "Sortowanie komórek"))
    self.Label_sub_1.setText(_translate("MainWindow", "Orientacja:"))
    self.Combo_sub_1.setItemText(0, _translate("MainWindow", "Wiersze"))
    self.Combo_sub_1.setItemText(1, _translate("MainWindow", "Kolumny"))
    self.Label_sub_2.setText(_translate("MainWindow", "Oś:"))
    self.BTN_execute.setText(_translate("MainWindow", "Wykonaj!"))
    self.BTN_add_cond_1.setText(_translate("MainWindow", "Dodaj"))
    self.BTN_clear_cond_1.setText(_translate("MainWindow", "Wyczyść"))
    self.Combo_sub_3.setItemText(0, _translate("MainWindow", "Rosnąco"))
    self.Combo_sub_3.setItemText(1, _translate("MainWindow", "Malejąco"))
    self.Label_sub_3.setText(_translate("MainWindow", "Sortuj:"))


    def refresh_a(db, a, b):
        b.clear()
        db_idx_list = list(db.index)
        db_col_list = list(db.columns)
        if a.currentText() == "Wiersze":
            for x in range(len(db_idx_list)):
                b.addItem("")
                b.setItemText(x, str(db.index[x]))
        elif a.currentText() == "Kolumny":
            for x in range(len(db_col_list)):
                b.addItem("")
                b.setItemText(x, str(db.columns[x]))

    def add_cond(b, c, d):
        b.addItem(f"{c.currentText()}: "+d.currentText())
        
    def clear_cond(a):
        if a is not None and len(a.selectedItems()) == 1:
            a.takeItem(a.currentRow())

    def execute_function(lst, cs1, db, tb):
        srt_by = []
        srt_asc = []
        if cs1.currentText() == 'Kolumny':
            for x in range(lst.count()):
                lw1s = lst.item(x).text().split(': ',1)[1]
                lw1n = lst.item(x).text().split(': ',1)[0]
                if lw1s == 'Rosnąco':
                    srt_asc.append(True)
                elif lw1s == 'Malejąco':
                    srt_asc.append(False)
                srt_by.append(lw1n)

            db = db.sort_values(by=srt_by, ascending=srt_asc)
            print(srt_by, srt_asc)
            self.refresh_table(db,tb)
            try:
                pass
            except:
                print('Nieprawidłowe sortowanie tabeli')


    self.Combo_sub_1.currentIndexChanged.connect(lambda: refresh_a(self.DB, self.Combo_sub_1, self.Combo_sub_2))
    self.BTN_add_cond_1.clicked.connect(lambda: add_cond(self.listWidget, self.Combo_sub_2, self.Combo_sub_3))
    self.BTN_clear_cond_1.clicked.connect(lambda: clear_cond(self.listWidget))
    self.BTN_execute.clicked.connect(lambda: execute_function(self.listWidget, self.Combo_sub_1, self.DB, self.TB))
    refresh_a(self.DB, self.Combo_sub_1, self.Combo_sub_2)