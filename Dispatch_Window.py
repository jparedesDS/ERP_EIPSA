from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import QtSql
from PyQt6.QtCore import Qt
from Database_Connection import createConnection
import configparser
from datetime import *
import os
import re

basedir = r"\\nas01\DATOS\Comunes\EIPSA-ERP"

class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignmentFlag.AlignCenter

class ColorDelegate(QtWidgets.QItemDelegate):
    def paint(self, painter, option, index: QtCore.QModelIndex):
        value = index.model().data(index, role=Qt.ItemDataRole.DisplayRole)
        # if index.column() == 16 and value <= 50 and value >= 1:
        #     background_color = QtGui.QColor(255, 255, 0) #Yellow
        # elif index.column() == 16 and value < 100  and value > 50:
        #     background_color = QtGui.QColor(0, 255, 0) #Green
        # elif index.column() == 16 and value == 100:
        #     background_color = QtGui.QColor(0, 102, 204) #Blue
        # else:
        #     background_color = QtGui.QColor(255, 255, 255) #White

        # painter.fillRect(option.rect, background_color)
        option.displayAlignment = QtCore.Qt.AlignmentFlag.AlignCenter
        super().paint(painter, option, index)


class CustomProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._filters = dict()
        self.header_names = {}

    @property
    def filters(self):
        return self._filters

    def setFilter(self, list_expresions, column, action_name=None):
        for expresion in list_expresions:
            if expresion or expresion == '':
                if column in self.filters:
                    if action_name or action_name == '':
                        self.filters[column].remove(expresion)
                    else:
                        self.filters[column].append(expresion)
                else:
                    self.filters[column] = [expresion]
            elif column in self.filters:
                if action_name or action_name == '':
                    self.filters[column].remove(expresion)
                    if not self.filters[column]:
                        del self.filters[column]
                else:
                    del self.filters[column]
        self.invalidateFilter()


    def filterAcceptsRow(self, source_row, source_parent):
        for column, expresions in self.filters.items():
            text = self.sourceModel().index(source_row, column, source_parent).data()

            if isinstance(text, QtCore.QDate): #Check if filters are QDate. If True, convert to text
                text = text.toString("yyyy-MM-dd")

            for expresion in expresions:
                if expresion == '':  # Si la expresión es vacía, coincidir con celdas vacías
                    if text == '':
                        break

                elif re.fullmatch(r'^(?:3[01]|[12][0-9]|0?[1-9])([\-/.])(0?[1-9]|1[1-2])\1\d{4}$', expresion):
                    expresion = QtCore.QDate.fromString(expresion, "dd/MM/yyyy")
                    expresion = expresion.toString("yyyy-MM-dd")
                    regex = QtCore.QRegularExpression(f".*{re.escape(str(expresion))}.*", QtCore.QRegularExpression.PatternOption.CaseInsensitiveOption)
                    if regex.match(str(text)).hasMatch():
                        break

                else:
                    regex = QtCore.QRegularExpression(f".*{re.escape(str(expresion))}.*", QtCore.QRegularExpression.PatternOption.CaseInsensitiveOption)
                    if regex.match(str(text)).hasMatch():
                        break
            else:
                return False
        return True

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
        if index.column() < 54:
            flags &= ~Qt.ItemFlag.ItemIsEditable
            return flags | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled
        else:
            return flags | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable

    def getColumnHeaders(self, visible_columns):
        column_headers = [self.headerData(col, Qt.Orientation.Horizontal) for col in visible_columns]
        return column_headers


class Ui_Dispatch_Window(QtWidgets.QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.model = EditableTableModel()
        self.proxy = CustomProxyModel()
        self.checkbox_states = {}
        self.dict_valuesuniques = {}
        self.dict_ordersort = {}
        self.action_checkbox_map = {}
        self.checkbox_filters = {}
        self.db = db
        self.model.dataChanged.connect(self.saveChanges)
        self.setupUi(self)

    def closeEvent(self, event):
    # Closing database connection
        if self.model:
            self.model.clear()
        self.closeConnection()

    def closeConnection(self):
    # Closing database connection
        self.tableDispatch.setModel(None)
        del self.model
        if self.db:
            self.db.close()
            del self.db
            if QtSql.QSqlDatabase.contains("qt_sql_default_connection"):
                QtSql.QSqlDatabase.removeDatabase("qt_sql_default_connection")


    def setupUi(self, Dispatch_Window):
        self.id_list = []
        data_list = []
        Dispatch_Window.setObjectName("Dispatch_Window")
        Dispatch_Window.resize(400, 561)
        Dispatch_Window.setMinimumSize(QtCore.QSize(600, 575))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dispatch_Window.setWindowIcon(icon)
        Dispatch_Window.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=Dispatch_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.hcab=QtWidgets.QHBoxLayout()
        self.hcab.setObjectName("hcab")
        self.toolDeleteFilter = QtWidgets.QToolButton(self.frame)
        self.toolDeleteFilter.setObjectName("Save_Button")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/Filter_Delete.png"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolDeleteFilter.setIcon(icon)
        self.toolDeleteFilter.setIconSize(QtCore.QSize(25, 25))
        self.hcab.addWidget(self.toolDeleteFilter)
        self.hcabspacer=QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hcab.addItem(self.hcabspacer)
        self.gridLayout_2.addLayout(self.hcab, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.hLayout = QtWidgets.QHBoxLayout()
        self.hLayout.setObjectName("hLayout")
        self.Button_All = QtWidgets.QPushButton(parent=self.frame)
        self.Button_All.setMinimumSize(QtCore.QSize(150, 35))
        self.Button_All.setMaximumSize(QtCore.QSize(150, 35))
        self.Button_All.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Button_All.setObjectName("Button_All")
        self.hLayout.addWidget(self.Button_All)
        self.gridLayout_2.addLayout(self.hLayout, 2, 0, 1, 1)
        self.tableDispatch=QtWidgets.QTableView(parent=self.frame)
        self.model = EditableTableModel()
        self.tableDispatch.setObjectName("tableDispatch")
        self.gridLayout_2.addWidget(self.tableDispatch, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        Dispatch_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Dispatch_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        Dispatch_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Dispatch_Window)
        self.statusbar.setObjectName("statusbar")
        Dispatch_Window.setStatusBar(self.statusbar)
        self.tableDispatch.setSortingEnabled(True)
        self.tableDispatch.horizontalHeader().setStyleSheet("QHeaderView::section {background-color: #33bdef; border: 1px solid black;}")
        # Dispatch_Window.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint, False)

        self.retranslateUi(Dispatch_Window)
        QtCore.QMetaObject.connectSlotsByName(Dispatch_Window)

        self.model.setTable("purch_fact.invoice_header")
        # self.model.setFilter("num_order LIKE 'P-%' AND num_order NOT LIKE '%R%' AND (porc_deliveries <> 100 OR porc_deliveries IS NULL)")
        self.model.setSort(0, QtCore.Qt.SortOrder.DescendingOrder)
        self.model.select()

        self.proxy.setSourceModel(self.model)
        self.tableDispatch.setModel(self.proxy)

    # Getting the unique values for each column of the model
        for column in range(self.model.columnCount()):
            list_valuesUnique = []
            if column not in self.checkbox_states:
                self.checkbox_states[column] = {}
                self.checkbox_states[column]['Seleccionar todo'] = True
                for row in range(self.model.rowCount()):
                    value = self.model.record(row).value(column)
                    if value not in list_valuesUnique:
                        if isinstance(value, QtCore.QDate):
                            value=value.toString("dd/MM/yyyy")
                        list_valuesUnique.append(str(value))
                        self.checkbox_states[column][str(value)] = True
                self.dict_valuesuniques[column] = list_valuesUnique

        for i in range(2,4):
            self.tableDispatch.hideColumn(i)
        for i in range(5,9):
            self.tableDispatch.hideColumn(i)
        for i in range(10,54):
            self.tableDispatch.hideColumn(i)
        self.tableDispatch.hideColumn(60)
        self.tableDispatch.hideColumn(61)
        self.tableDispatch.hideColumn(62)

        headers=['ID', 'Nº Factura', '', '', 'Nº Albarán', '', '', '', '', 'Nº Pedido',
                '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', 'Destino', 'Bultos', 'Peso', 'Descripción', 'Transporte', 'Fecha', '', '', '']

        self.tableDispatch.setItemDelegate(AlignDelegate(self.tableDispatch))
        # self.color_delegate = ColorDelegate(self)
        # self.tableDispatch.setItemDelegateForColumn(16, self.color_delegate)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(57, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(59, QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.tableDispatch.horizontalHeader().setStyleSheet("::section{font: 800 10pt; background-color: #33bdef; border: 1px solid black;}")
        self.gridLayout_2.addWidget(self.tableDispatch, 3, 0, 1, 1)

        self.model.setAllColumnHeaders(headers)

        self.toolDeleteFilter.clicked.connect(self.delete_allFilters)
        self.Button_All.clicked.connect(self.query_all_Dispatch)
        self.tableDispatch.setSortingEnabled(False)
        self.tableDispatch.horizontalHeader().sectionClicked.connect(self.on_view_horizontalHeader_sectionClicked)
        self.model.dataChanged.connect(self.saveChanges)


    def retranslateUi(self, Dispatch_Window):
        _translate = QtCore.QCoreApplication.translate
        Dispatch_Window.setWindowTitle(_translate("EditTags_Window", "Despachos"))
        self.Button_All.setText(_translate("EditTags_Window", "Ver Todos"))


    def query_all_Dispatch(self):
        self.model.dataChanged.disconnect(self.saveChanges)
        self.model.setTable("purch_fact.invoice_header")
        # self.model.setFilter("num_order LIKE 'P-%' AND num_order NOT LIKE '%R%' AND (porc_deliveries <> 100 OR porc_deliveries IS NULL)")
        self.model.setSort(0, QtCore.Qt.SortOrder.DescendingOrder)
        self.model.select()

        self.proxy.setSourceModel(self.model)
        self.tableDispatch.setModel(self.proxy)

        # Getting the unique values for each column of the model
        for column in range(self.model.columnCount()):
            list_valuesUnique = []
            if column not in self.checkbox_states:
                self.checkbox_states[column] = {}
                self.checkbox_states[column]['Seleccionar todo'] = True
                for row in range(self.model.rowCount()):
                    value = self.model.record(row).value(column)
                    if value not in list_valuesUnique:
                        if isinstance(value, QtCore.QDate):
                            value=value.toString("dd/MM/yyyy")
                        list_valuesUnique.append(str(value))
                        self.checkbox_states[column][str(value)] = True
                self.dict_valuesuniques[column] = list_valuesUnique

        for i in range(2,4):
            self.tableDispatch.hideColumn(i)
        for i in range(5,9):
            self.tableDispatch.hideColumn(i)
        for i in range(10,54):
            self.tableDispatch.hideColumn(i)
        self.tableDispatch.hideColumn(60)
        self.tableDispatch.hideColumn(61)
        self.tableDispatch.hideColumn(62)

        headers=['ID', 'Nº Factura', '', '', 'Nº Albarán', '', '', '', '', 'Nº Pedido',
                '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', 'Destino', 'Bultos', 'Peso', 'Descripción', 'Transporte', 'Fecha', '', '', '']

        self.tableDispatch.setItemDelegate(AlignDelegate(self.tableDispatch))
        # self.color_delegate = ColorDelegate(self)
        # self.tableDispatch.setItemDelegateForColumn(16, self.color_delegate)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(57, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(59, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableDispatch.horizontalHeader().setStyleSheet("::section{font: 800 10pt; background-color: #33bdef; border: 1px solid black;}")
        self.gridLayout_2.addWidget(self.tableDispatch, 3, 0, 1, 1)

        self.model.setAllColumnHeaders(headers)
        self.model.dataChanged.connect(self.saveChanges)

# Function to delete all filters when tool button is clicked
    def delete_allFilters(self):
        columns_number=self.model.columnCount()
        for index in range(columns_number):
            if index in self.proxy.filters:
                del self.proxy.filters[index]
            self.model.setIconColumnHeader(index, '')

        self.checkbox_states = {}
        self.dict_valuesuniques = {}
        self.dict_ordersort = {}
        self.checkbox_filters = {}

        self.proxy.invalidateFilter()
        self.tableDispatch.setModel(None)
        self.tableDispatch.setModel(self.proxy)

        # Getting the unique values for each column of the model
        for column in range(self.model.columnCount()):
            list_valuesUnique = []
            if column not in self.checkbox_states:
                self.checkbox_states[column] = {}
                self.checkbox_states[column]['Seleccionar todo'] = True
                for row in range(self.model.rowCount()):
                    value = self.model.record(row).value(column)
                    if value not in list_valuesUnique:
                        if isinstance(value, QtCore.QDate):
                            value=value.toString("dd/MM/yyyy")
                        list_valuesUnique.append(str(value))
                        self.checkbox_states[column][value] = True
                self.dict_valuesuniques[column] = list_valuesUnique

        self.tableDispatch.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(3,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(8,QtWidgets.QHeaderView.ResizeMode.Stretch)

# Function to save changes into database
    def saveChanges(self):
        self.model.submitAll()

        for column in range(self.model.columnCount()):
            list_valuesUnique = []
            for row in range(self.model.rowCount()):
                value = self.model.record(row).value(column)
                if value not in list_valuesUnique:
                    if isinstance(value, QtCore.QDate):
                        value=value.toString("dd/MM/yyyy")
                    list_valuesUnique.append(str(value))
                    if value not in self.checkbox_states[column]:
                        self.checkbox_states[column][value] = True
            self.dict_valuesuniques[column] = list_valuesUnique

# Function when header is clicked
    def on_view_horizontalHeader_sectionClicked(self, logicalIndex):
        self.logicalIndex = logicalIndex
        self.menuValues = QtWidgets.QMenu(self)
        self.signalMapper = QtCore.QSignalMapper(self.tableDispatch)

        valuesUnique_view = []
        for row in range(self.tableDispatch.model().rowCount()):
            index = self.tableDispatch.model().index(row, self.logicalIndex)
            value = index.data(Qt.ItemDataRole.DisplayRole)
            if value not in valuesUnique_view:
                if isinstance(value, QtCore.QDate):
                    value=value.toString("dd/MM/yyyy")
                valuesUnique_view.append(value)

        actionSortAscending = QtGui.QAction("Ordenar Ascendente", self.tableDispatch)
        actionSortAscending.triggered.connect(self.on_actionSortAscending_triggered)
        self.menuValues.addAction(actionSortAscending)
        actionSortDescending = QtGui.QAction("Ordenar Descendente", self.tableDispatch)
        actionSortDescending.triggered.connect(self.on_actionSortDescending_triggered)
        self.menuValues.addAction(actionSortDescending)
        self.menuValues.addSeparator()

        actionDeleteFilterColumn = QtGui.QAction("Quitar Filtro", self.tableDispatch)
        actionDeleteFilterColumn.triggered.connect(self.on_actionDeleteFilterColumn_triggered)
        self.menuValues.addAction(actionDeleteFilterColumn)
        self.menuValues.addSeparator()

        actionTextFilter = QtGui.QAction("Buscar...", self.tableDispatch)
        actionTextFilter.triggered.connect(self.on_actionTextFilter_triggered)
        self.menuValues.addAction(actionTextFilter)
        self.menuValues.addSeparator()

        scroll_menu = QtWidgets.QScrollArea()
        scroll_menu.setStyleSheet("background-color: rgb(255, 255, 255)")
        scroll_menu.setWidgetResizable(True)
        scroll_widget = QtWidgets.QWidget(scroll_menu)
        scroll_menu.setWidget(scroll_widget)
        scroll_layout = QtWidgets.QVBoxLayout(scroll_widget)

        checkbox_all_widget = QtWidgets.QCheckBox('Seleccionar todo')

        if not self.checkbox_states[self.logicalIndex]['Seleccionar todo'] == True:
            checkbox_all_widget.setChecked(False)
        else:
            checkbox_all_widget.setChecked(True)
        
        checkbox_all_widget.toggled.connect(lambda checked, name='Seleccionar todo': self.on_select_all_toggled(checked, name))

        scroll_layout.addWidget(checkbox_all_widget)
        self.action_checkbox_map['Seleccionar todo'] = checkbox_all_widget

        if len(self.dict_ordersort) != 0 and self.logicalIndex in self.dict_ordersort:
            list_uniquevalues = sorted(list(set(self.dict_valuesuniques[self.logicalIndex])))
        else:
            list_uniquevalues = sorted(list(set(valuesUnique_view)))

        for actionName in list_uniquevalues:
            checkbox_widget = QtWidgets.QCheckBox(actionName)

            if self.logicalIndex not in self.checkbox_filters:
                checkbox_widget.setChecked(True)
            elif actionName not in self.checkbox_filters[self.logicalIndex]:
                checkbox_widget.setChecked(False)
            else:
                checkbox_widget.setChecked(True)

            checkbox_widget.toggled.connect(lambda checked, name=actionName: self.on_checkbox_toggled(checked, name))

            scroll_layout.addWidget(checkbox_widget)
            self.action_checkbox_map[actionName] = checkbox_widget

        action_scroll_menu = QtWidgets.QWidgetAction(self.menuValues)
        action_scroll_menu.setDefaultWidget(scroll_menu)
        self.menuValues.addAction(action_scroll_menu)

        self.menuValues.addSeparator()

        accept_button = QtGui.QAction("ACEPTAR", self.tableDispatch)
        accept_button.triggered.connect(self.menu_acceptbutton_triggered)

        cancel_button = QtGui.QAction("CANCELAR", self.tableDispatch)
        cancel_button.triggered.connect(self.menu_cancelbutton_triggered)

        self.menuValues.addAction(accept_button)
        self.menuValues.addAction(cancel_button)

        self.menuValues.setStyleSheet("QMenu { color: black; }"
                                        "QMenu { background-color: rgb(255, 255, 255); }"
                                        "QMenu::item:selected { background-color: #33bdef; }"
                                        "QMenu::item:pressed { background-color: rgb(1, 140, 190); }")

        headerPos = self.tableDispatch.mapToGlobal(self.tableDispatch.horizontalHeader().pos())        

        posY = headerPos.y() + self.tableDispatch.horizontalHeader().height()
        scrollX = self.tableDispatch.horizontalScrollBar().value()
        xInView = self.tableDispatch.horizontalHeader().sectionViewportPosition(logicalIndex)
        posX = headerPos.x() + xInView - scrollX

        self.menuValues.exec(QtCore.QPoint(posX, posY))

# Function when cancel button of menu is clicked
    def menu_cancelbutton_triggered(self):
        self.menuValues.hide()

# Function when accept button of menu is clicked
    def menu_acceptbutton_triggered(self):
        for column, filters in self.checkbox_filters.items():
            if filters:
                self.proxy.setFilter(filters, column)
            else:
                self.proxy.setFilter(None, column)

        self.tableDispatch.setItemDelegate(AlignDelegate(self.tableDispatch))
        self.color_delegate = ColorDelegate(self)
        self.tableDispatch.setItemDelegateForColumn(16, self.color_delegate)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(16, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(17, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(18, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(19, QtWidgets.QHeaderView.ResizeMode.Interactive)

# Function when select all checkbox is clicked
    def on_select_all_toggled(self, checked, action_name):
        filterColumn = self.logicalIndex
        imagen_path = os.path.abspath(os.path.join(basedir, "Resources/Iconos/Filter_Active.png"))
        icono = QtGui.QIcon(QtGui.QPixmap.fromImage(QtGui.QImage(imagen_path)))

        if checked:
            for checkbox_name, checkbox_widget in self.action_checkbox_map.items():
                checkbox_widget.setChecked(checked)
                self.checkbox_states[self.logicalIndex][checkbox_name] = checked

            if all(checkbox_widget.isChecked() for checkbox_widget in self.action_checkbox_map.values()):
                self.model.setIconColumnHeader(filterColumn, icono)
            else:
                self.model.setIconColumnHeader(filterColumn, '')
        
        else:
            for checkbox_name, checkbox_widget in self.action_checkbox_map.items():
                checkbox_widget.setChecked(checked)
                self.checkbox_states[self.logicalIndex][checkbox_widget.text()] = checked

# Function when checkbox of header menu is clicked
    def on_checkbox_toggled(self, checked, action_name):
        filterColumn = self.logicalIndex
        imagen_path = os.path.abspath(os.path.join(basedir, "Resources/Iconos/Filter_Active.png"))
        icono = QtGui.QIcon(QtGui.QPixmap.fromImage(QtGui.QImage(imagen_path)))

        if checked:
            if filterColumn not in self.checkbox_filters:
                self.checkbox_filters[filterColumn] = [action_name]
            else:
                if action_name not in self.checkbox_filters[filterColumn]:
                    self.checkbox_filters[filterColumn].append(action_name)
        else:
            if filterColumn in self.checkbox_filters and action_name in self.checkbox_filters[filterColumn]:
                self.checkbox_filters[filterColumn].remove(action_name)

        if all(checkbox_widget.isChecked() for checkbox_widget in self.action_checkbox_map.values()):
            self.model.setIconColumnHeader(filterColumn, '')
        else:
            self.model.setIconColumnHeader(filterColumn, icono)

# Function to delete individual column filter
    def on_actionDeleteFilterColumn_triggered(self):
        filterColumn = self.logicalIndex
        if filterColumn in self.proxy.filters:
            del self.proxy.filters[filterColumn]
        self.model.setIconColumnHeader(filterColumn, '')
        self.proxy.invalidateFilter()

        # self.tableDispatch.setModel(None)
        self.tableDispatch.setModel(self.proxy)

        if filterColumn in self.checkbox_filters:
            del self.checkbox_filters[filterColumn]

        self.checkbox_states[self.logicalIndex].clear()
        self.checkbox_states[self.logicalIndex]['Seleccionar todo'] = True
        for row in range(self.tableDispatch.model().rowCount()):
            value = self.model.record(row).value(filterColumn)
            if isinstance(value, QtCore.QDate):
                    value=value.toString("dd/MM/yyyy")
            self.checkbox_states[self.logicalIndex][str(value)] = True

        self.tableDispatch.setItemDelegate(AlignDelegate(self.tableDispatch))
        self.color_delegate = ColorDelegate(self)
        self.tableDispatch.setItemDelegateForColumn(16, self.color_delegate)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(16, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(17, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(18, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.tableDispatch.horizontalHeader().setSectionResizeMode(19, QtWidgets.QHeaderView.ResizeMode.Interactive)

# Function to order column ascending
    def on_actionSortAscending_triggered(self):
        sortColumn = self.logicalIndex
        sortOrder = Qt.SortOrder.AscendingOrder
        self.tableDispatch.sortByColumn(sortColumn, sortOrder)

# Function to order column descending
    def on_actionSortDescending_triggered(self):
        sortColumn = self.logicalIndex
        sortOrder = Qt.SortOrder.DescendingOrder
        self.tableDispatch.sortByColumn(sortColumn, sortOrder)

# Function when text is searched
    def on_actionTextFilter_triggered(self):
        filterColumn = self.logicalIndex
        dlg = QtWidgets.QInputDialog()
        new_icon = QtGui.QIcon()
        new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        dlg.setWindowIcon(new_icon)
        dlg.setWindowTitle('Buscar')
        clickedButton=dlg.exec()

        if clickedButton == 1:
            stringAction = dlg.textValue()
            if re.fullmatch(r'^(?:3[01]|[12][0-9]|0?[1-9])([\-/.])(0?[1-9]|1[1-2])\1\d{4}$', stringAction):
                stringAction=QtCore.QDate.fromString(stringAction,"dd/MM/yyyy")
                stringAction=stringAction.toString("yyyy-MM-dd")

            filterString = QtCore.QRegularExpression(stringAction, QtCore.QRegularExpression.PatternOption(0))
            # del self.proxy.filters[filterColumn]
            self.proxy.setFilter([stringAction], filterColumn)

            imagen_path = os.path.abspath(os.path.join(basedir, "Resources/Iconos/Filter_Active.png"))
            icono = QtGui.QIcon(QtGui.QPixmap.fromImage(QtGui.QImage(imagen_path)))
            self.model.setIconColumnHeader(filterColumn, icono)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    config_obj = configparser.ConfigParser()
    config_obj.read(r"C:\Program Files\ERP EIPSA\database.ini")
    dbparam = config_obj["postgresql"]
    # set your parameters for the database connection URI using the keys from the configfile.ini
    user_database = dbparam["user"]
    password_database = dbparam["password"]

    db = createConnection(user_database, password_database)
    if not db:
        sys.exit()

    Dispatch_Window = Ui_Dispatch_Window(db)
    Dispatch_Window.show()
    sys.exit(app.exec())