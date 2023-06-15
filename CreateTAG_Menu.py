# Form implementation generated from reading ui file 'CreateTAG_Menu.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from ImportTAG_Window import Ui_ImportTAG_Window
from TypeTAGCreation_Menu import Ui_TypeTagCreation_Menu


class Ui_CreateTag_Menu(object):
    def setupUi(self, Create_Tag_Menu):
        Create_Tag_Menu.setObjectName("Create_Tag_Menu")
        Create_Tag_Menu.resize(300, 340)
        Create_Tag_Menu.setMinimumSize(QtCore.QSize(300, 340))
        Create_Tag_Menu.setMaximumSize(QtCore.QSize(300, 340))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Create_Tag_Menu.setWindowIcon(icon)
        Create_Tag_Menu.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=Create_Tag_Menu)
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
        self.Button_Create = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Create.setMinimumSize(QtCore.QSize(250, 35))
        self.Button_Create.setMaximumSize(QtCore.QSize(250, 35))
        self.Button_Create.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_Create.setObjectName("Button_Create")
        self.gridLayout_2.addWidget(self.Button_Create, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.Button_Import = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Import.setMinimumSize(QtCore.QSize(250, 35))
        self.Button_Import.setMaximumSize(QtCore.QSize(250, 35))
        self.Button_Import.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_Import.setObjectName("Button_Import")
        self.gridLayout_2.addWidget(self.Button_Import, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.Button_Cancel = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Cancel.setEnabled(True)
        self.Button_Cancel.setMinimumSize(QtCore.QSize(100, 35))
        self.Button_Cancel.setMaximumSize(QtCore.QSize(100, 35))
        self.Button_Cancel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_Cancel.setObjectName("Button_Cancel")
        self.horizontalLayout.addWidget(self.Button_Cancel)
        self.gridLayout_2.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        Create_Tag_Menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Create_Tag_Menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menubar.setObjectName("menubar")
        Create_Tag_Menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Create_Tag_Menu)
        self.statusbar.setObjectName("statusbar")
        Create_Tag_Menu.setStatusBar(self.statusbar)

        self.retranslateUi(Create_Tag_Menu)
        self.Button_Cancel.clicked.connect(Create_Tag_Menu.close) # type: ignore
        self.Button_Create.clicked.connect(lambda: self.create_tag(Create_Tag_Menu))
        self.Button_Import.clicked.connect(lambda: self.import_tag(Create_Tag_Menu))
        QtCore.QMetaObject.connectSlotsByName(Create_Tag_Menu)


    def retranslateUi(self, Create_Tag_Menu):
        _translate = QtCore.QCoreApplication.translate
        Create_Tag_Menu.setWindowTitle(_translate("Create_Tag_Menu", "Crear TAG"))
        self.Button_Create.setText(_translate("Create_Tag_Menu", "Crear TAG"))
        self.Button_Import.setText(_translate("Create_Tag_Menu", "Importar TAG"))
        self.Button_Cancel.setText(_translate("Create_Tag_Menu", "Cancelar"))


    def create_tag(self,Create_Tag_Menu):
        self.typetag_window=QtWidgets.QMainWindow()
        self.ui=Ui_TypeTagCreation_Menu()
        self.ui.setupUi(self.typetag_window)
        self.typetag_window.show()
        Create_Tag_Menu.hide()
        self.ui.Button_Cancel.clicked.connect(Create_Tag_Menu.show)


    def import_tag(self,Create_Tag_Menu):
        self.import_tag_window=QtWidgets.QMainWindow()
        self.ui=Ui_ImportTAG_Window()
        self.ui.setupUi(self.import_tag_window)
        self.import_tag_window.show()
        Create_Tag_Menu.close()
        self.ui.Button_Cancel.clicked.connect(Create_Tag_Menu.show)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Create_Tag_Menu = QtWidgets.QMainWindow()
    ui = Ui_CreateTag_Menu()
    ui.setupUi(Create_Tag_Menu)
    Create_Tag_Menu.show()
    sys.exit(app.exec())
