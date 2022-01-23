from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np


def window_execute(self, DB, TB):
    self.DB = DB
    self.TB = TB
    self.setObjectName("MainWindow")
    self.resize(500, 600)
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
    self.Label_sub_1.setGeometry(QtCore.QRect(60, 50, 141, 31))
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
    self.Combo_sub_1.setGeometry(QtCore.QRect(210, 50, 161, 31))
    self.Combo_sub_1.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
    self.Combo_sub_1.setObjectName("Combo_sub_1")
    self.Combo_sub_1.addItem("")
    self.Combo_sub_1.addItem("")
    self.Label_sub_2 = QtWidgets.QLabel(self.Frame_Central)
    self.Label_sub_2.setGeometry(QtCore.QRect(60, 100, 141, 31))
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
    self.BTN_execute.setGeometry(QtCore.QRect(160, 300, 111, 31))
    self.BTN_execute.setFont(font)
    self.BTN_execute.setObjectName("BTN_execute")
    self.BTN_execute_2 = QtWidgets.QPushButton(self.Frame_Central)
    self.BTN_execute_2.setGeometry(QtCore.QRect(160, 510, 111, 31))
    self.BTN_execute_2.setFont(font)
    self.BTN_execute_2.setObjectName("BTN_execute")
    self.Combo_sub_2 = QtWidgets.QComboBox(self.Frame_Central)
    self.Combo_sub_2.setGeometry(QtCore.QRect(210, 100, 161, 31))
    self.Combo_sub_2.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
    self.Combo_sub_2.setObjectName("Combo_sub_2")
    self.Label_sub_3 = QtWidgets.QLabel(self.Frame_Central)
    self.Label_sub_3.setGeometry(QtCore.QRect(60, 140, 331, 31))
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
    self.listWidget = QtWidgets.QListWidget(self.Frame_Central)
    self.listWidget.setGeometry(QtCore.QRect(60, 220, 311, 61))
    self.listWidget.setObjectName("listWidget")
    self.Label_sub_4 = QtWidgets.QLabel(self.Frame_Central)
    self.Label_sub_4.setGeometry(QtCore.QRect(60, 350, 331, 31))
    font = QtGui.QFont()
    font.setPointSize(10)
    font.setBold(False)
    font.setItalic(False)
    font.setUnderline(False)
    font.setWeight(50)
    font.setStrikeOut(False)
    font.setKerning(True)
    self.Label_sub_4.setFont(font)
    self.Label_sub_4.setObjectName("Label_sub_4")
    self.listWidget_2 = QtWidgets.QListWidget(self.Frame_Central)
    self.listWidget_2.setGeometry(QtCore.QRect(60, 430, 311, 61))
    self.listWidget_2.setObjectName("listWidget_2")
    self.lineEdit_add_cond_1 = QtWidgets.QLineEdit(self.Frame_Central)
    self.lineEdit_add_cond_1.setGeometry(QtCore.QRect(60, 180, 141, 31))
    self.lineEdit_add_cond_1.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
    self.lineEdit_add_cond_1.setObjectName("lineEdit_add_cond_1")
    self.BTN_add_cond_1 = QtWidgets.QPushButton(self.Frame_Central)
    self.BTN_add_cond_1.setGeometry(QtCore.QRect(210, 180, 71, 31))
    font = QtGui.QFont()
    font.setPointSize(10)
    self.BTN_add_cond_1.setFont(font)
    self.BTN_add_cond_1.setObjectName("BTN_add_cond_1")
    self.BTN_clear_cond_1 = QtWidgets.QPushButton(self.Frame_Central)
    self.BTN_clear_cond_1.setGeometry(QtCore.QRect(290, 180, 81, 31))
    font = QtGui.QFont()
    font.setPointSize(10)
    self.BTN_clear_cond_1.setFont(font)
    self.BTN_clear_cond_1.setObjectName("BTN_clear_cond_1")
    self.BTN_add_cond_2 = QtWidgets.QPushButton(self.Frame_Central)
    self.BTN_add_cond_2.setGeometry(QtCore.QRect(210, 390, 71, 31))
    font = QtGui.QFont()
    font.setPointSize(10)
    self.BTN_add_cond_2.setFont(font)
    self.BTN_add_cond_2.setObjectName("BTN_add_cond_2")
    self.BTN_clear_cond_2 = QtWidgets.QPushButton(self.Frame_Central)
    self.BTN_clear_cond_2.setGeometry(QtCore.QRect(290, 390, 81, 31))
    font = QtGui.QFont()
    font.setPointSize(10)
    self.BTN_clear_cond_2.setFont(font)
    self.BTN_clear_cond_2.setObjectName("BTN_clear_cond_2")
    self.lineEdit_add_cond_2 = QtWidgets.QLineEdit(self.Frame_Central)
    self.lineEdit_add_cond_2.setGeometry(QtCore.QRect(60, 390, 141, 31))
    self.lineEdit_add_cond_2.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
    self.lineEdit_add_cond_2.setObjectName("lineEdit_add_cond_2")
    self.verticalLayout.addWidget(self.Frame_Central)
    self.setCentralWidget(self.FW_main)
    _translate = QtCore.QCoreApplication.translate
    self.setWindowTitle(_translate("MainWindow", "MainWindow"))
    self.Label_main.setText(_translate("MainWindow", "Filtrowanie komórek"))
    self.Label_sub_1.setText(_translate("MainWindow", "Orientacja:"))
    self.Combo_sub_1.setItemText(0, _translate("MainWindow", "Wiersze"))
    self.Combo_sub_1.setItemText(1, _translate("MainWindow", "Kolumny"))
    self.Label_sub_2.setText(_translate("MainWindow", "Wartość wstępna:"))
    self.BTN_execute.setText(_translate("MainWindow", "Wykonaj!"))
    self.BTN_execute_2.setText(_translate("MainWindow", "Wykonaj!"))
    self.Label_sub_3.setText(_translate("MainWindow", "Szukaj względem np. (>50, <20, \"Polska\" itp.):"))
    self.Label_sub_4.setText(_translate("MainWindow", "Wyrzuć np. (>100, 0, \"Niemcy\" itp.):"))
    self.BTN_add_cond_1.setText(_translate("MainWindow", "Dodaj"))
    self.BTN_clear_cond_1.setText(_translate("MainWindow", "Wyczyść"))
    self.BTN_add_cond_2.setText(_translate("MainWindow", "Dodaj"))
    self.BTN_clear_cond_2.setText(_translate("MainWindow", "Wyczyść"))
    QtCore.QMetaObject.connectSlotsByName(self)


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

    def add_cond(a, b, c):
        if a.text() != '':
            b.addItem(f"{c.currentText()}: "+a.text())
        
    def clear_cond(a):
        if a is not None and len(a.selectedItems()) == 1:
            a.takeItem(a.currentRow())

    def execute_fn_cnd(lw1, cs2):
        cond_mem = []
        for x in range(lw1.count()):
            lw1s = lw1.item(x).text().split(': ',1)[1]
            lw1n = lw1.item(x).text().split(': ',1)[0]
            #1. Przedziały
            if lw1s.find('<') == 0 or lw1s.find('>') == 0:
                if lw1s.find('<') == 0:
                    sign = '<'
                elif lw1s.find('>') == 0:
                    sign = '>'
                yn = lw1s.split(sign,1) 
                try:
                    cond_mem.append([sign, int(yn[1]), lw1n])
                except:
                    print(f"Sprawdź poprwność wprowadzenia wyjątku w: {lw1s}")
                    break
            else:
                #2. Liczby
                try:
                    if int(lw1s) or float(lw1s):
                        cond_mem.append(['Int / Float', lw1s, lw1n])
                        
                except:
                    try:
                        #3. Boolean
                        if eval(lw1s) is True or eval(lw1s) is False:
                            cond_mem.append(['Bool', lw1s, lw1n])
                    except:
                        try:
                            #4. String
                            cond_mem.append(['Str', lw1s, lw1n])
                        except:
                            pass
        return cond_mem

    def execute_function_1(db, lw1, lw2, cs1, cs2, tb):
        cond_mem = execute_fn_cnd(lw1, cs2)
  
        if cs1.currentText() == 'Kolumny':

            for i in cond_mem:
                if i[0] == '>':
                    db = db.loc[db[i[2]]>i[1]]
                elif i[0] == '<':
                    db = db.loc[db[i[2]]<i[1]]
                elif i[0] == 'Int / Float':
                    db = db.loc[db[i[2]]==eval(i[1])]
                elif i[0] == 'Bool':
                    db = db.loc[db[i[2]]==eval(i[1])]
                elif i[0] == 'Str':
                    db = db.loc[db[i[2]]==str(i[1])]

            self.refresh_table(db,tb)

    def execute_function_2(db, lw1, lw2, cs1, cs2, tb):
        cond_mem = execute_fn_cnd(lw2, cs2)
  
        if cs1.currentText() == 'Kolumny':

            for i in cond_mem:
                if i[0] == '>':
                    db = db.loc[~(db[i[2]]>i[1])]
                elif i[0] == '<':
                    db = db.loc[~(db[i[2]]<i[1])]
                elif i[0] == 'Int / Float':
                    db = db.loc[~(db[i[2]]==eval(i[1]))]
                elif i[0] == 'Bool':
                    db = db.loc[~(db[i[2]]==eval(i[1]))]
                elif i[0] == 'Str':
                    db = db.loc[~(db[i[2]]==str(i[1]))]

            self.refresh_table(db,tb)


    self.Combo_sub_1.currentIndexChanged.connect(lambda: refresh_a(self.DB, self.Combo_sub_1, self.Combo_sub_2))
    self.BTN_add_cond_1.clicked.connect(lambda: add_cond(self.lineEdit_add_cond_1, self.listWidget, self.Combo_sub_2))
    self.BTN_clear_cond_1.clicked.connect(lambda: clear_cond(self.listWidget))
    self.BTN_add_cond_2.clicked.connect(lambda: add_cond(self.lineEdit_add_cond_2, self.listWidget_2, self.Combo_sub_2))
    self.BTN_clear_cond_2.clicked.connect(lambda: clear_cond(self.listWidget_2))
    self.BTN_execute.clicked.connect(lambda: execute_function_1(self.DB, self.listWidget, self.listWidget_2, self.Combo_sub_1, self.Combo_sub_2, self.TB))
    self.BTN_execute_2.clicked.connect(lambda: execute_function_2(self.DB, self.listWidget, self.listWidget_2, self.Combo_sub_1, self.Combo_sub_2, self.TB))
    refresh_a(self.DB, self.Combo_sub_1, self.Combo_sub_2)