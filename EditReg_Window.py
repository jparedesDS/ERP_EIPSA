# Form implementation generated from reading ui file 'EditReg_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import QtSql
from config import config
import re
import psycopg2
import configparser
from Database_Connection import createConnection
from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlQuery


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignmentFlag.AlignCenter


class CustomProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._filters = dict()
        self.header_names = {}


    @property
    def filters(self):
        return self._filters


    def setFilter(self, expresion, column):
        if expresion:
            self.filters[column] = expresion
        elif column in self.filters:
            del self.filters[column]
        self.invalidateFilter()


    def filterAcceptsRow(self, source_row, source_parent):
        for column, expresion in self.filters.items():
            text = self.sourceModel().index(source_row, column, source_parent).data()

            if isinstance(text, QtCore.QDate): #Check if filters are QDate. If True, convert to text
                text = text.toString("yyyy-MM-dd")

            if re.fullmatch(r'^(?:3[01]|[12][0-9]|0?[1-9])([\-/.])(0?[1-9]|1[1-2])\1\d{4}$', expresion): #Check date format from selected filter and convert if necessary
                expresion = QtCore.QDate.fromString(expresion,"dd/MM/yyyy")
                expresion = expresion.toString("yyyy-MM-dd")
            else:
                pass

            regex = QtCore.QRegularExpression(f".*{re.escape(expresion)}.*", QtCore.QRegularExpression.PatternOption.CaseInsensitiveOption)
            if not regex.match(text).hasMatch():
                return False
        return True


class EditableTableModel(QtSql.QSqlTableModel):
    updateFailed = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.originalData = {}
        self.relations={}


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
        return flags | QtCore.Qt.ItemFlag.ItemIsEditable


    def setOriginalData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if index.isValid() and role == Qt.ItemDataRole.EditRole:
            column = index.column()
            if column not in self.originalData:
                self.originalData[column] = self.data(index) # Saving the original data before edition
        return super().setData(index, value, role)


    def getOriginalValue(self, index):
        row = index.row()
        column = index.column()
        return self.originalData.get(column)


    def setChanges(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole:
            column = index.column()
            self.modifiedCells.append((index.row(), column, value))  # Saving changes in list
        return super().setChanges(index, value, role)


    def update_record(self, record, index):
        query = QSqlQuery(self.database())
        primary_key = self.primaryKey()
        id_column = primary_key.fieldName(0)

        column_index = index.column() # Obtaining modified column index from modified cell index
        column_name = self.record().fieldName(column_index) # Obtaining modified column name
        new_value = index.data(Qt.ItemDataRole.EditRole) #Obtaining new value
        old_value = self.originalData.get(column_index, "") # Obtaining old value

        # Verify if values are NULL
        if new_value is None:
            new_value = ""
        if old_value is None:
            old_value = ""

        query.prepare(f"UPDATE {self.tableName()} SET {column_name} = :newValue WHERE {id_column} = :id")
        query.bindValue(":newValue", new_value)
        query.bindValue(":id", record.value(id_column))

        query.exec()
        query_text = query.executedQuery()
        # print("SQL Query:", query_text)

        if query.lastError().isValid():
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Recursos/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("Editar Documentos")
            dlg.setText("Ha habido un error al actualizar los datos. No serán guardados")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            dlg.exec()

            print("Error en la consulta:", query.lastError().nativeErrorCode())
            print("Mensaje de error:", query.lastError().text())
            return None
        else:
            return query_text


class Ui_EditReg_Window(object):
    def __init__(self):
        self.model = EditableTableModel()
        self.proxy = CustomProxyModel()

    def setupUi(self, EditReg_Window):
        EditReg_Window.setObjectName("EditReg_Window")
        EditReg_Window.resize(400, 561)
        EditReg_Window.setMinimumSize(QtCore.QSize(400, 525))
        EditReg_Window.setMaximumSize(QtCore.QSize(400, 561))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Recursos/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        EditReg_Window.setWindowIcon(icon)
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
        self.frame.setMinimumSize(QtCore.QSize(350, 500))
        self.frame.setMaximumSize(QtCore.QSize(350, 500))
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
        # spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        # self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        # self.hLayout2 = QtWidgets.QHBoxLayout()
        # self.hLayout2.setObjectName("hLayout3")
        # self.Button_EditReg = QtWidgets.QPushButton(parent=self.frame)
        # self.Button_EditReg.setMinimumSize(QtCore.QSize(100, 35))
        # self.Button_EditReg.setMaximumSize(QtCore.QSize(100, 35))
        # self.Button_EditReg.setObjectName("Button_EditReg")
        # self.hLayout2.addWidget(self.Button_EditReg)
        # spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        # self.hLayout2.addItem(spacerItem3)
        # self.Button_Cancel = QtWidgets.QPushButton(parent=self.frame)
        # self.Button_Cancel.setMinimumSize(QtCore.QSize(100, 35))
        # self.Button_Cancel.setMaximumSize(QtCore.QSize(100, 35))
        # self.Button_Cancel.setObjectName("Button_Cancel")
        # self.hLayout2.addWidget(self.Button_Cancel)
        # self.gridLayout_2.addLayout(self.hLayout2, 4, 0, 1, 1)

        self.model = EditableTableModel()
        self.model.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnFieldChange)
        self.model.select()
        self.proxy.setSourceModel(self.model)

        self.tableWidget = QtWidgets.QTableView(parent=self.frame)
        self.tableWidget.setModel(self.proxy)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout_2.addWidget(self.tableWidget, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        EditReg_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=EditReg_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        EditReg_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=EditReg_Window)
        self.statusbar.setObjectName("statusbar")
        EditReg_Window.setStatusBar(self.statusbar)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.retranslateUi(EditReg_Window)
        # self.Button_Cancel.clicked.connect(EditReg_Window.close) # type: ignore
        # self.Button_EditReg.clicked.connect(self.EditReg) 
        self.comboBox.currentIndexChanged.connect(self.loadtable)
        QtCore.QMetaObject.connectSlotsByName(EditReg_Window)


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

        self.model.dataChanged.connect(self.saveChanges)


    def retranslateUi(self, EditReg_Window):
        _translate = QtCore.QCoreApplication.translate
        EditReg_Window.setWindowTitle(_translate("EditReg_Window", "Editar Registros Base de Datos"))
        self.labelTable.setText(_translate("EditReg_Window", "Tabla:"))
        # self.Button_EditReg.setText(_translate("EditReg_Window", "Guardar"))
        # self.Button_Cancel.setText(_translate("EditReg_Window", "Cancelar"))


# Function to upload changes in database when field change
    def saveChanges(self):
        self.model.submitAll()

    # def EditReg(self):
    #     columns_number=self.model.columnCount()
    #     if self.model.database().isOpen():
    #         self.model.database().transaction()
    #         success = True

    #         for index in range(columns_number):
    #             self.proxy.setFilter("", index)
    #             self.model.setIconColumnHeader(index, '')

    #         for row in range(self.model.rowCount()):
    #             for column in range(self.model.columnCount()):
    #                 index = self.model.index(row, column)
    #                 current_value = index.data(Qt.ItemDataRole.DisplayRole)
    #                 original_value = self.model.getOriginalValue(index)
    #                 if current_value != original_value:
    #                     record = self.model.record(row)
    #                     query = self.model.update_record(record, index)
    #                     if not query:
    #                         success = False
    #                         break

    #         if success:
    #             self.model.database().commit()
    #             dlg = QtWidgets.QMessageBox()
    #             new_icon = QtGui.QIcon()
    #             new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Recursos/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    #             dlg.setWindowIcon(new_icon)
    #             dlg.setWindowTitle("Editar Documentos")
    #             dlg.setText("Datos guardados con éxito")
    #             dlg.setIcon(QtWidgets.QMessageBox.Icon.Information)
    #             dlg.exec()
    #         else:
    #             self.model.database().rollback()
    #             dlg = QtWidgets.QMessageBox()
    #             new_icon = QtGui.QIcon()
    #             new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Recursos/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    #             dlg.setWindowIcon(new_icon)
    #             dlg.setWindowTitle("Editar Documentos")
    #             dlg.setText("Ha habido un problema al guardar los datos")
    #             dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
    #             dlg.exec()


    def loadtable(self):
        table_name = "validation_data." + self.comboBox.currentText()

        self.model.setTable(table_name)
        self.model.select()
        self.model.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnFieldChange)

        self.proxy.setSourceModel(self.model)
        self.tableWidget.setModel(self.proxy)

        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setItemDelegate(AlignDelegate(self.tableWidget))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setStyleSheet("::section{font: 800 10pt; background-color: #33bdef; border: 1px solid black;}")
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout_2.addWidget(self.tableWidget, 5, 0, 1, 1)
        self.tableWidget.setSortingEnabled(False)

        for row in range(self.model.rowCount()):
            for column in range(self.model.columnCount()):
                index = self.model.index(row, column)
                self.model.setOriginalData(index, self.model.data(index))

        self.model.dataChanged.connect(self.saveChanges)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    config_obj = configparser.ConfigParser()
    config_obj.read(r"C:\Program Files\ERP EIPSA\database.ini")
    dbparam = config_obj["postgresql"]
    # set your parameters for the database connection URI using the keys from the configfile.ini
    user_database = dbparam["user"]
    password_database = dbparam["password"]

    if not createConnection(user_database, password_database):
        sys.exit()
    EditReg_Window = QtWidgets.QMainWindow()
    ui = Ui_EditReg_Window()
    ui.setupUi(EditReg_Window)
    EditReg_Window.show()
    sys.exit(app.exec())