from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUiType
from os.path import dirname, realpath, join
import COW_win, NCW_win, NRW_win, FW_win, SW_win, PW_win
import pandas as pd
import os
import sys


class Update:
    def __init__(self):
        pass

    def default_database(self, db, memory, tb):
        self.memory = memory
        tb.clear
        tb.setRowCount(0)
        tb.setColumnCount(0)
        db = None
        self.memory.clear()
        self.data_loaded = False

    def refresh_table(self, db, tb):
        self.data_loaded = True
        self.tb = tb
        self.db = db
        self.cols = list(db.columns)
        tb.setColumnCount(len(db.columns))
        tb.setRowCount(len(db.index))
        for i in range(len(db.index)):
            for j in range(len(db.columns)):
                tb.setItem(i,j, QtWidgets.QTableWidgetItem(str(db.iat[i,j])))

        for x in range(len(db.columns)):
            self.header_item = QtWidgets.QTableWidgetItem(str(self.cols[x]))
            tb.setHorizontalHeaderItem(x, self.header_item)

    def update_log(self, add_log):
        self.log_memory.append(add_log)

    def db_back(self):
        if self.data_loaded:
            mn = self.memory.index(self.db)
            if len(self.memory)>0:
                self.refresh_table(self.memory[mn-1], self.tb)

    def db_forward(self):
        if self.data_loaded:
            mn = self.memory.index(self.db)
            if len(self.memory)>mn:
                self.refresh_table(self.memory[mn+1], self.tb)

class Import(Update):
    def __init__(self, log_memory):
        self.log_memory = log_memory
        
    def import_dialog(self, tb, db):
        self.F_name = QtWidgets.QFileDialog.getOpenFileName(None, 'Otwórz Plik', 'C:\\Users\\Cheap Mouse\\Desktop\\Intro\\IT\\Python\\Projekty\\DataAnalysis', '(*.xml, *.csv *.json *.txt)')[0]
        self.base_name = os.path.basename(self.F_name)
        self.title_name = os.path.splitext(self.base_name)[0]
        
        if self.title_name != '':
            print('PLIK',self.title_name)
            db = pd.read_csv(self.F_name,encoding = 'latin-1').fillna(0)
            #self.show_database(db, tb)
            self.refresh_table(db, tb)
            self.update_log(f'Zaimportowano plik: {self.F_name}')
        else:
            print('Nie załadowano żadnego pliku')
            self.update_log('Błąd w importowaniu pliku')
        return db

    def show_database(self, db, tb):
        self.cols = list(db.columns)
        tb.setColumnCount(len(db.columns))
        tb.setRowCount(len(db.index))
        for i in range(len(db.index)):
            for j in range(len(db.columns)):
                tb.setItem(i,j, QtWidgets.QTableWidgetItem(str(db.iat[i,j])))

        for x in range(len(db.columns)):
            self.header_item = QtWidgets.QTableWidgetItem(str(self.cols[x]))
            tb.setHorizontalHeaderItem(x, self.header_item)

class Export(Update):
    def __init__(self, log_memory):
        pass

    def export_dialog(self, db):
        self.filename = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File', filter='*.csv')[0]
        if self.filename == '':
            pass
        else:
            print(db.head(5))
            db.to_csv(self.filename, index = False)
            print('Saved: '+self.filename)

class Core(Update):
    def __init__(self, db, memory, tb):

        self.db = db
        self.memory = memory
        self.tb = tb
        self.default_database(self.db, self.memory, self.tb)


class Settings:
    def __init__(self, theme_combo, language_combo, fontsize_table_combo, fontsize_logs_combo):
        self.theme_combo = theme_combo
        self.language_combo = language_combo
        self.fontsize_table_combo = fontsize_table_combo
        self.fontsize_logs_combo = fontsize_logs_combo
        self.theme_combo.currentIndexChanged.connect(self.theme_combo_new_value)
        self.language_combo.currentIndexChanged.connect(self.language_combo_new_value)
        self.fontsize_table_combo.currentIndexChanged.connect(self.fontsize_table_combo_new_value)
        self.fontsize_logs_combo.currentIndexChanged.connect(self.fontsize_logs_combo_new_value)

    def theme_combo_new_value(self):
        self.theme_combo_str = self.theme_combo.currentText()

    def language_combo_new_value(self):
        self.language_combo_str = self.language_combo.currentText()

    def fontsize_table_combo_new_value(self):
        self.fontsize_table_combo_str = self.fontsize_table_combo.currentText()

    def fontsize_logs_combo_new_value(self):
        self.fontsize_logs_combo_str = self.fontsize_logs_combo.currentText()

class Cell_Operations_Window(QtWidgets.QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        COW_win.window_execute(self, self.db)


class New_Colmuns_Window(QtWidgets.QMainWindow, Update):
    def __init__(self, db, tb):
        super().__init__()
        self.setWindowTitle('Nowe kolumny')
        self.db = db
        self.tb = tb
        NCW_win.window_execute(self, self.db, self.tb)

class New_Rows_Window(QtWidgets.QMainWindow, Update):
    def __init__(self, db, tb):
        super().__init__()
        self.setWindowTitle('Nowe wiersze')
        self.db = db
        self.tb = tb
        NRW_win.window_execute(self, self.db, self.tb)

class Filtering_Window(QtWidgets.QMainWindow, Update):
    def __init__(self, db, tb):
        super().__init__()
        self.setWindowTitle('Filtrowanie')
        self.db = db
        self.tb = tb
        FW_win.window_execute(self, self.db, self.tb)

class Sorting_Window(QtWidgets.QMainWindow, Update):
    def __init__(self, db, tb):
        super().__init__()
        self.setWindowTitle('Sortowanie')
        self.db = db
        self.tb = tb
        SW_win.window_execute(self, self.db, self.tb)
        

class Default_Window(QtWidgets.QMainWindow, Update):
    def __init__(self, db, memory, tb):
        super().__init__()
        self.db = db
        self.memory = memory
        self.tb = tb
        self.default_database(self.db,self.memory,self.tb)

class Plot_Window(QtWidgets.QMainWindow, Update):
    def __init__(self, db, tb, tp):
        super().__init__()
        self.db = db
        self.tb = tb
        self.tp = tp
        PW_win.window_execute(self, self.db, self.tb, self.tp)
