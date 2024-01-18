# Form implementation generated from reading ui file 'EditPassword_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import re
import psycopg2
from config import config
import os

basedir = r"\\nas01\DATOS\Comunes\EIPSA-ERP"


class Ui_EditPasswordWindow(object):
    def __init__(self, username):
        self.username=username


    def setupUi(self, EditPasswordWindow):
        EditPasswordWindow.setObjectName("EditPasswordWindow")
        EditPasswordWindow.resize(270, 511)
        EditPasswordWindow.setMinimumSize(QtCore.QSize(270, 475))
        EditPasswordWindow.setMaximumSize(QtCore.QSize(270, 511))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        EditPasswordWindow.setWindowIcon(icon)
        EditPasswordWindow.setStyleSheet("QWidget {\n"
    "background-color: rgb(255, 255, 255);\n"
    "}\n"
    "\n"
    ".QFrame {\n"
    "    border: 2px solid black;\n"
    "}")
        self.centralwidget = QtWidgets.QWidget(parent=EditPasswordWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(230, 450))
        self.frame.setMaximumSize(QtCore.QSize(230, 450))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(4, -1, 0, -1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_password_new = QtWidgets.QLabel(parent=self.frame)
        self.label_password_new.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_password_new.sizePolicy().hasHeightForWidth())
        self.label_password_new.setSizePolicy(sizePolicy)
        self.label_password_new.setMinimumSize(QtCore.QSize(200, 25))
        self.label_password_new.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_password_new.setFont(font)
        self.label_password_new.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_password_new.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_password_new.setObjectName("label_password_new")
        self.verticalLayout.addWidget(self.label_password_new)
        self.password_new = QtWidgets.QLineEdit(parent=self.frame)
        self.password_new.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_new.sizePolicy().hasHeightForWidth())
        self.password_new.setSizePolicy(sizePolicy)
        self.password_new.setMinimumSize(QtCore.QSize(200, 25))
        self.password_new.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_new.setFont(font)
        self.password_new.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_new.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.password_new.setObjectName("password_new")
        self.verticalLayout.addWidget(self.password_new)
        self.label_password_confirm = QtWidgets.QLabel(parent=self.frame)
        self.label_password_confirm.setMinimumSize(QtCore.QSize(200, 25))
        self.label_password_confirm.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_password_confirm.setFont(font)
        self.label_password_confirm.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_password_confirm.setObjectName("label_password_confirm")
        self.verticalLayout.addWidget(self.label_password_confirm)
        self.password_confirm = QtWidgets.QLineEdit(parent=self.frame)
        self.password_confirm.setMinimumSize(QtCore.QSize(200, 25))
        self.password_confirm.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_confirm.setFont(font)
        self.password_confirm.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhHiddenText|QtCore.Qt.InputMethodHint.ImhNoAutoUppercase|QtCore.Qt.InputMethodHint.ImhNoPredictiveText|QtCore.Qt.InputMethodHint.ImhSensitiveData)
        self.password_confirm.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_confirm.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.password_confirm.setObjectName("password_confirm")
        self.verticalLayout.addWidget(self.password_confirm)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.accept_editpassword = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accept_editpassword.sizePolicy().hasHeightForWidth())
        self.accept_editpassword.setSizePolicy(sizePolicy)
        self.accept_editpassword.setMinimumSize(QtCore.QSize(200, 30))
        self.accept_editpassword.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.accept_editpassword.setFont(font)
        self.accept_editpassword.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.accept_editpassword.setStyleSheet("QPushButton {\n"
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
        self.accept_editpassword.setObjectName("accept_editpassword")
        self.verticalLayout.addWidget(self.accept_editpassword)
        self.exit_editpassword = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_editpassword.sizePolicy().hasHeightForWidth())
        self.exit_editpassword.setSizePolicy(sizePolicy)
        self.exit_editpassword.setMinimumSize(QtCore.QSize(200, 30))
        self.exit_editpassword.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.exit_editpassword.setFont(font)
        self.exit_editpassword.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.exit_editpassword.setStyleSheet("QPushButton {\n"
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
        self.exit_editpassword.setObjectName("exit_editpassword")
        self.verticalLayout.addWidget(self.exit_editpassword)
        self.label_error = QtWidgets.QLabel(parent=self.frame)
        self.label_error.setMinimumSize(QtCore.QSize(200, 25))
        self.label_error.setMaximumSize(QtCore.QSize(200, 25))
        self.label_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_error.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_error.setWordWrap(True)
        self.label_error.setObjectName("label_error")
        self.verticalLayout.addWidget(self.label_error)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 2)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        EditPasswordWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=EditPasswordWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 270, 22))
        self.menubar.setObjectName("menubar")
        EditPasswordWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=EditPasswordWindow)
        self.statusbar.setObjectName("statusbar")
        EditPasswordWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EditPasswordWindow)
        self.accept_editpassword.clicked.connect(self.editpassword)
        self.exit_editpassword.clicked.connect(EditPasswordWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(EditPasswordWindow)


    def retranslateUi(self, EditPasswordWindow):
        _translate = QtCore.QCoreApplication.translate
        EditPasswordWindow.setWindowTitle(_translate("EditPasswordWindow", "Editar Contraseña"))
        self.label_password_new.setText(_translate("EditPasswordWindow", "Nueva Contraseña:"))
        self.label_password_confirm.setText(_translate("EditPasswordWindow", "Confirmar Contraseña"))
        self.accept_editpassword.setText(_translate("EditPasswordWindow", "Confirmar"))
        self.exit_editpassword.setText(_translate("EditPasswordWindow", "Salir"))


    def editpassword(self):
        new_password=self.password_new.text()
        confirm_password=self.password_confirm.text()

        if new_password != confirm_password:
            self.label_error.setText('Las contraseñas no coinciden')

        elif not re.fullmatch(r'[A-Za-z0-9¡!¿?%&]{8,}', new_password):
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("Contraseña no válida")
            dlg.setText("·La contraseña debe tener al menos 8 caracteres\n"
                        "·Debe contener al menos una mayúscula\n"
                        "·Debe contener al menos una minúscula\n"
                        "·Debe contener al menos un número\n"
                        "·Solo admite los siguientes caracteres especiales: ¡!¿?%&")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            dlg.exec()

        else:
        #SQL Query for updating values in database
            commands_editpassword = ("""
                        UPDATE users_data.registration
                        SET "password" = %s
                        WHERE "username" = %s
                        """)
            conn = None
            try:
            # read the connection parameters
                params = config()
            # connect to the PostgreSQL server
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
            # execution of commands one by one
                data=(new_password,self.username,)
                cur.execute(commands_editpassword,data)
            # close communication with the PostgreSQL database server
                cur.close()
            # commit the changes
                conn.commit()

            # showing success window
                dlg = QtWidgets.QMessageBox()
                new_icon = QtGui.QIcon()
                new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                dlg.setWindowIcon(new_icon)
                dlg.setWindowTitle("Editar Contraseña")
                dlg.setText("Contraseña editada con éxito")
                dlg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                dlg.exec()
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditPasswordWindow = QtWidgets.QMainWindow()
    ui = Ui_EditPasswordWindow()
    ui.setupUi(EditPasswordWindow)
    EditPasswordWindow.show()
    sys.exit(app.exec())
