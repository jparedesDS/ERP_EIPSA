# Form implementation generated from reading ui file 'ReportPurchaseRefDate_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from config import config
import psycopg2
import locale
import os
basedir = r"\\nas01\DATOS\Comunes\EIPSA-ERP"


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignmentFlag.AlignCenter

class Ui_ReportPurRefDate_Window(object):
    def setupUi(self, ReportPurRefDate_Window):
        ReportPurRefDate_Window.setObjectName("ReportPurRefDate_Window")
        ReportPurRefDate_Window.resize(1165, 945)
        ReportPurRefDate_Window.setMinimumSize(QtCore.QSize(1165, 945))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Resources/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ReportPurRefDate_Window.setWindowIcon(icon)
        ReportPurRefDate_Window.setStyleSheet("QWidget {\n"
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
"  font-size: 10px;\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=ReportPurRefDate_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout1 = QtWidgets.QGridLayout()
        self.gridLayout1.setObjectName("gridLayout1")
        self.label_item = QtWidgets.QLabel(parent=self.frame)
        self.label_item.setMinimumSize(QtCore.QSize(int(100//1.5), int(25//1.5)))
        self.label_item.setMaximumSize(QtCore.QSize(int(100//1.5), int(25//1.5)))
        font = QtGui.QFont()
        font.setPointSize(int(11//1.5))
        font.setBold(True)
        self.label_item.setFont(font)
        self.label_item.setObjectName("label_item")
        self.gridLayout1.addWidget(self.label_item, 0, 0, 1, 1)
        self.ItemName = QtWidgets.QComboBox(parent=self.frame)
        self.ItemName.setMinimumSize(QtCore.QSize(0, int(25//1.5)))
        self.ItemName.setMaximumSize(QtCore.QSize(16777215, int(25//1.5)))
        font = QtGui.QFont()
        font.setPointSize(int(10//1.5))
        self.ItemName.setFont(font)
        self.ItemName.setObjectName("ItemName")
        self.gridLayout1.addWidget(self.ItemName, 0, 1, 1, 2)
        self.Button_Export = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Export.setMinimumSize(QtCore.QSize(int(175//1.5), int(35//1.5)))
        self.Button_Export.setMaximumSize(QtCore.QSize(int(175//1.5), int(35//1.5)))
        self.Button_Export.setStyleSheet("QPushButton {\n"
"background-color: #33bdef;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 3px;\n"
"  color: #fff;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",\"Liberation Sans\",sans-serif;\n"
"  font-size: 10px;\n"
"  font-weight: 800;\n"
"  line-height: 1.15385;\n"
"  margin: 0;\n"
"  outline: none;\n"
"  padding: 4px .8em;\n"
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
        self.Button_Export.setObjectName("Button_Export")
        self.gridLayout1.addWidget(self.Button_Export, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout1.addItem(spacerItem2, 1, 1, 1, 1)
        self.label_dates = QtWidgets.QLabel(parent=self.frame)
        self.label_dates.setMinimumSize(QtCore.QSize(int(100//1.5), int(25//1.5)))
        self.label_dates.setMaximumSize(QtCore.QSize(int(100//1.5), int(25//1.5)))
        font = QtGui.QFont()
        font.setPointSize(int(11//1.5))
        font.setBold(True)
        self.label_dates.setFont(font)
        self.label_dates.setObjectName("label_dates")
        self.gridLayout1.addWidget(self.label_dates, 2, 0, 1, 1)
        self.DateStart = QtWidgets.QDateEdit(calendarPopup=True)
        self.DateStart.setMinimumSize(QtCore.QSize(int(300//1.5), int(25//1.5)))
        self.DateStart.setMaximumSize(QtCore.QSize(int(300//1.5), int(25//1.5)))
        self.DateStart.setDate(QtCore.QDate.currentDate())
        font = QtGui.QFont()
        font.setPointSize(int(10//1.5))
        self.DateStart.setFont(font)
        self.DateStart.setObjectName("DateStart")
        self.DateStart.setStyleSheet("QCalendarWidget QWidget{\n"
"background-color: rgb(3, 174, 236);\n"
"}\n"
"\n"
"QCalendarWidget QTableView{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    color: white;\n"
"    font-size:10px;\n"
"    icon-size:20px 20px;\n"
"    background-color:rgb(3, 174, 236);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::hover {\n"
"    background-color : #019ad2;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::pressed {\n"
"    background-color: rgb(1, 140, 190);\n"
"    border: 3px solid;\n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid;\n"
"    border-color: rgb(3,174, 236);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"    selection-background-color: rgb(3, 174, 236);\n"
"    selection-color: white;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth {\n"
"    qproperty-icon: url(//nas01/DATOS/Comunes/EIPSA-ERP/Resources/Iconos/back_arrow.png);\n"
"}\n"
"#qt_calendar_nextmonth {\n"
"    qproperty-icon: url(//nas01/DATOS/Comunes/EIPSA-ERP/Resources/Iconos/forward_arrow.png);\n"
"}")
        self.gridLayout1.addWidget(self.DateStart, 2, 1, 1, 1)
        self.DateEnd = QtWidgets.QDateEdit(calendarPopup=True)
        self.DateEnd.setMinimumSize(QtCore.QSize(int(300//1.5), int(25//1.5)))
        self.DateEnd.setMaximumSize(QtCore.QSize(int(300//1.5), int(25//1.5)))
        font = QtGui.QFont()
        font.setPointSize(int(10//1.5))
        self.DateEnd.setFont(font)
        self.DateEnd.setDate(QtCore.QDate.currentDate())
        self.DateEnd.setObjectName("DateEnd")
        self.DateEnd.setStyleSheet("QCalendarWidget QWidget{\n"
"background-color: rgb(3, 174, 236);\n"
"}\n"
"\n"
"QCalendarWidget QTableView{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    color: white;\n"
"    font-size:10px;\n"
"    icon-size:20px 20px;\n"
"    background-color:rgb(3, 174, 236);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::hover {\n"
"    background-color : #019ad2;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::pressed {\n"
"    background-color: rgb(1, 140, 190);\n"
"    border: 3px solid;\n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid;\n"
"    border-color: rgb(3,174, 236);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"    selection-background-color: rgb(3, 174, 236);\n"
"    selection-color: white;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth {\n"
"    qproperty-icon: url(//nas01/DATOS/Comunes/EIPSA-ERP/Resources/Iconos/back_arrow.png);\n"
"}\n"
"#qt_calendar_nextmonth {\n"
"    qproperty-icon: url(//nas01/DATOS/Comunes/EIPSA-ERP/Resources/Iconos/forward_arrow.png);\n"
"}")
        self.gridLayout1.addWidget(self.DateEnd, 2, 2, 1, 1)
        self.Button_Load = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Load.setMinimumSize(QtCore.QSize(int(175//1.5), int(35//1.5)))
        self.Button_Load.setMaximumSize(QtCore.QSize(int(175//1.5), int(35//1.5)))
        self.Button_Load.setStyleSheet("QPushButton {\n"
"background-color: #33bdef;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 3px;\n"
"  color: #fff;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",\"Liberation Sans\",sans-serif;\n"
"  font-size: 10px;\n"
"  font-weight: 800;\n"
"  line-height: 1.15385;\n"
"  margin: 0;\n"
"  outline: none;\n"
"  padding: 4px .8em;\n"
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
        self.Button_Load.setObjectName("Button_Load")
        self.gridLayout1.addWidget(self.Button_Load, 2, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout1, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        for i in range(6):
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(int(10//1.5))
            font.setBold(True)
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(i, item)
        self.gridLayout_2.addWidget(self.tableWidget, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_Total = QtWidgets.QLabel(parent=self.frame)
        self.label_Total.setMinimumSize(QtCore.QSize(0, int(50//1.5)))
        self.label_Total.setMaximumSize(QtCore.QSize(16777215, int(50//1.5)))
        font = QtGui.QFont()
        font.setPointSize(int(11//1.5))
        self.label_Total.setFont(font)
        self.label_Total.setObjectName("label_Total")
        self.horizontalLayout.addWidget(self.label_Total)
        self.label_TotalValue = QtWidgets.QLabel(parent=self.frame)
        self.label_TotalValue.setMinimumSize(QtCore.QSize(int(100//1.5), int(50//1.5)))
        self.label_TotalValue.setMaximumSize(QtCore.QSize(int(100//1.5), int(50//1.5)))
        font = QtGui.QFont()
        font.setPointSize(int(11//1.5))
        self.label_TotalValue.setFont(font)
        self.label_TotalValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_TotalValue.setObjectName("label_TotalValue")
        self.horizontalLayout.addWidget(self.label_TotalValue)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        ReportPurRefDate_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ReportPurRefDate_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1165, 22))
        self.menubar.setObjectName("menubar")
        ReportPurRefDate_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ReportPurRefDate_Window)
        self.statusbar.setObjectName("statusbar")
        ReportPurRefDate_Window.setStatusBar(self.statusbar)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section {background-color: #33bdef; border: 1px solid black;}")

        self.retranslateUi(ReportPurRefDate_Window)
        QtCore.QMetaObject.connectSlotsByName(ReportPurRefDate_Window)

        commands_supplies = "SELECT * FROM purch_fact.supplies"
        conn = None
        try:
        # read the connection parameters
            params = config()
        # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # execution of commands one by one
            cur.execute(commands_supplies)
            results_supplies=cur.fetchall()
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

        list_supplies=[x[3] + ' | ' + x[4] for x in results_supplies]
        self.ItemName.addItems(sorted(list_supplies))

        self.Button_Load.clicked.connect(self.loaddata)

    def retranslateUi(self, ReportPurRefDate_Window):
        _translate = QtCore.QCoreApplication.translate
        ReportPurRefDate_Window.setWindowTitle(_translate("ReportPurRefDate_Window", "Resumen Cliente"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ReportPurRefDate_Window", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ReportPurRefDate_Window", "Fecha Pedido"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ReportPurRefDate_Window", "Nº Pedido"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ReportPurRefDate_Window", "Cantidad"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ReportPurRefDate_Window", "Total"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ReportPurRefDate_Window", "Subtotal"))
        self.label_item.setText(_translate("ReportPurRefDate_Window", "Artículo"))
        self.label_dates.setText(_translate("ReportPurRefDate_Window", "Fechas"))
        self.Button_Export.setText(_translate("ReportPurRefDate_Window", "Exportar"))
        self.Button_Load.setText(_translate("ReportPurRefDate_Window", "Cargar Datos"))
        self.label_Total.setText(_translate("ReportPurRefDate_Window", "Total Comprado"))
        self.label_TotalValue.setText(_translate("ReportPurRefDate_Window", ""))


    def loaddata(self):
        supply_name = self.ItemName.currentText()
        supply_name = supply_name[:supply_name.find(" |")]
        start_date = self.DateStart.date().toString(QtCore.Qt.DateFormat.ISODate)
        end_date = self.DateEnd.date().toString(QtCore.Qt.DateFormat.ISODate)


        query1 = """
                SELECT so_header."order_date", suppliers."name", so_header."supplier_order_num", so_det."supplier_ord_header_id"
                FROM purch_fact.suppliers AS suppliers
                LEFT JOIN (purch_fact.supplier_ord_header AS so_header LEFT JOIN purch_fact."supplier_ord_detail" AS so_det ON so_header."id" = so_det."supplier_ord_header_id") ON suppliers."id" = so_header."supplier_id"
                GROUP BY so_header."order_date", suppliers."name", so_header."supplier_order_num", so_det."supplier_ord_header_id"
                HAVING (((so_det."supplier_ord_header_id") Is Not Null))
                ORDER BY so_header."supplier_order_num"
                """

        query2 = """
                SELECT so_det."supplier_ord_header_id", supplies."reference", supplies."description", so_det."quantity", so_det."unit_value", supplies."id"
                FROM purch_fact.supplies AS supplies
                LEFT JOIN purch_fact.supplier_ord_detail AS so_det ON supplies."id" = so_det."supply_id"
                WHERE (((so_det."supplier_ord_header_id") Is Not Null))
                ORDER BY supplies."reference"
                """

        query3 = f"""
                SELECT query2."reference", query2."description", query1."name", query1."order_date", query1."supplier_order_num", query2."quantity", query2."unit_value"
                FROM ({query1}) AS query1 
                RIGHT JOIN ({query2}) AS query2 ON query1."supplier_ord_header_id" = query2."supplier_ord_header_id"
                ORDER BY query2."reference"
                """
        commands_supplies = f"""
                            SELECT query3."name", TO_CHAR(query3."order_date", 'DD-MM-YYYY') AS formatted_date, query3."supplier_order_num", query3."quantity", query3."unit_value", CAST(("quantity"*CAST(query3."unit_value" AS numeric)) AS money) AS SBTOT
                            FROM ({query3}) AS query3
                            WHERE (((query3."reference")='{supply_name}') AND ((query3."order_date") BETWEEN '{start_date}' And '{end_date}'))
                            ORDER BY query3."reference"
                            """
        conn = None

        try:
        # read the connection parameters
            params = config()
        # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # execution of commands one by one
            cur.execute(commands_supplies)
            results=cur.fetchall()
        # close communication with the PostgreSQL database server
            cur.close()
        # commit the changes
            conn.commit()

            self.tableWidget.setRowCount(len(results))
            tablerow=0

            font = QtGui.QFont()
            font.setPointSize(int(10//1.5))

        # fill the Qt Table with the query results
            for row in results:
                for column in range(6):
                    value = row[column]
                    if value is None:
                        value = ''
                    it = QtWidgets.QTableWidgetItem(str(value))
                    it.setFlags(it.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                    it.setFont(font)
                    self.tableWidget.setItem(tablerow, column, it)

                self.tableWidget.setItemDelegateForRow(tablerow, AlignDelegate(self.tableWidget))
                tablerow+=1

            self.tableWidget.verticalHeader().hide()
            self.tableWidget.setSortingEnabled(False)
            self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
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

        self.calculate_total()



#  Function to calculate the total amount
    def calculate_total(self):
            locale.setlocale(locale.LC_ALL, '')
            total = 0
            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, 5)
                if item is not None:
                    value = item.text()
                    value=value.replace(".","")
                    value=value.replace(",",".")
                    value=value[:value.find(" €")]
                    total += float(value)
            total = locale.format_string("%.2f", total, grouping=True)
            total = total + " €"
            self.label_TotalValue.setText(total)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReportPurRefDate_Window = QtWidgets.QMainWindow()
    ui = Ui_ReportPurRefDate_Window()
    ui.setupUi(ReportPurRefDate_Window)
    ReportPurRefDate_Window.show()
    sys.exit(app.exec())
