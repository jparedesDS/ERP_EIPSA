# Form implementation generated from reading ui file 'EditOffer_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from SubmitOffer_Window import Ui_SubmitOffer_Window
from EditOffer_Window import Ui_Edit_Offer_Window


class Ui_EditOffer_Menu(object):
    def setupUi(self, EditOffer_Menu):
        EditOffer_Menu.setObjectName("EditOffer_Menu")
        EditOffer_Menu.resize(300, 336)
        EditOffer_Menu.setMinimumSize(QtCore.QSize(300, 300))
        EditOffer_Menu.setMaximumSize(QtCore.QSize(300, 340))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        EditOffer_Menu.setWindowIcon(icon)
        EditOffer_Menu.setStyleSheet("QWidget {\n"
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
"}"
)
        self.centralwidget = QtWidgets.QWidget(parent=EditOffer_Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(275, 275))
        self.frame.setMaximumSize(QtCore.QSize(275, 275))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        self.Button_Submit = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Submit.setMinimumSize(QtCore.QSize(250, 35))
        self.Button_Submit.setMaximumSize(QtCore.QSize(250, 35))
        self.Button_Submit.setObjectName("Button_Submit")
        self.gridLayout_2.addWidget(self.Button_Submit, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.Button_Edit = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Edit.setMinimumSize(QtCore.QSize(250, 35))
        self.Button_Edit.setMaximumSize(QtCore.QSize(250, 35))

        self.Button_Edit.setObjectName("Button_Edit")
        self.gridLayout_2.addWidget(self.Button_Edit, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.Button_Cancel = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Cancel.setEnabled(True)
        self.Button_Cancel.setMinimumSize(QtCore.QSize(100, 35))
        self.Button_Cancel.setMaximumSize(QtCore.QSize(100, 35))
        self.Button_Cancel.setObjectName("Button_Cancel")
        self.horizontalLayout.addWidget(self.Button_Cancel)
        self.gridLayout_2.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        EditOffer_Menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=EditOffer_Menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menubar.setObjectName("menubar")
        EditOffer_Menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=EditOffer_Menu)
        self.statusbar.setObjectName("statusbar")
        EditOffer_Menu.setStatusBar(self.statusbar)

        self.retranslateUi(EditOffer_Menu)
        self.Button_Cancel.clicked.connect(EditOffer_Menu.close) # type: ignore
        self.Button_Submit.clicked.connect(self.SubmitOffer)
        self.Button_Edit.clicked.connect(self.EditOffer)
        QtCore.QMetaObject.connectSlotsByName(EditOffer_Menu)


    def retranslateUi(self, EditOffer_Menu):
        _translate = QtCore.QCoreApplication.translate
        EditOffer_Menu.setWindowTitle(_translate("EditOffer_Menu", "Editar Oferta"))
        self.Button_Submit.setText(_translate("EditOffer_Menu", "Presentar Oferta"))
        self.Button_Edit.setText(_translate("EditOffer_Menu", "Editar Oferta"))
        self.Button_Cancel.setText(_translate("EditOffer_Menu", "Cancelar"))


    def SubmitOffer(self):
        self.submitoffer_window=QtWidgets.QMainWindow()
        self.ui=Ui_SubmitOffer_Window()
        self.ui.setupUi(self.submitoffer_window)
        self.submitoffer_window.show()
        EditOffer_Menu.hide()
        self.ui.Button_Cancel.clicked.connect(EditOffer_Menu.show)


    def EditOffer(self):
        self.editoffer_window=QtWidgets.QMainWindow()
        self.ui=Ui_Edit_Offer_Window()
        self.ui.setupUi(self.editoffer_window)
        self.editoffer_window.show()
        EditOffer_Menu.hide()
        self.ui.Button_Cancel.clicked.connect(EditOffer_Menu.show)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    EditOffer_Menu = QtWidgets.QMainWindow()
    ui = Ui_EditOffer_Menu()
    ui.setupUi(EditOffer_Menu)
    EditOffer_Menu.show()
    sys.exit(app.exec())
