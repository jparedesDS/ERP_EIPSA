# Form implementation generated from reading ui file 'QueryOffer_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import re
from PyQt6 import QtCore, QtGui, QtWidgets
import psycopg2
from config import config
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeySequence, QTextDocument, QTextCursor
from PyQt6.QtWidgets import QApplication
import locale
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os

basedir = os.path.dirname(__file__)


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignmentFlag.AlignCenter

        if index.column() == 2:  # Verifica que estemos en la tercera columna
            value = index.data()

            if value == "Adjudicada":  
                color = QtGui.QColor(0, 255, 0)  # Green if "Adjudicada"
            elif value == "Desestimada":
                color = QtGui.QColor(255, 124, 128)  # Red if "Desestimada"
            elif value == "Estimación":
                color = QtGui.QColor(142, 162, 219)  # Blue if "Estimación"
            elif value == "Presentada":
                color = QtGui.QColor(255, 255, 0)  # Yellow if "Presentada"
            elif value == "Rechazada":
                color = QtGui.QColor(244, 176, 132)  # Orange if "Rechazada"
            else:
                color = QtGui.QColor(255, 255, 255)  # White for rest

            option.backgroundBrush = color


class Ui_QueryOffer_Window(object):
    def setupUi(self, QueryOffer_Window):
        QueryOffer_Window.setObjectName("QueryOffer_Window")
        QueryOffer_Window.resize(845, 590)
        QueryOffer_Window.setMinimumSize(QtCore.QSize(1000, 590))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(basedir, "Resources/Iconos/icon.ico")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        QueryOffer_Window.setWindowIcon(icon)
        QueryOffer_Window.setStyleSheet("QWidget {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
".QFrame {\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: #33bdef;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 3px;\n"
"  color: #fff;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",\"Liberation Sans\",sans-serif;\n"
"  font-size: 15px;\n"
"  font-weight: 800;\n"
"  line-height: 1.15385;\n"
"  margin: 0;\n"
"  outline: none;\n"
"  padding: 8px .8em;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  vertical-align: baseline;\n"
"  white-space: nowrap;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #019ad2;\n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #019ad2;\n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1, 140, 190);\n"
"    border-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:focus:pressed {\n"
"    background-color: rgb(1, 140, 190);\n"
"    border-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=QueryOffer_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.hLayout1 = QtWidgets.QHBoxLayout()
        self.hLayout1.setObjectName("hLayout1")
        self.label_NumOffer = QtWidgets.QLabel(parent=self.frame)
        self.label_NumOffer.setMinimumSize(QtCore.QSize(95, 25))
        self.label_NumOffer.setMaximumSize(QtCore.QSize(95, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_NumOffer.setFont(font)
        self.label_NumOffer.setObjectName("label_NumOffer")
        self.hLayout1.addWidget(self.label_NumOffer)
        self.Numoffer_QueryOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.Numoffer_QueryOffer.setMinimumSize(QtCore.QSize(250, 25))
        self.Numoffer_QueryOffer.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Numoffer_QueryOffer.setFont(font)
        self.Numoffer_QueryOffer.setObjectName("Numoffer_QueryOffer")
        self.hLayout1.addWidget(self.Numoffer_QueryOffer)
        self.label_RefNum = QtWidgets.QLabel(parent=self.frame)
        self.label_RefNum.setMinimumSize(QtCore.QSize(90, 25))
        self.label_RefNum.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_RefNum.setFont(font)
        self.label_RefNum.setObjectName("label_RefNum")
        self.hLayout1.addWidget(self.label_RefNum)
        self.Ref_QueryOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.Ref_QueryOffer.setMinimumSize(QtCore.QSize(250, 25))
        self.Ref_QueryOffer.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Ref_QueryOffer.setFont(font)
        self.Ref_QueryOffer.setObjectName("Ref_QueryOffer")
        self.hLayout1.addWidget(self.Ref_QueryOffer)
        self.gridLayout_2.addLayout(self.hLayout1, 1, 0, 1, 1)
        self.hLayout2 = QtWidgets.QHBoxLayout()
        self.hLayout2.setObjectName("hLayout2")
        self.label_Responsible = QtWidgets.QLabel(parent=self.frame)
        self.label_Responsible.setMinimumSize(QtCore.QSize(95, 25))
        self.label_Responsible.setMaximumSize(QtCore.QSize(95, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_Responsible.setFont(font)
        self.label_Responsible.setObjectName("label_Responsible")
        self.hLayout2.addWidget(self.label_Responsible)
        self.Responsible_QueryOffer = QtWidgets.QComboBox(parent=self.frame)
        self.Responsible_QueryOffer.setMinimumSize(QtCore.QSize(250, 25))
        self.Responsible_QueryOffer.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Responsible_QueryOffer.setFont(font)
        self.Responsible_QueryOffer.setObjectName("Responsible_QueryOffer")
        self.hLayout2.addWidget(self.Responsible_QueryOffer)
        self.label_Client = QtWidgets.QLabel(parent=self.frame)
        self.label_Client.setMinimumSize(QtCore.QSize(90, 25))
        self.label_Client.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_Client.setFont(font)
        self.label_Client.setObjectName("label_Client")
        self.hLayout2.addWidget(self.label_Client)
        self.Client_QueryOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.Client_QueryOffer.setMinimumSize(QtCore.QSize(250, 25))
        self.Client_QueryOffer.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Client_QueryOffer.setFont(font)
        self.Client_QueryOffer.setObjectName("Client_QueryOffer")
        self.hLayout2.addWidget(self.Client_QueryOffer)
        self.gridLayout_2.addLayout(self.hLayout2, 2, 0, 1, 1)
        self.hLayout3 = QtWidgets.QHBoxLayout()
        self.hLayout3.setObjectName("hLayout3")
        self.label_State = QtWidgets.QLabel(parent=self.frame)
        self.label_State.setMinimumSize(QtCore.QSize(95, 25))
        self.label_State.setMaximumSize(QtCore.QSize(95, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_State.setFont(font)
        self.label_State.setObjectName("label_State")
        self.hLayout3.addWidget(self.label_State)
        self.State_QueryOffer = QtWidgets.QComboBox(parent=self.frame)
        self.State_QueryOffer.setMinimumSize(QtCore.QSize(250, 25))
        self.State_QueryOffer.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.State_QueryOffer.setFont(font)
        self.State_QueryOffer.setObjectName("State_QueryOffer")
        self.hLayout3.addWidget(self.State_QueryOffer)
        self.label_FinalClient = QtWidgets.QLabel(parent=self.frame)
        self.label_FinalClient.setMinimumSize(QtCore.QSize(90, 25))
        self.label_FinalClient.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_FinalClient.setFont(font)
        self.label_FinalClient.setObjectName("label_FinalClient")
        self.hLayout3.addWidget(self.label_FinalClient)
        self.FinalClient_QueryOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.FinalClient_QueryOffer.setMinimumSize(QtCore.QSize(250, 25))
        self.FinalClient_QueryOffer.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FinalClient_QueryOffer.setFont(font)
        self.FinalClient_QueryOffer.setObjectName("FinalClient_QueryOffer")
        self.hLayout3.addWidget(self.FinalClient_QueryOffer)
        self.gridLayout_2.addLayout(self.hLayout3, 3, 0, 1, 1)
        self.hLayout4 = QtWidgets.QHBoxLayout()
        self.hLayout4.setObjectName("hLayout4")
        self.label_Material = QtWidgets.QLabel(parent=self.frame)
        self.label_Material.setMinimumSize(QtCore.QSize(90, 25))
        self.label_Material.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_Material.setFont(font)
        self.label_Material.setObjectName("label_Material")
        self.hLayout4.addWidget(self.label_Material)
        self.Material_QueryOffer = QtWidgets.QComboBox(parent=self.frame)
        self.Material_QueryOffer.setMinimumSize(QtCore.QSize(250, 25))
        self.Material_QueryOffer.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Material_QueryOffer.setFont(font)
        self.Material_QueryOffer.setObjectName("Material_QueryOffer")
        self.hLayout4.addWidget(self.Material_QueryOffer)
        self.gridLayout_2.addLayout(self.hLayout4, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 5, 0, 1, 1)
        self.hLayout4 = QtWidgets.QHBoxLayout()
        self.hLayout4.setObjectName("hLayout4")
        self.Button_Clean = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Clean.setMinimumSize(QtCore.QSize(150, 35))
        self.Button_Clean.setMaximumSize(QtCore.QSize(150, 35))
        self.Button_Clean.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Button_Clean.setObjectName("Button_Clean")
        self.hLayout4.addWidget(self.Button_Clean)
        self.Button_Query = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Query.setMinimumSize(QtCore.QSize(150, 35))
        self.Button_Query.setMaximumSize(QtCore.QSize(150, 35))
        self.Button_Query.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Button_Query.setObjectName("Button_Query")
        self.hLayout4.addWidget(self.Button_Query)
        self.Button_Export = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Export.setMinimumSize(QtCore.QSize(150, 35))
        self.Button_Export.setMaximumSize(QtCore.QSize(150, 35))
        self.Button_Export.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Button_Export.setObjectName("Button_Export")
        self.hLayout4.addWidget(self.Button_Export)
        self.gridLayout_2.addLayout(self.hLayout4, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 7, 0, 1, 1)
        self.tableQueryOffer = QtWidgets.QTableWidget(parent=self.frame)
        self.tableQueryOffer.setObjectName("tableQueryOffer")
        self.tableQueryOffer.setColumnCount(11)
        self.tableQueryOffer.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableQueryOffer.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableQueryOffer.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableQueryOffer.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableQueryOffer.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableQueryOffer.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableQueryOffer.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableQueryOffer.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableQueryOffer.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableQueryOffer.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableQueryOffer.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableQueryOffer.setHorizontalHeaderItem(10, item)
        self.tableQueryOffer.setSortingEnabled(True)
        self.tableQueryOffer.horizontalHeader().setStyleSheet("QHeaderView::section {background-color: #33bdef; border: 1px solid black;}")
        self.gridLayout_2.addWidget(self.tableQueryOffer, 8, 0, 1, 1)
        self.hLayout5 = QtWidgets.QHBoxLayout()
        self.hLayout5.setObjectName("hLayout5")
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hLayout5.addItem(spacerItem3)
        self.label_SumItems = QtWidgets.QLabel(parent=self.frame)
        self.label_SumItems.setMinimumSize(QtCore.QSize(40, 10))
        self.label_SumItems.setMaximumSize(QtCore.QSize(40, 10))
        self.label_SumItems.setText("")
        self.label_SumItems.setObjectName("label_SumItems")
        self.hLayout5.addWidget(self.label_SumItems)
        self.label_SumValue = QtWidgets.QLabel(parent=self.frame)
        self.label_SumValue.setMinimumSize(QtCore.QSize(80, 20))
        self.label_SumValue.setMaximumSize(QtCore.QSize(80, 20))
        self.label_SumValue.setText("")
        self.label_SumValue.setObjectName("label_SumValue")
        self.hLayout5.addWidget(self.label_SumValue)
        self.label_CountItems = QtWidgets.QLabel(parent=self.frame)
        self.label_CountItems.setMinimumSize(QtCore.QSize(60, 10))
        self.label_CountItems.setMaximumSize(QtCore.QSize(60, 10))
        self.label_CountItems.setText("")
        self.label_CountItems.setObjectName("label_CountItems")
        self.hLayout5.addWidget(self.label_CountItems)
        self.label_CountValue = QtWidgets.QLabel(parent=self.frame)
        self.label_CountValue.setMinimumSize(QtCore.QSize(80, 10))
        self.label_CountValue.setMaximumSize(QtCore.QSize(80, 10))
        self.label_CountValue.setText("")
        self.label_CountValue.setObjectName("label_CountValue")
        self.hLayout5.addWidget(self.label_CountValue)
        self.gridLayout_2.addLayout(self.hLayout5, 9, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        QueryOffer_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=QueryOffer_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 22))
        self.menubar.setObjectName("menubar")
        QueryOffer_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=QueryOffer_Window)
        self.statusbar.setObjectName("statusbar")
        QueryOffer_Window.setStatusBar(self.statusbar)
        self.tableQueryOffer.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        commands_comboboxes1queryoffer = ("""
                        SELECT *
                        FROM product_type
                        """)
        commands_comboboxes2queryoffer = ("""
                        SELECT *
                        FROM offers
                        """)
        conn = None
        try:
        # read the connection parameters
            params = config()
        # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # execution of commands one by one
            cur.execute(commands_comboboxes1queryoffer)
            results1=cur.fetchall()
            cur.execute(commands_comboboxes2queryoffer)
            results2=cur.fetchall()
        # close communication with the PostgreSQL database server
            cur.close()
        # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        list_material = [''] + list(set([x[1] for x in results1]))
        self.Material_QueryOffer.addItems(sorted(list_material))

        list_states = [''] + list(set([x[1] for x in results2]))
        self.State_QueryOffer.addItems(sorted(list_states))

        list_responsibles = [''] + list(set([x[2] for x in results2]))
        self.Responsible_QueryOffer.addItems(sorted(list_responsibles))

        self.retranslateUi(QueryOffer_Window)
        QtCore.QMetaObject.connectSlotsByName(QueryOffer_Window)
        self.Button_Clean.clicked.connect(self.clean_boxes) # type: ignore
        self.Button_Query.clicked.connect(self.query_offer)
        self.Button_Export.clicked.connect(self.export_data)  # type: ignore
        self.Numoffer_QueryOffer.returnPressed.connect(self.query_offer)
        self.Client_QueryOffer.returnPressed.connect(self.query_offer)
        self.FinalClient_QueryOffer.returnPressed.connect(self.query_offer)
        self.Ref_QueryOffer.returnPressed.connect(self.query_offer)
        self.Responsible_QueryOffer.currentIndexChanged.connect(self.query_offer)
        self.State_QueryOffer.currentIndexChanged.connect(self.query_offer)
        self.Material_QueryOffer.currentIndexChanged.connect(self.query_offer)
        self.tableQueryOffer.itemSelectionChanged.connect(self.countSelectedCells)
        self.tableQueryOffer.itemDoubleClicked.connect(self.on_item_double_clicked)


    def retranslateUi(self, QueryOffer_Window):
        _translate = QtCore.QCoreApplication.translate
        QueryOffer_Window.setWindowTitle(_translate("QueryOffer_Window", "Consultar Oferta"))
        item = self.tableQueryOffer.horizontalHeaderItem(0)
        item.setText(_translate("QueryOffer_Window", "Nº Oferta"))
        item = self.tableQueryOffer.horizontalHeaderItem(1)
        item.setText(_translate("QueryOffer_Window", "Responsable"))
        item = self.tableQueryOffer.horizontalHeaderItem(2)
        item.setText(_translate("QueryOffer_Window", "Estado"))
        item = self.tableQueryOffer.horizontalHeaderItem(3)
        item.setText(_translate("QueryOffer_Window", "Referencia"))
        item = self.tableQueryOffer.horizontalHeaderItem(4)
        item.setText(_translate("QueryOffer_Window", "Cliente"))
        item = self.tableQueryOffer.horizontalHeaderItem(5)
        item.setText(_translate("QueryOffer_Window", "Cliente Final"))
        item = self.tableQueryOffer.horizontalHeaderItem(6)
        item.setText(_translate("QueryOffer_Window", "Material"))
        item = self.tableQueryOffer.horizontalHeaderItem(7)
        item.setText(_translate("QueryOffer_Window", "Importe"))
        item = self.tableQueryOffer.horizontalHeaderItem(8)
        item.setText(_translate("QueryOffer_Window", "Tipo Tarifa"))
        item = self.tableQueryOffer.horizontalHeaderItem(9)
        item.setText(_translate("QueryOffer_Window", "Notas"))
        item = self.tableQueryOffer.horizontalHeaderItem(10)
        item.setText(_translate("QueryOffer_Window", "Ptos. Importantes"))
        self.Button_Clean.setText(_translate("QueryOffer_Window", "Limpiar Filtros"))
        self.Button_Query.setText(_translate("QueryOffer_Window", "Buscar"))
        self.Button_Export.setText(_translate("QueryOffer_Window", "Exportar Excel"))
        self.label_NumOffer.setText(_translate("QueryOffer_Window", "Nº Oferta:"))
        self.label_Client.setText(_translate("QueryOffer_Window", "Cliente:"))
        self.label_Responsible.setText(_translate("QueryOffer_Window", "Responsable:"))
        self.label_State.setText(_translate("QueryOffer_Window", "Estado:"))
        self.label_FinalClient.setText(_translate("QueryOffer_Window", "Cliente Final:"))
        self.label_RefNum.setText(_translate("QueryOffer_Window", "Referencia:"))
        self.label_Material.setText(_translate("QueryOffer_Window", "Material:"))


    def clean_boxes(self):
        self.Numoffer_QueryOffer.setText("")
        self.Client_QueryOffer.setText("")
        self.Responsible_QueryOffer.setCurrentText("")
        self.State_QueryOffer.setCurrentText("")
        self.FinalClient_QueryOffer.setText("")
        self.Ref_QueryOffer.setText("")
        self.Material_QueryOffer.setCurrentText("")


    def query_offer(self):
        numoffer=self.Numoffer_QueryOffer.text()
        client=self.Client_QueryOffer.text()
        responsible=self.Responsible_QueryOffer.currentText()
        state=self.State_QueryOffer.currentText()
        finalclient=self.FinalClient_QueryOffer.text()
        reference=self.Ref_QueryOffer.text()
        material=self.Material_QueryOffer.currentText()

        if ((numoffer=="" or numoffer==" ") and (client=="" or client==" ") and (responsible=="" or responsible==" ") and (state=="" or state==" ")
        and (finalclient=="" or finalclient==" ") and (reference=="" or reference==" ") and (material=="" or material==" ")):
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.join(basedir, "Resources/Iconos/icon.ico")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("Consultar Oferta")
            dlg.setText("Introduce un filtro en alguno de los campos")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            dlg.exec()
            del dlg,new_icon

        else:
            commands_queryoffer = ("""
                        SELECT offers."num_offer",offers."responsible",offers."state",offers."num_ref_offer",offers."client",offers."final_client",product_type."variable",offers."offer_amount",offers."rate_type",offers."notes",offers."important"
                        FROM offers
                        INNER JOIN product_type ON (offers."material"=product_type."material")
                        WHERE (UPPER(offers."num_offer") LIKE UPPER('%%'||%s||'%%')
                        AND
                        UPPER(offers."num_ref_offer") LIKE UPPER('%%'||%s||'%%')
                        AND
                        UPPER(offers."client") LIKE UPPER('%%'||%s||'%%')
                        AND
                        UPPER(offers."final_client") LIKE UPPER('%%'||%s||'%%')
                        AND
                        UPPER(offers."responsible") LIKE UPPER('%%'||%s||'%%')
                        AND
                        UPPER(offers."state") LIKE UPPER('%%'||%s||'%%')
                        AND
                        product_type."variable" LIKE '%%'||%s||'%%'
                        )
                        ORDER BY offers."num_offer"
                        """)
            conn = None
            try:
            # read the connection parameters
                params = config()
            # connect to the PostgreSQL server
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
            # execution of commands
                data=(numoffer,reference,client,finalclient,responsible,state,material,)
                cur.execute(commands_queryoffer,data)
                results=cur.fetchall()
                self.tableQueryOffer.setRowCount(0)
                self.tableQueryOffer.setRowCount(len(results))
                tablerow=0

            # fill the Qt Table with the query results
                for row in results:
                    for column in range(11):
                        value = row[column]
                        if value is None:
                            value = ''
                        it = QtWidgets.QTableWidgetItem(str(value))
                        it.setFlags(it.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                        self.tableQueryOffer.setItem(tablerow, column, it)

                    self.tableQueryOffer.setItemDelegateForRow(tablerow, AlignDelegate(self.tableQueryOffer))
                    tablerow+=1

                self.tableQueryOffer.verticalHeader().hide()


            # close communication with the PostgreSQL database server
                cur.close()
            # commit the changes
                conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()


    def countSelectedCells(self):
        if len(self.tableQueryOffer.selectedIndexes()) > 1:
            locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
            self.label_SumItems.setText("")
            self.label_SumValue.setText("")
            self.label_CountItems.setText("")
            self.label_CountValue.setText("")

            sum_value = sum([self.euro_string_to_float(ix.data()) if re.match(r'^[\d.,]+\s€$', ix.data()) else float(ix.data()) if ix.data().replace(',', '.', 1).replace('.', '', 1).isdigit() else 0 for ix in self.tableQueryOffer.selectedIndexes()])
            count_value = len([ix for ix in self.tableQueryOffer.selectedIndexes() if ix.data() != ""])
            if sum_value > 0:
                self.label_SumItems.setText("Suma:")
                self.label_SumValue.setText(locale.format_string("%.2f", sum_value, grouping=True))
            if count_value > 0:
                self.label_CountItems.setText("Recuento:")
                self.label_CountValue.setText(str(count_value))
        else:
            self.label_SumItems.setText("")
            self.label_SumValue.setText("")
            self.label_CountItems.setText("")
            self.label_CountValue.setText("")

    def euro_string_to_float(self, euro_str):
        match = re.match(r'^([\d.,]+)\s€$', euro_str)
        if match:
            number_str = match.group(1)
            number_str = number_str.replace('.', '').replace(',', '.')
            return float(number_str)
        else:
            return 0.0


    def on_item_double_clicked(self, item):
        if item.column() in [9,10]:
            cell_content = item.text()
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.join(basedir, "Resources/Iconos/icon.ico")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("Ofertas")
            dlg.setText(cell_content)
            dlg.exec()
            del dlg, new_icon


    def export_data(self):
        num_rows = self.tableQueryOffer.rowCount()
        if num_rows > 0:
            num_columns = 8

            column_names = [self.tableQueryOffer.horizontalHeaderItem(col).text() for col in range(num_columns)]

            df = pd.DataFrame(columns=column_names)

            for row in range(num_rows):
                row_data = []
                for col in range(num_columns):
                    item = self.tableQueryOffer.item(row,col)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                df.loc[row] = row_data

            root = tk.Tk()
            root.withdraw()

            file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])

            if file_path:
                df.to_excel(file_path, index=False)

        else:
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.join(basedir, "Resources/Iconos/icon.ico")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("Consultar Oferta")
            dlg.setText("No hay datos para exportar")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            dlg.exec()
            del dlg,new_icon


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QueryOffer_Window = QtWidgets.QMainWindow()
    ui = Ui_QueryOffer_Window()
    ui.setupUi(QueryOffer_Window)
    QueryOffer_Window.show()
    sys.exit(app.exec())
