# Form implementation generated from reading ui file 'AddReg_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from config import config
import psycopg2
import os

basedir = os.path.dirname(__file__)


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignmentFlag.AlignCenter


class Ui_AddReg_Window(object):
    def setupUi(self, AddReg_Window):
        AddReg_Window.setObjectName("AddReg_Window")
        AddReg_Window.resize(400, 561)
        AddReg_Window.setMinimumSize(QtCore.QSize(600, 775))
        # AddReg_Window.setMaximumSize(QtCore.QSize(400, 575))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(basedir, "Resources/Iconos/icon.ico")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        AddReg_Window.setWindowIcon(icon)
        AddReg_Window.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=AddReg_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(550, 700))
        # self.frame.setMaximumSize(QtCore.QSize(350, 500))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.hLayout1 = QtWidgets.QHBoxLayout()
        self.hLayout1.setObjectName("hLayout1")
        self.labelTable = QtWidgets.QLabel(parent=self.frame)
        self.labelTable.setMinimumSize(QtCore.QSize(90, 25))
        self.labelTable.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.labelTable.setFont(font)
        self.labelTable.setObjectName("labelTable")
        self.hLayout1.addWidget(self.labelTable)
        self.comboBox = QtWidgets.QComboBox(parent=self.frame)
        self.comboBox.setMinimumSize(QtCore.QSize(225, 25))
        self.comboBox.setMaximumSize(QtCore.QSize(225, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.hLayout1.addWidget(self.comboBox)
        self.gridLayout_2.addLayout(self.hLayout1, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.hLayout2 = QtWidgets.QHBoxLayout()
        self.hLayout2.setObjectName("hLayout2")
        self.labelValue = QtWidgets.QLabel(parent=self.frame)
        self.labelValue.setMinimumSize(QtCore.QSize(90, 25))
        self.labelValue.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.labelValue.setFont(font)
        self.labelValue.setObjectName("labelValue")
        self.hLayout2.addWidget(self.labelValue)
        self.lineEdit_value = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_value.setMinimumSize(QtCore.QSize(225, 25))
        self.lineEdit_value.setMaximumSize(QtCore.QSize(225, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_value.setFont(font)
        self.lineEdit_value.setObjectName("lineEdit_value")
        self.hLayout2.addWidget(self.lineEdit_value)
        self.gridLayout_2.addLayout(self.hLayout2, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        self.hLayout3 = QtWidgets.QHBoxLayout()
        self.hLayout3.setObjectName("hLayout2")
        self.labelCode = QtWidgets.QLabel(parent=self.frame)
        self.labelCode.setMinimumSize(QtCore.QSize(90, 25))
        self.labelCode.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.labelCode.setFont(font)
        self.labelCode.setObjectName("labelCode")
        self.hLayout3.addWidget(self.labelCode)
        self.lineEdit_code = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_code.setMinimumSize(QtCore.QSize(225, 25))
        self.lineEdit_code.setMaximumSize(QtCore.QSize(225, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_code.setFont(font)
        self.lineEdit_code.setObjectName("lineEdit_code")
        self.hLayout3.addWidget(self.lineEdit_code)
        self.gridLayout_2.addLayout(self.hLayout3, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 6, 0, 1, 1)
        self.hLayout4 = QtWidgets.QHBoxLayout()
        self.hLayout4.setObjectName("hLayout3")
        self.Button_AddReg = QtWidgets.QPushButton(parent=self.frame)
        self.Button_AddReg.setMinimumSize(QtCore.QSize(100, 35))
        self.Button_AddReg.setMaximumSize(QtCore.QSize(100, 35))
        self.Button_AddReg.setObjectName("Button_AddReg")
        self.hLayout4.addWidget(self.Button_AddReg)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hLayout4.addItem(spacerItem3)
        self.Button_Cancel = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Cancel.setMinimumSize(QtCore.QSize(100, 35))
        self.Button_Cancel.setMaximumSize(QtCore.QSize(100, 35))
        self.Button_Cancel.setObjectName("Button_Cancel")
        self.hLayout4.addWidget(self.Button_Cancel)
        self.gridLayout_2.addLayout(self.hLayout4, 7, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 8, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout_2.addWidget(self.tableWidget, 9, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        AddReg_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=AddReg_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        AddReg_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=AddReg_Window)
        self.statusbar.setObjectName("statusbar")
        AddReg_Window.setStatusBar(self.statusbar)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section {background-color: #33bdef; border: 1px solid black;}")

        self.retranslateUi(AddReg_Window)
        self.Button_Cancel.clicked.connect(AddReg_Window.close) # type: ignore
        self.Button_AddReg.clicked.connect(self.addreg) 
        self.comboBox.currentIndexChanged.connect(self.loadtable)
        QtCore.QMetaObject.connectSlotsByName(AddReg_Window)


        query_tablechanges = """SELECT table_name
                                FROM information_schema.tables
                                WHERE table_schema = 'validation_data' AND table_type = 'BASE TABLE';"""

        conn = None
        try:
        # read the connection parameters
            params = config()
        # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # execution of commands one by one
            cur.execute(query_tablechanges)
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

        tables_names=[x[0] for x in results]
        tables_names.sort()
        tables_names.insert(0,"")
        self.comboBox.addItems(tables_names)


    def retranslateUi(self, AddReg_Window):
        _translate = QtCore.QCoreApplication.translate
        AddReg_Window.setWindowTitle(_translate("AddReg_Window", "Agregar Registro Base de Datos"))
        self.labelValue.setText(_translate("AddReg_Window", "Valor Nuevo:"))
        self.labelCode.setText(_translate("AddReg_Window", "Cód. Nuevo:"))
        self.labelTable.setText(_translate("AddReg_Window", "Tabla:"))
        self.Button_AddReg.setText(_translate("AddReg_Window", "Agregar"))
        self.Button_Cancel.setText(_translate("AddReg_Window", "Cancelar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AddReg_Window", "Valor"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AddReg_Window", "Código"))


    def addreg(self):
        table_name = "validation_data." + self.comboBox.currentText()
        value_reg=self.lineEdit_value.text()
        code_reg=self.lineEdit_code.text()

        if table_name == "" or value_reg == "":
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.join(basedir, "Resources/Iconos/icon.ico")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("ERP EIPSA")
            dlg.setText("Los campos deben estar rellenos")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            dlg.exec()
            del dlg, new_icon

        else:
            commands_addreg = f"INSERT INTO {table_name} VALUES (default, '{value_reg}', '{code_reg})"
            commands_loadtableaddreg = f"SELECT * FROM validation_data.{table_name} ORDER BY 1"
            conn = None
            try:
            # read the connection parameters
                params = config()
            # connect to the PostgreSQL server
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
            # execution of commands one by one
                cur.execute(commands_addreg)
                cur.execute(commands_loadtableaddreg)
                results=cur.fetchall()
            # close communication with the PostgreSQL database server
                cur.close()
            # commit the changes
                conn.commit()

                self.tableWidget.setRowCount(len(results))
                tablerow=0

            # fill the Qt Table with the query results
                for row in results:
                    for column in range(3):
                        value = row[column]
                        if value is None:
                            value = ''
                        it = QtWidgets.QTableWidgetItem(str(value))
                        it.setFlags(it.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                        self.tableWidget.setItem(tablerow, column, it)

                    tablerow+=1

                self.tableWidget.verticalHeader().hide()
                self.tableWidget.setItemDelegate(AlignDelegate(self.tableWidget))

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()


    def loadtable(self):
        table_name = self.comboBox.currentText()

        if table_name != "":
            commands_loadtableaddreg = f"SELECT * FROM validation_data.{table_name} ORDER BY 1"
            conn = None
            try:
            # read the connection parameters
                params = config()
            # connect to the PostgreSQL server
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
            # execution of commands one by one
                cur.execute(commands_loadtableaddreg)
                results=cur.fetchall()
            # close communication with the PostgreSQL database server
                cur.close()
            # commit the changes
                conn.commit()

                self.tableWidget.setRowCount(len(results))
                tablerow=0
            # fill the Qt Table with the query results
                for row in results:
                    for column in range(2):
                        value = row[column]
                        if value is None:
                            value = ''
                        it = QtWidgets.QTableWidgetItem(str(value))
                        it.setFlags(it.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                        self.tableWidget.setItem(tablerow, column, it)

                    tablerow+=1

                self.tableWidget.verticalHeader().hide()
                self.tableWidget.setItemDelegate(AlignDelegate(self.tableWidget))
            
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddReg_Window = QtWidgets.QMainWindow()
    ui = Ui_AddReg_Window()
    ui.setupUi(AddReg_Window)
    AddReg_Window.show()
    sys.exit(app.exec())