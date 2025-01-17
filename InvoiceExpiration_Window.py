# Form implementation generated from reading ui file 'ExpiringInvoice_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import re
from PyQt6 import QtCore, QtGui, QtWidgets
import psycopg2
from config import config
import os
from datetime import *
from openpyxl.styles import NamedStyle
import tkinter as tk
from tkinter import filedialog
import pandas as pd

basedir = r"\\nas01\DATOS\Comunes\EIPSA-ERP"


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignmentFlag.AlignCenter


class CustomTableWidget(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.list_filters=[]
        self.column_filters = {}
        self.column_actions = {}
        self.checkbox_states = {}
        self.rows_hidden = {}
        self.general_rows_to_hide = set()

# Function to show the menu
    def show_unique_values_menu(self, column_index, header_pos, header_height):
        menu = QtWidgets.QMenu(self)
        actionDeleteFilterColumn = QtGui.QAction("Quitar Filtro")
        actionDeleteFilterColumn.triggered.connect(lambda: self.delete_filter(column_index))
        menu.addAction(actionDeleteFilterColumn)
        menu.addSeparator()
        actionOrderAsc = menu.addAction("Ordenar Ascendente")
        actionOrderAsc.triggered.connect(lambda: self.sort_column(column_index, QtCore.Qt.SortOrder.AscendingOrder))
        actionOrderDesc = menu.addAction("Ordenar Descendente")
        actionOrderDesc.triggered.connect(lambda: self.sort_column(column_index, QtCore.Qt.SortOrder.DescendingOrder))
        menu.addSeparator()
        actionFilterByText = menu.addAction("Buscar Texto")
        actionFilterByText.triggered.connect(lambda: self.filter_by_text(column_index))
        menu.addSeparator()

        menu.setStyleSheet("QMenu { color: black; }"
                        "QMenu::item:selected { background-color: #33bdef; }"
                        "QMenu::item:pressed { background-color: rgb(1, 140, 190); }")

        if column_index not in self.column_filters:
            self.column_filters[column_index] = set()

        scroll_menu = QtWidgets.QScrollArea()
        scroll_menu.setWidgetResizable(True)
        scroll_widget = QtWidgets.QWidget(scroll_menu)
        scroll_menu.setWidget(scroll_widget)
        scroll_layout = QtWidgets.QVBoxLayout(scroll_widget)

        checkboxes = []

        select_all_checkbox = QtWidgets.QCheckBox("Seleccionar todo")
        if column_index in self.checkbox_states:
            select_all_checkbox.setCheckState(QtCore.Qt.CheckState(self.checkbox_states[column_index].get("Seleccionar todo", QtCore.Qt.CheckState(2))))
        else:
            select_all_checkbox.setCheckState(QtCore.Qt.CheckState(2))
        scroll_layout.addWidget(select_all_checkbox)
        checkboxes.append(select_all_checkbox)

        unique_values = self.get_unique_values(column_index)
        filtered_values = self.get_filtered_values()

        for value in sorted(unique_values):
            checkbox = QtWidgets.QCheckBox(value)
            if select_all_checkbox.isChecked(): 
                checkbox.setCheckState(QtCore.Qt.CheckState(2))
            else:
                if column_index in self.checkbox_states and value in self.checkbox_states[column_index]:
                    checkbox.setCheckState(QtCore.Qt.CheckState(self.checkbox_states[column_index][value]))
                elif filtered_values is None or value in filtered_values[column_index]:
                    checkbox.setCheckState(QtCore.Qt.CheckState(2))
                else:
                    checkbox.setCheckState(QtCore.Qt.CheckState(0))
            scroll_layout.addWidget(checkbox)
            checkboxes.append(checkbox)

        select_all_checkbox.stateChanged.connect(lambda state: self.set_all_checkboxes_state(checkboxes, state, column_index))

        for value, checkbox in zip(sorted(unique_values), checkboxes[1:]):
            checkbox.stateChanged.connect(lambda checked, value=value, checkbox=checkbox: self.apply_filter(column_index, value, checked))

    # Action for drop down menu and adding scroll area as widget
        action_scroll_menu = QtWidgets.QWidgetAction(menu)
        action_scroll_menu.setDefaultWidget(scroll_menu)
        menu.addAction(action_scroll_menu)

        menu.exec(header_pos - QtCore.QPoint(0, header_height))


# Function to delete filter on selected column
    def delete_filter(self,column_index):
        if column_index in self.column_filters:
            del self.column_filters[column_index]
        if column_index in self.checkbox_states:
            del self.checkbox_states[column_index]
        if column_index in self.rows_hidden:
            for item in self.rows_hidden[column_index]:
                self.setRowHidden(item, False)
                if item in self.general_rows_to_hide:
                    self.general_rows_to_hide.remove(item)
            del self.rows_hidden[column_index]
        header_item = self.horizontalHeaderItem(column_index)
        header_item.setIcon(QtGui.QIcon())


# Function to set all checkboxes state
    def set_all_checkboxes_state(self, checkboxes, state, column_index):
        if column_index not in self.checkbox_states:
            self.checkbox_states[column_index] = {}

        for checkbox in checkboxes:
            checkbox.setCheckState(QtCore.Qt.CheckState(state))

        self.checkbox_states[column_index]["Seleccionar todo"] = state


# Function to apply filters to table
    def apply_filter(self, column_index, value, checked, text_filter=None, filter_dialog=None):
        if column_index not in self.column_filters:
            self.column_filters[column_index] = set()

        if text_filter is None:
            if value is None:
                self.column_filters[column_index] = set()
            elif checked:
                self.column_filters[column_index].add(value)
            elif value in self.column_filters[column_index]:
                self.column_filters[column_index].remove(value)

        rows_to_hide = set()
        for row in range(self.rowCount()):
            show_row = True

            # Check filters for all columns
            for col, filters in self.column_filters.items():
                item = self.item(row, col)
                if item:
                    item_value = item.text()
                    if text_filter is None:
                        if filters and item_value not in filters:
                            show_row = False
                            break

        # Filtering by text
            if text_filter is not None:
                filter_dialog.accept()
                item = self.item(row, column_index)
                if item:
                    if text_filter.upper() in item.text().upper():
                        self.column_filters[column_index].add(item.text())
                    else:
                        show_row = False

            if not show_row:
                if row not in self.general_rows_to_hide:
                    self.general_rows_to_hide.add(row)
                    rows_to_hide.add(row)
            else:
                if row in self.general_rows_to_hide:
                    self.general_rows_to_hide.remove(row)

        # Update hidden rows for this column depending on checkboxes
        if checked and text_filter is None:
            if column_index not in self.rows_hidden:
                self.rows_hidden[column_index] = set(rows_to_hide)
            else:
                self.rows_hidden[column_index].update(rows_to_hide)

        # Update hidden rows for this column depending on filtered text
        if text_filter is not None and value is None:
            if column_index not in self.rows_hidden:
                self.rows_hidden[column_index] = set(rows_to_hide)
            else:
                self.rows_hidden[column_index].update(rows_to_hide)

        # Iterate over all rows to hide them as necessary
        for row in range(self.rowCount()):
            self.setRowHidden(row, row in self.general_rows_to_hide)

        header_item = self.horizontalHeaderItem(column_index)
        if len(self.general_rows_to_hide) > 0:
            header_item.setIcon(QtGui.QIcon(os.path.abspath(os.path.join(basedir, "Resources/Iconos/Filter_Active.png"))))
        else:
            header_item.setIcon(QtGui.QIcon())


    def filter_by_text(self, column_index):
        filter_dialog = QtWidgets.QDialog(self)
        filter_dialog.setWindowTitle("Filtrar por texto")
        
        label = QtWidgets.QLabel("Texto a filtrar:")
        text_input = QtWidgets.QLineEdit()
        
        filter_button = QtWidgets.QPushButton("Filtrar")
        filter_button.setStyleSheet("QPushButton {\n"
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
"  padding: 2px .8em;\n"
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
        filter_button.clicked.connect(lambda: self.apply_filter(column_index, None, False, text_input.text(), filter_dialog))

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(text_input)
        layout.addWidget(filter_button)

        filter_dialog.setLayout(layout)
        filter_dialog.exec()


# Function to obtain the unique matching applied filters 
    def get_unique_values(self, column_index):
        unique_values = set()
        for row in range(self.rowCount()):
            show_row = True
            for col, filters in self.column_filters.items():
                if col != column_index:
                    item = self.item(row, col)
                    if item:
                        item_value = item.text()
                        if filters and item_value not in filters:
                            show_row = False
                            break
            if show_row:
                item = self.item(row, column_index)
                if item:
                    unique_values.add(item.text())
        return unique_values

# Function to get values filtered by all columns
    def get_filtered_values(self):
        filtered_values = {}
        for col, filters in self.column_filters.items():
            filtered_values[col] = filters
        return filtered_values

# Function to sort column
    def sort_column(self, column_index, sortOrder):
        if column_index in [11, 13, 14]:
            self.custom_sort(column_index, sortOrder)
        else:
            self.sortByColumn(column_index, sortOrder)


    def custom_sort(self, column, order):
    # Obtén la cantidad de filas en la tabla
        row_count = self.rowCount()

        # Crea una lista de índices ordenados según las fechas
        indexes = list(range(row_count))
        indexes.sort(key=lambda i: QtCore.QDateTime.fromString(self.item(i, column).text(), "dd/MM/yyyy"))

        # Si el orden es descendente, invierte la lista
        if order == QtCore.Qt.SortOrder.DescendingOrder:
            indexes.reverse()

        # Guarda el estado actual de las filas ocultas
        hidden_rows = [row for row in range(row_count) if self.isRowHidden(row)]

        # Actualiza las filas en la tabla en el orden ordenado
        rows = self.rowCount()
        for i in range(rows):
            self.insertRow(i)

        for new_row, old_row in enumerate(indexes):
            for col in range(self.columnCount()):
                item = self.takeItem(old_row + rows, col)
                self.setItem(new_row, col, item)

        for i in range(rows):
            self.removeRow(rows)

        for row in hidden_rows:
            self.setRowHidden(row, True)

# Function with the menu configuration
    def contextMenuEvent(self, event):
        if self.horizontalHeader().visualIndexAt(event.pos().x()) >= 0:
            logical_index = self.horizontalHeader().logicalIndexAt(event.pos().x())
            header_pos = self.mapToGlobal(self.horizontalHeader().pos())
            header_height = self.horizontalHeader().height()
            self.show_unique_values_menu(logical_index, header_pos, header_height)
        else:
            super().contextMenuEvent(event)


class Ui_ExpiringInvoice_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, ExpiringInvoice_Window):
        ExpiringInvoice_Window.setObjectName("ExpiringInvoice_Window")
        ExpiringInvoice_Window.resize(845, 590)
        ExpiringInvoice_Window.setMinimumSize(QtCore.QSize(1000, 590))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ExpiringInvoice_Window.setWindowIcon(icon)
        ExpiringInvoice_Window.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=ExpiringInvoice_Window)
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
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.Button_ExportExcel = QtWidgets.QPushButton(parent=self.frame)
        self.Button_ExportExcel.setMinimumSize(QtCore.QSize(150, 30))
        self.Button_ExportExcel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Button_ExportExcel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_ExportExcel.setAutoDefault(True)
        self.Button_ExportExcel.setStyleSheet("QPushButton {\n"
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
"  padding: 2px .8em;\n"
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
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-color: #019ad2;\n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:focus:pressed {\n"
"    background-color: rgb(1, 140, 190);\n"
"    border-color: rgb(255, 255, 255);\n"
"}")
        self.Button_ExportExcel.setObjectName("Button_ExportExcel")
        self.Button_ExportExcel.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.gridLayout_2.addWidget(self.Button_ExportExcel, 1, 0, 1, 1)
        self.tableQueryInvoice = CustomTableWidget()
        self.tableQueryInvoice.setObjectName("tableQueryInvoice")
        self.tableQueryInvoice.setColumnCount(12)
        self.tableQueryInvoice.setRowCount(0)
        for i in range(12):
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            item.setFont(font)
            self.tableQueryInvoice.setHorizontalHeaderItem(i, item)
        self.tableQueryInvoice.setSortingEnabled(True)
        self.tableQueryInvoice.horizontalHeader().setStyleSheet("QHeaderView::section {background-color: #33bdef; border: 1px solid black;}")
        self.gridLayout_2.addWidget(self.tableQueryInvoice, 2, 0, 1, 11)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        ExpiringInvoice_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ExpiringInvoice_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 22))
        self.menubar.setObjectName("menubar")
        ExpiringInvoice_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ExpiringInvoice_Window)
        self.statusbar.setObjectName("statusbar")
        ExpiringInvoice_Window.setStatusBar(self.statusbar)
        self.tableQueryInvoice.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.retranslateUi(ExpiringInvoice_Window)
        QtCore.QMetaObject.connectSlotsByName(ExpiringInvoice_Window)
        self.tableQueryInvoice.itemDoubleClicked.connect(self.on_item_double_clicked)
        self.tableQueryInvoice.horizontalHeader().sectionClicked.connect(self.on_header_section_clicked)
        self.Button_ExportExcel.clicked.connect(self.export_data)

        self.query_all_invoices()


    def retranslateUi(self, ExpiringInvoice_Window):
        _translate = QtCore.QCoreApplication.translate
        ExpiringInvoice_Window.setWindowTitle(_translate("ExpiringInvoice_Window", "Vencimiento Facturas"))
        self.Button_ExportExcel.setText(_translate("ExpiringInvoice_Window", "Exportar A Excel"))
        item = self.tableQueryInvoice.horizontalHeaderItem(0)
        item.setText(_translate("ExpiringInvoice_Window", "Nº Factura"))
        item = self.tableQueryInvoice.horizontalHeaderItem(1)
        item.setText(_translate("ExpiringInvoice_Window", "Total Fact."))
        item = self.tableQueryInvoice.horizontalHeaderItem(2)
        item.setText(_translate("ExpiringInvoice_Window", "Fecha Factura"))
        item = self.tableQueryInvoice.horizontalHeaderItem(3)
        item.setText(_translate("ExpiringInvoice_Window", "Fecha Vto."))
        item = self.tableQueryInvoice.horizontalHeaderItem(4)
        item.setText(_translate("ExpiringInvoice_Window", "OK"))
        item = self.tableQueryInvoice.horizontalHeaderItem(5)
        item.setText(_translate("ExpiringInvoice_Window", "Estado"))
        item = self.tableQueryInvoice.horizontalHeaderItem(6)
        item.setText(_translate("ExpiringInvoice_Window", "Cod. Cliente"))
        item = self.tableQueryInvoice.horizontalHeaderItem(7)
        item.setText(_translate("ExpiringInvoice_Window", "Grupo"))
        item = self.tableQueryInvoice.horizontalHeaderItem(8)
        item.setText(_translate("ExpiringInvoice_Window", "Cliente"))
        item = self.tableQueryInvoice.horizontalHeaderItem(9)
        item.setText(_translate("ExpiringInvoice_Window", "S/ Ref"))
        item = self.tableQueryInvoice.horizontalHeaderItem(10)
        item.setText(_translate("ExpiringInvoice_Window", "N/ Ref"))
        item = self.tableQueryInvoice.horizontalHeaderItem(11)
        item.setText(_translate("ExpiringInvoice_Window", "Obs."))




    def query_all_invoices(self):
        self.tableQueryInvoice.setRowCount(0)

        commands_queryinvoice = ("""
                        SELECT invoice."num_invoice", (invoice."tax_base_amount" + (invoice."tax_base_amount" * invoice."iva"/100)) AS TOTALFACT, TO_CHAR(invoice."date_invoice",'dd/MM/yyyy'),
                        TO_CHAR(DATE(
                            CASE 
                                WHEN EXTRACT(MONTH FROM (invoice."date_invoice" + INTERVAL '1 day' * pay_way."num_days")) + 1 > 12 THEN EXTRACT(YEAR FROM (invoice."date_invoice" + INTERVAL '1 day' * pay_way."num_days")) + 1
                                ELSE EXTRACT(YEAR FROM (invoice."date_invoice" + INTERVAL '1 day' * pay_way."num_days"))
                            END || '-' ||
                            CASE 
                                WHEN EXTRACT(MONTH FROM (invoice."date_invoice" + INTERVAL '1 day' * pay_way."num_days")) + 1 > 12 THEN 1
                                ELSE EXTRACT(MONTH FROM (invoice."date_invoice" + INTERVAL '1 day' * pay_way."num_days"))
                            END || '-' ||
                            CASE 
                                WHEN EXTRACT(DAY FROM (invoice."date_invoice" + INTERVAL '1 day' * pay_way."num_days")) < COALESCE(NULLIF(clients."vto_prog1",''), '1')::INTEGER THEN COALESCE(NULLIF(clients."vto_prog1",''), '1')
                                WHEN EXTRACT(DAY FROM (invoice."date_invoice" + INTERVAL '1 day' * pay_way."num_days")) < COALESCE(NULLIF(clients."vto_prog2",''), '1')::INTEGER THEN COALESCE(NULLIF(clients."vto_prog2",''), '1')
                                WHEN EXTRACT(DAY FROM (invoice."date_invoice" + INTERVAL '1 day' * pay_way."num_days")) > COALESCE(NULLIF(clients."vto_prog2",''), '1')::INTEGER THEN COALESCE(NULLIF(clients."vto_prog1",''), '1')
                                ELSE EXTRACT(DAY FROM (invoice."date_invoice" + INTERVAL '1 day' * pay_way."num_days"))::TEXT
                            END
                        ),'dd/MM/yyyy') AS FchVto,
                        TO_CHAR(invoice."pay_date",'dd/MM/yyyy'),
                        CASE 
                            WHEN invoice."pay_date" IS NOT NULL THEN 'PAGADO'
                            WHEN invoice."date_invoice" + pay_way."num_days" > CURRENT_TIMESTAMP THEN 'PENDIENTE'
                            ELSE 'VENCIDA'
                        END AS Estado,
                        clients."code", invoice."client_group", clients."name", invoice."their_ref", invoice."our_ref", invoice."obs_delivnote"
                        FROM purch_fact.invoice_header AS invoice
                        INNER JOIN purch_fact.clients AS clients ON (invoice."id_client" = clients."id")
                        INNER JOIN purch_fact.pay_way AS pay_way ON (clients."pay_way_id" = pay_way."id")
                        ORDER BY invoice."num_invoice"
                        """)

        conn = None
        try:
        # read the connection parameters
            params = config()
        # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # execution of commands
            cur.execute(commands_queryinvoice)
            results=cur.fetchall()
            self.tableQueryInvoice.setRowCount(len(results))
            tablerow=0

        # fill the Qt Table with the query results
            for row in results:
                for column in range(12):
                    value = row[column]
                    if value is None:
                        value = ''
                    it = QtWidgets.QTableWidgetItem(str(value))
                    it.setFlags(it.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                    self.tableQueryInvoice.setItem(tablerow, column, it)

                self.tableQueryInvoice.setItemDelegateForRow(tablerow, AlignDelegate(self.tableQueryInvoice))
                tablerow+=1

            # self.tableQueryInvoice.verticalHeader().hide()
            self.tableQueryInvoice.setSortingEnabled(False)
            self.tableQueryInvoice.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            self.tableQueryInvoice.horizontalHeader().setSectionResizeMode(11, QtWidgets.QHeaderView.ResizeMode.Stretch)


        # close communication with the PostgreSQL database server
            cur.close()
        # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
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


    def euro_string_to_float(self, euro_str):
        match = re.match(r'^([\d.,]+)\s€$', euro_str)
        if match:
            number_str = match.group(1)
            number_str = number_str.replace('.', '').replace(',', '.')
            return float(number_str)
        else:
            return 0.0


    def on_item_double_clicked(self, item):
        if item.column() in [0]:
            num_invoice = self.tableQueryInvoice.item(item.row(), 0).text()

            from InvoiceNew_Window import Ui_InvoiceNew_Window
            self.invoice_window=QtWidgets.QMainWindow()
            self.ui=Ui_InvoiceNew_Window(num_invoice)
            self.ui.setupUi(self.invoice_window)
            self.invoice_window.showMaximized()


#Function when clicking on table header
    def on_header_section_clicked(self, logical_index):
        header_pos = self.tableQueryInvoice.horizontalHeader().sectionViewportPosition(logical_index)
        header_height = self.tableQueryInvoice.horizontalHeader().height()
        popup_pos = self.tableQueryInvoice.viewport().mapToGlobal(QtCore.QPoint(header_pos, header_height))
        self.tableQueryInvoice.show_unique_values_menu(logical_index, popup_pos, header_height)


    def export_data(self):
        if self.tableQueryInvoice.rowCount() > 0:
            df = pd.DataFrame()
            for col in range(self.tableQueryInvoice.columnCount()):
                header = self.tableQueryInvoice.horizontalHeaderItem(col).text()
                column_data = []
                for row in range(self.tableQueryInvoice.rowCount()):
                    if not self.tableQueryInvoice.isRowHidden(row):
                        item = self.tableQueryInvoice.item(row,col)
                        if item is not None:
                            if col in [2, 3, 4]:  # date column
                                date_str = item.text()
                                if date_str:  
                                    date_obj = datetime.strptime(date_str, "%d/%m/%Y")
                                    column_data.append(date_obj)
                                else:
                                    column_data.append('')
                            elif col in [1]:  # currency columns
                                currency_str = item.text()
                                if currency_str:
                                    currency_str=currency_str.replace(".","")
                                    currency_str=currency_str.replace(",",".")
                                    currency_str=currency_str[:currency_str.find(" €")]
                                    currency_value = float(currency_str)
                                    column_data.append(currency_value)
                                else:
                                    column_data.append('')
                            else:
                                column_data.append(item.text())
                        else:
                            column_data.append('')
                df[header] = column_data

            root = tk.Tk()
            root.withdraw()

            file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])

            if file_path:
                # df.to_excel(file_path, index=False)
                writer = pd.ExcelWriter(file_path, engine='openpyxl')
                df.to_excel(writer, index=False, sheet_name='Sheet1')

                # Set date format
                date_style = NamedStyle(name='date_style', number_format='DD/MM/YYYY')
                currency_style  = NamedStyle(name='currency_style ', number_format='#,##0.00" €"')
                for col_num in range(1, self.tableQueryInvoice.columnCount() + 1):
                    if col_num in [3,4,5]:  
                        for row_num in range(2, self.tableQueryInvoice.rowCount() + 2):
                            cell = writer.sheets['Sheet1'].cell(row=row_num, column=col_num)
                            cell.style = date_style

                    elif col_num in [2]:  
                        for row_num in range(2, self.tableQueryInvoice.rowCount() + 2):
                            cell = writer.sheets['Sheet1'].cell(row=row_num, column=col_num)
                            cell.style = currency_style

                writer._save()

            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("Vencimiento Facturas")
            dlg.setText("Datos exportados con éxito")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            dlg.exec()
            del dlg,new_icon


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExpiringInvoice_Window = Ui_ExpiringInvoice_Window()
    ExpiringInvoice_Window.show()
    sys.exit(app.exec())
