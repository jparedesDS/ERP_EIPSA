# Form implementation generated from reading ui file 'Setup_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import os
import ctypes
import sys
import psycopg2
import os

basedir = r"\\nas01\DATOS\Comunes\EIPSA-ERP"


class Ui_SetupWindow(object):
    def setupUi(self, SetupWindow):
        SetupWindow.setObjectName("SetupWindow")
        SetupWindow.resize(270, 365)
        SetupWindow.setMinimumSize(QtCore.QSize(270, 490))
        SetupWindow.setMaximumSize(QtCore.QSize(270, 490))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        SetupWindow.setWindowIcon(icon)
        SetupWindow.setStyleSheet("QWidget {\n"
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
"  padding: 0px .8em;\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=SetupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(230, 425))
        self.frame.setMaximumSize(QtCore.QSize(230, 425))
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
        self.labelText = QtWidgets.QLabel(self.frame)
        self.labelText.setObjectName("labelText")
        self.labelText.setMinimumSize(QtCore.QSize(0, 50))
        self.labelText.setMaximumSize(QtCore.QSize(16777215, 50))
        self.labelText.setWordWrap(True)
        self.verticalLayout.addWidget(self.labelText)
        self.label_username_regdb = QtWidgets.QLabel(parent=self.frame)
        self.label_username_regdb.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_username_regdb.sizePolicy().hasHeightForWidth())
        self.label_username_regdb.setSizePolicy(sizePolicy)
        self.label_username_regdb.setMinimumSize(QtCore.QSize(200, 25))
        self.label_username_regdb.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_username_regdb.setFont(font)
        self.label_username_regdb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_username_regdb.setObjectName("label_username_regdb")
        self.verticalLayout.addWidget(self.label_username_regdb)
        self.username_regdb = QtWidgets.QLineEdit(parent=self.frame)
        self.username_regdb.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_regdb.sizePolicy().hasHeightForWidth())
        self.username_regdb.setSizePolicy(sizePolicy)
        self.username_regdb.setMinimumSize(QtCore.QSize(200, 25))
        self.username_regdb.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_regdb.setFont(font)
        self.username_regdb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.username_regdb.setObjectName("username_regdb")
        self.verticalLayout.addWidget(self.username_regdb)
        self.label_password_regdb = QtWidgets.QLabel(parent=self.frame)
        self.label_password_regdb.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_password_regdb.sizePolicy().hasHeightForWidth())
        self.label_password_regdb.setSizePolicy(sizePolicy)
        self.label_password_regdb.setMinimumSize(QtCore.QSize(200, 25))
        self.label_password_regdb.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_password_regdb.setFont(font)
        self.label_password_regdb.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_password_regdb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_password_regdb.setObjectName("label_password_regdb")
        self.verticalLayout.addWidget(self.label_password_regdb)
        self.password_regdb = QtWidgets.QLineEdit(parent=self.frame)
        self.password_regdb.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_regdb.sizePolicy().hasHeightForWidth())
        self.password_regdb.setSizePolicy(sizePolicy)
        self.password_regdb.setMinimumSize(QtCore.QSize(200, 25))
        self.password_regdb.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_regdb.setFont(font)
        self.password_regdb.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_regdb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.password_regdb.setObjectName("password_regdb")
        self.verticalLayout.addWidget(self.password_regdb)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.accept_regdb = QtWidgets.QPushButton(parent=self.frame)
        self.accept_regdb.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accept_regdb.sizePolicy().hasHeightForWidth())
        self.accept_regdb.setSizePolicy(sizePolicy)
        self.accept_regdb.setMinimumSize(QtCore.QSize(200, 30))
        self.accept_regdb.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("-apple-system")
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.accept_regdb.setFont(font)
        self.accept_regdb.setStyleSheet("QPushButton:focus{\n"
"background-color: #019ad2;\n"
"border-color: rgb(0, 0, 0);\n"
"}")
        self.accept_regdb.setAutoDefault(True)
        self.accept_regdb.setObjectName("accept_regdb")
        self.verticalLayout.addWidget(self.accept_regdb)
        self.exit_regdb = QtWidgets.QPushButton(parent=self.frame)
        self.exit_regdb.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_regdb.sizePolicy().hasHeightForWidth())
        self.exit_regdb.setSizePolicy(sizePolicy)
        self.exit_regdb.setMinimumSize(QtCore.QSize(200, 30))
        self.exit_regdb.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("-apple-system")
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.exit_regdb.setFont(font)
        self.exit_regdb.setStyleSheet("QPushButton:focus{\n"
"background-color: #019ad2;\n"
"border-color: rgb(0, 0, 0);\n"
"}")
        self.exit_regdb.setAutoDefault(True)
        self.exit_regdb.setObjectName("exit_regdb")
        self.verticalLayout.addWidget(self.exit_regdb)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 2)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        SetupWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=SetupWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 270, 22))
        self.menubar.setObjectName("menubar")
        SetupWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=SetupWindow)
        self.statusbar.setObjectName("statusbar")
        SetupWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SetupWindow)
        self.accept_regdb.clicked.connect(self.setup)
        self.exit_regdb.clicked.connect(SetupWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SetupWindow)


    def retranslateUi(self, SetupWindow):
        _translate = QtCore.QCoreApplication.translate
        SetupWindow.setWindowTitle(_translate("SetupWindow", "Instalación"))
        self.labelText.setText(_translate("SetupWindow", "Introduce el usuario proporcionado por el administrador y una contraseña para la instalación."))
        self.label_username_regdb.setText(_translate("SetupWindow", "Nombre de Usuario:"))
        self.label_password_regdb.setText(_translate("SetupWindow", "Contraseña:"))
        self.accept_regdb.setText(_translate("SetupWindow", "Registrar"))
        self.exit_regdb.setText(_translate("SetupWindow", "Salir"))


    def setup(self):
        username=self.username_regdb.text()
        password=self.password_regdb.text()
    # Execute the function to create the .ini file
        if not is_admin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            sys.exit()
        self.create_ini_file(username, password)


    def create_ini_file(self, username, password):
        # Obtaining the full path to set the file
        base_dir = r"C:\Program Files\ERP EIPSA"

        # Full path of .ini file
        ini_file_path = os.path.abspath(os.path.join(base_dir, "database.ini")

        # Check if path exists. If not, create it
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

        if os.path.exists(ini_file_path):
            try:
                os.remove(ini_file_path)
            except Exception as e:
                print(f'Error : {e}')

        # Create the content of .ini file
        ini_content = "[postgresql]\n"
        ini_content += "host = 10.1.20.252\n"
        ini_content += "database = ERP_EIPSA\n"
        ini_content += f"user = {username}\n"
        ini_content += f"password = {password}\n"

        # Create the .ini file
        with open(ini_file_path, 'w') as ini_file:
            ini_file.write(ini_content)

        # Setting the file as hidden
        try:
            # Getting file attributes
            file_attributes = ctypes.windll.kernel32.GetFileAttributesW(ini_file_path)

            # Setting the "hidden" attribute
            ctypes.windll.kernel32.SetFileAttributesW(ini_file_path, file_attributes + 2)

            params = {
            "host": '10.1.20.252',
            "port": 5432,
            "database": 'ERP_EIPSA',
            "user": 'postgres',
            "password": 'EIPS@0545$@!'
            }
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

            command_create_user = f"CREATE USER \"{username}\" WITH PASSWORD '{password}'"

            commands_privileges = """
                                DO
                                $$
                                DECLARE
                                    schema_name TEXT;
                                BEGIN
                                    FOR schema_name IN (SELECT nspname FROM pg_catalog.pg_namespace)
                                    LOOP
                                        EXECUTE format('GRANT INSERT, SELECT, UPDATE, DELETE ON ALL TABLES IN SCHEMA %I TO "{}";', schema_name);
                                        EXECUTE format('GRANT TRUNCATE ON ALL TABLES IN SCHEMA %I TO "{}";', schema_name);
                                        EXECUTE format('GRANT REFERENCES ON ALL TABLES IN SCHEMA %I TO "{}";', schema_name);
                                        EXECUTE format('GRANT TRIGGER ON ALL TABLES IN SCHEMA %I TO "{}";', schema_name);
                                        EXECUTE format('GRANT USAGE, SELECT, UPDATE ON ALL SEQUENCES IN SCHEMA %I TO "{}";', schema_name);
                                    END LOOP;
                                END;
                                $$;
                                """.format(username, username, username, username, username, username, username, username, username, username)

            commands_superuser=f"ALTER ROLE \"{username}\" WITH SUPERUSER"

            command_database_update =("""INSERT INTO users_data.database_passwords ("username","password")
                            VALUES (%s,%s)""") 

            # Create user
            cur.execute(command_create_user)

            # Grant privileges
            cur.execute(commands_privileges)

            # Superuser privileges
            cur.execute(commands_superuser)

            cur.execute(command_database_update,(username,password,))
            conn.commit()

            # Close connection
            cur.close()
            conn.close()

            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("ERP EIPSA")
            dlg.setText("Instalación completada con éxito")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            dlg.exec()
            del dlg, new_icon

            sys.exit(app.exec())

        except Exception as e:
            print(f"Error: {str(e)}")


#Function to execute the script as admin
def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False


if __name__ == "__main__":
    import sys
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

    app = QtWidgets.QApplication(sys.argv)
    SetupWindow = QtWidgets.QMainWindow()
    ui = Ui_SetupWindow()
    ui.setupUi(SetupWindow)
    SetupWindow.show()
    sys.exit(app.exec())
