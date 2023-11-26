# Form implementation generated from reading ui file 'OrderAccept_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import psycopg2
from config import config  
import os
from docxtpl import DocxTemplate
from tkinter.filedialog import asksaveasfilename
from datetime import *
import locale
from babel.dates import format_date


basedir = r"\\nas01\DATOS\Comunes\EIPSA-ERP"


class Ui_OrderAccept_Window(object):
    def __init__(self, username=None):
        self.username=username

    def setupUi(self, OrderAccept_Window):
        OrderAccept_Window.setObjectName("OrderAccept_Window")
        OrderAccept_Window.resize(300, 450)
        OrderAccept_Window.setMinimumSize(QtCore.QSize(300, 450))
        OrderAccept_Window.setMaximumSize(QtCore.QSize(300, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        OrderAccept_Window.setWindowIcon(icon)
        OrderAccept_Window.setAutoFillBackground(False)
        OrderAccept_Window.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=OrderAccept_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_numorder_orderaccept = QtWidgets.QLabel(parent=self.frame)
        self.label_numorder_orderaccept.setEnabled(True)
        self.label_numorder_orderaccept.setMinimumSize(QtCore.QSize(200, 25))
        self.label_numorder_orderaccept.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_numorder_orderaccept.setFont(font)
        self.label_numorder_orderaccept.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_numorder_orderaccept.setObjectName("label_numorder_orderaccept")
        self.verticalLayout.addWidget(self.label_numorder_orderaccept, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.numorder_orderaccept = QtWidgets.QLineEdit(parent=self.frame)
        self.numorder_orderaccept.setEnabled(True)
        self.numorder_orderaccept.setMinimumSize(QtCore.QSize(200, 25))
        self.numorder_orderaccept.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.numorder_orderaccept.setFont(font)
        self.numorder_orderaccept.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.numorder_orderaccept.setObjectName("numorder_orderaccept")
        self.verticalLayout.addWidget(self.numorder_orderaccept, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_revision_orderaccept = QtWidgets.QLabel(parent=self.frame)
        self.label_revision_orderaccept.setEnabled(True)
        self.label_revision_orderaccept.setMinimumSize(QtCore.QSize(200, 25))
        self.label_revision_orderaccept.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_revision_orderaccept.setFont(font)
        self.label_revision_orderaccept.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_revision_orderaccept.setObjectName("label_revision_orderaccept")
        self.verticalLayout.addWidget(self.label_revision_orderaccept, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.revision_orderaccept = QtWidgets.QLineEdit(parent=self.frame)
        self.revision_orderaccept.setEnabled(True)
        self.revision_orderaccept.setMinimumSize(QtCore.QSize(200, 100))
        self.revision_orderaccept.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.revision_orderaccept.setFont(font)
        self.revision_orderaccept.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.revision_orderaccept.setObjectName("revision_orderaccept")
        self.verticalLayout.addWidget(self.revision_orderaccept, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.checkbox_bond = QtWidgets.QCheckBox(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkbox_bond.setFont(font)
        self.checkbox_bond.setObjectName("checkbox_bond")
        self.verticalLayout.addWidget(self.checkbox_bond, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.hLayout1 = QtWidgets.QHBoxLayout()
        self.hLayout1.setObjectName("hLayout1")
        self.longformat = QtWidgets.QRadioButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.longformat.setFont(font)
        self.longformat.setObjectName("longformat")
        self.hLayout1.addWidget(self.longformat)
        self.shortformat = QtWidgets.QRadioButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.shortformat.setFont(font)
        self.shortformat.setObjectName("shortformat")
        self.hLayout1.addWidget(self.shortformat)
        self.verticalLayout.addLayout(self.hLayout1)
        self.generate_orderaccept = QtWidgets.QPushButton(parent=self.frame)
        self.generate_orderaccept.setEnabled(True)
        self.generate_orderaccept.setMinimumSize(QtCore.QSize(200, 35))
        self.generate_orderaccept.setMaximumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.generate_orderaccept.setFont(font)
        self.generate_orderaccept.setStyleSheet("QPushButton {\n"
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
        self.generate_orderaccept.setAutoDefault(True)
        self.generate_orderaccept.setObjectName("generate_orderaccept")
        self.verticalLayout.addWidget(self.generate_orderaccept, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        OrderAccept_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=OrderAccept_Window)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 275, 22))
        self.menubar.setObjectName("menubar")
        OrderAccept_Window.setMenuBar(self.menubar)

        self.retranslateUi(OrderAccept_Window)
        self.generate_orderaccept.clicked.connect(lambda: self.generateoffer(OrderAccept_Window))
        self.revision_orderaccept.returnPressed.connect(lambda: self.generateoffer(OrderAccept_Window))
        QtCore.QMetaObject.connectSlotsByName(OrderAccept_Window)


    def retranslateUi(self, OrderAccept_Window):
        _translate = QtCore.QCoreApplication.translate
        OrderAccept_Window.setWindowTitle(_translate("OrderAccept_Window", "Generar Acuse Pedido"))
        self.label_numorder_orderaccept.setText(_translate("OrderAccept_Window", "Número Pedido:"))
        self.label_revision_orderaccept.setText(_translate("OrderAccept_Window", "Revisión:"))
        self.generate_orderaccept.setText(_translate("OrderAccept_Window", "Generar"))
        self.checkbox_bond.setText(_translate("OrderAccept_Window", "Aval"))
        self.longformat.setText(_translate("TAGOfferToOrder_Window", "Formato Largo"))
        self.shortformat.setText(_translate("TAGOfferToOrder_Window", "Formato Corto"))


    def generateoffer(self, OrderAccept_Window):
        numorder=self.numorder_orderaccept.text()
        revision=self.revision_orderaccept.text()
        actual_date=date.today()

        locale.setlocale(locale.LC_TIME, '')
        locale_actual = locale.getlocale(locale.LC_TIME)

        english_actual_date = format_date(actual_date, format='long', locale='en')

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
            cur.execute(commands_checkorder,(numorder,))
            results=cur.fetchall()
            match=list(filter(lambda x:numorder in x, results))
        # close communication with the PostgreSQL database server
            cur.close()
        # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        if numorder=="" or (numorder==" " or len(match)==0):
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("Generar Acuse Pedido")
            dlg.setText("El número de pedido no se encuentra registrado")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            dlg.exec()
            del dlg, new_icon

        else:
            commands_queryorder = ("""
                                SELECT orders."num_order",offers."num_offer", orders."num_ref_order", offers."client", orders."expected_date", orders."order_amount", orders."order_date", offers."delivery_term", offers."delivery_time", offers."payment_term", offers."validity"
                                FROM offers
                                INNER JOIN orders ON (offers."num_offer"=orders."num_offer")
                                WHERE orders."num_order" = %s
                                ORDER BY orders."num_order"
                                """)
            conn = None
            try:
            # read the connection parameters
                params = config()
            # connect to the PostgreSQL server
                conn = psycopg2.connect(**params)
                cur=conn.cursor()
                cur.execute(commands_queryorder,(numorder,))
                results_queryorder=cur.fetchall()

            # close communication with the PostgreSQL database server
            # commit the changes
                conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()

            num_order = results_queryorder[0][0]
            num_offer = results_queryorder[0][1]
            num_ref_order = results_queryorder[0][2]
            client = results_queryorder[0][3]
            expected_date = results_queryorder[0][4]
            order_amount = results_queryorder[0][5]
            order_date = results_queryorder[0][6]
            delivery_term = results_queryorder[0][7]
            delivery_time = results_queryorder[0][8]
            payment_term_db = results_queryorder[0][9]
            # validity = int(results_queryorder[0][10])
            validity = 30

            expected_date += timedelta(days=(validity + 28))

            payment_term_db = "90_10"

            if payment_term_db == "100_delivery":
                payment_term_english = "100% of total amount of purchase order upon delivery of material according to Incoterms 2020"
                payment_term_spanish = "Pago del 100% del valor total de la orden de compra a la entrega del material según Incoterm 2020"
            elif payment_term_db == "100_order":
                payment_term_english = "100% of the total amount of purchase order upon receipt of purchase order."
                payment_term_spanish = "Pago del 100% del valor total de la orden de compra a la recepción de la orden."
            elif payment_term_db == "90_10":
                payment_term_english = "90% of the total amount of PO upon delivery of material according to Incoterms 2020 and 10% at take over certificate."
                payment_term_spanish = "Pago del 90% del Valor total de la orden de compra a la entrega del material según Incoterm 2020 y el 10% restante con la certificación final."
            elif payment_term_db == "50_50":
                payment_term_english = "50% of the total amount of purchase order upon receipt of purchase order. Remaining 50% before be delivered according to Incoterms 2020"
                payment_term_spanish = "Pago del 50% del valor total de la orden de compra a la recepción de la orden. El 50% restante antes de la entrega del material según Incoterm 2020"
            elif payment_term_db == "Others":
                    payment_term_english = "PAYMENT TERMS TO BE DEFINED"
                    payment_term_spanish = "TERMINOS DE PAGO POR DEFINIR"

            english_estimated_date = format_date(expected_date, format='long', locale='en')
            spanish_estimated_date = format_date(expected_date, format='long', locale='es')

            english_order_date = format_date(order_date, format='long', locale='en')
            spanish_order_date = format_date(order_date, format='long', locale='es')

            if self.checkbox_bond.isChecked():
                note_bond_english = "The text of warranty bond will be according to the usual document agreed with " + client + " for the last projects."
                note_bond_spanish = "El texto del aval será de acuerdo al documento habitual acordado con " + client + " para los últimos proyectos"
            else:
                note_bond_english = "Note that for orders with an amount lower than 30.000,00 €, warranty bonds are not issued."
                note_bond_spanish = "Les hacemos notar que para pedidos con importe inferior a 30.000,00 € no se emiten avales bancarios de garantía"

            if self.longformat.isChecked()==True:
                doc = DocxTemplate(r"\\nas01\DATOS\Comunes\EIPSA-ERP\Plantillas Exportación\Plantilla Acuse Pedido.docx")
                context = {'english_actual_date': english_actual_date,
                            'num_ref_order': num_ref_order,
                            'num_order': num_order,
                            'english_order_date': english_order_date,
                            'spanish_order_date': spanish_order_date,
                            'order_amount': order_amount,
                            'delivery_term': delivery_term,
                            'delivery_time': delivery_time,
                            'payment_term_english': payment_term_english,
                            'payment_term_spanish': payment_term_spanish,
                            'english_estimated_date': english_estimated_date,
                            'spanish_estimated_date': spanish_estimated_date,
                            'num_offer': num_offer,
                            'client': client,
                            'note_bond_english': note_bond_english,
                            'note_bond_spanish': note_bond_spanish}
                doc.render(context)
                self.save_document(doc)

                dlg = QtWidgets.QMessageBox()
                new_icon = QtGui.QIcon()
                new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                dlg.setWindowIcon(new_icon)
                dlg.setWindowTitle("Generar Acuse")
                dlg.setText("Acuse generado con éxito\n\n"
                            "Revise los apartados de plazo de entrega, incoterms y aval")
                dlg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                dlg.exec()
                del dlg, new_icon
                OrderAccept_Window.close()

            elif self.shortformat.isChecked()==True:
                doc = DocxTemplate(r"\\nas01\DATOS\Comunes\EIPSA-ERP\Plantillas Exportación\Plantilla Acuse Corto Pedido.docx")
                context = {'client': "World company"}
                doc.render(context)
                self.save_document(doc)

                dlg = QtWidgets.QMessageBox()
                new_icon = QtGui.QIcon()
                new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                dlg.setWindowIcon(new_icon)
                dlg.setWindowTitle("Generar Acuse")
                dlg.setText("Acuse generado con éxito\n\n"
                            "Revise los apartados de plazo de entrega, incoterms y aval")
                dlg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                dlg.exec()
                del dlg, new_icon
                OrderAccept_Window.close()

            else:
                dlg = QtWidgets.QMessageBox()
                new_icon = QtGui.QIcon()
                new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                dlg.setWindowIcon(new_icon)
                dlg.setWindowTitle("Generar Acuse")
                dlg.setText("Elige un formato")
                dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                dlg.exec()
                del dlg, new_icon


    def save_document(self, document):
        output_path_accept = asksaveasfilename(
                defaultextension=".docx",
                filetypes=[("Archivos de Word", "*.docx")],
                title="Guardar Acuse Pedido",
            )
        if output_path_accept:
            document.save(output_path_accept)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OrderAccept_Window = QtWidgets.QMainWindow()
    ui = Ui_OrderAccept_Window()
    ui.setupUi(OrderAccept_Window)
    OrderAccept_Window.show()
    sys.exit(app.exec())