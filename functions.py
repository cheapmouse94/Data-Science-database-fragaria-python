from PyQt5 import QtCore, QtGui, QtWidgets

class Core:
    def __init__(self):
        pass

class Import(QtWidgets.QTableWidget):
    def __init__(self):
        super().__init__(1,1)
        self.F_name = None
    def button_event(self):
        self.F_name = QtWidgets.QFileDialog.getOpenFileName(None, 'Otwórz Plik', 'C:\\Users\\Cheap Mouse\\Desktop\\Intro\\IT\\Python\\Projekty\\DataAnalysis', '(*.xml, *.csv *.json *.txt)')
        print(self.F_name[0])
        self.open_csv_sheet(self.F_name)  
    def open_csv_sheet(self, file):
        if file[0] != '':
            with open(file[0], newline='') as csv_file:
                self.setRowCount(5)
                self.setColumnCount(5)
                #my_file = csv.

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
        

