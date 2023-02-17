# Form implementation generated from reading ui file 'Login_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from Registration_Window import *


class Ui_Login_Window(object):
    def setupUi(self, Login_Window):
        Login_Window.setObjectName("Login_Window")
        Login_Window.resize(670, 392)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login_Window.sizePolicy().hasHeightForWidth())
        Login_Window.setSizePolicy(sizePolicy)
        Login_Window.setMaximumSize(QtCore.QSize(670, 392))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Login_Window.setWindowIcon(icon)
        Login_Window.setAutoFillBackground(False)
        Login_Window.setStyleSheet("QWidget {\n"
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
"  box-shadow: rgba(255, 255, 255, .4) 0 1px 0 0 inset;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",\"Liberation Sans\",sans-serif;\n"
"  font-size: 15px;\n"
"  font-weight: 800;\n"
"  line-height: 1.15385;\n"
"  margin: 0;\n"
"  outline: none;\n"
"  padding: 8px .8em;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  text-shadow: 0px 1px 0px #263666;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
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
        Login_Window.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(parent=Login_Window)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(652, 352))
        self.frame.setMaximumSize(QtCore.QSize(652, 352))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.logo = QtWidgets.QLabel(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMaximumSize(QtCore.QSize(256, 234))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Logo.ico"))
        self.logo.setScaledContents(False)
        self.logo.setObjectName("logo")
        self.horizontalLayout.addWidget(self.logo)
        spacerItem1 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_username_login = QtWidgets.QLabel(parent=self.frame)
        self.label_username_login.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_username_login.sizePolicy().hasHeightForWidth())
        self.label_username_login.setSizePolicy(sizePolicy)
        self.label_username_login.setMinimumSize(QtCore.QSize(200, 25))
        self.label_username_login.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_username_login.setFont(font)
        self.label_username_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_username_login.setObjectName("label_username_login")
        self.verticalLayout.addWidget(self.label_username_login)
        self.username_login = QtWidgets.QLineEdit(parent=self.frame)
        self.username_login.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_login.sizePolicy().hasHeightForWidth())
        self.username_login.setSizePolicy(sizePolicy)
        self.username_login.setMinimumSize(QtCore.QSize(200, 25))
        self.username_login.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_login.setFont(font)
        self.username_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.username_login.setObjectName("username_login")
        self.verticalLayout.addWidget(self.username_login)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.label_password_login = QtWidgets.QLabel(parent=self.frame)
        self.label_password_login.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_password_login.sizePolicy().hasHeightForWidth())
        self.label_password_login.setSizePolicy(sizePolicy)
        self.label_password_login.setMinimumSize(QtCore.QSize(200, 25))
        self.label_password_login.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_password_login.setFont(font)
        self.label_password_login.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_password_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_password_login.setObjectName("label_password_login")
        self.verticalLayout.addWidget(self.label_password_login)
        self.password_login = QtWidgets.QLineEdit(parent=self.frame)
        self.password_login.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_login.sizePolicy().hasHeightForWidth())
        self.password_login.setSizePolicy(sizePolicy)
        self.password_login.setMinimumSize(QtCore.QSize(200, 25))
        self.password_login.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_login.setFont(font)
        self.password_login.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.password_login.setObjectName("password_login")
        self.verticalLayout.addWidget(self.password_login)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.accept_login = QtWidgets.QPushButton(parent=self.frame)
        self.accept_login.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accept_login.sizePolicy().hasHeightForWidth())
        self.accept_login.setSizePolicy(sizePolicy)
        self.accept_login.setMinimumSize(QtCore.QSize(200, 30))
        self.accept_login.setMaximumSize(QtCore.QSize(200, 30))
        self.accept_login.setStyleSheet("QPushButton:focus{\n"
"    background-color: #019ad2;\n"
"    border-color: rgb(0, 0, 0);\n"
"}"
)
        self.accept_login.setAutoDefault(True)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.accept_login.setFont(font)
        self.accept_login.setObjectName("accept_login")
        self.verticalLayout.addWidget(self.accept_login)
        self.exit_login = QtWidgets.QPushButton(parent=self.frame)
        self.exit_login.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_login.sizePolicy().hasHeightForWidth())
        self.exit_login.setSizePolicy(sizePolicy)
        self.exit_login.setMinimumSize(QtCore.QSize(200, 30))
        self.exit_login.setMaximumSize(QtCore.QSize(200, 30))
        self.exit_login.setStyleSheet("QPushButton:focus{\n"
"    background-color: #019ad2;\n"
"    border-color: rgb(0, 0, 0);\n"
"}"
)
        self.exit_login.setAutoDefault(True)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.exit_login.setFont(font)
        self.exit_login.setObjectName("exit_login")
        self.verticalLayout.addWidget(self.exit_login)
        self.label_error_login = QtWidgets.QLabel(parent=self.frame)
        self.label_error_login.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_error_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_error_login.setMinimumSize(QtCore.QSize(200, 25))
        self.label_error_login.setMaximumSize(QtCore.QSize(200, 25))
        self.label_error_login.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_error_login.setText("")
        self.label_error_login.setObjectName("label_error_login")
        self.verticalLayout.addWidget(self.label_error_login)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        Login_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Login_Window)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 22))
        self.menubar.setObjectName("menubar")
        Login_Window.setMenuBar(self.menubar)

        self.retranslateUi(Login_Window)
        self.accept_login.clicked.connect(self.verification_login) # type: ignore
        self.exit_login.clicked.connect(Login_Window.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Login_Window)


    def retranslateUi(self, Login_Window):
        _translate = QtCore.QCoreApplication.translate
        Login_Window.setWindowTitle(_translate("Login_Window", "ERP EIPSA"))
        self.label_username_login.setText(_translate("Login_Window", "Nombre de Usuario:"))
        self.label_password_login.setText(_translate("Login_Window", "Contraseña:"))
        self.accept_login.setText(_translate("Login_Window", "Acceder"))
        self.exit_login.setText(_translate("Login_Window", "Salir"))


    def verification_login(self):
        login_username = self.username_login.text()
        login_password = self.password_login.text()
        list_files = os.listdir('C:/Users/Enrique.serrano/Documents/GIT/ERP_EIPSA/Passwords')

        if login_username =="" or login_password=="":
            self.label_error_login.setText('Rellene todos los campos')

        else:

            if login_username in list_files:
                path=os.path.join('C:/Users/Enrique.serrano/Documents/GIT/ERP_EIPSA/Passwords',login_username)
                verif_file = open(path, 'r')
                verification = verif_file.read().splitlines()

                if login_password in verification:
                    self.reg_window=QtWidgets.QMainWindow()
                    self.ui=Ui_RegistrationWindow()
                    self.ui.setupUi(self.reg_window)
                    self.reg_window.show()

                else:
                    self.label_error_login.setText('Contraseña incorrecta')

            else:
                self.label_error_login.setText('Usuario y/o contraseña incorrecto')


        del login_password, list_files
        return login_username


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Login_Window = QtWidgets.QMainWindow()
    ui = Ui_Login_Window()
    ui.setupUi(Login_Window)
    Login_Window.show()
    sys.exit(app.exec())
