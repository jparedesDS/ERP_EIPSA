# Form implementation generated from reading ui file 'EditDB_Menu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import configparser
from Database_Connection import createConnection
from AddReg_Window import Ui_AddReg_Window
from EditReg_Window import Ui_EditReg_Window
import os

basedir = r"\\nas01\DATOS\Comunes\EIPSA-ERP"


class Ui_EditDB_Menu(object):
    def setupUi(self, EditDB_Menu):
        EditDB_Menu.setObjectName("EditDB_Menu")
        EditDB_Menu.resize(300, 336)
        EditDB_Menu.setMinimumSize(QtCore.QSize(300, 300))
        EditDB_Menu.setMaximumSize(QtCore.QSize(300, 340))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        EditDB_Menu.setWindowIcon(icon)
        EditDB_Menu.setStyleSheet("QWidget {\n"
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
"}")
        self.centralwidget = QtWidgets.QWidget(parent=EditDB_Menu)
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
        self.Button_AddReg = QtWidgets.QPushButton(parent=self.frame)
        self.Button_AddReg.setMinimumSize(QtCore.QSize(250, 35))
        self.Button_AddReg.setMaximumSize(QtCore.QSize(250, 35))
        self.Button_AddReg.setObjectName("Button_AddReg")
        self.gridLayout_2.addWidget(self.Button_AddReg, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.Button_EditReg = QtWidgets.QPushButton(parent=self.frame)
        self.Button_EditReg.setMinimumSize(QtCore.QSize(250, 35))
        self.Button_EditReg.setMaximumSize(QtCore.QSize(250, 35))
        self.Button_EditReg.setObjectName("Button_EditReg")
        self.gridLayout_2.addWidget(self.Button_EditReg, 3, 0, 1, 1)
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
        EditDB_Menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=EditDB_Menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menubar.setObjectName("menubar")
        EditDB_Menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=EditDB_Menu)
        self.statusbar.setObjectName("statusbar")
        EditDB_Menu.setStatusBar(self.statusbar)

        self.retranslateUi(EditDB_Menu)
        self.Button_Cancel.clicked.connect(EditDB_Menu.close) # type: ignore
        self.Button_AddReg.clicked.connect(lambda: self.addreg(EditDB_Menu))
        self.Button_EditReg.clicked.connect(lambda: self.editreg(EditDB_Menu))
        QtCore.QMetaObject.connectSlotsByName(EditDB_Menu)


    def retranslateUi(self, EditDB_Menu):
        _translate = QtCore.QCoreApplication.translate
        EditDB_Menu.setWindowTitle(_translate("EditDB_Menu", "Editar Base de Datos"))
        self.Button_AddReg.setText(_translate("EditDB_Menu", "Agregar Registros"))
        self.Button_EditReg.setText(_translate("EditDB_Menu", "Editar Registros"))
        self.Button_Cancel.setText(_translate("EditDB_Menu", "Cancelar"))


    def addreg(self,EditDB_Menu):
        self.addreg_window=QtWidgets.QMainWindow()
        self.ui=Ui_AddReg_Window()
        self.ui.setupUi(self.addreg_window)
        self.addreg_window.show()
        EditDB_Menu.hide()
        self.ui.Button_Cancel.clicked.connect(EditDB_Menu.show)


    def editreg(self,EditDB_Menu):
        config_obj = configparser.ConfigParser()
        config_obj.read(r"C:\Program Files\ERP EIPSA\database.ini")
        dbparam = config_obj["postgresql"]
        # set your parameters for the database connection URI using the keys from the configfile.ini
        user = dbparam["user"]
        password = dbparam["password"]

        self.db_connection = createConnection(user, password)
        if not self.db_connection:
            sys.exit()
        self.editreg_window=QtWidgets.QMainWindow()
        self.ui=Ui_EditReg_Window()
        self.ui.setupUi(self.editreg_window)
        self.editreg_window.show()


    def closeDatabaseConnection(self):
        print('a')
        if self.db_connection.isOpen():
            self.db_connection.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditDB_Menu = QtWidgets.QMainWindow()
    ui = Ui_EditDB_Menu()
    ui.setupUi(EditDB_Menu)
    EditDB_Menu.show()
    sys.exit(app.exec())
