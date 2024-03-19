# Form implementation generated from reading ui file 'ClientsGeneralResume_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from config import config
import psycopg2
from datetime import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import ticker
from ClientResume_Window import Ui_ClientResume_Window
import os

basedir = r"\\nas01\DATOS\Comunes\EIPSA-ERP"


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignmentFlag.AlignCenter


class Ui_ClientsGeneralResume_Window(object):
    def setupUi(self, ClientsGeneralResume_Window):
        ClientsGeneralResume_Window.setObjectName("ClientsGeneralResume_Window")
        ClientsGeneralResume_Window.resize(790, 595)
        ClientsGeneralResume_Window.setMinimumSize(QtCore.QSize(1200, 900))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ClientsGeneralResume_Window.setWindowIcon(icon)
        ClientsGeneralResume_Window.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=ClientsGeneralResume_Window)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_Graphs = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Graphs.setMinimumSize(QtCore.QSize(250, 35))
        self.Button_Graphs.setMaximumSize(QtCore.QSize(250, 35))
        self.Button_Graphs.setObjectName("Button_Graphs")
        self.Button_Graphs.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.horizontalLayout.addWidget(self.Button_Graphs)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.label.setText('Importes adjudicados por año')
        self.horizontalLayout2.addWidget(self.label)
        self.gridLayout_2.addLayout(self.horizontalLayout2, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.tableClientsResume = QtWidgets.QTableWidget(parent=self.frame)
        self.tableClientsResume.setAlternatingRowColors(False)
        self.tableClientsResume.setObjectName("tableClientsResume")
        self.tableClientsResume.setColumnCount(5)
        self.tableClientsResume.setRowCount(0)
        for i in range(5):
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            item.setFont(font)
            self.tableClientsResume.setHorizontalHeaderItem(i, item)
        self.gridLayout_2.addWidget(self.tableClientsResume, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        ClientsGeneralResume_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ClientsGeneralResume_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 22))
        self.menubar.setObjectName("menubar")
        ClientsGeneralResume_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ClientsGeneralResume_Window)
        self.statusbar.setObjectName("statusbar")
        ClientsGeneralResume_Window.setStatusBar(self.statusbar)
        self.tableClientsResume.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableClientsResume.verticalHeader().setVisible(False)
        self.tableClientsResume.setSortingEnabled(False)
        self.tableClientsResume.horizontalHeader().setStyleSheet("QHeaderView::section {background-color: #33bdef; border: 1px solid black; font: 800 10pt;}")

        commands_loadtableresume = (f"""
                                    SELECT
                                        all_clients."client",
                                        COALESCE(a."sum(year-{date.today().year-3})", '0€') AS "sum(year-{date.today().year-3})",
                                        COALESCE(b."sum(year-{date.today().year-2})", '0€') AS "sum(year-{date.today().year-2})",
                                        COALESCE(c."sum(year-{date.today().year-1})", '0€') AS "sum(year-{date.today().year-1})",
                                        COALESCE(d."sum(year-{date.today().year})", '0€') AS "sum(year-{date.today().year})"
                                    FROM (
                                        SELECT DISTINCT "client"
                                        FROM offers
                                    ) all_clients
                                    LEFT JOIN (
                                        SELECT "client", CAST(SUM("offer_amount") AS money) AS "sum(year-{date.today().year-3})"
                                        FROM offers
                                        WHERE "offer_year" = {date.today().year-3} AND "state" = 'Adjudicada'
                                        GROUP BY "client"
                                    ) AS a ON all_clients."client" = a."client"
                                    LEFT JOIN (
                                        SELECT "client", CAST(SUM("offer_amount") AS money) AS "sum(year-{date.today().year-2})"
                                        FROM offers
                                        WHERE "offer_year" = {date.today().year-2} AND "state" = 'Adjudicada'
                                        GROUP BY "client"
                                    ) AS b ON all_clients."client" = b."client"
                                    LEFT JOIN (
                                        SELECT "client", CAST(SUM("offer_amount") AS money) AS "sum(year-{date.today().year-1})"
                                        FROM offers
                                        WHERE "offer_year" = {date.today().year-1} AND "state" = 'Adjudicada'
                                        GROUP BY "client"
                                    ) AS c ON all_clients."client" = c."client"
                                    LEFT JOIN (
                                        SELECT "client", CAST(SUM("offer_amount") AS money) AS "sum(year-{date.today().year})"
                                        FROM offers
                                        WHERE "offer_year" = {date.today().year} AND "state" = 'Adjudicada'
                                        GROUP BY "client"
                                    ) AS d ON all_clients."client" = d."client"
                                    ORDER BY all_clients."client";
                                """)
        conn = None
        try:
        # read the connection parameters
            params = config()
        # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # execution of commands
            cur.execute(commands_loadtableresume)
            results=cur.fetchall()

            self.tableClientsResume.setRowCount(len(results))
            tablerow=0

        # fill the Qt Table with the query results
            for row in results:
                for column in range(5):
                    value = row[column]
                    if value is None:
                        value = ''
                    it = QtWidgets.QTableWidgetItem(str(value))
                    if column == 0:
                        it.setFlags(it.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                        it.setCheckState(QtCore.Qt.CheckState.Unchecked)
                        self.tableClientsResume.setItem(tablerow, column, it)
                    else:
                        it.setFlags(it.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                        self.tableClientsResume.setItem(tablerow, column, it)

                tablerow+=1

            self.tableClientsResume.verticalHeader().hide()
            self.tableClientsResume.setItemDelegate(AlignDelegate(self.tableClientsResume))
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

        self.retranslateUi(ClientsGeneralResume_Window)
        QtCore.QMetaObject.connectSlotsByName(ClientsGeneralResume_Window)
        self.Button_Graphs.clicked.connect(self.graphsclientsselected)
        self.tableClientsResume.itemDoubleClicked.connect(self.on_item_double_clicked) #Asign function wjen double click on cell


    def retranslateUi(self, ClientsGeneralResume_Window):
        _translate = QtCore.QCoreApplication.translate
        ClientsGeneralResume_Window.setWindowTitle(_translate("ClientsGeneralResume_Window", "Resumen Clientes"))
        self.tableClientsResume.setSortingEnabled(True)
        item = self.tableClientsResume.horizontalHeaderItem(0)
        item.setText(_translate("ClientsGeneralResume_Window", "Cliente"))
        item = self.tableClientsResume.horizontalHeaderItem(1)
        item.setText(_translate("ClientsGeneralResume_Window", str(date.today().year-3)))
        item = self.tableClientsResume.horizontalHeaderItem(2)
        item.setText(_translate("ClientsGeneralResume_Window", str(date.today().year-2)))
        item = self.tableClientsResume.horizontalHeaderItem(3)
        item.setText(_translate("ClientsGeneralResume_Window", str(date.today().year-1)))
        item = self.tableClientsResume.horizontalHeaderItem(4)
        item.setText(_translate("ClientsGeneralResume_Window", str(date.today().year)))
        self.Button_Graphs.setText(_translate("ClientsGeneralResume_Window", "Gráfico"))


    def graphsclientsselected(self):
        for row in range(self.tableClientsResume.rowCount()):
            if self.tableClientsResume.item(row,0).checkState() == QtCore.Qt.CheckState.Checked:
                print([self.tableClientsResume.item(row,col).text() for col in range(2)])#range(self.tableClientsResume.columnCount())]) #PRINTA UNA LISTA POR CADA FILA CON TODOS LOS VALORES DE LA FILA

        commands_graph = ("""
                        SELECT COUNT(offers."num_offer"), product_type."variable"
                        FROM offers
                        INNER JOIN product_type ON (offers."material"=product_type."material")
                        WHERE ("responsible"=%s
                        AND
                        "offer_year"=%s
                        AND
                        "state"='Adjudicada')
                        GROUP BY product_type."variable"
                        """)
        conn = None
        try:
        # read the connection parameters
            params = config()
        # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # execution of commands
            data=("AC", date.today().year,)
            cur.execute(commands_graph, data)
            results2=cur.fetchall()
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

        count=[x[0] for x in results2]
        labels=[x[1] for x in results2]

        self.canvas2=FigureCanvas(Figure())
        ax=self.canvas2.figure.subplots()
        ax.pie(count,labels=labels,autopct='%1.1f%%')
        ax.set_title('Proporción equipos vendidos')

        self.canvas2.setMinimumSize(QtCore.QSize(500, 200))
        self.canvas2.setMaximumSize(QtCore.QSize(500, 200))
        self.canvas2.setObjectName("canvas2")
        self.gridLayout_2.addWidget(self.canvas2, 5, 0, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)


# Function to check if column index of double clicked cell is equal to first column index
    def on_item_double_clicked(self, item):
        if item.column() == 0:
            self.clientresume(item)


# Function when double clicked cell is in first column
    def clientresume(self, item):
        clientname=item.text()
        self.client_resume_window=QtWidgets.QMainWindow()
        self.ui=Ui_ClientResume_Window(clientname)
        self.ui.setupUi(self.client_resume_window)
        self.client_resume_window.showMaximized()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClientsGeneralResume_Window = QtWidgets.QMainWindow()
    ui = Ui_ClientsGeneralResume_Window()
    ui.setupUi(ClientsGeneralResume_Window)
    ClientsGeneralResume_Window.show()
    sys.exit(app.exec())
