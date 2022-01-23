from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def window_execute(self, DB, TB, TP):
    self.DB = DB
    self.TB = TB
    self.TP = TP
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
    self.Frame_Central.setEnabled(True)
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
    self.BTN_execute = QtWidgets.QPushButton(self.Frame_Central)
    self.BTN_execute.setGeometry(QtCore.QRect(230, 290, 151, 31))
    font = QtGui.QFont()
    font.setPointSize(10)
    self.BTN_execute.setFont(font)
    self.BTN_execute.setObjectName("BTN_execute")
    self.listWidget = QtWidgets.QListWidget(self.Frame_Central)
    self.listWidget.setGeometry(QtCore.QRect(70, 200, 311, 81))
    self.listWidget.setObjectName("listWidget")
    self.BTN_clear = QtWidgets.QPushButton(self.Frame_Central)
    self.BTN_clear.setGeometry(QtCore.QRect(70, 290, 151, 31))
    font = QtGui.QFont()
    font.setPointSize(10)
    self.BTN_clear.setFont(font)
    self.BTN_clear.setObjectName("BTN_clear")
    self.BTN_add_2 = QtWidgets.QPushButton(self.Frame_Central)
    self.BTN_add_2.setGeometry(QtCore.QRect(370, 110, 30, 30))
    font = QtGui.QFont()
    font.setPointSize(15)
    font.setBold(True)
    font.setWeight(75)
    self.BTN_add_2.setFont(font)
    self.BTN_add_2.setStyleSheet("color: green;")
    self.BTN_add_2.setObjectName("BTN_add_2")
    self.Label_sub_3 = QtWidgets.QLabel(self.Frame_Central)
    self.Label_sub_3.setEnabled(True)
    self.Label_sub_3.setGeometry(QtCore.QRect(70, 110, 131, 31))
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
    self.BTN_add_5 = QtWidgets.QPushButton(self.Frame_Central)
    self.BTN_add_5.setGeometry(QtCore.QRect(370, 150, 30, 30))
    font = QtGui.QFont()
    font.setPointSize(15)
    font.setBold(True)
    font.setWeight(75)
    self.BTN_add_5.setFont(font)
    self.BTN_add_5.setStyleSheet("color: green;")
    self.BTN_add_5.setObjectName("BTN_add_5")
    self.Label_sub_4 = QtWidgets.QLabel(self.Frame_Central)
    self.Label_sub_4.setGeometry(QtCore.QRect(70, 70, 41, 31))
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
    self.Combo_sub_4 = QtWidgets.QComboBox(self.Frame_Central)
    self.Combo_sub_4.setGeometry(QtCore.QRect(100, 70, 261, 31))
    self.Combo_sub_4.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
    self.Combo_sub_4.setObjectName("Combo_sub_4")
    self.Combo_sub_4.addItem("")
    self.Combo_sub_4.addItem("")
    self.Label_sub_17 = QtWidgets.QLabel(self.Frame_Central)
    self.Label_sub_17.setGeometry(QtCore.QRect(70, 150, 141, 31))
    font = QtGui.QFont()
    font.setPointSize(10)
    font.setBold(False)
    font.setItalic(False)
    font.setUnderline(False)
    font.setWeight(50)
    font.setStrikeOut(False)
    font.setKerning(True)
    self.Label_sub_17.setFont(font)
    self.Label_sub_17.setObjectName("Label_sub_17")
    self.Combo_sub_11 = QtWidgets.QComboBox(self.Frame_Central)
    self.Combo_sub_11.setGeometry(QtCore.QRect(210, 110, 151, 31))
    self.Combo_sub_11.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
    self.Combo_sub_11.setObjectName("Combo_sub_11")
    self.Combo_sub_12 = QtWidgets.QComboBox(self.Frame_Central)
    self.Combo_sub_12.setEnabled(True)
    self.Combo_sub_12.setGeometry(QtCore.QRect(210, 150, 151, 31))
    self.Combo_sub_12.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
    self.Combo_sub_12.setObjectName("Combo_sub_12")
    self.Label_sub_5 = QtWidgets.QLabel(self.Frame_Central)
    self.Label_sub_5.setEnabled(True)
    self.Label_sub_5.setGeometry(QtCore.QRect(70, 350, 301, 141))
    font = QtGui.QFont()
    font.setPointSize(10)
    font.setBold(False)
    font.setItalic(False)
    font.setUnderline(False)
    font.setWeight(50)
    font.setStrikeOut(False)
    font.setKerning(True)
    self.Label_sub_5.setFont(font)
    self.Label_sub_5.setStyleSheet("color: red;")
    self.Label_sub_5.setScaledContents(False)
    self.Label_sub_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
    self.Label_sub_5.setWordWrap(True)
    self.Label_sub_5.setObjectName("Label_sub_5")
    self.verticalLayout.addWidget(self.Frame_Central)
    self.setCentralWidget(self.FW_main)
    QtCore.QMetaObject.connectSlotsByName(self)
    _translate = QtCore.QCoreApplication.translate
    self.setWindowTitle(_translate("MainWindow", "MainWindow"))
    self.Label_main.setText(_translate("MainWindow", "Tworzenie wykresu XXX"))
    self.BTN_execute.setText(_translate("MainWindow", "Wykonaj!"))
    self.BTN_clear.setText(_translate("MainWindow", "Usuń pozycje"))
    self.BTN_add_2.setText(_translate("MainWindow", "+"))
    self.Label_sub_3.setText(_translate("MainWindow", "Dziedzina:"))
    self.BTN_add_5.setText(_translate("MainWindow", "+"))
    self.Label_sub_4.setText(_translate("MainWindow", "Oś:"))
    self.Combo_sub_4.setItemText(0, _translate("MainWindow", "Kolumny"))
    self.Combo_sub_4.setItemText(1, _translate("MainWindow", "Wiersze"))
    self.Label_sub_17.setText(_translate("MainWindow", "Nazwa kolumny:"))
    self.Label_sub_5.setText(_translate("MainWindow", ""))

    def window_refresh_a(tp):
        if tp == 'linear':
            return 'liniowego'
        elif tp == 'circle':
            return 'kołowego'
        elif tp == 'stake':
            return 'stożkowego'
        elif tp == 'point':
            return 'punktowego'

    txt_syn_01 = window_refresh_a(self.TP)
    self.Label_main.setText(_translate("MainWindow", f"Tworzenie wykresu {txt_syn_01}"))

    def window_refresh_b(db, a, b, c, lst):
        lst.clear()
        cs1 = a.currentText()        
        dbs = db
        b.clear()
        c.clear()
        db_idx_list = list(dbs.index)
        db_col_list = list(dbs.columns)
        
        if cs1 == 'Kolumny':
            for x in range(len(db_col_list)):
                b.addItem("")
                c.addItem("")
                b.setItemText(x, str(dbs.columns[x]))
                c.setItemText(x, str(dbs.columns[x]))

        elif cs1 == 'Wiersze':
            for x in range(len(db_idx_list)):
                c.addItem("")
                b.addItem("")
                c.setItemText(x, str(dbs.index[x]))
                b.setItemText(x, str(dbs.index[x]))

    def btn_add_range(lst):
        self.Cs12 = self.Combo_sub_12

        self.exst_in_list = False
        for x in range(lst.count()):
            lw1s = lst.item(x).text().split(': ',1)[1]
            lw1k = lst.item(x).text().split(': ',1)[0]
            if lw1k == 'Wartości' and lw1s == self.Cs12.currentText():
                self.exst_in_list = True
        if self.exst_in_list is False: 
            lst.addItem(f'Wartości: {self.Cs12.currentText()}')
        else:
            self.Label_sub_5.setText(_translate("MainWindow", 'Dany zakres wartości już istnieje na liści'))
            print('Dany zakres wartości już istnieje na liście')

    def btn_add_domain(lst):
        self.Cs11 = self.Combo_sub_11
        self.exst_in_list = False
        for x in range(lst.count()):
            if lst.item(x).text().find('Dziedzina:') == 0:
                self.exst_in_list = True
                break
        if self.exst_in_list:
            print('Nie można wprowadzić dodatkową dziedzinę. Usuń pierwszą by wprowadzić nową dziedzinę')
            self.Label_sub_5.setText(_translate("MainWindow", 'Nie można wprowadzić dodatkową dziedzinę. Usuń pierwszą by wprowadzić nową dziedzinę'))
        else:
            lst.addItem(f'Dziedzina: {self.Cs11.currentText()}')
            
    def btn_remove(lst):
        if lst is not None and len(lst.selectedItems()) == 1:
            lst.takeItem(lst.currentRow())

    def get_data_info(lst, tp):
        dbn_dom = []
        dbn_rng = []
        err = None
        if lst.count() >= 2:
            for x in range(lst.count()):
                lw1s = lst.item(x).text().split(': ',1)[1]
                lw1k = lst.item(x).text().split(': ',1)[0]
                if lw1k == 'Dziedzina':
                    dbn_dom.append(lw1s)
                elif lw1k == 'Wartości':
                    dbn_rng.append(lw1s)
            txt = 'Parametry zostały wprowadzone poprawnie'
            err = False
            if len(dbn_dom) == 0:
                txt = 'Error: Brakuję dziedziny'
                err = True
            elif len(dbn_rng) == 0:
                txt = 'Error: Brakuję zbioru wartości'
                err = True
            if len(dbn_dom) == 0 and len(dbn_rng) == 0:
                txt = 'Error: Brakuje dziedziny oraz zbioru wartości'
                err = True
            if len(dbn_rng) >= 1 and tp is 'circle':
                txt = 'Error: Nie możesz wygenerować wykresów dla wielu linii wartosci'
                err = True
            return dbn_dom, dbn_rng, txt, err
        else:
            txt = 'Error: Nie wprowadzono danych'
            err = True
            return dbn_dom, dbn_rng, txt, err

    def btn_execute(lst, db, tp):
        dbn_dom_o, dbn_rng_o, txt, err = get_data_info(lst, tp)
        self.Label_sub_5.setText(_translate("MainWindow", txt))
        print(dbn_dom_o, dbn_rng_o, txt, err)
        dbn_dom = db[dbn_dom_o[0]]
        dbn_rng = []
        for x in dbn_rng_o:
            dbn_rng.append(db[x])
        if err is False:
            if tp is 'circle':
                fig1, ax1 = plt.subplots()
                ax1.pie(dbn_rng, labels=dbn_dom, autopct='%1.1f%%',
                shadow=True, startangle=90)
                ax1.axis('equal') 
                plt.show()
            if tp is 'linear':
                plt.figure()
                for x in dbn_rng:
                    plt.plot(dbn_dom, x)
                plt.show()
            if tp is 'stake':
                plt.figure()
                for x in dbn_rng:
                    plt.bar(dbn_dom, x)
                plt.show()
            if tp is 'point':
                plt.figure()
                for x in dbn_rng:
                    plt.plot(dbn_dom, x, 'ro')
                plt.show()

    window_refresh_b(self.DB, self.Combo_sub_4, self.Combo_sub_11, self.Combo_sub_12, self.listWidget)
    self.Combo_sub_4.currentIndexChanged.connect(lambda: window_refresh_b(self.DB, self.Combo_sub_4, self.Combo_sub_11, self.Combo_sub_12, self.listWidget))
    self.BTN_add_5.clicked.connect(lambda: btn_add_range(self.listWidget))
    self.BTN_add_2.clicked.connect(lambda: btn_add_domain(self.listWidget))
    self.BTN_clear.clicked.connect(lambda: btn_remove(self.listWidget))
    self.BTN_execute.clicked.connect(lambda: btn_execute(self.listWidget, self.DB, self.TP))
    