# Form implementation generated from reading ui file 'EditReg_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import QtSql
from config import config
import psycopg2
from PyQt6.QtCore import Qt
import os
import configparser
from Database_Connection import createConnection

basedir = r"\\nas01\DATOS\Comunes\EIPSA-ERP"


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignmentFlag.AlignCenter


class EditableTableModel(QtSql.QSqlTableModel):
    updateFailed = QtCore.pyqtSignal(str)

    def __init__(self, parent=None, column_range=None):
        super().__init__(parent)
        self.column_range = column_range

    def setAllColumnHeaders(self, headers):
        for column, header in enumerate(headers):
            self.setHeaderData(column, Qt.Orientation.Horizontal, header, Qt.ItemDataRole.DisplayRole)

    def setIndividualColumnHeader(self, column, header):
        self.setHeaderData(column, Qt.Orientation.Horizontal, header, Qt.ItemDataRole.DisplayRole)

    def setIconColumnHeader(self, column, icon):
        self.setHeaderData(column, QtCore.Qt.Orientation.Horizontal, icon, Qt.ItemDataRole.DecorationRole)

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return super().headerData(section, orientation, role)
        return super().headerData(section, orientation, role)

    def flags(self, index):
        flags = super().flags(index)
        column_name = self.headerData(index.column(), Qt.Orientation.Horizontal)
        if column_name == "id":
            flags &= ~Qt.ItemFlag.ItemIsEditable
            return flags | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled
        else:
            return flags | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable

    def getColumnHeaders(self, visible_columns):
        column_headers = [self.headerData(col, Qt.Orientation.Horizontal) for col in visible_columns]
        return column_headers


class Ui_DBEditRegVerif_Window(QtWidgets.QMainWindow):
    def __init__(self, db, username):
        super().__init__()
        self.model = EditableTableModel()
        self.db = db
        self.username = username
        self.setupUi(self)
        self.model.dataChanged.connect(self.saveChanges)

    def closeEvent(self, event):
    # Closing database connection
        if self.model:
            self.model.clear()
        self.closeConnection()

    def closeConnection(self):
    # Closing database connection
        self.tableWidget.setModel(None)
        del self.model
        if self.db:
            self.db.close()
            del self.db
            if QtSql.QSqlDatabase.contains("qt_sql_default_connection"):
                QtSql.QSqlDatabase.removeDatabase("qt_sql_default_connection")

    def setupUi(self, EditReg_Window):
        EditReg_Window.setObjectName("EditReg_Window")
        EditReg_Window.setMinimumSize(QtCore.QSize(1000, 725))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        EditReg_Window.setWindowIcon(icon)
        if self.username == 'm.gil':
            EditReg_Window.setStyleSheet("QWidget {\n"
    "background-color: rgb(38, 38, 38); color: rgb(255, 255, 255);\n"
    "}\n"
    "\n"
    ".QFrame {\n"
    "    border: 2px solid white;\n"
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
        else:
            EditReg_Window.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=EditReg_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        # self.frame.setMinimumSize(QtCore.QSize(1000, 700))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.labelTable = QtWidgets.QLabel(parent=self.frame)
        self.labelTable.setMinimumSize(QtCore.QSize(90, 25))
        # self.labelTable.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.labelTable.setFont(font)
        self.labelTable.setObjectName("labelTable")
        self.gridLayout_2.addWidget(self.labelTable, 1, 1, 1, 2)
        self.comboBox = QtWidgets.QComboBox(parent=self.frame)
        self.comboBox.setMinimumSize(QtCore.QSize(390, 25))
        self.comboBox.setMaximumSize(QtCore.QSize(390, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 1, 3, 1, 2)
        self.label_code1 = QtWidgets.QLabel(parent=self.frame)
        self.label_code1.setMinimumSize(QtCore.QSize(150, 25))
        self.label_code1.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_code1.setFont(font)
        self.label_code1.setObjectName("label_code1")
        self.gridLayout_2.addWidget(self.label_code1, 2, 1, 1, 1)
        self.code1_DBReg = QtWidgets.QLineEdit(parent=self.frame)
        self.code1_DBReg.setMinimumSize(QtCore.QSize(150, 25))
        self.code1_DBReg.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.code1_DBReg.setFont(font)
        self.code1_DBReg.setObjectName("code1_DBReg")
        self.gridLayout_2.addWidget(self.code1_DBReg, 2, 2, 1, 1)
        self.label_code2 = QtWidgets.QLabel(parent=self.frame)
        self.label_code2.setMinimumSize(QtCore.QSize(150, 25))
        self.label_code2.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_code2.setFont(font)
        self.label_code2.setObjectName("label_code2")
        self.gridLayout_2.addWidget(self.label_code2, 2, 3, 1, 1)
        self.code2_DBReg = QtWidgets.QLineEdit(parent=self.frame)
        self.code2_DBReg.setMinimumSize(QtCore.QSize(150, 25))
        self.code2_DBReg.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.code2_DBReg.setFont(font)
        self.code2_DBReg.setObjectName("code2_DBReg")
        self.gridLayout_2.addWidget(self.code2_DBReg, 2, 4, 1, 1)
        self.label_code3 = QtWidgets.QLabel(parent=self.frame)
        self.label_code3.setMinimumSize(QtCore.QSize(150, 25))
        self.label_code3.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_code3.setFont(font)
        self.label_code3.setObjectName("label_code3")
        self.gridLayout_2.addWidget(self.label_code3, 3, 1, 1, 1)
        self.code3_DBReg = QtWidgets.QLineEdit(parent=self.frame)
        self.code3_DBReg.setMinimumSize(QtCore.QSize(150, 25))
        self.code3_DBReg.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.code3_DBReg.setFont(font)
        self.code3_DBReg.setObjectName("code3_DBReg")
        self.code3_DBReg.setVisible(False)
        self.gridLayout_2.addWidget(self.code3_DBReg, 3, 2, 1, 1)
        self.label_code4 = QtWidgets.QLabel(parent=self.frame)
        self.label_code4.setMinimumSize(QtCore.QSize(150, 25))
        self.label_code4.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_code4.setFont(font)
        self.label_code4.setObjectName("label_code4")
        self.gridLayout_2.addWidget(self.label_code4, 3, 3, 1, 1)
        self.code4_DBReg = QtWidgets.QLineEdit(parent=self.frame)
        self.code4_DBReg.setMinimumSize(QtCore.QSize(150, 25))
        self.code4_DBReg.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.code4_DBReg.setFont(font)
        self.code4_DBReg.setObjectName("code4_DBReg")
        self.code4_DBReg.setVisible(False)
        self.gridLayout_2.addWidget(self.code4_DBReg, 3, 4, 1, 1)
        self.label_code5 = QtWidgets.QLabel(parent=self.frame)
        self.label_code5.setMinimumSize(QtCore.QSize(150, 25))
        self.label_code5.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_code5.setFont(font)
        self.label_code5.setObjectName("label_code5")
        self.gridLayout_2.addWidget(self.label_code5, 4, 1, 1, 1)
        self.code5_DBReg = QtWidgets.QLineEdit(parent=self.frame)
        self.code5_DBReg.setMinimumSize(QtCore.QSize(150, 25))
        self.code5_DBReg.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.code5_DBReg.setFont(font)
        self.code5_DBReg.setObjectName("code5_DBReg")
        self.code5_DBReg.setVisible(False)
        self.gridLayout_2.addWidget(self.code5_DBReg, 4, 2, 1, 1)
        self.label_code6 = QtWidgets.QLabel(parent=self.frame)
        self.label_code6.setMinimumSize(QtCore.QSize(150, 25))
        self.label_code6.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_code6.setFont(font)
        self.label_code6.setObjectName("label_code6")
        self.gridLayout_2.addWidget(self.label_code6, 4, 3, 1, 1)
        self.code6_DBReg = QtWidgets.QLineEdit(parent=self.frame)
        self.code6_DBReg.setMinimumSize(QtCore.QSize(150, 25))
        self.code6_DBReg.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.code6_DBReg.setFont(font)
        self.code6_DBReg.setObjectName("code6_DBReg")
        self.code6_DBReg.setVisible(False)
        self.gridLayout_2.addWidget(self.code6_DBReg, 4, 4, 1, 1)
        self.label_code7 = QtWidgets.QLabel(parent=self.frame)
        self.label_code7.setMinimumSize(QtCore.QSize(150, 25))
        self.label_code7.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_code7.setFont(font)
        self.label_code7.setObjectName("label_code7")
        self.gridLayout_2.addWidget(self.label_code7, 5, 1, 1, 1)
        self.code7_DBReg = QtWidgets.QLineEdit(parent=self.frame)
        self.code7_DBReg.setMinimumSize(QtCore.QSize(150, 25))
        self.code7_DBReg.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.code7_DBReg.setFont(font)
        self.code7_DBReg.setObjectName("code7_DBReg")
        self.code7_DBReg.setVisible(False)
        self.gridLayout_2.addWidget(self.code7_DBReg, 5, 2, 1, 1)
        self.Button_Add = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Add.setMinimumSize(QtCore.QSize(150, 35))
        # self.Button_Add.setMaximumSize(QtCore.QSize(150, 35))
        self.Button_Add.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Button_Add.setStyleSheet("QPushButton {\n"
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
        self.Button_Add.setObjectName("Button_Add")
        self.gridLayout_2.addWidget(self.Button_Add, 6, 2, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 7, 1, 1, 1)
        self.model = EditableTableModel()
        self.tableWidget = QtWidgets.QTableView(parent=self.frame)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout_2.addWidget(self.tableWidget, 8, 0, 1, 7)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        EditReg_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=EditReg_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        EditReg_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=EditReg_Window)
        self.statusbar.setObjectName("statusbar")
        EditReg_Window.setStatusBar(self.statusbar)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.retranslateUi(EditReg_Window)
        self.comboBox.currentIndexChanged.connect(self.loadtable)
        self.Button_Add.clicked.connect(self.add_dbregister)
        QtCore.QMetaObject.connectSlotsByName(EditReg_Window)


        query_tablechanges = """SELECT table_name
                                FROM information_schema.tables
                                WHERE table_schema = 'verification' AND table_type = 'BASE TABLE'
                                ORDER BY table_name;"""

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

        tables_db_names = [x[0] for x in results]

        tables_names = ['Verif. Planos AL', 'Valores Fuerza Bola', 'Calibraciones', 'Albaranes', 'Verif. Planos DIM',
                        'Herramientas Taller', 'Revisiones Herramientas', 'Verif. EXP', 'Tabla 5 Dureza', 'Tabla 6 Dureza', 'Valores PT100 INTA', 'Valores TC INTA',
                        'Coladas Liq. Penetrantes', 'Verif. Planos M', 'Máquinas Taller',
                        'Revisiones Máquinas', 'Manometros', 'Patrones Calibración', 'Patrones Termoelementos',
                        'Desplegables No-Conformidad', 'Informes No-Conformidad', 'Verif. Planos OF', 'Equipos. Verif.', 'Verif. PPI',
                        'Valores PT100 Norma', 'Valores TC B Norma', 'Valores TC C Norma', 'Valores TC E Norma', 'Valores TC J Norma',
                        'Valores TC K Norma', 'Valores TC N Norma', 'Valores TC R Norma', 'Valores TC S Norma', 'Valores TC T Norma',
                        'Estados Verif.', 'Estados Almacén', 'Proveedores Albaranes', 'Pruebas Dureza', 'Pruebas Hidróstaticas',
                        'Pruebas Líquidos Penetrantes', 'Pruebas Otros', 'Tolerancias Termoelementos',
                        'Planos DIM Taller', 'Planos OF Taller']

        self.dict_tables = dict(zip(tables_db_names, tables_names))

        tables_to_delete = ['al_drawing_verification', 'calibration_thermoelements', 'delivnote_suppliers', 'dim_drawing_verification',
                            'handtools_workshop','handtools_workshop_revisions','exp_verification', 'm_drawing_verification', 'machines_workshop',
                            'machines_workshop_revisions', 'nc_comboboxes', 'nc_report', 'of_drawing_verification',
                            'ppi_verification', 'suppliers_verification', 'test_hardness', 'test_hydro',
                            'test_liquid', 'test_others', 'workshop_dim_drawings', 'workshop_of_drawings']

        for table in tables_to_delete:
            del self.dict_tables[table]

        list_tables = list(self.dict_tables.values())
        list_tables.insert(0,"")
        self.comboBox.addItems(sorted(list_tables))


    def retranslateUi(self, EditReg_Window):
        _translate = QtCore.QCoreApplication.translate
        EditReg_Window.setWindowTitle(_translate("EditReg_Window", "Editar Registros Base de Datos"))
        self.labelTable.setText(_translate("EditReg_Window", "Tabla:"))
        self.Button_Add.setText(_translate("Countries_Window", "Agregar"))


# Function to upload changes in database when field change
    def saveChanges(self):
        self.model.submitAll()

# Function to add a new register to table
    def add_dbregister(self):
        table_name = "verification." + self.comboBox.currentText()
        code1 = self.code1_DBReg.text()
        code2 = self.code2_DBReg.text()
        code3 = self.code3_DBReg.text()
        code4 = self.code4_DBReg.text()
        code5 = self.code5_DBReg.text()
        code6 = self.code6_DBReg.text()
        code7 = self.code7_DBReg.text().replace('.',',')

        columns = [self.model.headerData(col, Qt.Orientation.Horizontal) for col in range(self.columns_number)]

        if self.columns_number > 7:
            columns = columns[1:]
            values = [code1,code2,code3,code4,code5,code6,code7]
        elif self.columns_number > 3:
            if self.column_headers[0] == 'id':
                columns = columns[1:]
                values = [code1,code2,code3]
            else:
                values = [code1,code2,code3,code4]
        elif self.columns_number > 2:
            if self.column_headers[0] == 'id':
                columns = columns[1:]
                values = [code1,code2]
            else:
                values = [code1,code2,code3]
        elif self.columns_number > 1:
            if self.column_headers[0] == 'id':
                columns = columns[1:]
                values = [code1]
            else:
                values = [code1,code2]
        elif self.columns_number > 0:
            values = [code1]

        columns = ', '.join([column for column in columns])
        values = ', '.join([f"'{value}'" for value in values])

        commands_new = f" INSERT INTO {table_name} ({columns}) VALUES ({values})"
        conn = None
        try:
        # read the connection parameters
            params = config()
        # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # execution of commands
            cur.execute(commands_new)
        # close communication with the PostgreSQL database server
            cur.close()
        # commit the changes
            conn.commit()

            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("Editar Registros")
            dlg.setText("Datos insertados con éxito")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            dlg.exec()
            del dlg,new_icon

            self.code1_DBReg.setText('')
            self.code2_DBReg.setText('')
            self.code3_DBReg.setText('')
            self.code4_DBReg.setText('')
            self.code5_DBReg.setText('')
            self.code6_DBReg.setText('')
            self.code7_DBReg.setText('')

            self.loadtable()

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

# Function to load table after selection on checkbox
    def loadtable(self):
        value_table = self.comboBox.currentText()

        if value_table != '':
            table_name = "verification." + self.get_key_from_value(self.dict_tables, value_table)


            self.model.setTable(table_name)
            self.model.setSort(0, QtCore.Qt.SortOrder.AscendingOrder)
            self.model.select()
            self.tableWidget.setModel(self.model)

            self.tableWidget.verticalHeader().hide()
            self.tableWidget.setItemDelegate(AlignDelegate(self.tableWidget))
            self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            if self.username == 'm.gil':
                self.tableWidget.setStyleSheet("gridline-color: rgb(128, 128, 128);")
                self.tableWidget.horizontalHeader().setStyleSheet("::section{font: 800 10pt; background-color: #33bdef; border: 1px solid white;}")
                self.tableWidget.verticalHeader().setStyleSheet("::section{font: 10pt; background-color: #121212; border: 0.5px solid white;}")
            else:
                self.tableWidget.horizontalHeader().setStyleSheet("::section{font: 800 10pt; background-color: #33bdef; border: 1px solid black;}")
            self.tableWidget.setObjectName("tableWidget")
            self.gridLayout_2.addWidget(self.tableWidget, 8, 0, 1, 6)
            self.model.dataChanged.connect(self.saveChanges)

            self.columns_number = self.model.columnCount()
            self.column_headers = [self.model.headerData(col, Qt.Orientation.Horizontal) for col in range(self.columns_number)]

            if self.columns_number > 4:
                if self.column_headers[0] == 'id':
                    self.label_code1.setText(self.column_headers[1])
                    self.label_code2.setText(self.column_headers[2])
                    self.label_code3.setText(self.column_headers[3])
                    self.label_code4.setText(self.column_headers[4])
                    self.code2_DBReg.setText('')
                    self.code2_DBReg.setVisible(True)
                    self.code3_DBReg.setText('')
                    self.code3_DBReg.setVisible(True)
                    self.code4_DBReg.setText('')
                    self.code4_DBReg.setVisible(True)
                    self.code5_DBReg.setText('')
                    self.code5_DBReg.setVisible(False)
                else:
                    self.label_code1.setText(self.column_headers[0])
                    self.label_code2.setText(self.column_headers[1])
                    self.label_code3.setText(self.column_headers[2])
                    self.label_code4.setText(self.column_headers[3])
                    self.code2_DBReg.setVisible(True)
                    self.code2_DBReg.setText('')
                    self.code2_DBReg.setEnabled(True)
                    self.code3_DBReg.setVisible(True)
                    self.code3_DBReg.setText('')
                    self.code3_DBReg.setEnabled(True)
                    self.code4_DBReg.setVisible(True)
                    self.code4_DBReg.setText('')
                    self.code4_DBReg.setEnabled(True)
                    self.code5_DBReg.setVisible(True)
                    self.code5_DBReg.setText('')
                    self.code5_DBReg.setEnabled(True)
                self.label_code6.setText('')
                self.code6_DBReg.setText('')
                self.code6_DBReg.setVisible(False)
                self.label_code7.setText('')
                self.code7_DBReg.setText('')
                self.code7_DBReg.setVisible(False)

            elif self.columns_number > 3:
                if self.column_headers[0] == 'id':
                    self.label_code1.setText(self.column_headers[1])
                    self.label_code2.setText(self.column_headers[2])
                    self.label_code3.setText(self.column_headers[3])
                    self.label_code4.setText('')
                    self.code2_DBReg.setText('')
                    self.code2_DBReg.setVisible(True)
                    self.code3_DBReg.setText('')
                    self.code3_DBReg.setVisible(True)
                    self.code4_DBReg.setText('')
                    self.code4_DBReg.setVisible(False)
                else:
                    self.label_code1.setText(self.column_headers[0])
                    self.label_code2.setText(self.column_headers[1])
                    self.label_code3.setText(self.column_headers[2])
                    self.label_code4.setText(self.column_headers[3])
                    self.code2_DBReg.setVisible(True)
                    self.code2_DBReg.setText('')
                    self.code2_DBReg.setEnabled(True)
                    self.code3_DBReg.setVisible(True)
                    self.code3_DBReg.setText('')
                    self.code3_DBReg.setEnabled(True)
                    self.code4_DBReg.setVisible(True)
                    self.code4_DBReg.setText('')
                    self.code4_DBReg.setEnabled(True)
                self.label_code5.setText('')
                self.code5_DBReg.setText('')
                self.code5_DBReg.setVisible(False)
                self.label_code6.setText('')
                self.code6_DBReg.setText('')
                self.code6_DBReg.setVisible(False)
                self.label_code7.setText('')
                self.code7_DBReg.setText('')
                self.code7_DBReg.setVisible(False)

            elif self.columns_number > 2:
                if self.column_headers[0] == 'id':
                    self.label_code1.setText(self.column_headers[1])
                    self.label_code2.setText(self.column_headers[2])
                    self.code2_DBReg.setText('')
                    self.code2_DBReg.setVisible(True)
                    self.code3_DBReg.setText('')
                    self.code3_DBReg.setVisible(False)
                else:
                    self.label_code1.setText(self.column_headers[0])
                    self.label_code2.setText(self.column_headers[1])
                    self.label_code3.setText(self.column_headers[2])
                    self.code3_DBReg.setVisible(True)
                    self.code3_DBReg.setText('')
                self.label_code4.setText('')
                self.code4_DBReg.setVisible(False)
                self.code4_DBReg.setText('')
                self.label_code5.setText('')
                self.code5_DBReg.setVisible(False)
                self.code5_DBReg.setText('')
                self.label_code6.setText('')
                self.code6_DBReg.setVisible(False)
                self.code6_DBReg.setText('')
                self.label_code7.setText('')
                self.code7_DBReg.setVisible(False)
                self.code7_DBReg.setText('')

            elif self.columns_number > 1:
                if self.column_headers[0] == 'id':
                    self.label_code1.setText(self.column_headers[1])
                    self.label_code2.setText('')
                    self.code2_DBReg.setVisible(False)
                    self.code2_DBReg.setText('')
                else:
                    self.label_code1.setText(self.column_headers[0])
                    self.label_code2.setText(self.column_headers[1])
                    self.code2_DBReg.setVisible(True)
                    self.code2_DBReg.setText('')
                    self.code2_DBReg.setEnabled(True)
                self.label_code3.setText('')
                self.code3_DBReg.setVisible(False)
                self.code3_DBReg.setText('')
                self.label_code4.setText('')
                self.code4_DBReg.setVisible(False)
                self.code4_DBReg.setText('')
                self.label_code5.setText('')
                self.code5_DBReg.setVisible(False)
                self.code5_DBReg.setText('')
                self.label_code6.setText('')
                self.code6_DBReg.setVisible(False)
                self.code6_DBReg.setText('')
                self.label_code7.setText('')
                self.code7_DBReg.setVisible(False)
                self.code7_DBReg.setText('')

            elif self.columns_number > 0:
                self.label_code1.setText(self.column_headers[0])
                self.label_code2.setText('')
                self.code2_DBReg.setVisible(False)
                self.code2_DBReg.setText('')
                self.label_code3.setText('')
                self.code3_DBReg.setVisible(False)
                self.code3_DBReg.setText('')
                self.label_code4.setText('')
                self.code4_DBReg.setVisible(False)
                self.code4_DBReg.setText('')
                self.label_code5.setText('')
                self.code5_DBReg.setVisible(False)
                self.code5_DBReg.setText('')
                self.label_code6.setText('')
                self.code6_DBReg.setVisible(False)
                self.code6_DBReg.setText('')
                self.label_code7.setText('')
                self.code7_DBReg.setVisible(False)
                self.code7_DBReg.setText('')


    def get_key_from_value(self, dictionary, value):
        return next((k for k, v in dictionary.items() if v == value), None)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    config_obj = configparser.ConfigParser()
    config_obj.read(r"C:\Program Files\ERP EIPSA\database.ini")
    dbparam = config_obj["postgresql"]
    # set your parameters for the database connection URI using the keys from the configfile.ini
    user_database = dbparam["user"]
    password_database = dbparam["password"]

    db_validation = createConnection(user_database, password_database)
    if not db_validation:
        sys.exit()


    EditReg_Window = Ui_DBEditRegVerif_Window(db_validation, 'm.gil')
    EditReg_Window.show()
    sys.exit(app.exec())