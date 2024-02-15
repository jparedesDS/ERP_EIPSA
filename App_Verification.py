# Form implementation generated from reading ui file 'App_Verification.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMenu
import sys
import configparser
from Database_Connection import createConnection
from datetime import *
import os
import locale

basedir = r"\\nas01\DATOS\Comunes\EIPSA-ERP"


class Ui_App_Verification(object):
    def __init__(self, name, username):
        self.name=name
        self.username=username
        locale.setlocale(locale.LC_TIME, 'es_ES.utf8')


    def setupUi(self, App_Verification):
        App_Verification.setObjectName("App_Verification")
        App_Verification.resize(1254, 860)
        App_Verification.setMinimumSize(QtCore.QSize(945, 860))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        App_Verification.setWindowIcon(icon)
        if self.username == 'm.gil':
            App_Verification.setStyleSheet("background-color: rgb(38, 38, 38);")
        else:
            App_Verification.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=App_Verification)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.FrameApp = QtWidgets.QVBoxLayout()
        self.FrameApp.setObjectName("FrameApp")
        self.Header = QtWidgets.QHBoxLayout()
        self.Header.setContentsMargins(-1, 0, -1, -1)
        self.Header.setObjectName("Header")
        self.LogoIcon = QtWidgets.QLabel(parent=self.frame)
        self.LogoIcon.setMinimumSize(QtCore.QSize(220, 52))
        self.LogoIcon.setMaximumSize(QtCore.QSize(220, 52))
        self.LogoIcon.setText("")
        self.LogoIcon.setPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/Logo Nobg.ico"))))
        self.LogoIcon.setScaledContents(True)
        self.LogoIcon.setObjectName("LogoIcon")
        self.Header.addWidget(self.LogoIcon)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.Header.addItem(spacerItem)
        self.Button_DBEdit = QtWidgets.QPushButton(parent=self.frame)
        self.Button_DBEdit.setMinimumSize(QtCore.QSize(50, 50))
        self.Button_DBEdit.setMaximumSize(QtCore.QSize(50, 50))
        self.Button_DBEdit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        if self.username == 'm.gil':
            self.Button_DBEdit.setStyleSheet("QPushButton{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(3, 174, 236);\n"
    "    background-color: rgb(38, 38, 38);\n"
    "    border-radius: 10px;\n"
    "}\n"
    "\n"
    "QPushButton:hover{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(0, 0, 0);\n"
    "    color: rgb(0,0,0);\n"
    "    background-color: rgb(255, 255, 255);\n"
    "    border-radius: 10px;\n"
    "}\n"
    "\n"
    "QPushButton:pressed{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(0, 0, 0);\n"
    "    color: rgb(0,0,0);\n"
    "    background-color: rgb(200, 200, 200);\n"
    "    border-radius: 10px;\n"
    "}")
        else:
            self.Button_DBEdit.setStyleSheet("QPushButton{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(3, 174, 236);\n"
    "    background-color: rgb(255, 255, 255);\n"
    "    border-radius: 10px;\n"
    "}\n"
    "\n"
    "QPushButton:hover{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(0, 0, 0);\n"
    "    color: rgb(0,0,0);\n"
    "    background-color: rgb(255, 255, 255);\n"
    "    border-radius: 10px;\n"
    "}\n"
    "\n"
    "QPushButton:pressed{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(0, 0, 0);\n"
    "    color: rgb(0,0,0);\n"
    "    background-color: rgb(200, 200, 200);\n"
    "    border-radius: 10px;\n"
    "}")
        self.Button_DBEdit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/Database_Admin.png"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_DBEdit.setIcon(icon2)
        self.Button_DBEdit.setIconSize(QtCore.QSize(40, 40))
        self.Button_DBEdit.setObjectName("Button_DBEdit")
        self.Header.addWidget(self.Button_DBEdit)
        self.Button_DBEdit.clicked.connect(self.editdb)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.Header.addItem(spacerItem5)
        self.Button_Timer = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Timer.setMinimumSize(QtCore.QSize(50, 50))
        self.Button_Timer.setMaximumSize(QtCore.QSize(50, 50))
        self.Button_Timer.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        if self.username == 'm.gil':
            self.Button_Timer.setStyleSheet("QPushButton{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(3, 174, 236);\n"
    "    background-color: rgb(38, 38, 38);\n"
    "    border-radius: 10px;\n"
    "}\n"
    "\n"
    "QPushButton:hover{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(0, 0, 0);\n"
    "    color: rgb(0,0,0);\n"
    "    background-color: rgb(255, 255, 255);\n"
    "    border-radius: 10px;\n"
    "}\n"
    "\n"
    "QPushButton:pressed{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(0, 0, 0);\n"
    "    color: rgb(0,0,0);\n"
    "    background-color: rgb(200, 200, 200);\n"
    "    border-radius: 10px;\n"
    "}")
        else:
            self.Button_Timer.setStyleSheet("QPushButton{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(3, 174, 236);\n"
    "    background-color: rgb(255, 255, 255);\n"
    "    border-radius: 10px;\n"
    "}\n"
    "\n"
    "QPushButton:hover{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(0, 0, 0);\n"
    "    color: rgb(0,0,0);\n"
    "    background-color: rgb(255, 255, 255);\n"
    "    border-radius: 10px;\n"
    "}\n"
    "\n"
    "QPushButton:pressed{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(0, 0, 0);\n"
    "    color: rgb(0,0,0);\n"
    "    background-color: rgb(200, 200, 200);\n"
    "    border-radius: 10px;\n"
    "}")
        self.Button_Timer.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/Timer.png"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Timer.setIcon(icon5)
        self.Button_Timer.setIconSize(QtCore.QSize(40, 40))
        self.Button_Timer.setObjectName("Button_Timer")
        self.Header.addWidget(self.Button_Timer)
        self.Button_Timer.clicked.connect(self.timer)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.Header.addItem(spacerItem1)
        self.HeaderName = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.HeaderName.setFont(font)
        self.HeaderName.setStyleSheet("color:rgb(3, 174, 236)")
        self.HeaderName.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.HeaderName.setObjectName("HeaderName")
        self.Header.addWidget(self.HeaderName)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.Header.addItem(spacerItem6)
        self.Button_Profile = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Profile.setMinimumSize(QtCore.QSize(50, 50))
        self.Button_Profile.setMaximumSize(QtCore.QSize(50, 50))
        if self.username == 'm.gil':
            self.Button_Profile.setStyleSheet("QPushButton{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(3, 174, 236);\n"
    "    background-color: rgb(38, 38, 38);\n"
    "    border-radius: 10px;\n"
    "}\n"
    "\n"
    "QPushButton:hover{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(0, 0, 0);\n"
    "    color: rgb(0,0,0);\n"
    "    background-color: rgb(255, 255, 255);\n"
    "    border-radius: 10px;\n"
    "}\n"
    "\n"
    "QPushButton:pressed{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(0, 0, 0);\n"
    "    color: rgb(0,0,0);\n"
    "    background-color: rgb(200, 200, 200);\n"
    "    border-radius: 10px;\n"
    "}")
        else:
            self.Button_Profile.setStyleSheet("QPushButton{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(3, 174, 236);\n"
    "    background-color: rgb(255, 255, 255);\n"
    "    border-radius: 10px;\n"
    "}\n"
    "\n"
    "QPushButton:hover{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(0, 0, 0);\n"
    "    color: rgb(0,0,0);\n"
    "    background-color: rgb(255, 255, 255);\n"
    "    border-radius: 10px;\n"
    "}\n"
    "\n"
    "QPushButton:pressed{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(0, 0, 0);\n"
    "    color: rgb(0,0,0);\n"
    "    background-color: rgb(200, 200, 200);\n"
    "    border-radius: 10px;\n"
    "}")
        self.Button_Profile.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/Mario.png"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Profile.setIcon(icon6)
        self.Button_Profile.setIconSize(QtCore.QSize(40, 40))
        self.Button_Profile.setObjectName("Button_Profile")
        self.Header.addWidget(self.Button_Profile)
        self.FrameApp.addLayout(self.Header)
        spacerItem7 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.FrameApp.addItem(spacerItem7)
        self.PrincipalScreen = QtWidgets.QHBoxLayout()
        self.PrincipalScreen.setObjectName("PrincipalScreen")
        self.ButtonFrame = QtWidgets.QFrame(parent=self.frame)
        self.ButtonFrame.setMinimumSize(QtCore.QSize(220, 0))
        self.ButtonFrame.setMaximumSize(QtCore.QSize(220, 16777215))
        self.ButtonFrame.setAutoFillBackground(False)
        if self.username == 'm.gil':
            self.ButtonFrame.setStyleSheet("QFrame{\n"
    "    background-color: rgb(3, 174, 236);\n"
    "}\n"
    "\n"
    "QPushButton{\n"
    "    border: 1px solid transparent;\n"
    "    color: rgb(3, 174, 236);\n"
    "    background-color: rgb(38, 38, 38);\n"
    "    border-radius: 10px;\n"
    "}\n"
    "\n"
    "QPushButton:hover{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(0, 0, 0);\n"
    "    color: rgb(0,0,0);\n"
    "    background-color: rgb(255, 255, 255);\n"
    "    border-radius: 10px;\n"
    "}\n"
    "\n"
    "QPushButton:pressed{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(0, 0, 0);\n"
    "    color: rgb(0,0,0);\n"
    "    background-color: rgb(200, 200, 200);\n"
    "    border-radius: 10px;\n"
    "}")
        else:
            self.ButtonFrame.setStyleSheet("QFrame{\n"
    "    background-color: rgb(3, 174, 236);\n"
    "}\n"
    "\n"
    "QPushButton{\n"
    "    border: 1px solid transparent;\n"
    "    color: rgb(3, 174, 236);\n"
    "    background-color: rgb(255, 255, 255);\n"
    "    border-radius: 10px;\n"
    "}\n"
    "\n"
    "QPushButton:hover{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(0, 0, 0);\n"
    "    color: rgb(0,0,0);\n"
    "    background-color: rgb(255, 255, 255);\n"
    "    border-radius: 10px;\n"
    "}\n"
    "\n"
    "QPushButton:pressed{\n"
    "    border: 1px solid transparent;\n"
    "    border-color: rgb(0, 0, 0);\n"
    "    color: rgb(0,0,0);\n"
    "    background-color: rgb(200, 200, 200);\n"
    "    border-radius: 10px;\n"
    "}")
        self.ButtonFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.ButtonFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ButtonFrame.setObjectName("ButtonFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ButtonFrame)
        self.verticalLayout_3.setContentsMargins(9, 0, -1, 0)
        self.verticalLayout_3.setSpacing(25)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Button_QueryTag = QtWidgets.QPushButton(parent=self.ButtonFrame)
        self.Button_QueryTag.setMinimumSize(QtCore.QSize(int(200), int(50)))
        self.Button_QueryTag.setMaximumSize(QtCore.QSize(int(200), int(50)))
        font = QtGui.QFont()
        font.setPointSize(int(12))
        font.setBold(True)
        self.Button_QueryTag.setFont(font)
        self.Button_QueryTag.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/TAG_Search.png"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_QueryTag.setIcon(icon1)
        self.Button_QueryTag.setIconSize(QtCore.QSize(int(40), int(40)))
        self.Button_QueryTag.setObjectName("Button_QueryTag")
        self.verticalLayout_3.addWidget(self.Button_QueryTag)
        self.Button_Verification = QtWidgets.QPushButton(parent=self.ButtonFrame)
        self.Button_Verification.setMinimumSize(QtCore.QSize(200, 50))
        self.Button_Verification.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.Button_Verification.setFont(font)
        self.Button_Verification.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/Verification.png"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Verification.setIcon(icon1)
        self.Button_Verification.setIconSize(QtCore.QSize(40, 40))
        self.Button_Verification.setObjectName("Button_Verification")
        self.verticalLayout_3.addWidget(self.Button_Verification)
        self.Button_Hydro = QtWidgets.QPushButton(parent=self.ButtonFrame)
        self.Button_Hydro.setMinimumSize(QtCore.QSize(200, 50))
        self.Button_Hydro.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.Button_Hydro.setFont(font)
        self.Button_Hydro.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/Hydro.png"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Hydro.setIcon(icon2)
        self.Button_Hydro.setIconSize(QtCore.QSize(40, 40))
        self.Button_Hydro.setObjectName("Button_Hydro")
        self.verticalLayout_3.addWidget(self.Button_Hydro)
        self.Button_Liquid = QtWidgets.QPushButton(parent=self.ButtonFrame)
        self.Button_Liquid.setMinimumSize(QtCore.QSize(200, 50))
        self.Button_Liquid.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.Button_Liquid.setFont(font)
        self.Button_Liquid.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/Liquid.png"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Liquid.setIcon(icon3)
        self.Button_Liquid.setIconSize(QtCore.QSize(40, 40))
        self.Button_Liquid.setObjectName("Button_Liquid")
        self.verticalLayout_3.addWidget(self.Button_Liquid)
        self.Button_Hardness = QtWidgets.QPushButton(parent=self.ButtonFrame)
        self.Button_Hardness.setMinimumSize(QtCore.QSize(200, 50))
        self.Button_Hardness.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.Button_Hardness.setFont(font)
        self.Button_Hardness.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/Hardness.png"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Hardness.setIcon(icon4)
        self.Button_Hardness.setIconSize(QtCore.QSize(40, 40))
        self.Button_Hardness.setObjectName("Button_Hardness")
        self.verticalLayout_3.addWidget(self.Button_Hardness)
        self.Button_Calibration = QtWidgets.QPushButton(parent=self.ButtonFrame)
        self.Button_Calibration.setMinimumSize(QtCore.QSize(200, 50))
        self.Button_Calibration.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.Button_Calibration.setFont(font)
        self.Button_Calibration.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/Calibration.png"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Calibration.setIcon(icon7)
        self.Button_Calibration.setIconSize(QtCore.QSize(100, 100))
        self.Button_Calibration.setObjectName("Button_Calibration")
        self.verticalLayout_3.addWidget(self.Button_Calibration)
        self.Button_Suppliers = QtWidgets.QPushButton(parent=self.ButtonFrame)
        self.Button_Suppliers.setMinimumSize(QtCore.QSize(200, 50))
        self.Button_Suppliers.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.Button_Suppliers.setFont(font)
        self.Button_Suppliers.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/Supplier.png"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Suppliers.setIcon(icon7)
        self.Button_Suppliers.setIconSize(QtCore.QSize(100, 100))
        self.Button_Suppliers.setObjectName("Button_Suppliers")
        self.verticalLayout_3.addWidget(self.Button_Suppliers)
        self.PrincipalScreen.addWidget(self.ButtonFrame)
        self.ClockFrame = QtWidgets.QFrame(parent=self.frame)
        self.ClockFrame.setMinimumSize(QtCore.QSize(220, 0))
        self.ClockFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ClockFrame.setAutoFillBackground(False)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ClockFrame)
        self.gridLayout_3.setObjectName("gridLayout")
        self.clock_indicator = QtWidgets.QLabel(parent=self.frame)
        font_id = QtGui.QFontDatabase.addApplicationFont(os.path.abspath(os.path.join(basedir, "Resources/Iconos/DS-DIGI.ttf")))
        if font_id != -1:
            font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]
            font = QtGui.QFont(font_family, 350)
        else:
            font = QtGui.QFont("arial", 150)
        font.setBold(True)
        self.clock_indicator.setFont(font)
        self.clock_indicator.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        if self.username == 'm.gil':
            self.clock_indicator.setStyleSheet("color: white")
        self.clock = QtCore.QTimer()
        self.clock.timeout.connect(self.showTime)
        self.clock.start(1000)
        self.gridLayout_3.addWidget(self.clock_indicator, 0, 0, 1, 1)
        self.weekday_indicator = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        self.weekday_indicator.setFont(font)
        self.weekday_indicator.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        if self.username == 'm.gil':
            self.weekday_indicator.setStyleSheet("color: white")
        weekday = datetime.now().strftime("%A").encode('latin-1').decode('utf-8')
        actual_date = date.today().strftime("%d/%m/%Y")
        self.weekday_indicator.setText(f"{weekday}, {actual_date}")
        self.gridLayout_3.addWidget(self.weekday_indicator, 1, 0, 1, 1)
        self.PrincipalScreen.addWidget(self.ClockFrame)
        self.FrameApp.addLayout(self.PrincipalScreen)
        self.gridLayout.addLayout(self.FrameApp, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        App_Verification.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=App_Verification)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1254, 22))
        self.menubar.setObjectName("menubar")
        App_Verification.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=App_Verification)
        self.statusbar.setObjectName("statusbar")
        App_Verification.setStatusBar(self.statusbar)

        self.retranslateUi(App_Verification)
        QtCore.QMetaObject.connectSlotsByName(App_Verification)

        self.Button_QueryTag.clicked.connect(self.query_tag)
        self.Button_Verification.clicked.connect(self.verification)
        self.Button_Hydro.clicked.connect(self.hydrotest)
        self.Button_Liquid.clicked.connect(self.liquidtest)
        self.Button_Hardness.clicked.connect(self.hardtest)
        self.Button_Calibration.clicked.connect(self.calibration)
        self.Button_Suppliers.clicked.connect(self.suppliers_delivnote)
        self.Button_Profile.clicked.connect(self.showMenu)


    def retranslateUi(self, App_Verification):
        _translate = QtCore.QCoreApplication.translate
        App_Verification.setWindowTitle(_translate("App_Verification", "ERP EIPSA"))
        self.HeaderName.setText(_translate("App_Verification", self.name))
        self.Button_QueryTag.setText(_translate("App_Verification", "    Consultar TAG(s)"))
        self.Button_Verification.setText(_translate("App_Verification", "    Verificación"))
        self.Button_Liquid.setText(_translate("App_Verification", "  Liq. Penetrantes"))
        self.Button_Hydro.setText(_translate("App_Verification", "    Prueba Hidro."))
        self.Button_Hardness.setText(_translate("App_Verification", "    Prueba Dureza"))
        self.Button_Calibration.setText(_translate("App_Verification", "    Calibraciones"))
        self.Button_Suppliers.setText(_translate("App_Verification", "    Proveedores"))


# Function to show the current time on screen
    def showTime(self):
        # getting current time
        current_time = QtCore.QTime.currentTime()
        # converting QTime object to string
        label_time = current_time.toString('hh:mm')
        # showing it to the label
        self.clock_indicator.setText(label_time)


# Function to open corresponding window when Edit DB button is clicked
    def editdb(self):
        from DBEditRegVerif_Window import Ui_DBEditRegVerif_Window
        config_obj = configparser.ConfigParser()
        config_obj.read(r"C:\Program Files\ERP EIPSA\database.ini")
        dbparam = config_obj["postgresql"]
        # set your parameters for the database connection URI using the keys from the configfile.ini
        user_database = dbparam["user"]
        password_database = dbparam["password"]

        db_validation = createConnection(user_database, password_database)
        if not db_validation:
            sys.exit()

        self.dbedit_window=Ui_DBEditRegVerif_Window(db_validation, self.username)
        self.dbedit_window.show()


# Function to open corresponding window when Query Tags button is clicked
    def query_tag(self):
        from TAGEdit_Verification_Window import Ui_EditTags_Verification_Window
        config_obj = configparser.ConfigParser()
        config_obj.read(r"C:\Program Files\ERP EIPSA\database.ini")
        dbparam = config_obj["postgresql"]
        # set your parameters for the database connection URI using the keys from the configfile.ini
        user_database = dbparam["user"]
        password_database = dbparam["password"]

        db_tags_tech = createConnection(user_database, password_database)
        if not db_tags_tech:
            sys.exit()

        self.edit_tags_app = Ui_EditTags_Verification_Window(self.name, db_tags_tech, self.username)
        self.edit_tags_app.show()


# Function to open corresponding window when Verification button is clicked
    def verification(self):
        from Verification_Menu import Ui_Verification_Menu
        self.verif_menu=QtWidgets.QMainWindow()
        self.ui=Ui_Verification_Menu(self.username)
        self.ui.setupUi(self.verif_menu)
        self.verif_menu.show()


# Function to open corresponding window when Hydrostatic Test button is clicked
    def hydrotest(self):
        from TestHydro_Menu import Ui_TestHydro_Menu
        self.testhydro_menu=QtWidgets.QMainWindow()
        self.ui=Ui_TestHydro_Menu(self.username)
        self.ui.setupUi(self.testhydro_menu)
        self.testhydro_menu.show()


# Function to open corresponding window when Liquid Test button is clicked
    def liquidtest(self):
        from TestLiquid_Menu import Ui_TestLiquid_Menu
        self.testliquid_menu=QtWidgets.QMainWindow()
        self.ui=Ui_TestLiquid_Menu(self.username)
        self.ui.setupUi(self.testliquid_menu)
        self.testliquid_menu.show()


# Function to open corresponding window when Hardness Test button is clicked
    def hardtest(self):
        from TestHard_Menu import Ui_TestHard_Menu
        self.testhard_menu=QtWidgets.QMainWindow()
        self.ui=Ui_TestHard_Menu(self.username)
        self.ui.setupUi(self.testhard_menu)
        self.testhard_menu.show()


# Function to open corresponding window when Calibration button is clicked
    def calibration(self):
        from Calibration_ThermoElements_Window import Ui_Calibration_ThermoElements_Window
        config_obj = configparser.ConfigParser()
        config_obj.read(r"C:\Program Files\ERP EIPSA\database.ini")
        dbparam = config_obj["postgresql"]
        # set your parameters for the database connection URI using the keys from the configfile.ini
        user_database = dbparam["user"]
        password_database = dbparam["password"]

        db_calibration = createConnection(user_database, password_database)
        if not db_calibration:
            sys.exit()

        self.calibration_window = Ui_Calibration_ThermoElements_Window(db_calibration, self.username)
        self.calibration_window.showMaximized()


# Function to open corresponding window when Suppliers button is clicked
    def suppliers_delivnote(self):
        from VerifSupplierInsert_Window import Ui_VerifSupplierInsert_Window
        self.verifsupplier_window=QtWidgets.QMainWindow()
        self.ui=Ui_VerifSupplierInsert_Window(self.username)
        self.ui.setupUi(self.verifsupplier_window)
        self.verifsupplier_window.show()


# Function to show menu when Profile button is clicked 
    def showMenu(self):
        menu = QMenu(self.centralwidget)
        if self.username == 'm.gil':
            menu.setStyleSheet("QMenu { background-color: rgb(255, 255, 255); border: 1px solid black; width: 125px; right: -1px; }"
            "QMenu::item:selected { background-color: rgb(3, 174, 236); color: white; }")
        else:
            menu.setStyleSheet("QMenu { border: 1px solid black; width: 125px; right: -1px; }"
            "QMenu::item:selected { background-color: rgb(3, 174, 236); color: white; }")
        option1 = menu.addAction("Editar contraseña")
        option1.triggered.connect(lambda: self.editpassword())
        menu.addAction(option1)
        button = self.Button_Profile
        menu.exec(button.mapToGlobal(QtCore.QPoint(-75, 50)))


# Function to open corresponding window when Edit Password option is clicked
    def editpassword(self):
        from PasswordEdit_Window import Ui_EditPasswordWindow
        self.edit_password_window=QtWidgets.QMainWindow()
        self.ui=Ui_EditPasswordWindow(self.username)
        self.ui.setupUi(self.edit_password_window)
        self.edit_password_window.show()


    def timer(self):
        from TimerWindow import Ui_TimerWindow
        self.timerwindow=Ui_TimerWindow(self.username)
        self.timerwindow.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    App_Verification = QtWidgets.QMainWindow()
    ui = Ui_App_Verification('Mario Gil', 'm.gil')
    ui.setupUi(App_Verification)
    App_Verification.show()
    sys.exit(app.exec())