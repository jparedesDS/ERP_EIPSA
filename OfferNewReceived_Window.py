# Form implementation generated from reading ui file 'NewOffer_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import *
import psycopg2
from config import config
import os
import re
from OfferClientAdd_Window import Ui_OfferClientAdd_Window

basedir = r"\\nas01\DATOS\Comunes\EIPSA-ERP"


class Ui_New_OfferReceived_Window(object):
    def __init__(self,username):
        self.username=username

    def setupUi(self, New_OfferReceived):
        New_OfferReceived.setObjectName("New_OfferReceived")
        New_OfferReceived.resize(670, 425)
        New_OfferReceived.setMinimumSize(QtCore.QSize(700, 550))
        New_OfferReceived.setMaximumSize(QtCore.QSize(700, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        New_OfferReceived.setWindowIcon(icon)
        New_OfferReceived.setStyleSheet("QWidget {\n"
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
"QPushButton:pressed {\n"
"    background-color: rgb(1, 140, 190);\n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-color: #019ad2;\n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:focus:pressed {\n"
"    background-color: rgb(1, 140, 190);\n"
"    border-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=New_OfferReceived)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridlayout_main = QtWidgets.QGridLayout(self.frame)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridlayout_main.addItem(spacerItem, 0, 0, 1, 1)
        self.label_Client = QtWidgets.QLabel(parent=self.frame)
        self.label_Client.setMinimumSize(QtCore.QSize(60, 25))
        self.label_Client.setMaximumSize(QtCore.QSize(60, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_Client.setFont(font)
        self.label_Client.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_Client.setObjectName("label_Client")
        self.gridlayout_main.addWidget(self.label_Client, 1, 0, 1, 1)
        self.Button_NewClient = QtWidgets.QPushButton(parent=self.frame)
        self.Button_NewClient.setMinimumSize(QtCore.QSize(50, 25))
        self.Button_NewClient.setMaximumSize(QtCore.QSize(50, 25))
        self.Button_NewClient.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_NewClient.setObjectName("Button_NewClient")
        self.Button_NewClient.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Button_NewClient.setStyleSheet("QPushButton {\n"
"background-color: #33bdef;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 3px;\n"
"  color: #fff;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",\"Liberation Sans\",sans-serif;\n"
"  font-size: 20px;\n"
"  font-weight: 800;\n"
"  line-height: 1.15385;\n"
"  margin: 0;\n"
"  outline: none;\n"
"  padding: 1px .1em;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  vertical-align: center;\n"
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
        self.gridlayout_main.addWidget(self.Button_NewClient, 1, 1, 1, 1)
        self.Client_NewOffer = QtWidgets.QComboBox(parent=self.frame)
        self.Client_NewOffer.setMinimumSize(QtCore.QSize(200, 25))
        self.Client_NewOffer.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Client_NewOffer.setFont(font)
        self.Client_NewOffer.setObjectName("Client_NewOffer")
        self.gridlayout_main.addWidget(self.Client_NewOffer, 1, 2, 1, 1)
        self.label_RecepDate = QtWidgets.QLabel(parent=self.frame)
        self.label_RecepDate.setMinimumSize(QtCore.QSize(110, 25))
        self.label_RecepDate.setMaximumSize(QtCore.QSize(110, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_RecepDate.setFont(font)
        self.label_RecepDate.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_RecepDate.setObjectName("label_RecepDate")
        self.gridlayout_main.addWidget(self.label_RecepDate, 1, 3, 1, 1)
        self.RecepDate_NewOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.RecepDate_NewOffer.setMinimumSize(QtCore.QSize(200, 25))
        self.RecepDate_NewOffer.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RecepDate_NewOffer.setFont(font)
        self.RecepDate_NewOffer.setObjectName("RecepDate_NewOffer")
        self.gridlayout_main.addWidget(self.RecepDate_NewOffer, 1, 4, 1, 1)
        self.label_FinalClient = QtWidgets.QLabel(parent=self.frame)
        self.label_FinalClient.setMinimumSize(QtCore.QSize(110, 25))
        self.label_FinalClient.setMaximumSize(QtCore.QSize(110, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_FinalClient.setFont(font)
        self.label_FinalClient.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_FinalClient.setObjectName("label_FinalClient")
        self.gridlayout_main.addWidget(self.label_FinalClient, 2, 0, 1, 2)
        self.FinalClient_NewOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.FinalClient_NewOffer.setMinimumSize(QtCore.QSize(200, 25))
        self.FinalClient_NewOffer.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FinalClient_NewOffer.setFont(font)
        self.FinalClient_NewOffer.setObjectName("FinalClient_NewOffer")
        self.gridlayout_main.addWidget(self.FinalClient_NewOffer, 2, 2, 1, 1)
        self.label_LimitDate = QtWidgets.QLabel(parent=self.frame)
        self.label_LimitDate.setMinimumSize(QtCore.QSize(110, 25))
        self.label_LimitDate.setMaximumSize(QtCore.QSize(110, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_LimitDate.setFont(font)
        self.label_LimitDate.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_LimitDate.setObjectName("label_LimitDate")
        self.gridlayout_main.addWidget(self.label_LimitDate, 2, 3, 1, 1)
        self.LimitDate_NewOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.LimitDate_NewOffer.setMinimumSize(QtCore.QSize(200, 25))
        self.LimitDate_NewOffer.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LimitDate_NewOffer.setFont(font)
        self.LimitDate_NewOffer.setObjectName("LimitDate_NewOffer")
        self.gridlayout_main.addWidget(self.LimitDate_NewOffer, 2, 4, 1, 1)
        self.label_NumRef = QtWidgets.QLabel(parent=self.frame)
        self.label_NumRef.setMinimumSize(QtCore.QSize(110, 25))
        # self.label_NumRef.setMaximumSize(QtCore.QSize(105, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_NumRef.setFont(font)
        self.label_NumRef.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_NumRef.setObjectName("label_NumRef")
        self.gridlayout_main.addWidget(self.label_NumRef, 3, 0, 1, 2)
        self.NumRef_NewOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.NumRef_NewOffer.setMinimumSize(QtCore.QSize(200, 25))
        self.NumRef_NewOffer.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NumRef_NewOffer.setFont(font)
        self.NumRef_NewOffer.setObjectName("NumRef_NewOffer")
        self.gridlayout_main.addWidget(self.NumRef_NewOffer, 3, 2, 1, 1)
        self.label_Description = QtWidgets.QLabel(parent=self.frame)
        self.label_Description.setMinimumSize(QtCore.QSize(110, 25))
        self.label_Description.setMaximumSize(QtCore.QSize(110, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_Description.setFont(font)
        self.label_Description.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_Description.setObjectName("label_Description")
        self.gridlayout_main.addWidget(self.label_Description, 3, 3, 1, 1)
        self.Description_NewOffer = QtWidgets.QTextEdit(parent=self.frame)
        self.Description_NewOffer.setMinimumSize(QtCore.QSize(200, 25))
        self.Description_NewOffer.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Description_NewOffer.setFont(font)
        self.Description_NewOffer.setObjectName("Description_NewOffer")
        self.gridlayout_main.addWidget(self.Description_NewOffer, 3, 4, 1, 1)
        self.label_Material = QtWidgets.QLabel(parent=self.frame)
        self.label_Material.setMinimumSize(QtCore.QSize(110, 25))
        # self.label_Material.setMaximumSize(QtCore.QSize(110, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_Material.setFont(font)
        self.label_Material.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_Material.setObjectName("label_Material")
        self.gridlayout_main.addWidget(self.label_Material, 4, 0, 1, 2)
        self.Material_NewOffer = QtWidgets.QComboBox(parent=self.frame)
        self.Material_NewOffer.setMinimumSize(QtCore.QSize(200, 25))
        self.Material_NewOffer.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Material_NewOffer.setFont(font)
        self.Material_NewOffer.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.Material_NewOffer.setObjectName("Material_NewOffer")
        self.gridlayout_main.addWidget(self.Material_NewOffer, 4, 2, 1, 1)
        self.label_NumItems = QtWidgets.QLabel(parent=self.frame)
        self.label_NumItems.setMinimumSize(QtCore.QSize(110, 25))
        self.label_NumItems.setMaximumSize(QtCore.QSize(110, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_NumItems.setFont(font)
        self.label_NumItems.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_NumItems.setObjectName("label_NumItems")
        self.gridlayout_main.addWidget(self.label_NumItems, 4, 3, 1, 1)
        self.NumItems_NewOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.NumItems_NewOffer.setMinimumSize(QtCore.QSize(200, 25))
        self.NumItems_NewOffer.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NumItems_NewOffer.setFont(font)
        self.NumItems_NewOffer.setObjectName("NumItems_NewOffer")
        self.gridlayout_main.addWidget(self.NumItems_NewOffer, 4, 4, 1, 1)
        self.label_Notes = QtWidgets.QLabel(parent=self.frame)
        self.label_Notes.setMinimumSize(QtCore.QSize(110, 25))
        # self.label_Notes.setMaximumSize(QtCore.QSize(110, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_Notes.setFont(font)
        self.label_Notes.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_Notes.setObjectName("label_Notes")
        self.gridlayout_main.addWidget(self.label_Notes, 5, 0, 1, 2)
        self.Notes_NewOffer = QtWidgets.QTextEdit(parent=self.frame)
        self.Notes_NewOffer.setMinimumSize(QtCore.QSize(200, 25))
        self.Notes_NewOffer.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Notes_NewOffer.setFont(font)
        self.Notes_NewOffer.setObjectName("Notes_NewOffer")
        self.gridlayout_main.addWidget(self.Notes_NewOffer, 5, 2, 1, 3)
        self.Button_NewOffer = QtWidgets.QPushButton(parent=self.frame)
        self.Button_NewOffer.setMinimumSize(QtCore.QSize(200, 30))
        self.Button_NewOffer.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Button_NewOffer.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_NewOffer.setAutoDefault(True)
        self.Button_NewOffer.setObjectName("Button_NewOffer")
        self.gridlayout_main.addWidget(self.Button_NewOffer, 6, 2, 1, 1)
        self.Button_Cancel = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Cancel.setMinimumSize(QtCore.QSize(200, 30))
        self.Button_Cancel.setMaximumSize(QtCore.QSize(200, 30))
        self.Button_Cancel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_Cancel.setAutoDefault(True)
        self.Button_Cancel.setObjectName("Button_Cancel")
        self.gridlayout_main.addWidget(self.Button_Cancel, 6, 4, 1, 1)        
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        New_OfferReceived.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=New_OfferReceived)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 22))
        self.menubar.setObjectName("menubar")
        New_OfferReceived.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=New_OfferReceived)
        self.statusbar.setObjectName("statusbar")
        New_OfferReceived.setStatusBar(self.statusbar)
        New_OfferReceived.setWindowFlags(QtCore.Qt.WindowType.WindowMinimizeButtonHint)

        self.retranslateUi(New_OfferReceived)
        self.Button_Cancel.clicked.connect(New_OfferReceived.close) # type: ignore
        self.Button_NewOffer.clicked.connect(self.NewOffer)
        self.Button_NewClient.clicked.connect(self.NewClient)
        QtCore.QMetaObject.connectSlotsByName(New_OfferReceived)

        commands_productype = ("""
                        SELECT * 
                        FROM product_type
                        """)
        conn = None
        try:
        # read the connection parameters
            params = config()
        # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # execution of commands one by one
            cur.execute(commands_productype)
            results_producttype=cur.fetchall()
        # close communication with the PostgreSQL database server
            cur.close()
        # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("ERP EIPSA")
            dlg.setText("Ha ocurrido el siguiente error:\n"
                        + str(error))
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            dlg.exec()
            del dlg, new_icon
        finally:
            if conn is not None:
                conn.close()

        list_material=[x[0] for x in results_producttype]
        list_material.sort()
        self.Material_NewOffer.addItems(list_material)

        self.load_clients()


    def retranslateUi(self, New_OfferReceived):
        _translate = QtCore.QCoreApplication.translate
        New_OfferReceived.setWindowTitle(_translate("New_OfferReceived", "Nueva Oferta"))
        self.label_Description.setText(_translate("New_OfferReceived", "Descripción:"))
        self.label_Client.setText(_translate("New_OfferReceived", "Cliente:"))
        self.label_FinalClient.setText(_translate("New_OfferReceived", "Cliente Final:"))
        self.label_NumRef.setText(_translate("New_OfferReceived", "Nº Referencia:"))
        self.label_RecepDate.setText(_translate("New_OfferReceived", "Fecha Recep.:"))
        self.label_LimitDate.setText(_translate("New_OfferReceived", "Fecha Límite:"))
        self.label_Material.setText(_translate("New_OfferReceived", "Instrumento:"))
        self.label_NumItems.setText(_translate("New_OfferReceived", "Nº Equipos:"))
        self.label_Notes.setText(_translate("New_OfferReceived", "Notas:"))
        self.Button_NewOffer.setText(_translate("New_OfferReceived", "Crear Oferta"))
        self.Button_Cancel.setText(_translate("New_OfferReceived", "Cancelar"))
        self.Button_NewClient.setText(_translate("New_OfferReceived", "+"))

    def load_clients(self):
        self.Client_NewOffer.clear()
        commands_clients = ("""
                        SELECT * 
                        FROM clients_list
                        """)
        conn = None
        try:
        # read the connection parameters
            params = config()
        # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # execution of commands one by one
            cur.execute(commands_clients)
            results_clients=cur.fetchall()
        # close communication with the PostgreSQL database server
            cur.close()
        # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("ERP EIPSA")
            dlg.setText("Ha ocurrido el siguiente error:\n"
                        + str(error))
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            dlg.exec()
            del dlg, new_icon
        finally:
            if conn is not None:
                conn.close()

        list_clients=[x[0] for x in results_clients]
        list_clients.sort()
        self.Client_NewOffer.addItems(list_clients)


    def NewOffer(self):
        client=self.Client_NewOffer.currentText()
        finalclient=self.FinalClient_NewOffer.text()
        numref=self.NumRef_NewOffer.text()
        limitdate=self.LimitDate_NewOffer.text()
        recepdate=self.RecepDate_NewOffer.text()
        material=self.Material_NewOffer.currentText()
        description=self.Description_NewOffer.toPlainText()
        items_number=self.NumItems_NewOffer.text()
        notes=self.Notes_NewOffer.toPlainText()
        actual_date=date.today()
        actual_date=actual_date.strftime("%d/%m/%Y")

        if numref=="" or (recepdate=="" or (limitdate=="" or (description=="" or items_number==""))):
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("ERP EIPSA")
            dlg.setText("Rellene todos los campos")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            dlg.exec()
            del dlg, new_icon

        elif not (items_number.isdigit() or (items_number.startswith('-') and items_number[1:].isdigit())) or float(items_number) < 0:
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("ERP EIPSA")
            dlg.setText("Introduce un número de equipos válido. En caso de no saber el alcance definitivo, pon 0")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            dlg.exec()
            del dlg, new_icon

        elif not re.match(r'^\d{2}[/\-]\d{2}[/\-]\d{4}$', recepdate) or not re.match(r'^\d{2}[/\-]\d{2}[/\-]\d{4}$', limitdate):
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("ERP EIPSA")
            dlg.setText("Las fechas debe tener formato dd/mm/yyyy o dd-mm-yyyy")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            dlg.exec()
            del dlg, new_icon

        else:
            commands_newoffer = ("""
                        INSERT INTO received_offers (
                        "responsible","client","final_client","num_ref_offer","material","register_date",
                        "recep_date","limit_date","description","items_number","state","notes"
                        )
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """)
            conn = None
            try:
            # read the connection parameters
                params = config()
            # connect to the PostgreSQL server
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
            # execution of commands
                data=(self.username, client, finalclient, numref, material, actual_date, recepdate, limitdate, description, items_number, 'Recibida', notes)
                cur.execute(commands_newoffer, data)
            # close communication with the PostgreSQL database server
                cur.close()
            # commit the changes
                conn.commit()

                dlg = QtWidgets.QMessageBox()
                new_icon = QtGui.QIcon()
                new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                dlg.setWindowIcon(new_icon)
                dlg.setWindowTitle("Crear Oferta")
                dlg.setText("Oferta creada con éxito")
                dlg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                dlg.exec()
                del dlg,new_icon

                self.FinalClient_NewOffer.setText('')
                self.NumRef_NewOffer.setText('')
                self.RecepDate_NewOffer.setText('')
                self.Description_NewOffer.setText('')
                self.LimitDate_NewOffer.setText('')
                self.NumItems_NewOffer.setText('')
                self.Notes_NewOffer.setText('')

            except (Exception, psycopg2.DatabaseError) as error:
                dlg = QtWidgets.QMessageBox()
                new_icon = QtGui.QIcon()
                new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                dlg.setWindowIcon(new_icon)
                dlg.setWindowTitle("ERP EIPSA")
                dlg.setText("Ha ocurrido el siguiente error:\n"
                            + str(error))
                dlg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                dlg.exec()
                del dlg, new_icon
            finally:
                if conn is not None:
                    conn.close()


    def NewClient(self):
        self.new_client_window=QtWidgets.QMainWindow()
        self.ui=Ui_OfferClientAdd_Window()
        self.ui.setupUi(self.new_client_window)
        self.new_client_window.show()
        self.ui.exit_OfferClientAdd.clicked.connect(self.load_clients)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    New_OfferReceived = QtWidgets.QMainWindow()
    ui = Ui_New_OfferReceived_Window('a.calvo')
    ui.setupUi(New_OfferReceived)
    New_OfferReceived.show()
    sys.exit(app.exec())