# Form implementation generated from reading ui file 'CalibrationPrintCertificate_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import *
import psycopg2
from config import config
import os
import pandas as pd
from PDF_Styles import calibration_certificate_nuclear, calibration_certificate
from tkinter.filedialog import asksaveasfilename
from math import exp

basedir = r"\\nas01\DATOS\Comunes\EIPSA-ERP"


class Ui_CalibrationPrintCertificate_Window(object):
    def __init__(self, username):
        self.username = username

    def setupUi(self, CalibrationPrintCertificate_Window):
        CalibrationPrintCertificate_Window.setObjectName("CalibrationPrintCertificate_Window")
        CalibrationPrintCertificate_Window.resize(450, 325)
        CalibrationPrintCertificate_Window.setMinimumSize(QtCore.QSize(450, 325))
        CalibrationPrintCertificate_Window.setMaximumSize(QtCore.QSize(450, 325))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        CalibrationPrintCertificate_Window.setWindowIcon(icon)
        if self.username == 'm.gil':
            CalibrationPrintCertificate_Window.setStyleSheet("QWidget {\n"
    "background-color: #121212; color: rgb(255, 255, 255)\n"
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
    "}"
    )
        else:
            CalibrationPrintCertificate_Window.setStyleSheet("QWidget {\n"
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
    "}"
    )
        self.centralwidget = QtWidgets.QWidget(parent=CalibrationPrintCertificate_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 400, 275))
        self.frame.setMinimumSize(QtCore.QSize(400, 275))
        self.frame.setMaximumSize(QtCore.QSize(400, 275))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName = ("gridlayout")
        self.gridlayout.setVerticalSpacing(30)
        self.label_Order = QtWidgets.QLabel(parent=self.frame)
        self.label_Order.setMinimumSize(QtCore.QSize(100, 25))
        self.label_Order.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_Order.setFont(font)
        self.label_Order.setObjectName("label_Order")
        self.gridlayout.addWidget(self.label_Order, 0, 0, 1, 1)
        self.num_order_print = QtWidgets.QLineEdit(parent=self.frame)
        self.num_order_print.setMinimumSize(QtCore.QSize(150, 25))
        self.num_order_print.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.num_order_print.setFont(font)
        self.num_order_print.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.num_order_print.setObjectName("num_order_print")
        self.gridlayout.addWidget(self.num_order_print, 0, 1, 1, 1)
        self.label_Date = QtWidgets.QLabel(parent=self.frame)
        self.label_Date.setMinimumSize(QtCore.QSize(100, 25))
        self.label_Date.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_Date.setFont(font)
        self.label_Date.setObjectName("label_Date")
        self.gridlayout.addWidget(self.label_Date, 1, 0, 1, 1)
        self.Cert_Date = QtWidgets.QComboBox(parent=self.frame)
        self.Cert_Date.setMinimumSize(QtCore.QSize(150, 25))
        self.Cert_Date.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cert_Date.setFont(font)
        self.Cert_Date.setObjectName("Cert_Date")
        self.gridlayout.addWidget(self.Cert_Date, 1, 1, 1, 1)
        self.label_Sensor = QtWidgets.QLabel(parent=self.frame)
        self.label_Sensor.setMinimumSize(QtCore.QSize(75, 25))
        self.label_Sensor.setMaximumSize(QtCore.QSize(75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_Sensor.setFont(font)
        self.label_Sensor.setObjectName("label_Sensor")
        self.gridlayout.addWidget(self.label_Sensor, 2, 0, 1, 1)
        self.Sensor = QtWidgets.QComboBox(parent=self.frame)
        self.Sensor.setMinimumSize(QtCore.QSize(150, 25))
        self.Sensor.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Sensor.setFont(font)
        self.Sensor.setObjectName("Sensor")
        self.gridlayout.addWidget(self.Sensor, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridlayout, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_Print = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Print.setEnabled(True)
        self.Button_Print.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_Print.setMinimumSize(QtCore.QSize(100, 35))
        self.Button_Print.setMaximumSize(QtCore.QSize(100, 35))
        self.Button_Print.setAutoDefault(True)
        self.Button_Print.setObjectName("Button_Print")
        self.horizontalLayout.addWidget(self.Button_Print)
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.Button_Cancel = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Cancel.setEnabled(True)
        self.Button_Cancel.setMinimumSize(QtCore.QSize(100, 35))
        self.Button_Cancel.setMaximumSize(QtCore.QSize(100, 35))
        self.Button_Cancel.setAutoDefault(True)
        self.Button_Cancel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_Cancel.setObjectName("Button_Cancel")
        self.horizontalLayout.addWidget(self.Button_Cancel)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 4, 0, 1, 1)
        CalibrationPrintCertificate_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=CalibrationPrintCertificate_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 22))
        self.menubar.setObjectName("menubar")
        CalibrationPrintCertificate_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=CalibrationPrintCertificate_Window)
        self.statusbar.setObjectName("statusbar")
        CalibrationPrintCertificate_Window.setStatusBar(self.statusbar)
        CalibrationPrintCertificate_Window.setWindowFlags(QtCore.Qt.WindowType.WindowMinimizeButtonHint)

        self.retranslateUi(CalibrationPrintCertificate_Window)
        self.Button_Cancel.clicked.connect(CalibrationPrintCertificate_Window.close) # type: ignore
        self.Button_Print.clicked.connect(self.CalibrationPrintCertificate)
        self.num_order_print.returnPressed.connect(self.charge_dates)
        self.Cert_Date.currentTextChanged.connect(self.charge_sensor)
        QtCore.QMetaObject.connectSlotsByName(CalibrationPrintCertificate_Window)


    def retranslateUi(self, CalibrationPrintCertificate_Window):
        _translate = QtCore.QCoreApplication.translate
        CalibrationPrintCertificate_Window.setWindowTitle(_translate("CalibrationPrintCertificate_Window", "Imprimir Certificado"))
        self.Button_Print.setText(_translate("CalibrationPrintCertificate_Window", "Imprimir"))
        self.Button_Cancel.setText(_translate("CalibrationPrintCertificate_Window", "Cancelar"))
        self.label_Order.setText(_translate("CalibrationPrintCertificate_Window", "Nº Pedido:"))
        self.label_Sensor.setText(_translate("CalibrationPrintCertificate_Window", "Sensor:"))
        self.label_Date.setText(_translate("CalibrationPrintCertificate_Window", "Fecha:"))

    def CalibrationPrintCertificate(self):
        numorder=self.num_order_print.text()
        sensor_type=self.Sensor.currentText()
        cert_date = self.Cert_Date.currentText()

        numorder_check = numorder if numorder[:2] == 'PA' or len(numorder) > 8 else numorder + '-S00'

        if numorder=="":
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("Imprimir Certificado")
            dlg.setText("Introduce un número de pedido")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            dlg.exec()

        else:
            commands_checkorder = ("""
                        SELECT *
                        FROM orders
                        WHERE "num_order" = %s
                        """)
            conn = None
            try:
            # read the connection parameters
                params = config()
            # connect to the PostgreSQL server
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
            # execution of commands one by one
                cur.execute(commands_checkorder,(numorder_check,))
                results=cur.fetchall()
                match=list(filter(lambda x:numorder_check in x, results))
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

            if len(match)==0:
                    dlg = QtWidgets.QMessageBox()
                    new_icon = QtGui.QIcon()
                    new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                    dlg.setWindowIcon(new_icon)
                    dlg.setWindowTitle("Imprimir Certificado")
                    dlg.setText("El número de pedido introducido no existe")
                    dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    dlg.exec()

            else:
                commands_calib_data = ("""
                        SELECT "tag", "master", "master_1", "element_1", "error_1", "tolerance_1",
                        "master_2", "element_2", "error_2", "tolerance_2",
                        "master_3", "element_3", "error_3", "tolerance_3",
                        "master_4", "element_4", "error_4", "tolerance_4"
                        FROM verification.calibration_thermoelements
                        WHERE "num_order" = %s
                        AND
                        "test_date" = %s
                        AND
                        "sensor" = %s
                        """)

                conn = None
                try:
                # read the connection parameters
                    params = config()
                # connect to the PostgreSQL server
                    conn = psycopg2.connect(**params)
                    cur = conn.cursor()
                # execution of commands
                    cur.execute(commands_calib_data, (numorder, cert_date, sensor_type,))
                    results = cur.fetchall()

                    df = pd.DataFrame(results, columns=["tag", "master", "master_1", "element_1", "error_1", "tolerance_1",
                                            "master_2", "element_2", "error_2", "tolerance_2",
                                            "master_3", "element_3", "error_3", "tolerance_3",
                                            "master_4", "element_4", "error_4", "tolerance_4"])

                    df.sort_values(by=['tag'])

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

                master_element = df.iloc[0,1]

                pdf = calibration_certificate(numorder, cert_date, sensor_type, master_element)
                pdf.set_auto_page_break(auto=True, margin=2)
                pdf.add_page()
                pdf.alias_nb_pages()

                items = df.shape[0]

                for row in range(items):
                    pdf.set_x(1)
                    y_position = pdf.get_y()
                    pdf.set_font('Helvetica', '', 8)
                    pdf.cell(3, 0.8, str(df.iloc[row, 0]), align='L', border=1)
                    pdf.set_font('Helvetica', '', 7)
                    pdf.cell(1.1, 0.8, str(self.calculate_master(df.iloc[row, 2], master_element)).replace('.',','), align='C', border=1)
                    pdf.cell(1, 0.8, str(round(df.iloc[row, 2], 3)).replace('.', ',') if df.iloc[row, 2] is not None else "N/A", align='C', border=1)
                    pdf.cell(1.1, 0.8, str(self.calculate_element(df.iloc[row, 3], sensor_type)).replace('.',','), align='C', border=1)
                    pdf.cell(1, 0.8, str(round(df.iloc[row, 3], 3)).replace('.', ',') if df.iloc[row, 3] is not None else "N/A", align='C', border=1)
                    pdf.cell(1, 0.8, str(round(df.iloc[row, 4], 3)).replace('.', ',') if df.iloc[row, 4] is not None else "N/A", align='C', border=1)
                    pdf.cell(1, 0.8, "± " + str(round(df.iloc[row, 5], 3)).replace('.', ',') if df.iloc[row, 5] is not None else "N/A", align='C', border=1)

                    pdf.cell(1.1, 0.8, str(self.calculate_master(df.iloc[row, 6], master_element)).replace('.',','), align='C', border=1)
                    pdf.cell(1, 0.8, str(round(df.iloc[row, 6], 3)).replace('.', ',') if df.iloc[row, 6] is not None else "N/A", align='C', border=1)
                    pdf.cell(1.1, 0.8, str(self.calculate_element(df.iloc[row, 7], sensor_type)).replace('.',','), align='C', border=1)
                    pdf.cell(1, 0.8, str(round(df.iloc[row, 7], 3)).replace('.', ',') if df.iloc[row, 7] is not None else "N/A", align='C', border=1)
                    pdf.cell(1, 0.8, str(round(df.iloc[row, 8], 3)).replace('.', ',') if df.iloc[row, 8] is not None else "N/A", align='C', border=1)
                    pdf.cell(1, 0.8, "± " + str(round(df.iloc[row, 9], 3)).replace('.', ',') if df.iloc[row, 9] is not None else "N/A", align='C', border=1)

                    pdf.cell(1.1, 0.8, str(self.calculate_master(df.iloc[row, 10], master_element)).replace('.',','), align='C', border=1)
                    pdf.cell(1, 0.8, str(round(df.iloc[row, 10], 3)).replace('.', ',') if df.iloc[row, 10] is not None else "N/A", align='C', border=1)
                    pdf.cell(1.1, 0.8, str(self.calculate_element(df.iloc[row, 11], sensor_type)).replace('.',','), align='C', border=1)
                    pdf.cell(1, 0.8, str(round(df.iloc[row, 11], 3)).replace('.', ',') if df.iloc[row, 11] is not None else "N/A", align='C', border=1)
                    pdf.cell(1, 0.8, str(round(df.iloc[row, 12], 3)).replace('.', ',') if df.iloc[row, 12] is not None else "N/A", align='C', border=1)
                    pdf.cell(1, 0.8, "± " + str(round(df.iloc[row, 13], 3)).replace('.', ',') if df.iloc[row, 13] is not None else "N/A", align='C', border=1)

                    pdf.cell(1.1, 0.8, str(self.calculate_master(df.iloc[row, 14], master_element)).replace('.',','), align='C', border=1)
                    pdf.cell(1, 0.8, str(round(df.iloc[row, 14], 3)).replace('.', ',') if df.iloc[row, 14] is not None else "N/A", align='C', border=1)
                    pdf.cell(1.1, 0.8, str(self.calculate_element(df.iloc[row, 15], sensor_type)).replace('.',','), align='C', border=1)
                    pdf.cell(1, 0.8, str(round(df.iloc[row, 15], 3)).replace('.', ',') if df.iloc[row, 15] is not None else "N/A", align='C', border=1)
                    pdf.cell(1, 0.8, str(round(df.iloc[row, 16], 3)).replace('.', ',') if df.iloc[row, 16] is not None else "N/A", align='C', border=1)
                    pdf.cell(1, 0.8, "± " + str(round(df.iloc[row, 17], 3)).replace('.', ',') if df.iloc[row, 17] is not None else "N/A", align='C', border=1)
                    pdf.ln(0.8)
                    y_position = pdf.get_y()

                    pdf.set_line_width(0.05)
                    marks_table=3.5
                    pdf.line(1, y_position, 1, marks_table)

                    mark0=3
                    pdf.line(4, y_position, 4, mark0)
                    pdf.line(10.2, y_position, 10.2, mark0)
                    pdf.line(16.4, y_position, 16.4, mark0)
                    pdf.line(22.6, y_position, 22.6, mark0)
                    pdf.line(28.8, y_position, 28.8, mark0)
                    pdf.set_line_width(0.01)

                pdf.set_line_width(0.05)
                pdf.line(1, y_position, 28.8, y_position)

                pdf.image(os.path.abspath(os.path.join(basedir, "Resources/Iconos/QualityControlStamp.png")), 24, y_position + 2, 4.5, 3)

                output_path = "//nas01/DATOS/Comunes/MARIO GIL/VERIFICACION/CERTIFICADOS CALIBRACIÓN/" + numorder.replace('/','-') + '-' + sensor_type + ".pdf"

                if output_path:
                    try:
                        pdf.output(output_path)

                        dlg = QtWidgets.QMessageBox()
                        new_icon = QtGui.QIcon()
                        new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                        dlg.setWindowIcon(new_icon)
                        dlg.setWindowTitle("Certificado Calibración")
                        dlg.setText("PDF Generado con éxito")
                        dlg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        dlg.exec()
                        del dlg, new_icon

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


    def charge_dates(self):
        numorder=self.num_order_print.text().upper()

        if numorder=="":
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("Imprimir Certificado")
            dlg.setText("Introduce un número de pedido")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            dlg.exec()

        else:
            commands_querydates = ("""
                        SELECT DISTINCT TO_CHAR(test_date, 'DD/MM/YYYY')
                        FROM verification.calibration_thermoelements
                        WHERE UPPER("num_order") = UPPER(%s)
                        """)
            conn = None
            try:
            # read the connection parameters
                params = config()
            # connect to the PostgreSQL server
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
            # execution of commands one by one
                cur.execute(commands_querydates,(numorder,))
                results_dates=cur.fetchall()
                
                list_dates = [x[0] for x in results_dates]

                self.Cert_Date.clear()
                self.Cert_Date.addItems(list_dates)
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

            self.num_order_print.setText(numorder)


    def charge_sensor(self):
        numorder=self.num_order_print.text().upper()
        date_test = self.Cert_Date.currentText()

        if numorder=="":
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("Imprimir Certificado")
            dlg.setText("Introduce un número de pedido")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            dlg.exec()

        else:
            commands_querysensor = ("""
                        SELECT DISTINCT sensor
                        FROM verification.calibration_thermoelements
                        WHERE UPPER("num_order") = UPPER(%s) AND "test_date" = %s
                        """)
            conn = None
            try:
            # read the connection parameters
                params = config()
            # connect to the PostgreSQL server
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
            # execution of commands one by one
                cur.execute(commands_querysensor, (numorder, date_test,))
                results_dates=cur.fetchall()

                list_sensor = [x[0] for x in results_dates]

                self.Sensor.clear()
                self.Sensor.addItems(list_sensor)
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


    def calculate_master(self, temp, master):
        if temp is not None:
            if master in ['EIPSA-020', 'EIPSA-TE-01']:
                column_select = 'inta_pt100_values.' + master.replace('-','_')
                commands_intavalues = f"""
                                    SELECT {column_select}
                                    FROM verification.inta_pt100_values
                                    ORDER BY variables
                                    """
                conn = None
                try:
                # read the connection parameters
                    params = config()
                # connect to the PostgreSQL server
                    conn = psycopg2.connect(**params)
                    cur = conn.cursor()
                # execution of commands
                    cur.execute(commands_intavalues)
                    results = cur.fetchall()

                    a_inta = results[0][0]
                    b_inta = results[1][0]
                    c_inta = results[2][0]
                    r_zero = results[3][0]

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

                if temp < 0:
                    final_value = round(r_zero * (1 + a_inta * temp + b_inta * temp**2 + c_inta* (temp - 100) * temp**3), 3)
                else:
                    final_value = round(r_zero * (1 + a_inta * temp + b_inta * temp**2), 3)
            else:
                column_select = 'inta_tc_values.' + master.replace('-','_')
                commands_intavalues = f"""
                                    SELECT {column_select}
                                    FROM verification.inta_tc_values
                                    ORDER BY variables
                                    """
                conn = None
                try:
                # read the connection parameters
                    params = config()
                # connect to the PostgreSQL server
                    conn = psycopg2.connect(**params)
                    cur = conn.cursor()
                # execution of commands
                    cur.execute(commands_intavalues)
                    results = cur.fetchall()

                    a_inta = results[0][0]
                    b_inta = results[1][0]
                    c_inta = results[2][0]

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
                    print(error)
                    dlg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                    dlg.exec()
                    del dlg, new_icon

                finally:
                    if conn is not None:
                        conn.close()

                final_value = round((a_inta + b_inta * temp* + c_inta * temp**2)/1000, 3)

        else:
            final_value = 'N/A'

        return final_value


    def calculate_element(self, temp, sensor):
        if temp is not None:
            if 'PT100' in sensor:
                commands_stdvalues = ("""
                                    SELECT values
                                    FROM verification.standard_pt100_values
                                    ORDER BY variables
                                    """)
                conn = None
                try:
                # read the connection parameters
                    params = config()
                # connect to the PostgreSQL server
                    conn = psycopg2.connect(**params)
                    cur = conn.cursor()
                # execution of commands
                    cur.execute(commands_stdvalues)
                    results = cur.fetchall()

                    a_std = results[0][0]
                    b_std = results[1][0]
                    c_std = results[2][0]
                    r_zero = results[3][0]

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

                if temp < 0:
                    final_value = round(r_zero * (1 + a_std * temp + b_std * temp**2 + c_std* (temp - 100) * temp**3), 3)
                else:
                    final_value = round(r_zero * (1 + a_std * temp + b_std * temp**2), 3)

            else:
                if 'B' in sensor:
                    table = 'verification.standard_tc_b_values'
                    column = 'low' if temp <= 630.615 else 'high'
                elif 'C' in sensor:
                    table = 'verification.standard_tc_c_values'
                    column = 'low' if temp <= 630.615 else 'high'
                elif 'E' in sensor:
                    table = 'verification.standard_tc_e_values'
                    column = 'low' if temp <= 0 else 'high'
                elif 'J' in sensor:
                    table = 'verification.standard_tc_j_values'
                    column = 'low' if temp <= 760 else 'high'
                elif 'K' in sensor:
                    table = 'verification.standard_tc_k_values'
                    column = 'low' if temp <= 0 else 'high'
                elif 'N' in sensor:
                    table = 'verification.standard_tc_n_values'
                    column = 'low' if temp <= 0 else 'high'
                elif 'R' in sensor:
                    table = 'verification.standard_tc_r_values'
                    column = 'low' if temp <= 1064.18 else ('medium' if temp <= 1664.5 else 'high')
                elif 'S' in sensor:
                    table = 'verification.standard_tc_s_values'
                    column = 'low' if temp <= 1064.18 else ('medium' if temp <= 1664.5 else 'high')
                elif 'T' in sensor:
                    table = 'verification.standard_tc_t_values'
                    column = 'low' if temp <= 0 else 'high'

                commands_stdvalues = f"""
                                    SELECT {column}
                                    FROM {table}
                                    ORDER BY id
                                    """
                conn = None
                try:
                # read the connection parameters
                    params = config()
                # connect to the PostgreSQL server
                    conn = psycopg2.connect(**params)
                    cur = conn.cursor()
                # execution of commands
                    cur.execute(commands_stdvalues)
                    results = cur.fetchall()

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

                final_value = 0

                if 'K' in sensor:
                    for i in range(len(results)-2):
                        final_value += float(results[i][0]) * float(temp)**i

                    final_value += float(results[11][0]) * exp(float(results[12][0]) * (float(temp) - 126.9686)**2)

                else:
                    for i in range(len(results)):
                        final_value += results[i][0] * temp**i

                final_value = round(final_value, 3)

        else:
            final_value = 'N/A'

        return final_value


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    CalibrationPrintCertificate_Window = QtWidgets.QMainWindow()
    ui = Ui_CalibrationPrintCertificate_Window('m.gil')
    ui.setupUi(CalibrationPrintCertificate_Window)
    CalibrationPrintCertificate_Window.show()
    sys.exit(app.exec())