from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

def window_execute(self, DB):
        self.DB = DB
        self.setWindowTitle('Operacje na komórkach')
        self.resize(600, 500)
        self.setMaximumSize(QtCore.QSize(600, 500))
        self.COW_main = QtWidgets.QWidget(self)
        self.COW_main.setMinimumSize(QtCore.QSize(600, 500))
        self.COW_main.setMaximumSize(QtCore.QSize(600, 500))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.COW_main.setFont(font)
        self.COW_main.setObjectName("COW_main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.COW_main)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Frame_Top = QtWidgets.QFrame(self.COW_main)
        self.Frame_Top.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Frame_Top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_Top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_Top.setObjectName("Frame_Top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Frame_Top)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.COW_fn_label = QtWidgets.QLabel(self.Frame_Top)
        self.COW_fn_label.setMinimumSize(QtCore.QSize(0, 30))
        self.COW_fn_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.COW_fn_label.setFont(font)
        self.COW_fn_label.setObjectName("COW_fn_label")
        self.horizontalLayout.addWidget(self.COW_fn_label)
        self.comboBox_main = QtWidgets.QComboBox(self.Frame_Top)
        self.comboBox_main.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_main.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sans-Serif")
        font.setPointSize(-1)
        self.comboBox_main.setFont(font)
        self.comboBox_main.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
        self.comboBox_main.setObjectName("comboBox")
        self.comboBox_main.addItem("")
        self.comboBox_main.addItem("")
        self.comboBox_main.addItem("")
        self.comboBox_main.addItem("")
        self.comboBox_main.addItem("")
        self.comboBox_main.addItem("")
        self.comboBox_main.addItem("")
        self.comboBox_main.addItem("")
        self.comboBox_main.addItem("")
        self.comboBox_main.addItem("")
        self.comboBox_main.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_main)
        self.verticalLayout.addWidget(self.Frame_Top)
        self.Frame_Bottom = QtWidgets.QFrame(self.COW_main)
        self.Frame_Bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_Bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_Bottom.setObjectName("Frame_Bottom")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Frame_Bottom)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Stacked_Widget_Bottom = QtWidgets.QStackedWidget(self.Frame_Bottom)
        self.Stacked_Widget_Bottom.setObjectName("Stacked_Widget_Bottom")
        self.Bottom_Page1 = QtWidgets.QWidget()
        self.Bottom_Page1.setObjectName("Bottom_Page1")
        self.BP1_main_frame = QtWidgets.QFrame(self.Bottom_Page1)
        self.BP1_main_frame.setGeometry(QtCore.QRect(0, 0, 558, 400))
        self.BP1_main_frame.setMinimumSize(QtCore.QSize(558, 400))
        self.BP1_main_frame.setMaximumSize(QtCore.QSize(16777215, 75))
        self.BP1_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BP1_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BP1_main_frame.setObjectName("BP1_main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.BP1_main_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.BP1_sub_frame_1 = QtWidgets.QFrame(self.BP1_main_frame)
        self.BP1_sub_frame_1.setMinimumSize(QtCore.QSize(50, 400))
        self.BP1_sub_frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BP1_sub_frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BP1_sub_frame_1.setObjectName("BP1_sub_frame_1")
        self.BP1_fv1_combobox = QtWidgets.QComboBox(self.BP1_sub_frame_1)
        self.BP1_fv1_combobox.setGeometry(QtCore.QRect(150, 12, 211, 30))
        self.BP1_fv1_combobox.setMinimumSize(QtCore.QSize(0, 30))
        self.BP1_fv1_combobox.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
        self.BP1_fv1_combobox.setObjectName("BP1_fv1_combobox")
        self.BP1_fv1_combobox.addItem("")
        self.BP1_fv1_combobox.addItem("")
        self.BP1_fv1_combobox.addItem("")
        self.BP1_fv1_label = QtWidgets.QLabel(self.BP1_sub_frame_1)
        self.BP1_fv1_label.setGeometry(QtCore.QRect(10, 10, 81, 30))
        self.BP1_fv1_label.setObjectName("BP1_fv1_label")
        self.BP1_fv1_combobox_2 = QtWidgets.QComboBox(self.BP1_sub_frame_1)
        self.BP1_fv1_combobox_2.setGeometry(QtCore.QRect(150, 50, 211, 30))
        self.BP1_fv1_combobox_2.setMinimumSize(QtCore.QSize(0, 30))
        self.BP1_fv1_combobox_2.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
        self.BP1_fv1_combobox_2.setObjectName("BP1_fv1_combobox_2")
        self.BP1_fv1_combobox_2.addItem("")
        self.BP1_fv1_combobox_2.addItem("")
        self.BP1_fv1_label_2 = QtWidgets.QLabel(self.BP1_sub_frame_1)
        self.BP1_fv1_label_2.setGeometry(QtCore.QRect(10, 50, 81, 30))
        self.BP1_fv1_label_2.setObjectName("BP1_fv1_label_2")
        self.BP1_fv1_combobox_3 = QtWidgets.QComboBox(self.BP1_sub_frame_1)
        self.BP1_fv1_combobox_3.setGeometry(QtCore.QRect(150, 90, 211, 30))
        self.BP1_fv1_combobox_3.setMinimumSize(QtCore.QSize(0, 30))
        self.BP1_fv1_combobox_3.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
        self.BP1_fv1_combobox_3.setObjectName("BP1_fv1_combobox_3")
        self.BP1_fv1_label_3 = QtWidgets.QLabel(self.BP1_sub_frame_1)
        self.BP1_fv1_label_3.setGeometry(QtCore.QRect(10, 90, 81, 30))
        self.BP1_fv1_label_3.setObjectName("BP1_fv1_label_3")
        self.BP1_fv1_label_4 = QtWidgets.QLabel(self.BP1_sub_frame_1)
        self.BP1_fv1_label_4.setGeometry(QtCore.QRect(10, 130, 81, 30))
        self.BP1_fv1_label_4.setObjectName("BP1_fv1_label_4")
        self.BP1_fv1_combobox_4 = QtWidgets.QComboBox(self.BP1_sub_frame_1)
        self.BP1_fv1_combobox_4.setGeometry(QtCore.QRect(150, 130, 211, 30))
        self.BP1_fv1_combobox_4.setMinimumSize(QtCore.QSize(0, 30))
        self.BP1_fv1_combobox_4.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
        self.BP1_fv1_combobox_4.setObjectName("BP1_fv1_combobox_4")
        self.BP1_fv1_combobox_5 = QtWidgets.QComboBox(self.BP1_sub_frame_1)
        self.BP1_fv1_combobox_5.setGeometry(QtCore.QRect(150, 170, 211, 30))
        self.BP1_fv1_combobox_5.setMinimumSize(QtCore.QSize(0, 30))
        self.BP1_fv1_combobox_5.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
        self.BP1_fv1_combobox_5.setObjectName("BP1_fv1_combobox_5")
        self.BP1_fv1_label_5 = QtWidgets.QLabel(self.BP1_sub_frame_1)
        self.BP1_fv1_label_5.setGeometry(QtCore.QRect(10, 170, 111, 30))
        self.BP1_fv1_label_5.setObjectName("BP1_fv1_label_5")
        self.BP_fv1_btn_add = QtWidgets.QPushButton(self.BP1_sub_frame_1)
        self.BP_fv1_btn_add.setGeometry(QtCore.QRect(370, 170, 91, 30))
        self.BP_fv1_btn_add.setObjectName("BP_fv1_btn_add")
        self.BP_fv1_btn_sub = QtWidgets.QPushButton(self.BP1_sub_frame_1)
        self.BP_fv1_btn_sub.setGeometry(QtCore.QRect(370, 210, 93, 30))
        self.BP_fv1_btn_sub.setObjectName("BP_fv1_btn_sub")
        self.BP1_fv1_label_6 = QtWidgets.QLabel(self.BP1_sub_frame_1)
        self.BP1_fv1_label_6.setGeometry(QtCore.QRect(10, 210, 141, 30))
        self.BP1_fv1_label_6.setObjectName("BP1_fv1_label_6")

        #TUTAJ
        self.BP1_fv1_label_8 = QtWidgets.QLabel(self.BP1_sub_frame_1)
        self.BP1_fv1_label_8.setGeometry(QtCore.QRect(10, 250, 141, 30))
        self.BP1_fv1_label_8.setObjectName("BP1_fv1_label_8")

        self.BP1_fv1_combobox_6 = QtWidgets.QComboBox(self.BP1_sub_frame_1)
        self.BP1_fv1_combobox_6.setGeometry(QtCore.QRect(150, 210, 211, 30))
        self.BP1_fv1_combobox_6.setMinimumSize(QtCore.QSize(0, 30))
        self.BP1_fv1_combobox_6.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
        self.BP1_fv1_combobox_6.setObjectName("BP1_fv1_combobox_6")

        self.BP1_fv1_combobox_7 = QtWidgets.QComboBox(self.BP1_sub_frame_1)
        self.BP1_fv1_combobox_7.setGeometry(QtCore.QRect(150, 250, 211, 30))
        self.BP1_fv1_combobox_7.setMinimumSize(QtCore.QSize(0, 30))
        self.BP1_fv1_combobox_7.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid #595959; \n"
"font-size: 14px;\n"
"white-space: normal;\n"
"font-family: Sans-Serif;")
        self.BP1_fv1_combobox_7.setObjectName("BP1_fv1_combobox_7")

        self.BP_fv1_btn_add_2 = QtWidgets.QPushButton(self.BP1_sub_frame_1)
        self.BP_fv1_btn_add_2.setGeometry(QtCore.QRect(220, 290, 111, 31))
        self.BP_fv1_btn_add_2.setObjectName("BP_fv1_btn_add_2")
        self.BP1_fv1_label_7 = QtWidgets.QLabel(self.BP1_sub_frame_1)
        self.BP1_fv1_label_7.setGeometry(QtCore.QRect(10, 350, 521, 30))
        self.BP1_fv1_label_7.setFont(font)
        self.BP1_fv1_label_7.setStyleSheet("color: red;")
        self.BP1_fv1_label_7.setObjectName("BP1_fv1_label_7")
        self.verticalLayout_2.addWidget(self.BP1_sub_frame_1)
        self.Stacked_Widget_Bottom.addWidget(self.Bottom_Page1)
        self.Bottom_Page2 = QtWidgets.QWidget()
        self.Bottom_Page2.setObjectName("Bottom_Page2")
        self.Stacked_Widget_Bottom.addWidget(self.Bottom_Page2)
        self.Bottom_Page3 = QtWidgets.QWidget()
        self.Bottom_Page3.setObjectName("Bottom_Page3")
        self.Stacked_Widget_Bottom.addWidget(self.Bottom_Page3)
        self.Bottom_Page4 = QtWidgets.QWidget()
        self.Bottom_Page4.setObjectName("Bottom_Page4")
        self.Stacked_Widget_Bottom.addWidget(self.Bottom_Page4)
        self.Bottom_Page5 = QtWidgets.QWidget()
        self.Bottom_Page5.setObjectName("Bottom_Page5")
        self.Stacked_Widget_Bottom.addWidget(self.Bottom_Page5)
        self.Bottom_Page6 = QtWidgets.QWidget()
        self.Bottom_Page6.setObjectName("Bottom_Page6")
        self.Stacked_Widget_Bottom.addWidget(self.Bottom_Page6)
        self.horizontalLayout_2.addWidget(self.Stacked_Widget_Bottom)
        self.verticalLayout.addWidget(self.Frame_Bottom)
        self.setCentralWidget(self.COW_main)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.COW_fn_label.setText(_translate("MainWindow", "Funkcje:"))
        self.comboBox_main.setItemText(0, _translate("MainWindow", "Działania arytmetyczne"))
        self.comboBox_main.setItemText(1, _translate("MainWindow", "Średnie klasyczne"))
        self.comboBox_main.setItemText(2, _translate("MainWindow", "Przeciętne pozycjne i kwantylne"))
        self.comboBox_main.setItemText(3, _translate("MainWindow", "Bezwzględne miary zmienności"))
        self.comboBox_main.setItemText(4, _translate("MainWindow", "Wariancja"))
        self.comboBox_main.setItemText(5, _translate("MainWindow", "Współczynnik zmienności"))
        self.comboBox_main.setItemText(6, _translate("MainWindow", "Współczynnik asymetrii"))
        self.comboBox_main.setItemText(7, _translate("MainWindow", "Moment standaryzowany trzeciego rzędu"))
        self.comboBox_main.setItemText(8, _translate("MainWindow", "Współczynnik koncentracji"))
        self.comboBox_main.setItemText(9, _translate("MainWindow", "Współczynnik ekscesu"))
        self.comboBox_main.setItemText(10, _translate("MainWindow", "Współczynnik koncentracji Lorenza"))
        self.BP1_fv1_combobox.setItemText(0, _translate("MainWindow", "Dodawanie"))
        self.BP1_fv1_combobox.setItemText(1, _translate("MainWindow", "Odejmowanie"))
        self.BP1_fv1_combobox.setItemText(2, _translate("MainWindow", "Mnożenie"))
        self.BP1_fv1_label.setText(_translate("MainWindow", "Działanie:"))
        self.BP1_fv1_combobox_2.setItemText(0, _translate("MainWindow", "Wiersze"))
        self.BP1_fv1_combobox_2.setItemText(1, _translate("MainWindow", "Kolumny"))
        self.BP1_fv1_label_2.setText(_translate("MainWindow", "Oś:"))
        self.BP1_fv1_label_3.setText(_translate("MainWindow", "Zakres od:"))
        self.BP1_fv1_label_4.setText(_translate("MainWindow", "Zakres do:"))
        self.BP1_fv1_label_5.setText(_translate("MainWindow", "Dodaj wyjątki:"))
        self.BP_fv1_btn_add.setText(_translate("MainWindow", "Dodaj +"))
        self.BP_fv1_btn_sub.setText(_translate("MainWindow", "Usuń -"))
        self.BP1_fv1_label_6.setText(_translate("MainWindow", "Wyjątki dodane:"))
        self.BP1_fv1_label_8.setText(_translate("MainWindow", "Wyniki w:"))
        self.BP_fv1_btn_add_2.setText(_translate("MainWindow", "Wykonaj!"))
        self.BP1_fv1_label_7.setText(_translate("MainWindow", "Ostrzeżenie: Upewnij się, że wprowadzono odpowiednie parametry!"))
        QtCore.QMetaObject.connectSlotsByName(self)

        global comboBox_main_text, BP1_fv1_combobox_text, BP1_fv1_combobox_2_text, BP1_fv1_combobox_3_text, BP1_fv1_combobox_4_text, BP1_fv1_combobox_5_text, BP1_fv1_combobox_6_text, BP1_fv1_combobox_7_text
        global list_exc

        list_exc = list()

        comboBox_main_text = self.comboBox_main.currentText()
        BP1_fv1_combobox_text = self.BP1_fv1_combobox.currentText()
        BP1_fv1_combobox_2_text = self.BP1_fv1_combobox_2.currentText()
        BP1_fv1_combobox_3_text = self.BP1_fv1_combobox_3.currentText()
        BP1_fv1_combobox_4_text = self.BP1_fv1_combobox_4.currentText()
        BP1_fv1_combobox_5_text = self.BP1_fv1_combobox_5.currentText()
        BP1_fv1_combobox_6_text = self.BP1_fv1_combobox_6.currentText()
        BP1_fv1_combobox_7_text = self.BP1_fv1_combobox_7.currentText()

        def window_refresh_c(a):
                print(a.currentText())
                comboBox_main_text = a.currentText()

        def window_refresh_c1(a):
                print(a.currentText())
                BP1_fv1_combobox_text = a.currentText()

        def window_refresh_c2(a,b,c,d,e,db):
                
                BP1_fv1_combobox_2_text = a.currentText()
                dbs = db
                b.clear()
                c.clear()
                db_idx_list = list(dbs.index)
                db_col_list = list(dbs.columns)
                
                if BP1_fv1_combobox_2_text == "Wiersze":
                        
                        for x in range(len(db_idx_list)):
                                b.addItem("")
                                c.addItem("")
                                d.addItem("")
                                e.addItem("")
                                b.setItemText(x, str(dbs.index[x]))
                                c.setItemText(x, str(dbs.index[x]))
                                d.setItemText(x, str(dbs.index[x]))
                                e.setItemText(x, str(dbs.index[x]))

                elif BP1_fv1_combobox_2_text == "Kolumny":
    
                        for x in range(len(db_col_list)):
                                b.addItem("")
                                c.addItem("")
                                d.addItem("")
                                e.addItem("")
                                b.setItemText(x, str(dbs.columns[x]))
                                c.setItemText(x, str(dbs.columns[x]))
                                d.setItemText(x, str(dbs.columns[x]))
                                e.setItemText(x, str(dbs.columns[x]))
        
        def add_exception(a,b):
                if str(a.currentText()) not in list_exc:
                        b.clear()
                        list_exc.append(a.currentText())
                        for x in range(len(list_exc)):
                                b.addItem("asdasd")
                                b.setItemText(x, str(list_exc[x]))

        def remove_exception(a):
                if str(a.currentText()) in list_exc:
                        idx = list_exc.index(a.currentText())
                        a.clear()
                        list_exc.pop(idx)
                        for x in range(len(list_exc)):
                                a.addItem("asdasd")
                                a.setItemText(x, str(list_exc[x]))

        def execute_calculation_fv1(db, a, b, c):
                pass

        self.comboBox_main.currentIndexChanged.connect(lambda: window_refresh_c(self.comboBox_main))
        self.BP1_fv1_combobox.currentIndexChanged.connect(lambda: window_refresh_c1(self.BP1_fv1_combobox))
        self.BP1_fv1_combobox_2.currentIndexChanged.connect(lambda: window_refresh_c2(self.BP1_fv1_combobox_2,self.BP1_fv1_combobox_3,self.BP1_fv1_combobox_4, self.BP1_fv1_combobox_5,self.BP1_fv1_combobox_7,self.DB))
        self.BP_fv1_btn_add.clicked.connect(lambda: add_exception(self.BP1_fv1_combobox_5,self.BP1_fv1_combobox_6))
        self.BP_fv1_btn_sub.clicked.connect(lambda: remove_exception(self.BP1_fv1_combobox_6))
        self.BP_fv1_btn_add_2.clicked.connect(lambda: execute_calculation_fv1(self.DB,self.BP1_fv1_combobox,self.BP1_fv1_combobox_3,self.BP1_fv1_combobox_4))

        window_refresh_c(self.comboBox_main)
        window_refresh_c1(self.BP1_fv1_combobox)
        window_refresh_c2(self.BP1_fv1_combobox_2,self.BP1_fv1_combobox_3,self.BP1_fv1_combobox_4, self.BP1_fv1_combobox_5,self.BP1_fv1_combobox_7,self.DB)




