from PyQt5 import QtCore, QtGui, QtWidgets
from functions import *
import pandas as pd
import os


class Ui_MainWindow(object):
        def __init__(self):
                self.db = pd.DataFrame()
                self.db_memory = []
                self.log_list = []
                self.Table_widget = None

        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1000, 649)
                self.Main_widget = QtWidgets.QWidget(MainWindow)
                self.Main_widget.setMinimumSize(QtCore.QSize(1000, 600))
                self.Main_widget.setStyleSheet("font-family: Sans-Serif;")
                self.Main_widget.setObjectName("Main_widget")
                self.Main_widget_layout = QtWidgets.QHBoxLayout(self.Main_widget)
                self.Main_widget_layout.setContentsMargins(0, 0, 0, 0)
                self.Main_widget_layout.setSpacing(0)
                self.Main_widget_layout.setObjectName("Main_widget_layout")
                self.Visual_column_frame = QtWidgets.QFrame(self.Main_widget)
                self.Visual_column_frame.setMinimumSize(QtCore.QSize(800, 0))
                self.Visual_column_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Visual_column_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Visual_column_frame.setObjectName("Visual_column_frame")
                self.Visual_column_layout = QtWidgets.QVBoxLayout(self.Visual_column_frame)
                self.Visual_column_layout.setContentsMargins(0, 0, 0, 0)
                self.Visual_column_layout.setSpacing(0)
                self.Visual_column_layout.setObjectName("Visual_column_layout")
                self.Main_frame = QtWidgets.QFrame(self.Visual_column_frame)
                self.Main_frame.setMinimumSize(QtCore.QSize(0, 70))
                self.Main_frame.setMaximumSize(QtCore.QSize(16777215, 70))
                self.Main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Main_frame.setObjectName("Main_frame")
                self.Main_frame_layout = QtWidgets.QHBoxLayout(self.Main_frame)
                self.Main_frame_layout.setContentsMargins(0, 0, 0, 0)
                self.Main_frame_layout.setSpacing(0)
                self.Main_frame_layout.setObjectName("Main_frame_layout")
                self.Main_buttons_frame = QtWidgets.QFrame(self.Main_frame)
                self.Main_buttons_frame.setMinimumSize(QtCore.QSize(580, 0))
                self.Main_buttons_frame.setMaximumSize(QtCore.QSize(580, 16777215))
                self.Main_buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Main_buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Main_buttons_frame.setObjectName("Main_buttons_frame")
                self.Main_buttons_frame_layout = QtWidgets.QHBoxLayout(self.Main_buttons_frame)
                self.Main_buttons_frame_layout.setContentsMargins(0, 0, 0, 0)
                self.Main_buttons_frame_layout.setSpacing(0)
                self.Main_buttons_frame_layout.setObjectName("Main_buttons_frame_layout")
                self.Main_new_file_1 = QtWidgets.QPushButton(self.Main_buttons_frame)
                self.Main_new_file_1.setMaximumSize(QtCore.QSize(50, 50))
                self.Main_new_file_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Main_new_file_1.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}")
                self.Main_new_file_1.setText("")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/9-a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Main_new_file_1.setIcon(icon)
                self.Main_new_file_1.setIconSize(QtCore.QSize(50, 50))
                self.Main_new_file_1.setObjectName("Main_new_file_1")
                self.Main_new_file_1.installEventFilter(self.Main_buttons_frame)
                self.Main_buttons_frame_layout.addWidget(self.Main_new_file_1)
                self.Main_export_9 = QtWidgets.QPushButton(self.Main_buttons_frame)
                self.Main_export_9.setMaximumSize(QtCore.QSize(50, 50))
                self.Main_export_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Main_export_9.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}")
                self.Main_export_9.setText("")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("icons/4-a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Main_export_9.setIcon(icon1)
                self.Main_export_9.setIconSize(QtCore.QSize(50, 50))
                self.Main_export_9.setObjectName("Main_export_9")
                self.Main_buttons_frame_layout.addWidget(self.Main_export_9)
                self.Main_undo_2 = QtWidgets.QPushButton(self.Main_buttons_frame)
                self.Main_undo_2.setMaximumSize(QtCore.QSize(50, 50))
                self.Main_undo_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Main_undo_2.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}")
                self.Main_undo_2.setText("")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("icons/5-af.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Main_undo_2.setIcon(icon2)
                self.Main_undo_2.setIconSize(QtCore.QSize(50, 50))
                self.Main_undo_2.setObjectName("Main_undo_2")
                self.Main_buttons_frame_layout.addWidget(self.Main_undo_2)
                self.Main_reto_3 = QtWidgets.QPushButton(self.Main_buttons_frame)
                self.Main_reto_3.setMaximumSize(QtCore.QSize(50, 50))
                self.Main_reto_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Main_reto_3.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}")
                self.Main_reto_3.setText("")
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap("icons/5-a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Main_reto_3.setIcon(icon3)
                self.Main_reto_3.setIconSize(QtCore.QSize(50, 50))
                self.Main_reto_3.setObjectName("Main_reto_3")
                self.Main_buttons_frame_layout.addWidget(self.Main_reto_3)
                self.Main_clear_db_4 = QtWidgets.QPushButton(self.Main_buttons_frame)
                self.Main_clear_db_4.setMaximumSize(QtCore.QSize(50, 50))
                self.Main_clear_db_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Main_clear_db_4.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}")
                self.Main_clear_db_4.setText("")
                icon4 = QtGui.QIcon()
                icon4.addPixmap(QtGui.QPixmap("icons/10-a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Main_clear_db_4.setIcon(icon4)
                self.Main_clear_db_4.setIconSize(QtCore.QSize(50, 50))
                self.Main_clear_db_4.setObjectName("Main_clear_db_4")
                self.Main_buttons_frame_layout.addWidget(self.Main_clear_db_4)
                self.Main_maintools_5 = QtWidgets.QPushButton(self.Main_buttons_frame)
                self.Main_maintools_5.setMaximumSize(QtCore.QSize(50, 50))
                self.Main_maintools_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Main_maintools_5.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}")
                self.Main_maintools_5.setText("")
                icon5 = QtGui.QIcon()
                icon5.addPixmap(QtGui.QPixmap("icons/13-a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Main_maintools_5.setIcon(icon5)
                self.Main_maintools_5.setIconSize(QtCore.QSize(50, 50))
                self.Main_maintools_5.setObjectName("Main_maintools_5")
                self.Main_buttons_frame_layout.addWidget(self.Main_maintools_5)
                self.Main_plots_6 = QtWidgets.QPushButton(self.Main_buttons_frame)
                self.Main_plots_6.setMaximumSize(QtCore.QSize(50, 50))
                self.Main_plots_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Main_plots_6.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}")
                self.Main_plots_6.setText("")
                icon6 = QtGui.QIcon()
                icon6.addPixmap(QtGui.QPixmap("icons/12-a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Main_plots_6.setIcon(icon6)
                self.Main_plots_6.setIconSize(QtCore.QSize(50, 50))
                self.Main_plots_6.setObjectName("Main_plots_6")
                self.Main_buttons_frame_layout.addWidget(self.Main_plots_6)
                self.Main_predicdtions_7 = QtWidgets.QPushButton(self.Main_buttons_frame)
                self.Main_predicdtions_7.setMaximumSize(QtCore.QSize(50, 50))
                self.Main_predicdtions_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Main_predicdtions_7.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}")
                self.Main_predicdtions_7.setText("")
                icon7 = QtGui.QIcon()
                icon7.addPixmap(QtGui.QPixmap("icons/11-a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Main_predicdtions_7.setIcon(icon7)
                self.Main_predicdtions_7.setIconSize(QtCore.QSize(50, 50))
                self.Main_predicdtions_7.setObjectName("Main_predicdtions_7")
                self.Main_buttons_frame_layout.addWidget(self.Main_predicdtions_7)
                self.Main_settings_8 = QtWidgets.QPushButton(self.Main_buttons_frame)
                self.Main_settings_8.setMaximumSize(QtCore.QSize(50, 50))
                self.Main_settings_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Main_settings_8.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}")
                self.Main_settings_8.setText("")
                icon8 = QtGui.QIcon()
                icon8.addPixmap(QtGui.QPixmap("icons/1-a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Main_settings_8.setIcon(icon8)
                self.Main_settings_8.setIconSize(QtCore.QSize(50, 50))
                self.Main_settings_8.setObjectName("Main_settings_8")
                self.Main_buttons_frame_layout.addWidget(self.Main_settings_8)
                self.Main_frame_layout.addWidget(self.Main_buttons_frame)
                self.Main_label_frame = QtWidgets.QFrame(self.Main_frame)
                self.Main_label_frame.setMaximumSize(QtCore.QSize(16777215, 50))
                self.Main_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Main_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Main_label_frame.setObjectName("Main_label_frame")
                self.Main_label_frame_layout = QtWidgets.QVBoxLayout(self.Main_label_frame)
                self.Main_label_frame_layout.setContentsMargins(0, 0, 0, 0)
                self.Main_label_frame_layout.setSpacing(0)
                self.Main_label_frame_layout.setObjectName("Main_label_frame_layout")
                self.Mian_label_stack = QtWidgets.QStackedWidget(self.Main_label_frame)
                self.Mian_label_stack.setMaximumSize(QtCore.QSize(214, 16777215))
                self.Mian_label_stack.setObjectName("Mian_label_stack")
                self.Main_new_file_title_widget = QtWidgets.QWidget()
                self.Main_new_file_title_widget.setObjectName("Main_new_file_title_widget")
                self.Main_new_file_title_label = QtWidgets.QLabel(self.Main_new_file_title_widget)
                self.Main_new_file_title_label.setGeometry(QtCore.QRect(0, 0, 214, 48))
                self.Main_new_file_title_label.setStyleSheet("border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 16px;\n"
                "display: inline-block;")
                self.Main_new_file_title_label.setAlignment(QtCore.Qt.AlignCenter)
                self.Main_new_file_title_label.setWordWrap(True)
                self.Main_new_file_title_label.setObjectName("Main_new_file_title_label")
                self.Mian_label_stack.addWidget(self.Main_new_file_title_widget)
                self.Main_reto_title_widget = QtWidgets.QWidget()
                self.Main_reto_title_widget.setObjectName("Main_reto_title_widget")
                self.Main_reto_title_label = QtWidgets.QLabel(self.Main_reto_title_widget)
                self.Main_reto_title_label.setGeometry(QtCore.QRect(0, 0, 214, 48))
                self.Main_reto_title_label.setStyleSheet("border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 16px;\n"
                "display: inline-block;")
                self.Main_reto_title_label.setAlignment(QtCore.Qt.AlignCenter)
                self.Main_reto_title_label.setWordWrap(True)
                self.Main_reto_title_label.setObjectName("Main_reto_title_label")
                self.Mian_label_stack.addWidget(self.Main_reto_title_widget)
                self.Main_undo_title_widget = QtWidgets.QWidget()
                self.Main_undo_title_widget.setObjectName("Main_undo_title_widget")
                self.Main_undo_title_label = QtWidgets.QLabel(self.Main_undo_title_widget)
                self.Main_undo_title_label.setGeometry(QtCore.QRect(0, 0, 214, 48))
                self.Main_undo_title_label.setStyleSheet("border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 16px;\n"
                "display: inline-block;")
                self.Main_undo_title_label.setAlignment(QtCore.Qt.AlignCenter)
                self.Main_undo_title_label.setWordWrap(True)
                self.Main_undo_title_label.setObjectName("Main_undo_title_label")
                self.Mian_label_stack.addWidget(self.Main_undo_title_widget)
                self.Main_clear_db_widget = QtWidgets.QWidget()
                self.Main_clear_db_widget.setObjectName("Main_clear_db_widget")
                self.Main_clear_db_label = QtWidgets.QLabel(self.Main_clear_db_widget)
                self.Main_clear_db_label.setGeometry(QtCore.QRect(0, 0, 214, 48))
                self.Main_clear_db_label.setStyleSheet("border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 16px;\n"
                "display: inline-block;")
                self.Main_clear_db_label.setAlignment(QtCore.Qt.AlignCenter)
                self.Main_clear_db_label.setWordWrap(True)
                self.Main_clear_db_label.setObjectName("Main_clear_db_label")
                self.Mian_label_stack.addWidget(self.Main_clear_db_widget)
                self.Main_maintools_widget = QtWidgets.QWidget()
                self.Main_maintools_widget.setObjectName("Main_maintools_widget")
                self.Main_maintools_label = QtWidgets.QLabel(self.Main_maintools_widget)
                self.Main_maintools_label.setGeometry(QtCore.QRect(0, 0, 214, 48))
                self.Main_maintools_label.setStyleSheet("border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 16px;\n"
                "display: inline-block;")
                self.Main_maintools_label.setAlignment(QtCore.Qt.AlignCenter)
                self.Main_maintools_label.setWordWrap(True)
                self.Main_maintools_label.setObjectName("Main_maintools_label")
                self.Mian_label_stack.addWidget(self.Main_maintools_widget)
                self.Main_plot_widget = QtWidgets.QWidget()
                self.Main_plot_widget.setObjectName("Main_plot_widget")
                self.Main_plot_label = QtWidgets.QLabel(self.Main_plot_widget)
                self.Main_plot_label.setGeometry(QtCore.QRect(0, 0, 214, 48))
                self.Main_plot_label.setStyleSheet("border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 16px;\n"
                "display: inline-block;")
                self.Main_plot_label.setAlignment(QtCore.Qt.AlignCenter)
                self.Main_plot_label.setWordWrap(True)
                self.Main_plot_label.setObjectName("Main_plot_label")
                self.Mian_label_stack.addWidget(self.Main_plot_widget)
                self.Main_predictions_widget = QtWidgets.QWidget()
                self.Main_predictions_widget.setObjectName("Main_predictions_widget")
                self.Main_predictions_label = QtWidgets.QLabel(self.Main_predictions_widget)
                self.Main_predictions_label.setGeometry(QtCore.QRect(0, 0, 214, 48))
                self.Main_predictions_label.setStyleSheet("border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 16px;\n"
                "display: inline-block;")
                self.Main_predictions_label.setAlignment(QtCore.Qt.AlignCenter)
                self.Main_predictions_label.setWordWrap(True)
                self.Main_predictions_label.setObjectName("Main_predictions_label")
                self.Mian_label_stack.addWidget(self.Main_predictions_widget)
                self.Main_settings_widget = QtWidgets.QWidget()
                self.Main_settings_widget.setObjectName("Main_settings_widget")
                self.Main_settings_label = QtWidgets.QLabel(self.Main_settings_widget)
                self.Main_settings_label.setGeometry(QtCore.QRect(0, 0, 214, 48))
                self.Main_settings_label.setStyleSheet("border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 16px;\n"
                "display: inline-block;")
                self.Main_settings_label.setAlignment(QtCore.Qt.AlignCenter)
                self.Main_settings_label.setWordWrap(True)
                self.Main_settings_label.setObjectName("Main_settings_label")
                self.Mian_label_stack.addWidget(self.Main_settings_widget)
                self.Main_export_widget = QtWidgets.QWidget()
                self.Main_export_widget.setObjectName("Main_export_widget")
                self.Main_export_label = QtWidgets.QLabel(self.Main_export_widget)
                self.Main_export_label.setGeometry(QtCore.QRect(0, 0, 214, 48))
                self.Main_export_label.setStyleSheet("display: inline-block;\n"
                "border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 16px;")
                self.Main_export_label.setAlignment(QtCore.Qt.AlignCenter)
                self.Main_export_label.setWordWrap(True)
                self.Main_export_label.setObjectName("Main_export_label")
                self.Mian_label_stack.addWidget(self.Main_export_widget)
                self.Main_label_frame_layout.addWidget(self.Mian_label_stack)
                self.Main_frame_layout.addWidget(self.Main_label_frame)
                self.Visual_column_layout.addWidget(self.Main_frame)
                self.Table_frame = QtWidgets.QFrame(self.Visual_column_frame)
                self.Table_frame.setEnabled(True)
                self.Table_frame.setMinimumSize(QtCore.QSize(0, 350))
                self.Table_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Table_frame.setFrameShadow(QtWidgets.QFrame.Plain)
                self.Table_frame.setLineWidth(15)
                self.Table_frame.setObjectName("Table_frame")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Table_frame)
                self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_4.setSpacing(0)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.Table_widget = QtWidgets.QTableWidget(self.Table_frame)
                font = QtGui.QFont()
                font.setFamily("Sans-Serif")
                self.Table_widget.setFont(font)
                self.Table_widget.setStyleSheet("")
                self.Table_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.Table_widget.setLineWidth(2)
                self.Table_widget.setDragEnabled(False)
                self.Table_widget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
                self.Table_widget.setAlternatingRowColors(True)
                self.Table_widget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
                self.Table_widget.setObjectName("Table_widget")
                self.verticalLayout_4.addWidget(self.Table_widget)
                self.Visual_column_layout.addWidget(self.Table_frame)
                self.Logs_frame = QtWidgets.QFrame(self.Visual_column_frame)
                self.Logs_frame.setMinimumSize(QtCore.QSize(0, 150))
                self.Logs_frame.setMaximumSize(QtCore.QSize(16777215, 150))
                self.Logs_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Logs_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Logs_frame.setLineWidth(2)
                self.Logs_frame.setObjectName("Logs_frame")
                self.Logs_frame_layout = QtWidgets.QHBoxLayout(self.Logs_frame)
                self.Logs_frame_layout.setContentsMargins(0, 0, 0, 0)
                self.Logs_frame_layout.setSpacing(0)
                self.Logs_frame_layout.setObjectName("Logs_frame_layout")
                self.Logs_buttons_frame = QtWidgets.QFrame(self.Logs_frame)
                self.Logs_buttons_frame.setMinimumSize(QtCore.QSize(50, 0))
                self.Logs_buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Logs_buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Logs_buttons_frame.setObjectName("Logs_buttons_frame")
                self.Logs_buttons_frame_layout = QtWidgets.QVBoxLayout(self.Logs_buttons_frame)
                self.Logs_buttons_frame_layout.setContentsMargins(8, 0, 0, 0)
                self.Logs_buttons_frame_layout.setSpacing(0)
                self.Logs_buttons_frame_layout.setObjectName("Logs_buttons_frame_layout")
                self.Logs_clear_button = QtWidgets.QPushButton(self.Logs_buttons_frame)
                self.Logs_clear_button.setMaximumSize(QtCore.QSize(32, 32))
                self.Logs_clear_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Logs_clear_button.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}")
                self.Logs_clear_button.setText("")
                self.Logs_clear_button.setIcon(icon4)
                self.Logs_clear_button.setIconSize(QtCore.QSize(32, 32))
                self.Logs_clear_button.setObjectName("Logs_clear_button")
                self.Logs_buttons_frame_layout.addWidget(self.Logs_clear_button)
                self.Logs_font_h_button = QtWidgets.QPushButton(self.Logs_buttons_frame)
                self.Logs_font_h_button.setMaximumSize(QtCore.QSize(32, 32))
                self.Logs_font_h_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Logs_font_h_button.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}")
                self.Logs_font_h_button.setText("")
                icon9 = QtGui.QIcon()
                icon9.addPixmap(QtGui.QPixmap("icons/2-au.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Logs_font_h_button.setIcon(icon9)
                self.Logs_font_h_button.setIconSize(QtCore.QSize(32, 32))
                self.Logs_font_h_button.setObjectName("Logs_font_h_button")
                self.Logs_buttons_frame_layout.addWidget(self.Logs_font_h_button)
                self.Logs_fint_l_button = QtWidgets.QPushButton(self.Logs_buttons_frame)
                self.Logs_fint_l_button.setMaximumSize(QtCore.QSize(32, 32))
                self.Logs_fint_l_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Logs_fint_l_button.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}")
                self.Logs_fint_l_button.setText("")
                icon10 = QtGui.QIcon()
                icon10.addPixmap(QtGui.QPixmap("icons/2-ad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Logs_fint_l_button.setIcon(icon10)
                self.Logs_fint_l_button.setIconSize(QtCore.QSize(32, 32))
                self.Logs_fint_l_button.setObjectName("Logs_fint_l_button")
                self.Logs_buttons_frame_layout.addWidget(self.Logs_fint_l_button)
                self.Logs_frame_layout.addWidget(self.Logs_buttons_frame)
                self.Logs_list_widget = QtWidgets.QListWidget(self.Logs_frame)
                self.Logs_list_widget.setFrameShadow(QtWidgets.QFrame.Plain)
                self.Logs_list_widget.setLineWidth(2)
                self.Logs_list_widget.setObjectName("Logs_list_widget")
                item = QtWidgets.QListWidgetItem()
                self.Logs_list_widget.addItem(item)
                self.Logs_frame_layout.addWidget(self.Logs_list_widget)
                self.Visual_column_layout.addWidget(self.Logs_frame)
                self.Main_widget_layout.addWidget(self.Visual_column_frame)
                self.Operating_column_frame = QtWidgets.QFrame(self.Main_widget)
                self.Operating_column_frame.setMinimumSize(QtCore.QSize(200, 0))
                self.Operating_column_frame.setMaximumSize(QtCore.QSize(200, 16777215))
                self.Operating_column_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Operating_column_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Operating_column_frame.setObjectName("Operating_column_frame")
                self.Operating_column_frame_layout = QtWidgets.QVBoxLayout(self.Operating_column_frame)
                self.Operating_column_frame_layout.setContentsMargins(0, 0, 0, 0)
                self.Operating_column_frame_layout.setSpacing(0)
                self.Operating_column_frame_layout.setObjectName("Operating_column_frame_layout")
                self.Blank_frame = QtWidgets.QFrame(self.Operating_column_frame)
                self.Blank_frame.setMinimumSize(QtCore.QSize(0, 70))
                self.Blank_frame.setMaximumSize(QtCore.QSize(16777215, 70))
                self.Blank_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Blank_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Blank_frame.setObjectName("Blank_frame")
                self.Operating_column_frame_layout.addWidget(self.Blank_frame)
                self.Tools_out_frame = QtWidgets.QFrame(self.Operating_column_frame)
                self.Tools_out_frame.setEnabled(True)
                self.Tools_out_frame.setAcceptDrops(False)
                self.Tools_out_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.Tools_out_frame.setAutoFillBackground(False)
                self.Tools_out_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Tools_out_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Tools_out_frame.setObjectName("Tools_out_frame")
                self.Tools_stack = QtWidgets.QStackedWidget(self.Tools_out_frame)
                self.Tools_stack.setGeometry(QtCore.QRect(0, 0, 484, 450))
                self.Tools_stack.setMinimumSize(QtCore.QSize(0, 450))
                self.Tools_stack.setMaximumSize(QtCore.QSize(16777215, 450))
                self.Tools_stack.setObjectName("Tools_stack")
                self.Maintools_widget = QtWidgets.QWidget()
                self.Maintools_widget.setObjectName("Maintools_widget")
                self.Maintools_widget_layout = QtWidgets.QHBoxLayout(self.Maintools_widget)
                self.Maintools_widget_layout.setContentsMargins(12, 0, 0, 0)
                self.Maintools_widget_layout.setSpacing(0)
                self.Maintools_widget_layout.setObjectName("Maintools_widget_layout")
                self.Maintools_sub_frame = QtWidgets.QFrame(self.Maintools_widget)
                self.Maintools_sub_frame.setEnabled(True)
                self.Maintools_sub_frame.setMaximumSize(QtCore.QSize(16777215, 400))
                self.Maintools_sub_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Maintools_sub_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Maintools_sub_frame.setObjectName("Maintools_sub_frame")
                self.Maintools_sub_frame_layout = QtWidgets.QVBoxLayout(self.Maintools_sub_frame)
                self.Maintools_sub_frame_layout.setContentsMargins(0, 0, 0, 0)
                self.Maintools_sub_frame_layout.setSpacing(0)
                self.Maintools_sub_frame_layout.setObjectName("Maintools_sub_frame_layout")
                self.Maintools_oponcells_btn = QtWidgets.QPushButton(self.Maintools_sub_frame)
                self.Maintools_oponcells_btn.setMinimumSize(QtCore.QSize(0, 50))
                self.Maintools_oponcells_btn.setMaximumSize(QtCore.QSize(175, 50))
                self.Maintools_oponcells_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Maintools_oponcells_btn.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}\n"
                "")
                self.Maintools_oponcells_btn.setObjectName("Maintools_oponcells_btn")
                self.Maintools_sub_frame_layout.addWidget(self.Maintools_oponcells_btn)
                self.Maintools_newcol_btn = QtWidgets.QPushButton(self.Maintools_sub_frame)
                self.Maintools_newcol_btn.setMinimumSize(QtCore.QSize(0, 50))
                self.Maintools_newcol_btn.setMaximumSize(QtCore.QSize(175, 50))
                self.Maintools_newcol_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Maintools_newcol_btn.setAutoFillBackground(False)
                self.Maintools_newcol_btn.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}\n"
                "")
                self.Maintools_newcol_btn.setObjectName("Maintools_newcol_btn")
                self.Maintools_sub_frame_layout.addWidget(self.Maintools_newcol_btn)
                self.Maintools_newrow_btn = QtWidgets.QPushButton(self.Maintools_sub_frame)
                self.Maintools_newrow_btn.setMinimumSize(QtCore.QSize(0, 50))
                self.Maintools_newrow_btn.setMaximumSize(QtCore.QSize(175, 50))
                self.Maintools_newrow_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Maintools_newrow_btn.setAutoFillBackground(False)
                self.Maintools_newrow_btn.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}\n"
                "")
                self.Maintools_newrow_btn.setObjectName("Maintools_newrow_btn")
                self.Maintools_sub_frame_layout.addWidget(self.Maintools_newrow_btn)
                self.Maintools_filter_btn = QtWidgets.QPushButton(self.Maintools_sub_frame)
                self.Maintools_filter_btn.setMinimumSize(QtCore.QSize(0, 50))
                self.Maintools_filter_btn.setMaximumSize(QtCore.QSize(175, 50))
                self.Maintools_filter_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Maintools_filter_btn.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}\n"
                "")
                self.Maintools_filter_btn.setObjectName("Maintools_filter_btn")
                self.Maintools_sub_frame_layout.addWidget(self.Maintools_filter_btn)
                self.Maintools_sort_btn = QtWidgets.QPushButton(self.Maintools_sub_frame)
                self.Maintools_sort_btn.setMinimumSize(QtCore.QSize(0, 50))
                self.Maintools_sort_btn.setMaximumSize(QtCore.QSize(175, 50))
                self.Maintools_sort_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Maintools_sort_btn.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}\n"
                "")
                self.Maintools_sort_btn.setObjectName("Maintools_sort_btn")
                self.Maintools_sub_frame_layout.addWidget(self.Maintools_sort_btn)
                self.Maintools_default_btn = QtWidgets.QPushButton(self.Maintools_sub_frame)
                self.Maintools_default_btn.setMinimumSize(QtCore.QSize(0, 50))
                self.Maintools_default_btn.setMaximumSize(QtCore.QSize(175, 50))
                self.Maintools_default_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Maintools_default_btn.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}\n"
                "")
                self.Maintools_default_btn.setObjectName("Maintools_default_btn")
                self.Maintools_sub_frame_layout.addWidget(self.Maintools_default_btn)
                self.Maintools_widget_layout.addWidget(self.Maintools_sub_frame)
                self.Tools_stack.addWidget(self.Maintools_widget)
                self.Export_widget = QtWidgets.QWidget()
                self.Export_widget.setMaximumSize(QtCore.QSize(200, 16777215))
                self.Export_widget.setObjectName("Export_widget")
                self.Export_widget_layout = QtWidgets.QHBoxLayout(self.Export_widget)
                self.Export_widget_layout.setContentsMargins(10, 10, 10, 0)
                self.Export_widget_layout.setSpacing(0)
                self.Export_widget_layout.setObjectName("Export_widget_layout")
                self.Export_sub_frame = QtWidgets.QFrame(self.Export_widget)
                self.Export_sub_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Export_sub_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Export_sub_frame.setObjectName("Export_sub_frame")
                self.Export_sub_frame_layout = QtWidgets.QVBoxLayout(self.Export_sub_frame)
                self.Export_sub_frame_layout.setContentsMargins(0, 0, 0, 190)
                self.Export_sub_frame_layout.setSpacing(0)
                self.Export_sub_frame_layout.setObjectName("Export_sub_frame_layout")
                self.Export_file_label_1 = QtWidgets.QLabel(self.Export_sub_frame)
                self.Export_file_label_1.setStyleSheet("font-size:14px; padding-bottom: 10px;")
                self.Export_file_label_1.setWordWrap(True)
                self.Export_file_label_1.setObjectName("Export_file_label_1")
                self.Export_sub_frame_layout.addWidget(self.Export_file_label_1)
                self.Export_file_btn = QtWidgets.QPushButton(self.Export_sub_frame)
                self.Export_file_btn.setMinimumSize(QtCore.QSize(0, 30))
                self.Export_file_btn.setMaximumSize(QtCore.QSize(16777215, 30))
                self.Export_file_btn.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}\n"
                "")
                self.Export_file_btn.setObjectName("Export_file_btn")
                self.Export_file_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Export_sub_frame_layout.addWidget(self.Export_file_btn)
                self.Export_widget_layout.addWidget(self.Export_sub_frame)
                self.Tools_stack.addWidget(self.Export_widget)
                self.Import_widget = QtWidgets.QWidget()
                self.Import_widget.setMaximumSize(QtCore.QSize(200, 16777215))
                self.Import_widget.setObjectName("Import_widget")
                self.Import_widget_layout = QtWidgets.QHBoxLayout(self.Import_widget)
                self.Import_widget_layout.setContentsMargins(10, 10, 10, 0)
                self.Import_widget_layout.setSpacing(0)
                self.Import_widget_layout.setObjectName("Import_widget_layout")
                self.Import_sub_frame = QtWidgets.QFrame(self.Import_widget)
                self.Import_sub_frame.setStyleSheet("")
                self.Import_sub_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Import_sub_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Import_sub_frame.setObjectName("Import_sub_frame")
                self.Import_sub_frame_layout = QtWidgets.QVBoxLayout(self.Import_sub_frame)
                self.Import_sub_frame_layout.setContentsMargins(0, 0, 0, 130)
                self.Import_sub_frame_layout.setSpacing(0)
                self.Import_sub_frame_layout.setObjectName("Import_sub_frame_layout")
                self.Import_file_label_1 = QtWidgets.QLabel(self.Import_sub_frame)
                self.Import_file_label_1.setStyleSheet("font-size:14px; padding-bottom: 10px;")
                self.Import_file_label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.Import_file_label_1.setWordWrap(True)
                self.Import_file_label_1.setObjectName("Import_file_label_1")
                self.Import_sub_frame_layout.addWidget(self.Import_file_label_1)
                self.Import_file_label_2 = QtWidgets.QLabel(self.Import_sub_frame)
                self.Import_file_label_2.setMaximumSize(QtCore.QSize(16777215, 40))
                self.Import_file_label_2.setStyleSheet("font-size:14px;")
                self.Import_file_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.Import_file_label_2.setWordWrap(True)
                self.Import_file_label_2.setObjectName("Import_file_label_2")
                self.Import_sub_frame_layout.addWidget(self.Import_file_label_2)
                self.Import_file_btn = QtWidgets.QPushButton(self.Import_sub_frame)
                self.Import_file_btn.setMinimumSize(QtCore.QSize(0, 30))
                self.Import_file_btn.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}\n"
                "")
                self.Import_file_btn.setObjectName("Import_file_btn")
                self.Import_file_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Import_sub_frame_layout.addWidget(self.Import_file_btn)
                self.Import_widget_layout.addWidget(self.Import_sub_frame)
                self.Tools_stack.addWidget(self.Import_widget)
                self.Prediction_widget = QtWidgets.QWidget()
                self.Prediction_widget.setMaximumSize(QtCore.QSize(200, 16777215))
                self.Prediction_widget.setObjectName("Prediction_widget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.Prediction_widget)
                self.horizontalLayout.setContentsMargins(10, 10, 10, 0)
                self.horizontalLayout.setSpacing(0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.Prediction_sub_frame = QtWidgets.QFrame(self.Prediction_widget)
                self.Prediction_sub_frame.setMinimumSize(QtCore.QSize(150, 200))
                self.Prediction_sub_frame.setMaximumSize(QtCore.QSize(200, 16777215))
                self.Prediction_sub_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Prediction_sub_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Prediction_sub_frame.setObjectName("Prediction_sub_frame")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.Prediction_sub_frame)
                self.verticalLayout.setContentsMargins(0, 0, 0, 250)
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setObjectName("verticalLayout")
                self.Prediction_linreg_btn = QtWidgets.QPushButton(self.Prediction_sub_frame)
                self.Prediction_linreg_btn.setMaximumSize(QtCore.QSize(175, 50))
                self.Prediction_linreg_btn.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}\n"
                "")
                self.Prediction_linreg_btn.setObjectName("Prediction_linreg_btn")
                self.verticalLayout.addWidget(self.Prediction_linreg_btn)
                self.horizontalLayout.addWidget(self.Prediction_sub_frame)
                self.Tools_stack.addWidget(self.Prediction_widget)
                self.Settings_widget = QtWidgets.QWidget()
                self.Settings_widget.setMinimumSize(QtCore.QSize(0, 350))
                self.Settings_widget.setMaximumSize(QtCore.QSize(16777215, 400))
                self.Settings_widget.setObjectName("Settings_widget")
                self.Settings_widget_layout = QtWidgets.QHBoxLayout(self.Settings_widget)
                self.Settings_widget_layout.setContentsMargins(25, 0, 10, 0)
                self.Settings_widget_layout.setSpacing(0)
                self.Settings_widget_layout.setObjectName("Settings_widget_layout")
                self.Settings_sub_frame = QtWidgets.QFrame(self.Settings_widget)
                self.Settings_sub_frame.setMinimumSize(QtCore.QSize(155, 350))
                self.Settings_sub_frame.setMaximumSize(QtCore.QSize(16777215, 350))
                self.Settings_sub_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Settings_sub_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Settings_sub_frame.setObjectName("Settings_sub_frame")
                self.Settings_sub_frame_layout = QtWidgets.QVBoxLayout(self.Settings_sub_frame)
                self.Settings_sub_frame_layout.setContentsMargins(0, 0, 0, 0)
                self.Settings_sub_frame_layout.setSpacing(0)
                self.Settings_sub_frame_layout.setObjectName("Settings_sub_frame_layout")
                self.Settings_theme_label = QtWidgets.QLabel(self.Settings_sub_frame)
                self.Settings_theme_label.setMinimumSize(QtCore.QSize(0, 25))
                self.Settings_theme_label.setMaximumSize(QtCore.QSize(16777215, 25))
                self.Settings_theme_label.setStyleSheet("display: inline-block;\n"
                "font-size: 16px;\n"
                "white-space: normal;\n"
                "word-wrap: break-word;\n"
                "font-family: Sans-Serif;")
                self.Settings_theme_label.setObjectName("Settings_theme_label")
                self.Settings_sub_frame_layout.addWidget(self.Settings_theme_label)
                self.Settings_theme_combo = QtWidgets.QComboBox(self.Settings_sub_frame)
                self.Settings_theme_combo.setMinimumSize(QtCore.QSize(0, 30))
                self.Settings_theme_combo.setMaximumSize(QtCore.QSize(130, 30))
                self.Settings_theme_combo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Settings_theme_combo.setStyleSheet("\n"
                "border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "font-family: Sans-Serif;")
                self.Settings_theme_combo.setObjectName("Settings_theme_combo")
                self.Settings_theme_combo.addItem("")
                self.Settings_theme_combo.addItem("")
                self.Settings_sub_frame_layout.addWidget(self.Settings_theme_combo)
                self.Settings_language_label = QtWidgets.QLabel(self.Settings_sub_frame)
                self.Settings_language_label.setMaximumSize(QtCore.QSize(16777215, 25))
                self.Settings_language_label.setStyleSheet("display: inline-block;\n"
                "font-size: 16px;\n"
                "white-space: normal;\n"
                "word-wrap: break-word;\n"
                "font-family: Sans-Serif;")
                self.Settings_language_label.setObjectName("Settings_language_label")
                self.Settings_sub_frame_layout.addWidget(self.Settings_language_label)
                self.Settings_language_combo = QtWidgets.QComboBox(self.Settings_sub_frame)
                self.Settings_language_combo.setMinimumSize(QtCore.QSize(0, 30))
                self.Settings_language_combo.setMaximumSize(QtCore.QSize(130, 30))
                self.Settings_language_combo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Settings_language_combo.setStyleSheet("border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "font-family: Sans-Serif;")
                self.Settings_language_combo.setObjectName("Settings_language_combo")
                self.Settings_language_combo.addItem("")
                self.Settings_language_combo.addItem("")
                self.Settings_sub_frame_layout.addWidget(self.Settings_language_combo)
                self.Settings_table_font_label = QtWidgets.QLabel(self.Settings_sub_frame)
                self.Settings_table_font_label.setMaximumSize(QtCore.QSize(16777215, 25))
                self.Settings_table_font_label.setStyleSheet("display: inline-block;\n"
                "font-size: 16px;\n"
                "white-space: normal;\n"
                "word-wrap: break-word;\n"
                "font-family: Sans-Serif;")
                self.Settings_table_font_label.setObjectName("Settings_table_font_label")
                self.Settings_sub_frame_layout.addWidget(self.Settings_table_font_label)
                self.Settings_table_font_combo = QtWidgets.QComboBox(self.Settings_sub_frame)
                self.Settings_table_font_combo.setMinimumSize(QtCore.QSize(0, 30))
                self.Settings_table_font_combo.setMaximumSize(QtCore.QSize(130, 30))
                self.Settings_table_font_combo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Settings_table_font_combo.setStyleSheet("border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "font-family: Sans-Serif;")
                self.Settings_table_font_combo.setObjectName("Settings_table_font_combo")
                self.Settings_table_font_combo.addItem("")
                self.Settings_table_font_combo.addItem("")
                self.Settings_table_font_combo.addItem("")
                self.Settings_table_font_combo.addItem("")
                self.Settings_table_font_combo.addItem("")
                self.Settings_table_font_combo.addItem("")
                self.Settings_sub_frame_layout.addWidget(self.Settings_table_font_combo)
                self.Settings_log_font_label = QtWidgets.QLabel(self.Settings_sub_frame)
                self.Settings_log_font_label.setMaximumSize(QtCore.QSize(16777215, 25))
                self.Settings_log_font_label.setStyleSheet("display: inline-block;\n"
                "font-size: 16px;\n"
                "white-space: normal;\n"
                "word-wrap: break-word;\n"
                "font-family: Sans-Serif;")
                self.Settings_log_font_label.setObjectName("Settings_log_font_label")
                self.Settings_sub_frame_layout.addWidget(self.Settings_log_font_label)
                self.Settings_log_font_combo = QtWidgets.QComboBox(self.Settings_sub_frame)
                self.Settings_log_font_combo.setMinimumSize(QtCore.QSize(0, 30))
                self.Settings_log_font_combo.setMaximumSize(QtCore.QSize(130, 30))
                self.Settings_log_font_combo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Settings_log_font_combo.setStyleSheet("border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "font-family: Sans-Serif;")
                self.Settings_log_font_combo.setObjectName("Settings_log_font_combo")
                self.Settings_log_font_combo.addItem("")
                self.Settings_log_font_combo.addItem("")
                self.Settings_log_font_combo.addItem("")
                self.Settings_log_font_combo.addItem("")
                self.Settings_log_font_combo.addItem("")
                self.Settings_log_font_combo.addItem("")
                self.Settings_sub_frame_layout.addWidget(self.Settings_log_font_combo)
                self.Settings_widget_layout.addWidget(self.Settings_sub_frame)
                self.Tools_stack.addWidget(self.Settings_widget)
                self.Plot_widget = QtWidgets.QWidget()
                self.Plot_widget.setObjectName("Plot_widget")
                self.Plot_widget_layout = QtWidgets.QHBoxLayout(self.Plot_widget)
                self.Plot_widget_layout.setContentsMargins(12, 0, 0, 0)
                self.Plot_widget_layout.setObjectName("Plot_widget_layout")
                self.Plots_sub_frame = QtWidgets.QFrame(self.Plot_widget)
                self.Plots_sub_frame.setMaximumSize(QtCore.QSize(16777215, 400))
                self.Plots_sub_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Plots_sub_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Plots_sub_frame.setObjectName("Plots_sub_frame")
                self.Plots_sub_frame_layout = QtWidgets.QVBoxLayout(self.Plots_sub_frame)
                self.Plots_sub_frame_layout.setContentsMargins(0, 0, 0, 0)
                self.Plots_sub_frame_layout.setSpacing(0)
                self.Plots_sub_frame_layout.setObjectName("Plots_sub_frame_layout")
                self.Plots_column_btn = QtWidgets.QPushButton(self.Plots_sub_frame)
                self.Plots_column_btn.setMinimumSize(QtCore.QSize(0, 50))
                self.Plots_column_btn.setMaximumSize(QtCore.QSize(175, 50))
                self.Plots_column_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Plots_column_btn.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}\n"
                "")
                self.Plots_column_btn.setObjectName("Plots_column_btn")
                self.Plots_sub_frame_layout.addWidget(self.Plots_column_btn)
                self.Plots_linear_btn = QtWidgets.QPushButton(self.Plots_sub_frame)
                self.Plots_linear_btn.setMinimumSize(QtCore.QSize(0, 50))
                self.Plots_linear_btn.setMaximumSize(QtCore.QSize(175, 50))
                self.Plots_linear_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Plots_linear_btn.setAutoFillBackground(False)
                self.Plots_linear_btn.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}\n"
                "")
                self.Plots_linear_btn.setObjectName("Plots_linear_btn")
                self.Plots_sub_frame_layout.addWidget(self.Plots_linear_btn)
                self.Plots_circle_btn = QtWidgets.QPushButton(self.Plots_sub_frame)
                self.Plots_circle_btn.setMinimumSize(QtCore.QSize(0, 50))
                self.Plots_circle_btn.setMaximumSize(QtCore.QSize(175, 50))
                self.Plots_circle_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Plots_circle_btn.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}\n"
                "")
                self.Plots_circle_btn.setObjectName("Plots_circle_btn")
                self.Plots_sub_frame_layout.addWidget(self.Plots_circle_btn)
                self.Plots_stake_btn = QtWidgets.QPushButton(self.Plots_sub_frame)
                self.Plots_stake_btn.setMinimumSize(QtCore.QSize(0, 50))
                self.Plots_stake_btn.setMaximumSize(QtCore.QSize(175, 50))
                self.Plots_stake_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Plots_stake_btn.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}\n"
                "")
                self.Plots_stake_btn.setObjectName("Plots_stake_btn")
                self.Plots_sub_frame_layout.addWidget(self.Plots_stake_btn)
                self.Plots_point_btn = QtWidgets.QPushButton(self.Plots_sub_frame)
                self.Plots_point_btn.setMinimumSize(QtCore.QSize(0, 50))
                self.Plots_point_btn.setMaximumSize(QtCore.QSize(175, 50))
                self.Plots_point_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Plots_point_btn.setStyleSheet("QPushButton {\n"
                "background-color: Transparent;\n"
                "border-radius: 6px;\n"
                "border: 2px solid #595959; \n"
                "font-size: 14px;\n"
                "white-space: normal;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color: #d9d9d9;\n"
                "}\n"
                "")
                self.Plots_point_btn.setObjectName("Plots_point_btn")
                self.Plots_sub_frame_layout.addWidget(self.Plots_point_btn)
                self.Plot_widget_layout.addWidget(self.Plots_sub_frame)
                self.Tools_stack.addWidget(self.Plot_widget)
                self.Operating_column_frame_layout.addWidget(self.Tools_out_frame)
                self.Version_frame = QtWidgets.QFrame(self.Operating_column_frame)
                self.Version_frame.setMinimumSize(QtCore.QSize(0, 60))
                self.Version_frame.setMaximumSize(QtCore.QSize(16777215, 60))
                self.Version_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Version_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Version_frame.setObjectName("Version_frame")
                self.Version_frame_layout = QtWidgets.QVBoxLayout(self.Version_frame)
                self.Version_frame_layout.setContentsMargins(5, 5, 5, 5)
                self.Version_frame_layout.setSpacing(5)
                self.Version_frame_layout.setObjectName("Version_frame_layout")
                self.Version_label = QtWidgets.QLabel(self.Version_frame)
                self.Version_label.setMinimumSize(QtCore.QSize(60, 0))
                font = QtGui.QFont()
                font.setFamily("Sans-Serif")
                self.Version_label.setFont(font)
                self.Version_label.setStyleSheet("font-size: 12px")
                self.Version_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.Version_label.setWordWrap(True)
                self.Version_label.setObjectName("Version_label")
                self.Version_frame_layout.addWidget(self.Version_label)
                self.Operating_column_frame_layout.addWidget(self.Version_frame)
                self.Main_widget_layout.addWidget(self.Operating_column_frame)
                MainWindow.setCentralWidget(self.Main_widget)
                self.retranslateUi(MainWindow)
                self.Tools_stack.setCurrentIndex(3)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                self.set_page(MainWindow)

                self.settings = Settings(self.Settings_theme_combo, self.Settings_language_combo, self.Settings_table_font_combo, self.Settings_log_font_combo)
                self.core = Core(self.db, self.db_memory, self.Table_widget)
                self.import_ = Import(self.log_list)
                self.export_ = Export(self.log_list)
                self.update_ = Update()
                self.buttons_events()
                self.event_show_window_buttons()
                self.update_.default_database(self.db, self.db_memory, self.Table_widget)
                #self.Logs_list_widget.addItem('ZULUL')
                #self.Logs_list_widget.takeItem(0)

        def set_page(self, MainWindow):
                self.Main_new_file_1.clicked.connect(lambda: self.Tools_stack.setCurrentWidget(self.Import_widget))
                self.Main_new_file_1.clicked.connect(lambda: self.Mian_label_stack.setCurrentWidget(self.Main_new_file_title_widget))

                self.Main_export_9.clicked.connect(lambda: self.Tools_stack.setCurrentWidget(self.Export_widget))
                self.Main_export_9.clicked.connect(lambda: self.Mian_label_stack.setCurrentWidget(self.Main_export_widget))

                self.Main_maintools_5.clicked.connect(lambda: self.Tools_stack.setCurrentWidget(self.Maintools_widget))
                self.Main_maintools_5.clicked.connect(lambda: self.Mian_label_stack.setCurrentWidget(self.Main_maintools_widget))

                self.Main_plots_6.clicked.connect(lambda: self.Tools_stack.setCurrentWidget(self.Plot_widget))
                self.Main_plots_6.clicked.connect(lambda: self.Mian_label_stack.setCurrentWidget(self.Main_plot_widget))

                self.Main_predicdtions_7.clicked.connect(lambda: self.Tools_stack.setCurrentWidget(self.Prediction_widget))
                self.Main_predicdtions_7.clicked.connect(lambda: self.Mian_label_stack.setCurrentWidget(self.Main_predictions_widget))

                self.Main_settings_8.clicked.connect(lambda: self.Tools_stack.setCurrentWidget(self.Settings_widget))
                self.Main_settings_8.clicked.connect(lambda: self.Mian_label_stack.setCurrentWidget(self.Main_settings_widget))

        def buttons_events(self):
                self.Import_file_btn.clicked.connect(self.event_import)
                self.Export_file_btn.clicked.connect(self.event_export)
                self.Main_clear_db_4.clicked.connect(self.event_clear_db)
                self.Logs_clear_button.clicked.connect(self.event_clear_logs)

        def event_show_window_buttons(self):
                self.Maintools_oponcells_btn.clicked.connect(self.event_show_window_COW)
                self.Maintools_newcol_btn.clicked.connect(self.event_show_window_NCW)
                self.Maintools_newrow_btn.clicked.connect(self.event_show_window_NRW)
                self.Maintools_filter_btn.clicked.connect(self.event_show_window_FW)
                self.Maintools_sort_btn.clicked.connect(self.event_show_window_SW)
                self.Maintools_default_btn.clicked.connect(self.event_show_window_DW)
                self.Plots_linear_btn.clicked.connect(lambda: self.event_show_window_PW('linear'))
                self.Plots_circle_btn.clicked.connect(lambda: self.event_show_window_PW('circle'))
                self.Plots_stake_btn.clicked.connect(lambda: self.event_show_window_PW('stake'))
                self.Plots_point_btn.clicked.connect(lambda: self.event_show_window_PW('point'))
                self.Main_undo_2.clicked.connect(self.update_.db_back)
                self.Main_reto_3.clicked.connect(self.update_.db_forward)

        def event_show_window_COW(self):
                self.COW = Cell_Operations_Window(self.db)
                self.COW.show()
        
        def event_show_window_NCW(self):
                self.NCW = New_Colmuns_Window(self.db, self.Table_widget)
                self.NCW.show()

        def event_show_window_NRW(self):
                #Do poprawki!
                self.NRW = New_Rows_Window(self.db, self.Table_widget)
                self.NRW.show()

        def event_show_window_FW(self):
                #Testowanie
                self.FW = Filtering_Window(self.db, self.Table_widget)
                self.FW.show()

        def event_show_window_SW(self):
                self.SW = Sorting_Window(self.db, self.Table_widget)
                self.SW.show()

        def event_show_window_DW(self):
                self.DW = Default_Window(self.db, self.db_memory, self.Table_widget)
                
        def event_show_window_PW(self, typ):
                self.PW = Plot_Window(self.db, self.Table_widget, typ)
                self.PW.show()


        def event_clear_logs(self):
                self.Logs_list_widget.clear()
                self.log_list.clear()
                self.refresh_logs()

        def event_clear_db(self):
                self.update_.default_database(self.db, self.db_memory, self.Table_widget)
                self.refresh_logs()

        def event_import(self):
                self.db = self.import_.import_dialog(self.Table_widget, self.db)
                self.refresh_logs()
        
        def event_export(self):
                self.export_.export_dialog(self.db)
                self.refresh_logs()

        def refresh_logs(self):
                print(self.log_list)
                self.Logs_list_widget.clear()
                self.Logs_list_widget.addItems(self.log_list)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.Main_new_file_title_label.setText(_translate("MainWindow", "Importuj Plik"))
                self.Main_reto_title_label.setText(_translate("MainWindow", "Przywróć"))
                self.Main_undo_title_label.setText(_translate("MainWindow", "Cofnij"))
                self.Main_clear_db_label.setText(_translate("MainWindow", "Wyczyść Tabelę"))
                self.Main_maintools_label.setText(_translate("MainWindow", "Narzędzia"))
                self.Main_plot_label.setText(_translate("MainWindow", "Wykresy"))
                self.Main_predictions_label.setText(_translate("MainWindow", "Nauczanie Maszynowe"))
                self.Main_settings_label.setText(_translate("MainWindow", "Opcje"))
                self.Main_export_label.setText(_translate("MainWindow", "Eksport Pliku"))
                self.Maintools_oponcells_btn.setText(_translate("MainWindow", "Operacje na komórkach"))
                self.Maintools_newcol_btn.setText(_translate("MainWindow", "Nowe kolumny"))
                self.Maintools_newrow_btn.setText(_translate("MainWindow", "Nowe wiersze"))
                self.Maintools_filter_btn.setText(_translate("MainWindow", "Filtrowanie"))
                self.Maintools_sort_btn.setText(_translate("MainWindow", "Sortowanie"))
                self.Maintools_default_btn.setText(_translate("MainWindow", "Stan domyślny"))
                self.Export_file_label_1.setText(_translate("MainWindow", "Zaimportuj bazę danych za pomocą fukcji Import. Program obsługuję jedynie pliki, które są dedykowane do procesu podglądu, edycji, filtrowania itp. dużej ilości danych. Dane zawarte w plikach muszą być wstępnie przygotowane pod względem kompatybilności jeżeli mamy do czynienia z różnymi zapisami plików.  "))
                self.Export_file_btn.setText(_translate("MainWindow", "Eksport"))
                self.Import_file_label_1.setText(_translate("MainWindow", "Zaimportuj bazę danych za pomocą fukcji Import. Program obsługuję jedynie pliki, które są dedykowane do procesu podglądu, edycji, filtrowania itp. dużej ilości danych. Dane zawarte w plikach muszą być wstępnie przygotowane pod względem kompatybilności jeżeli mamy do czynienia z różnymi zapisami plików.  "))
                self.Import_file_label_2.setText(_translate("MainWindow", "Obsługiwane formaty: .json, .csv, .txt, .xml"))
                self.Import_file_btn.setText(_translate("MainWindow", "Import"))
                self.Prediction_linreg_btn.setText(_translate("MainWindow", "Regresja Liniowa"))
                self.Settings_theme_label.setText(_translate("MainWindow", "Motyw:"))
                self.Settings_theme_combo.setItemText(0, _translate("MainWindow", "Light"))
                self.Settings_theme_combo.setItemText(1, _translate("MainWindow", "Dark"))
                self.Settings_language_label.setText(_translate("MainWindow", "Język:"))
                self.Settings_language_combo.setItemText(0, _translate("MainWindow", "Polish"))
                self.Settings_language_combo.setItemText(1, _translate("MainWindow", "English"))
                self.Settings_table_font_label.setText(_translate("MainWindow", "Rozmiar czcionki (T):"))
                self.Settings_table_font_combo.setItemText(0, _translate("MainWindow", "8 px"))
                self.Settings_table_font_combo.setItemText(1, _translate("MainWindow", "10 px"))
                self.Settings_table_font_combo.setItemText(2, _translate("MainWindow", "12 px"))
                self.Settings_table_font_combo.setItemText(3, _translate("MainWindow", "14 px"))
                self.Settings_table_font_combo.setItemText(4, _translate("MainWindow", "16 px"))
                self.Settings_table_font_combo.setItemText(5, _translate("MainWindow", "18 px"))
                self.Settings_log_font_label.setText(_translate("MainWindow", "Rozmiar czcionki (L):"))
                self.Settings_log_font_combo.setItemText(0, _translate("MainWindow", "8 px"))
                self.Settings_log_font_combo.setItemText(1, _translate("MainWindow", "10 px"))
                self.Settings_log_font_combo.setItemText(2, _translate("MainWindow", "12 px"))
                self.Settings_log_font_combo.setItemText(3, _translate("MainWindow", "14 px"))
                self.Settings_log_font_combo.setItemText(4, _translate("MainWindow", "16 px"))
                self.Settings_log_font_combo.setItemText(5, _translate("MainWindow", "18 px"))
                self.Plots_column_btn.setText(_translate("MainWindow", "Analityka"))
                self.Plots_linear_btn.setText(_translate("MainWindow", "Wykres liniowy"))
                self.Plots_circle_btn.setText(_translate("MainWindow", "Wykres kołowy"))
                self.Plots_stake_btn.setText(_translate("MainWindow", "Wykres słupkowy"))
                self.Plots_point_btn.setText(_translate("MainWindow", "Wykres punktowy"))
                self.Version_label.setText(_translate("MainWindow", " Copyright Ⓒ 2021 Grzegorz Jakimiuk. All Right Reserved"))
                
       
if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
