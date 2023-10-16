# Form implementation generated from reading ui file 'HistoryTask_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from config import config
import psycopg2
from PyQt6.QtWidgets import QFileDialog
import pandas as pd
from PyQt6.QtWidgets import QApplication, QFileDialog, QAbstractItemView
from PyQt6.QtGui import QKeySequence, QTextDocument, QTextCursor
from PyQt6.QtCore import Qt
from EditTask_Window import Ui_EditTask_Window
import os

basedir = r"\\nas01\DATOS\Comunes\EIPSA-ERP"


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignmentFlag.AlignCenter

        if index.column() == 4:  # Verifica que estemos en la tercera columna
            value = index.data()

            if value == "Completado":  
                color = QtGui.QColor(0, 255, 0)  # Green if "Adjudicada"
            else:
                color = QtGui.QColor(255, 255, 255)  # White for rest

            option.backgroundBrush = color


class Ui_HistoryTask_Window(QtWidgets.QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.name=name
        self.setupUi(self)
    # def __init__(self):
    #     self.name="Luis Bravo"

    def setupUi(self, HistoryTask_Window):
        HistoryTask_Window.setObjectName("HistoryTask_Window")
        HistoryTask_Window.resize(400, 561)
        HistoryTask_Window.setMinimumSize(QtCore.QSize(600, 575))
        # HistoryTask_Window.setMaximumSize(QtCore.QSize(600, 575))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        HistoryTask_Window.setWindowIcon(icon)
        HistoryTask_Window.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=HistoryTask_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        # self.frame.setMinimumSize(QtCore.QSize(550, 500))
        # self.frame.setMaximumSize(QtCore.QSize(550, 500))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 2)
        self.Button_Cancel = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Cancel.setMinimumSize(QtCore.QSize(100, 35))
        self.Button_Cancel.setMaximumSize(QtCore.QSize(100, 35))
        self.Button_Cancel.setObjectName("Button_Cancel")
        self.gridLayout_2.addWidget(self.Button_Cancel, 1, 0, 1, 1)
        self.Button_Export = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Export.setMinimumSize(QtCore.QSize(100, 35))
        self.Button_Export.setMaximumSize(QtCore.QSize(100, 35))
        self.Button_Export.setObjectName("Button_Export")
        self.gridLayout_2.addWidget(self.Button_Export, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
        self.tableTasks = QtWidgets.QTableWidget(parent=self.frame)
        self.tableTasks.setObjectName("tableWidget")
        if self.name in ['Luis Bravo', 'Fernando Gallego']:
            self.tableTasks.setColumnCount(6)
        else:
            self.tableTasks.setColumnCount(5)
        self.tableTasks.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableTasks.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableTasks.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableTasks.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableTasks.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        self.tableTasks.setHorizontalHeaderItem(4, item)
        if self.name in ['Luis Bravo', 'Fernando Gallego']:
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            item.setFont(font)
            self.tableTasks.setHorizontalHeaderItem(5, item)
        self.gridLayout_2.addWidget(self.tableTasks, 2, 0, 1, 3)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        HistoryTask_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=HistoryTask_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        HistoryTask_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=HistoryTask_Window)
        self.statusbar.setObjectName("statusbar")
        HistoryTask_Window.setStatusBar(self.statusbar)
        self.tableTasks.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableTasks.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.tableTasks.setSortingEnabled(True)
        self.tableTasks.horizontalHeader().setStyleSheet("QHeaderView::section {background-color: #33bdef; border: 1px solid black;}")
        HistoryTask_Window.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint, False)

        self.retranslateUi(HistoryTask_Window)
        QtCore.QMetaObject.connectSlotsByName(HistoryTask_Window)

        self.Button_Cancel.clicked.connect(HistoryTask_Window.close)
        self.Button_Export.clicked.connect(self.export_to_excel)
        self.tableTasks.itemDoubleClicked.connect(self.on_item_double_clicked)
        self.QueryTask()


    def retranslateUi(self, HistoryTask_Window):
        _translate = QtCore.QCoreApplication.translate
        HistoryTask_Window.setWindowTitle(_translate("HistoryTask_Window", "Tareas"))
        item = self.tableTasks.horizontalHeaderItem(0)
        item.setText(_translate("HistoryTask_Window", "ID"))
        item = self.tableTasks.horizontalHeaderItem(1)
        item.setText(_translate("HistoryTask_Window", "Creador"))
        item = self.tableTasks.horizontalHeaderItem(2)
        item.setText(_translate("HistoryTask_Window", "Tarea"))
        item = self.tableTasks.horizontalHeaderItem(3)
        item.setText(_translate("HistoryTask_Window", "Fecha Fin"))
        item = self.tableTasks.horizontalHeaderItem(4)
        item.setText(_translate("HistoryTask_Window", "Estado"))
        if self.name in ['Luis Bravo', 'Fernando Gallego']:
            item = self.tableTasks.horizontalHeaderItem(5)
            item.setText(_translate("QueryTask_Window", "Responsable"))
        self.Button_Cancel.setText(_translate("HistoryTask_Window", "Salir"))
        self.Button_Export.setText(_translate("HistoryTask_Window", "Exportar"))


    def QueryTask(self):
        conn = None
        commands_QueryTask_All_LB = ("""
                                    SELECT "id", "creator", "task", TO_CHAR("task_date", 'DD-MM-YYYY'), "state", "responsible"
                                    FROM tasks
                                    WHERE "creator" IN ('CCH','LB','SS')
                                    ORDER BY "task_date"
                                    """)
        commands_QueryTask_All = ("""
                                    SELECT "id", "creator", "task", TO_CHAR("task_date", 'DD-MM-YYYY'), "state"
                                    FROM tasks
                                    WHERE ("responsible" = %s)
                                    ORDER BY "task_date"
                                    """)

        try:
        # read the connection parameters
            params = config()
        # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # execution of commands one by one
            if self.name in ['Luis Bravo', 'Fernando Gallego']:
                cur.execute(commands_QueryTask_All_LB)
            else:
                cur.execute(commands_QueryTask_All, (self.name,))
            results=cur.fetchall()
        # close communication with the PostgreSQL database server
            cur.close()
        # commit the changes
            conn.commit()

            self.tableTasks.setRowCount(len(results))
            tablerow=0

        # fill the Qt Table with the query results
            for row in results:
                if self.name in ['Luis Bravo', 'Fernando Gallego']:
                    for column in range(6):
                        value = row[column]
                        if value is None:
                            value = ''
                        it = QtWidgets.QTableWidgetItem(str(value))
                        it.setFlags(it.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                        self.tableTasks.setItem(tablerow, column, it)
                else:
                    for column in range(5):
                        value = row[column]
                        if value is None:
                            value = ''
                        it = QtWidgets.QTableWidgetItem(str(value))
                        it.setFlags(it.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                        self.tableTasks.setItem(tablerow, column, it)

                tablerow+=1

            self.tableTasks.verticalHeader().hide()
            self.tableTasks.setItemDelegate(AlignDelegate(self.tableTasks))

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


    def export_to_excel(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Guardar como Excel", "", "Archivos Excel (*.xlsx);;Todos los archivos (*)")

        if file_name:
            df = pd.DataFrame()
            for col in range(self.tableTasks.columnCount()):
                header = self.tableTasks.horizontalHeaderItem(col).text()
                column_data = [self.tableTasks.item(row, col).text() for row in range(self.tableTasks.rowCount())]
                df[header] = column_data

            with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
                df.to_excel(writer, index=False)


    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if event.matches(QtGui.QKeySequence.StandardKey.Copy):
            selected_indexes = self.tableTasks.selectedIndexes()
            if selected_indexes:
                clipboard = QApplication.clipboard()
                text = self.get_selected_text(selected_indexes)
                clipboard.setText(text)


    def get_selected_text(self, indexes):
        rows = set()
        cols = set()
        for index in indexes:
            rows.add(index.row())
            cols.add(index.column())

        text_doc = QTextDocument()
        cursor = QTextCursor(text_doc)

        header_labels = [self.tableTasks.horizontalHeaderItem(col).text() for col in sorted(cols)]
        for label in header_labels:
            cursor.insertText(label)
            cursor.insertText('\t')  # Tab separador de columnas
        cursor.insertText('\n')   # Salto de línea después de las cabeceras

        for row in sorted(rows):
            for col in sorted(cols):
                cell_data = self.tableTasks.item(row, col).data(Qt.ItemDataRole.DisplayRole)
                cursor.insertText(cell_data)
                cursor.insertText('\t')  # Tab separador de columnas
            cursor.insertText('\n')  # Salto de línea al final de la fila

        return text_doc.toPlainText()

    def on_item_double_clicked(self, item):
        if item.column() == 2:
            self.expand_cell(item)
        elif item.column() == 4:
            self.edittask(item)

    def expand_cell(self, item):
        if item.column() == 2:
            cell_content = item.text()
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("Tareas")
            dlg.setText(cell_content)
            dlg.exec()

    def edittask(self, item):
        task = item.tableWidget().item(item.row(), 2).text()
        id = item.tableWidget().item(item.row(), 0).text()
        date = item.tableWidget().item(item.row(), 3).text()
        state = item.tableWidget().item(item.row(), 4).text()

        self.edittaskwindow=QtWidgets.QMainWindow()
        self.ui=Ui_EditTask_Window(id, task, date, state)
        self.ui.setupUi(self.edittaskwindow)
        self.edittaskwindow.show()
        self.ui.Button_Cancel.clicked.connect(self.QueryTask)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HistoryTask_Window = Ui_HistoryTask_Window()
    HistoryTask_Window.show()
    sys.exit(app.exec())