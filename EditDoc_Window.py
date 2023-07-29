# Form implementation generated from reading ui file 'EditDocs_Commercial_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import QtSql
import re
import configparser
from Database_Connection import createConnection
from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlQuery


def imagen_to_base64(imagen):
    buffer = QtCore.QBuffer()
    buffer.open(QtCore.QIODevice.OpenModeFlag.WriteOnly)
    imagen.save(buffer, "PNG")
    base64_data = buffer.data().toBase64().data().decode()
    return base64_data


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
            new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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


class Ui_EditDoc_Window(object):
    def __init__(self):
        self.model = EditableTableModel()
        self.proxy = CustomProxyModel()

    def setupUi(self, EditDocs_Window):
        EditDocs_Window.setObjectName("EditDocs_Window")
        EditDocs_Window.resize(790, 595)
        EditDocs_Window.setMinimumSize(QtCore.QSize(900, 595))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        EditDocs_Window.setWindowIcon(icon)
        EditDocs_Window.setStyleSheet(
".QFrame {\n"
"    border: 2px solid black;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=EditDocs_Window)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.hcab=QtWidgets.QHBoxLayout()
        self.hcab.setObjectName("hcab")
        self.toolSave = QtWidgets.QToolButton(self.frame)
        self.toolSave.setObjectName("Save_Button")
        self.hcab.addWidget(self.toolSave)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Iconos/Save.png"),QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolSave.setIcon(icon)
        self.hcabspacer1=QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hcab.addItem(self.hcabspacer1)
        self.toolDeleteFilter = QtWidgets.QToolButton(self.frame)
        self.toolDeleteFilter.setObjectName("Save_Button")
        self.hcab.addWidget(self.toolDeleteFilter)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Iconos/Filter_Delete.png"),QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolDeleteFilter.setIcon(icon)
        self.hcabspacer2=QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hcab.addItem(self.hcabspacer2)
        self.gridLayout_2.addLayout(self.hcab, 0, 0, 1, 1)

        self.model = EditableTableModel()
        self.model.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
        self.model.select()
        self.proxy.setSourceModel(self.model)

        self.tableEditDocs=QtWidgets.QTableView(parent=self.frame)
        self.tableEditDocs.setModel(self.proxy)
        self.tableEditDocs.setObjectName("tableEditDocs")
        self.gridLayout_2.addWidget(self.tableEditDocs, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        EditDocs_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=EditDocs_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 22))
        self.menubar.setObjectName("menubar")
        EditDocs_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=EditDocs_Window)
        self.statusbar.setObjectName("statusbar")
        EditDocs_Window.setStatusBar(self.statusbar)

        self.retranslateUi(EditDocs_Window)
        QtCore.QMetaObject.connectSlotsByName(EditDocs_Window)
        self.query_documents()
        self.toolSave.clicked.connect(self.submit_all)
        self.toolDeleteFilter.clicked.connect(self.delete_allFilters)


    def retranslateUi(self, EditDocs_Window):
        _translate = QtCore.QCoreApplication.translate
        EditDocs_Window.setWindowTitle(_translate("EditDocs_Window", "Editar Documentos"))
        self.tableEditDocs.setSortingEnabled(True)


    def delete_allFilters(self):
        columns_number=self.model.columnCount()
        for index in range(columns_number):
            self.proxy.setFilter("", index)
            self.model.setIconColumnHeader(index, '')


    def submit_all(self):
        columns_number=self.model.columnCount()
        if self.model.database().isOpen():
            self.model.database().transaction()
            success = True

            for index in range(columns_number):
                self.proxy.setFilter("", index)
                self.model.setIconColumnHeader(index, '')

            for row in range(self.model.rowCount()):
                for column in range(self.model.columnCount()):
                    index = self.model.index(row, column)
                    current_value = index.data(Qt.ItemDataRole.DisplayRole)
                    original_value = self.model.getOriginalValue(index)
                    if current_value != original_value:
                        record = self.model.record(row)
                        query = self.model.update_record(record, index)
                        if not query:
                            success = False
                            break

            if success:
                self.model.database().commit()
                dlg = QtWidgets.QMessageBox()
                new_icon = QtGui.QIcon()
                new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                dlg.setWindowIcon(new_icon)
                dlg.setWindowTitle("Editar Documentos")
                dlg.setText("Datos guardados con éxito")
                dlg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                dlg.exec()
            else:
                self.model.database().rollback()
                dlg = QtWidgets.QMessageBox()
                new_icon = QtGui.QIcon()
                new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                dlg.setWindowIcon(new_icon)
                dlg.setWindowTitle("Editar Documentos")
                dlg.setText("Ha habido un problema al guardar los datos")
                dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                dlg.exec()

        else:
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("Editar Documentos")
            dlg.setText("No ha sido posible conectar con la base de datos. Contacte con su administrador")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            dlg.exec()


    def query_documents(self):
        self.model.setTable("documentation")
        self.model.select()
        self.model.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)

        column_names = ["doc_type_id"] # Ocultar columna según nombre
        for column_index in range(self.model.columnCount(),-1,-1):
            column_name = self.model.record().fieldName(column_index)
            if column_name in column_names:
                self.model.removeColumn(column_index)

        self.proxy.setSourceModel(self.model)
        self.tableEditDocs.setModel(self.proxy)

        self.tableEditDocs.verticalHeader().hide()
        self.tableEditDocs.setItemDelegate(AlignDelegate(self.tableEditDocs))
        self.tableEditDocs.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.tableEditDocs.horizontalHeader().setStyleSheet("::section{font: 800 10pt}")
        self.tableEditDocs.setObjectName("tableEditDocs")
        self.gridLayout_2.addWidget(self.tableEditDocs, 3, 0, 1, 1)
        self.tableEditDocs.setSortingEnabled(False)
        self.tableEditDocs.horizontalHeader().sectionClicked.connect(self.on_view_horizontalHeader_sectionClicked)

        # Change all column names
        headers = ["Nº Doc. EIPSA", "Nº Doc. Cliente", "Nº Pedido", "Título", "Crítico", "Estado", "Nº Revisión", "Fecha"]
        self.model.setAllColumnHeaders(headers)

        for row in range(self.model.rowCount()):
            for column in range(self.model.columnCount()):
                index = self.model.index(row, column)
                self.model.setOriginalData(index, self.model.data(index))


    def on_view_horizontalHeader_sectionClicked(self, logicalIndex):
        self.logicalIndex = logicalIndex
        self.menuValues = QtWidgets.QMenu(self.tableEditDocs)
        self.signalMapper = QtCore.QSignalMapper(self.tableEditDocs)  

        valuesUnique = []
        for row in range(self.model.rowCount()):
            value = self.model.record(row).value(self.logicalIndex)
            if value not in valuesUnique:
                if isinstance(value, QtCore.QDate):
                    value=value.toString("dd/MM/yyyy")
                valuesUnique.append(str(value))

        actionSortAscending = QtGui.QAction("Ordenar Ascendente", self.tableEditDocs)
        actionSortAscending.triggered.connect(self.on_actionSortAscending_triggered)
        self.menuValues.addAction(actionSortAscending)
        actionSortDescending = QtGui.QAction("Ordenar Descendente", self.tableEditDocs)
        actionSortDescending.triggered.connect(self.on_actionSortDescending_triggered)
        self.menuValues.addAction(actionSortDescending)
        self.menuValues.addSeparator()

        actionDeleteFilterColumn = QtGui.QAction("Quitar Filtro", self.tableEditDocs)
        actionDeleteFilterColumn.triggered.connect(self.on_actionDeleteFilterColumn_triggered)
        self.menuValues.addAction(actionDeleteFilterColumn)
        self.menuValues.addSeparator()

        actionTextFilter = QtGui.QAction("Buscar...", self.tableEditDocs)
        actionTextFilter.triggered.connect(self.on_actionTextFilter_triggered)
        self.menuValues.addAction(actionTextFilter)
        self.menuValues.addSeparator()

        for actionNumber, actionName in enumerate(sorted(list(set(valuesUnique)))):              
            action = QtGui.QAction(str(actionName), self.tableEditDocs)
            self.signalMapper.setMapping(action, actionNumber)  
            action.triggered.connect(self.signalMapper.map)  
            self.menuValues.addAction(action)

        self.menuValues.setStyleSheet("QMenu { color: black; }"
                                        "QMenu::item:selected { background-color: #33bdef; }"
                                        "QMenu::item:pressed { background-color: rgb(1, 140, 190); }")
        self.signalMapper.mappedInt.connect(self.on_signalMapper_mapped)  

        headerPos = self.tableEditDocs.mapToGlobal(self.tableEditDocs.horizontalHeader().pos())        

        posY = headerPos.y() + self.tableEditDocs.horizontalHeader().height()
        posX = headerPos.x() + self.tableEditDocs.horizontalHeader().sectionPosition(self.logicalIndex)

        self.menuValues.exec(QtCore.QPoint(posX, posY))


    def on_actionDeleteFilterColumn_triggered(self):
        filterColumn = self.logicalIndex
        self.proxy.setFilter("", filterColumn)
        self.model.setIconColumnHeader(filterColumn, '')


    def on_signalMapper_mapped(self, i):
        stringAction = self.signalMapper.mapping(i).text()
        filterColumn = self.logicalIndex
        self.proxy.setFilter(stringAction, filterColumn)

        imagen_path = "//nas01/DATOS/Comunes/EIPSA-ERP/Iconos/Filter_Active.png"
        icono = QtGui.QIcon(QtGui.QPixmap.fromImage(QtGui.QImage(imagen_path)))
        self.model.setIconColumnHeader(filterColumn, icono)


    def on_actionSortAscending_triggered(self):
        sortColumn = self.logicalIndex
        sortOrder = Qt.SortOrder.AscendingOrder
        self.tableEditDocs.sortByColumn(sortColumn, sortOrder)


    def on_actionSortDescending_triggered(self):
        sortColumn = self.logicalIndex
        sortOrder = Qt.SortOrder.DescendingOrder
        self.tableEditDocs.sortByColumn(sortColumn, sortOrder)


    def on_actionTextFilter_triggered(self):
        filterColumn = self.logicalIndex
        dlg = QtWidgets.QInputDialog()
        new_icon = QtGui.QIcon()
        new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        dlg.setWindowIcon(new_icon)
        dlg.setWindowTitle('Buscar')
        clickedButton=dlg.exec()

        if clickedButton == 1:
            stringAction = dlg.textValue()
            if re.fullmatch(r'^(?:3[01]|[12][0-9]|0?[1-9])([\-/.])(0?[1-9]|1[1-2])\1\d{4}$', stringAction):
                stringAction=QtCore.QDate.fromString(stringAction,"dd/MM/yyyy")
                stringAction=stringAction.toString("yyyy-MM-dd")

            filterString = QtCore.QRegularExpression(stringAction, QtCore.QRegularExpression.PatternOption(0))

            self.proxy.setFilter(filterString, filterColumn)


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

    EditDocs_Window = QtWidgets.QMainWindow()
    ui = Ui_EditDoc_Window()
    ui.setupUi(EditDocs_Window)
    EditDocs_Window.show()
    sys.exit(app.exec())