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


class Ui_New_Offer_Window(object):
    def __init__(self,name):
        self.name=name

    def setupUi(self, New_Offer):
        New_Offer.setObjectName("New_Offer")
        New_Offer.resize(670, 425)
        New_Offer.setMinimumSize(QtCore.QSize(670, 425))
        New_Offer.setMaximumSize(QtCore.QSize(670, 425))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Recursos/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        New_Offer.setWindowIcon(icon)
        New_Offer.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=New_Offer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.hLayout = QtWidgets.QHBoxLayout()
        self.hLayout.setObjectName("hLayout")
        self.vLayout1 = QtWidgets.QVBoxLayout()
        self.vLayout1.setContentsMargins(0, -1, 0, -1)
        self.vLayout1.setObjectName("vLayout1")
        self.label_NumOffer = QtWidgets.QLabel(parent=self.frame)
        self.label_NumOffer.setMinimumSize(QtCore.QSize(105, 25))
        self.label_NumOffer.setMaximumSize(QtCore.QSize(105, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_NumOffer.setFont(font)
        self.label_NumOffer.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_NumOffer.setObjectName("label_NumOffer")
        self.vLayout1.addWidget(self.label_NumOffer)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout1.addItem(spacerItem1)
        self.label_Client = QtWidgets.QLabel(parent=self.frame)
        self.label_Client.setMinimumSize(QtCore.QSize(105, 25))
        self.label_Client.setMaximumSize(QtCore.QSize(105, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_Client.setFont(font)
        self.label_Client.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_Client.setObjectName("label_Client")
        self.vLayout1.addWidget(self.label_Client)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout1.addItem(spacerItem2)
        self.label_FinalClient = QtWidgets.QLabel(parent=self.frame)
        self.label_FinalClient.setMinimumSize(QtCore.QSize(105, 25))
        self.label_FinalClient.setMaximumSize(QtCore.QSize(105, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_FinalClient.setFont(font)
        self.label_FinalClient.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_FinalClient.setObjectName("label_FinalClient")
        self.vLayout1.addWidget(self.label_FinalClient)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout1.addItem(spacerItem3)
        self.label_NumRef = QtWidgets.QLabel(parent=self.frame)
        self.label_NumRef.setMinimumSize(QtCore.QSize(105, 25))
        self.label_NumRef.setMaximumSize(QtCore.QSize(105, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_NumRef.setFont(font)
        self.label_NumRef.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_NumRef.setObjectName("label_NumRef")
        self.vLayout1.addWidget(self.label_NumRef)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout1.addItem(spacerItem4)
        self.label_NacExt = QtWidgets.QLabel(parent=self.frame)
        self.label_NacExt.setMinimumSize(QtCore.QSize(130, 25))
        self.label_NacExt.setMaximumSize(QtCore.QSize(130, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_NacExt.setFont(font)
        self.label_NacExt.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_NacExt.setObjectName("label_NacExt")
        self.vLayout1.addWidget(self.label_NacExt)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout1.addItem(spacerItem5)
        self.hLayout.addLayout(self.vLayout1)
        self.vLayout2 = QtWidgets.QVBoxLayout()
        self.vLayout2.setObjectName("vLayout2")
        self.NumOffer_NewOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.NumOffer_NewOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.NumOffer_NewOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NumOffer_NewOffer.setFont(font)
        self.NumOffer_NewOffer.setObjectName("NumOffer_NewOffer")
        self.vLayout2.addWidget(self.NumOffer_NewOffer)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout2.addItem(spacerItem5)
        self.Client_NewOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.Client_NewOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.Client_NewOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Client_NewOffer.setFont(font)
        self.Client_NewOffer.setObjectName("Client_NewOffer")
        self.vLayout2.addWidget(self.Client_NewOffer)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout2.addItem(spacerItem6)
        self.FinalClient_NewOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.FinalClient_NewOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.FinalClient_NewOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FinalClient_NewOffer.setFont(font)
        self.FinalClient_NewOffer.setObjectName("FinalClient_NewOffer")
        self.vLayout2.addWidget(self.FinalClient_NewOffer)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout2.addItem(spacerItem7)
        self.NumRef_NewOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.NumRef_NewOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.NumRef_NewOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NumRef_NewOffer.setFont(font)
        self.NumRef_NewOffer.setObjectName("NumRef_NewOffer")
        self.vLayout2.addWidget(self.NumRef_NewOffer)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout2.addItem(spacerItem8)
        self.NacExt_NewOffer = QtWidgets.QComboBox(parent=self.frame)
        self.NacExt_NewOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.NacExt_NewOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NacExt_NewOffer.setFont(font)
        self.NacExt_NewOffer.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.NacExt_NewOffer.setObjectName("NacExt_NewOffer")
        self.vLayout2.addWidget(self.NacExt_NewOffer)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout2.addItem(spacerItem9)
        self.hLayout.addLayout(self.vLayout2)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hLayout.addItem(spacerItem10)
        self.vLayout3 = QtWidgets.QVBoxLayout()
        self.vLayout3.setObjectName("vLayout3")
        self.label_LimitDate = QtWidgets.QLabel(parent=self.frame)
        self.label_LimitDate.setMinimumSize(QtCore.QSize(110, 25))
        self.label_LimitDate.setMaximumSize(QtCore.QSize(110, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_LimitDate.setFont(font)
        self.label_LimitDate.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_LimitDate.setObjectName("label_LimitDate")
        self.vLayout3.addWidget(self.label_LimitDate)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout3.addItem(spacerItem11)
        self.label_Buyer = QtWidgets.QLabel(parent=self.frame)
        self.label_Buyer.setMinimumSize(QtCore.QSize(110, 25))
        self.label_Buyer.setMaximumSize(QtCore.QSize(110, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_Buyer.setFont(font)
        self.label_Buyer.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_Buyer.setObjectName("label_Buyer")
        self.vLayout3.addWidget(self.label_Buyer)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout3.addItem(spacerItem12)
        self.label_Material = QtWidgets.QLabel(parent=self.frame)
        self.label_Material.setMinimumSize(QtCore.QSize(110, 25))
        self.label_Material.setMaximumSize(QtCore.QSize(110, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_Material.setFont(font)
        self.label_Material.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_Material.setObjectName("label_Material")
        self.vLayout3.addWidget(self.label_Material)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout3.addItem(spacerItem13)
        self.label_Notes = QtWidgets.QLabel(parent=self.frame)
        self.label_Notes.setMinimumSize(QtCore.QSize(110, 25))
        self.label_Notes.setMaximumSize(QtCore.QSize(110, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_Notes.setFont(font)
        self.label_Notes.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_Notes.setObjectName("label_Notes")
        self.vLayout3.addWidget(self.label_Notes)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout3.addItem(spacerItem14)
        self.label_RateType = QtWidgets.QLabel(parent=self.frame)
        self.label_RateType.setMinimumSize(QtCore.QSize(110, 25))
        self.label_RateType.setMaximumSize(QtCore.QSize(110, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_RateType.setFont(font)
        self.label_RateType.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_RateType.setObjectName("label_RateType")
        self.vLayout3.addWidget(self.label_RateType)
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout3.addItem(spacerItem15)
        self.hLayout.addLayout(self.vLayout3)
        self.vLayout4 = QtWidgets.QVBoxLayout()
        self.vLayout4.setObjectName("vLayout4")
        self.LimitDate_NewOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.LimitDate_NewOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.LimitDate_NewOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LimitDate_NewOffer.setFont(font)
        self.LimitDate_NewOffer.setObjectName("LimitDate_NewOffer")
        self.vLayout4.addWidget(self.LimitDate_NewOffer)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout4.addItem(spacerItem16)
        self.Buyer_NewOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.Buyer_NewOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.Buyer_NewOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Buyer_NewOffer.setFont(font)
        self.Buyer_NewOffer.setObjectName("Buyer_NewOffer")
        self.vLayout4.addWidget(self.Buyer_NewOffer)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout4.addItem(spacerItem17)
        self.Material_NewOffer = QtWidgets.QComboBox(parent=self.frame)
        self.Material_NewOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.Material_NewOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Material_NewOffer.setFont(font)
        self.Material_NewOffer.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.Material_NewOffer.setObjectName("Material_NewOffer")
        self.vLayout4.addWidget(self.Material_NewOffer)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout4.addItem(spacerItem18)
        self.Notes_NewOffer = QtWidgets.QTextEdit(parent=self.frame)
        self.Notes_NewOffer.setMinimumSize(QtCore.QSize(175, 40))
        self.Notes_NewOffer.setMaximumSize(QtCore.QSize(175, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Notes_NewOffer.setFont(font)
        self.Notes_NewOffer.setObjectName("Notes_NewOffer")
        self.vLayout4.addWidget(self.Notes_NewOffer)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout4.addItem(spacerItem19)
        self.RateType_NewOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.RateType_NewOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.RateType_NewOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RateType_NewOffer.setFont(font)
        self.RateType_NewOffer.setObjectName("RateType_NewOffer")
        self.vLayout4.addWidget(self.RateType_NewOffer)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout4.addItem(spacerItem20)
        self.hLayout.addLayout(self.vLayout4)
        self.verticalLayout.addLayout(self.hLayout)
        spacerItem21 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem21)
        self.hLayout1 = QtWidgets.QHBoxLayout()
        self.hLayout1.setObjectName("hLayout1")
        self.Button_NewOffer = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_NewOffer.sizePolicy().hasHeightForWidth())
        self.Button_NewOffer.setSizePolicy(sizePolicy)
        self.Button_NewOffer.setMinimumSize(QtCore.QSize(200, 30))
        self.Button_NewOffer.setMaximumSize(QtCore.QSize(200, 30))
        self.Button_NewOffer.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_NewOffer.setAutoDefault(True)
        self.Button_NewOffer.setObjectName("Button_NewOffer")
        self.hLayout1.addWidget(self.Button_NewOffer)
        self.Button_Cancel = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Cancel.sizePolicy().hasHeightForWidth())
        self.Button_Cancel.setSizePolicy(sizePolicy)
        self.Button_Cancel.setMinimumSize(QtCore.QSize(200, 30))
        self.Button_Cancel.setMaximumSize(QtCore.QSize(200, 30))
        self.Button_Cancel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_Cancel.setAutoDefault(True)
        self.Button_Cancel.setObjectName("Button_Cancel")
        self.hLayout1.addWidget(self.Button_Cancel)
        self.verticalLayout.addLayout(self.hLayout1)
        self.label_error_newoffer = QtWidgets.QLabel(parent=self.frame)
        self.label_error_newoffer.setStyleSheet("color: rgb(255, 0, 0);")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_error_newoffer.setFont(font)
        self.label_error_newoffer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_error_newoffer.setObjectName("label_error_newoffer")
        self.verticalLayout.addWidget(self.label_error_newoffer)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        New_Offer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=New_Offer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 22))
        self.menubar.setObjectName("menubar")
        New_Offer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=New_Offer)
        self.statusbar.setObjectName("statusbar")
        New_Offer.setStatusBar(self.statusbar)
        New_Offer.setWindowFlags(QtCore.Qt.WindowType.WindowMinimizeButtonHint)

        self.retranslateUi(New_Offer)
        self.Button_Cancel.clicked.connect(New_Offer.close) # type: ignore
        self.Button_NewOffer.clicked.connect(self.NewOffer)
        QtCore.QMetaObject.connectSlotsByName(New_Offer)

        list_nacext=['Exterior','Nacional']
        self.NacExt_NewOffer.addItems(list_nacext)

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
            results=cur.fetchall()
        # close communication with the PostgreSQL database server
            cur.close()
        # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        list_material=[x[0] for x in results]
        list_material.sort()
        self.Material_NewOffer.addItems(list_material)


    def retranslateUi(self, New_Offer):
        _translate = QtCore.QCoreApplication.translate
        New_Offer.setWindowTitle(_translate("New_Offer", "Nueva Oferta"))
        self.label_NumOffer.setText(_translate("New_Offer", "*Nº Oferta:"))
        self.label_Client.setText(_translate("New_Offer", "*Cliente:"))
        self.label_FinalClient.setText(_translate("New_Offer", "Cliente Final:"))
        self.label_NumRef.setText(_translate("New_Offer", "*Nº Referencia:"))
        self.label_NacExt.setText(_translate("New_Offer", "Nacional/Exterior:"))
        self.label_LimitDate.setText(_translate("New_Offer", "*Fecha Límite:"))
        self.label_Buyer.setText(_translate("New_Offer", "Comprador:"))
        self.label_Material.setText(_translate("New_Offer", "Instrumento:"))
        self.label_Notes.setText(_translate("New_Offer", "Notas:"))
        self.label_RateType.setText(_translate("New_Offer", "*Tipo Tarifa:"))
        self.Button_NewOffer.setText(_translate("New_Offer", "Crear Oferta"))
        self.Button_Cancel.setText(_translate("New_Offer", "Cancelar"))
        self.label_error_newoffer.setText(_translate("New_Offer", ""))


    def NewOffer(self):
        numoffer=self.NumOffer_NewOffer.text()
        client=self.Client_NewOffer.text()
        finalclient=self.FinalClient_NewOffer.text()
        numref=self.NumRef_NewOffer.text()
        nacext=self.NacExt_NewOffer.currentText()
        limitdate=self.LimitDate_NewOffer.text()
        buyer=self.Buyer_NewOffer.text()
        material=self.Material_NewOffer.currentText()
        notes=self.Notes_NewOffer.toPlainText()
        ratetype=self.RateType_NewOffer.text()
        state="Registrada"
        if self.name=='Carlos Crespo':
            responsible=self.name[0] + self.name[self.name.find(' ')+1]+'H'
        else:
            responsible=self.name[0] + self.name[self.name.find(' ')+1]
        actual_date=date.today()
        actual_date=actual_date.strftime("%d/%m/%Y")

        if numoffer=="" or (client=="" or (numref=="" or (limitdate=="" or ratetype==""))):
            self.label_error_newoffer.setText('Rellene todos los campos con *')

        else:
        #SQL Query for checking if offer number exists in database
            commands_checkoffer = ("""
                        SELECT * 
                        FROM offers
                        WHERE "num_offer" = %s
                        """)
            conn = None
            try:
            # read the connection parameters
                params = config()
            # connect to the PostgreSQL server
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
            # execution of commands one by one
                cur.execute(commands_checkoffer,(numoffer,))
                results=cur.fetchall()
                match=list(filter(lambda x:numoffer in x, results))
            # close communication with the PostgreSQL database server
                cur.close()
            # commit the changes
                conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()

            if len(match)>0:
                dlg = QtWidgets.QMessageBox()
                new_icon = QtGui.QIcon()
                new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Recursos/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                dlg.setWindowIcon(new_icon)
                dlg.setWindowTitle("Crear Oferta")
                dlg.setText("El número de oferta introducido ya está registrado")
                dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                dlg.exec()

                del dlg,new_icon

            else:
                commands_newoffer = ("""
                            INSERT INTO offers (
                            "num_offer","state","responsible","client","final_client","num_ref_offer","register_date","nac_ext","buyer","material","notes","limit_date","rate_type"
                            )
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """)
                conn = None
                try:
                # read the connection parameters
                    params = config()
                # connect to the PostgreSQL server
                    conn = psycopg2.connect(**params)
                    cur = conn.cursor()
                # execution of commands
                    data=(numoffer, state, responsible, client, finalclient, numref, actual_date, nacext, buyer, material, notes, limitdate, ratetype)
                    cur.execute(commands_newoffer, data)
                # close communication with the PostgreSQL database server
                    cur.close()
                # commit the changes
                    conn.commit()

                    dlg = QtWidgets.QMessageBox()
                    new_icon = QtGui.QIcon()
                    new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Recursos/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                    dlg.setWindowIcon(new_icon)
                    dlg.setWindowTitle("Crear Oferta")
                    dlg.setText("Oferta creada con éxito")
                    dlg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    dlg.exec()

                    self.NumOffer_NewOffer.setText('')
                    self.Client_NewOffer.setText('')
                    self.FinalClient_NewOffer.setText('')
                    self.NumRef_NewOffer.setText('')
                    self.Buyer_NewOffer.setText('')
                    self.Notes_NewOffer.setText('')
                    self.LimitDate_NewOffer.setText('')
                    self.RateType_NewOffer.setText('')

                    del dlg,new_icon

                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if conn is not None:
                        conn.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    New_Offer = QtWidgets.QMainWindow()
    ui = Ui_New_Offer_Window()
    ui.setupUi(New_Offer)
    New_Offer.show()
    sys.exit(app.exec())