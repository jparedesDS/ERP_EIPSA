# Form implementation generated from reading ui file 'EditUser_Menu.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from RegistrationUser_Window import Ui_RegistrationWindow
from DeleteUser_Window import Ui_DeleteUser_Window


class Ui_EditUser_Menu(object):
    def setupUi(self, EditUser_Menu):
        EditUser_Menu.setObjectName("EditUser_Menu")
        EditUser_Menu.resize(300, 340)
        EditUser_Menu.setMinimumSize(QtCore.QSize(300, 340))
        EditUser_Menu.setMaximumSize(QtCore.QSize(300, 340))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Recursos/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        EditUser_Menu.setWindowIcon(icon)
        EditUser_Menu.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=EditUser_Menu)
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
        self.Button_Register = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Register.setMinimumSize(QtCore.QSize(250, 35))
        self.Button_Register.setMaximumSize(QtCore.QSize(250, 35))
        self.Button_Register.setObjectName("Button_Register")
        self.gridLayout_2.addWidget(self.Button_Register, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.Button_Delete = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Delete.setMinimumSize(QtCore.QSize(250, 35))
        self.Button_Delete.setMaximumSize(QtCore.QSize(250, 35))
        self.Button_Delete.setObjectName("Button_Delete")
        self.gridLayout_2.addWidget(self.Button_Delete, 3, 0, 1, 1)
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
        EditUser_Menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=EditUser_Menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menubar.setObjectName("menubar")
        EditUser_Menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=EditUser_Menu)
        self.statusbar.setObjectName("statusbar")
        EditUser_Menu.setStatusBar(self.statusbar)

        self.retranslateUi(EditUser_Menu)
        self.Button_Cancel.clicked.connect(EditUser_Menu.close) # type: ignore
        self.Button_Delete.clicked.connect(lambda: self.user_delete(EditUser_Menu))
        self.Button_Register.clicked.connect(lambda: self.user_register(EditUser_Menu))
        QtCore.QMetaObject.connectSlotsByName(EditUser_Menu)


    def retranslateUi(self, EditUser_Menu):
        _translate = QtCore.QCoreApplication.translate
        EditUser_Menu.setWindowTitle(_translate("EditUser_Menu", "Editar Usuarios"))
        self.Button_Register.setText(_translate("EditUser_Menu", "Registrar Usuario"))
        self.Button_Delete.setText(_translate("EditUser_Menu", "Eliminar Usuario"))
        self.Button_Cancel.setText(_translate("EditUser_Menu", "Cancelar"))


    def user_register(self,EditUser_Menu):
        self.user_register_window=QtWidgets.QMainWindow()
        self.ui=Ui_RegistrationWindow()
        self.ui.setupUi(self.user_register_window)
        self.user_register_window.show()
        EditUser_Menu.hide()
        self.ui.exit_reg.clicked.connect(EditUser_Menu.show)


    def user_delete(self,EditUser_Menu):
        self.user_delete_window=QtWidgets.QMainWindow()
        self.ui=Ui_DeleteUser_Window()
        self.ui.setupUi(self.user_delete_window)
        self.user_delete_window.show()
        EditUser_Menu.hide()
        self.ui.Button_cancel.clicked.connect(EditUser_Menu.show)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditUser_Menu = QtWidgets.QMainWindow()
    ui = Ui_EditUser_Menu()
    ui.setupUi(EditUser_Menu)
    EditUser_Menu.show()
    sys.exit(app.exec())
