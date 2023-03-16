# Form implementation generated from reading ui file 'NewOrder_Window.ui'
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

class Ui_New_Order_Window(object):
    def setupUi(self, New_Order):
        New_Order.setObjectName("New_Order")
        New_Order.resize(680, 425)
        New_Order.setMinimumSize(QtCore.QSize(680, 425))
        New_Order.setMaximumSize(QtCore.QSize(680, 425))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        New_Order.setWindowIcon(icon)
        New_Order.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=New_Order)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.hLayout = QtWidgets.QHBoxLayout()
        self.hLayout.setObjectName("hLayout")
        self.vLayout1 = QtWidgets.QVBoxLayout()
        self.vLayout1.setContentsMargins(0, -1, 0, -1)
        self.vLayout1.setObjectName("vLayout1")
        self.label_NumOrder = QtWidgets.QLabel(parent=self.frame)
        self.label_NumOrder.setMinimumSize(QtCore.QSize(105, 25))
        self.label_NumOrder.setMaximumSize(QtCore.QSize(105, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_NumOrder.setFont(font)
        self.label_NumOrder.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_NumOrder.setObjectName("label_NumOrder")
        self.vLayout1.addWidget(self.label_NumOrder)
        spacerItem1 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout1.addItem(spacerItem1)
        self.label_NumOffer = QtWidgets.QLabel(parent=self.frame)
        self.label_NumOffer.setMinimumSize(QtCore.QSize(105, 25))
        self.label_NumOffer.setMaximumSize(QtCore.QSize(105, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_NumOffer.setFont(font)
        self.label_NumOffer.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_NumOffer.setObjectName("label_NumOffer")
        self.vLayout1.addWidget(self.label_NumOffer)
        spacerItem2 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout1.addItem(spacerItem2)
        self.label_NumRef = QtWidgets.QLabel(parent=self.frame)
        self.label_NumRef.setMinimumSize(QtCore.QSize(105, 25))
        self.label_NumRef.setMaximumSize(QtCore.QSize(105, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_NumRef.setFont(font)
        self.label_NumRef.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_NumRef.setObjectName("label_NumRef")
        self.vLayout1.addWidget(self.label_NumRef)
        self.hLayout.addLayout(self.vLayout1)
        self.vLayout2 = QtWidgets.QVBoxLayout()
        self.vLayout2.setObjectName("vLayout2")
        self.NumOrder_NewOrder = QtWidgets.QLineEdit(parent=self.frame)
        self.NumOrder_NewOrder.setMinimumSize(QtCore.QSize(175, 25))
        self.NumOrder_NewOrder.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NumOrder_NewOrder.setFont(font)
        self.NumOrder_NewOrder.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.NumOrder_NewOrder.setObjectName("NumOrder_NewOrder")
        self.vLayout2.addWidget(self.NumOrder_NewOrder)
        spacerItem3 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout2.addItem(spacerItem3)
        self.NumOffer_NewOrder = QtWidgets.QLineEdit(parent=self.frame)
        self.NumOffer_NewOrder.setMinimumSize(QtCore.QSize(175, 25))
        self.NumOffer_NewOrder.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NumOffer_NewOrder.setFont(font)
        self.NumOffer_NewOrder.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.NumOffer_NewOrder.setObjectName("NumOffer_NewOrder")
        self.vLayout2.addWidget(self.NumOffer_NewOrder)
        spacerItem4 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout2.addItem(spacerItem4)
        self.NumRef_NewOrder = QtWidgets.QLineEdit(parent=self.frame)
        self.NumRef_NewOrder.setMinimumSize(QtCore.QSize(175, 25))
        self.NumRef_NewOrder.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NumRef_NewOrder.setFont(font)
        self.NumRef_NewOrder.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.NumRef_NewOrder.setObjectName("NumRef_NewOrder")
        self.vLayout2.addWidget(self.NumRef_NewOrder)
        self.hLayout.addLayout(self.vLayout2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hLayout.addItem(spacerItem5)
        self.vLayout3 = QtWidgets.QVBoxLayout()
        self.vLayout3.setObjectName("vLayout3")
        self.label_ContracDate = QtWidgets.QLabel(parent=self.frame)
        self.label_ContracDate.setMinimumSize(QtCore.QSize(130, 25))
        self.label_ContracDate.setMaximumSize(QtCore.QSize(130, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_ContracDate.setFont(font)
        self.label_ContracDate.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_ContracDate.setObjectName("label_ContracDate")
        self.vLayout3.addWidget(self.label_ContracDate)
        spacerItem6 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout3.addItem(spacerItem6)
        self.label_NumItems = QtWidgets.QLabel(parent=self.frame)
        self.label_NumItems.setMinimumSize(QtCore.QSize(130, 25))
        self.label_NumItems.setMaximumSize(QtCore.QSize(130, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_NumItems.setFont(font)
        self.label_NumItems.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_NumItems.setObjectName("label_NumItems")
        self.vLayout3.addWidget(self.label_NumItems)
        spacerItem7 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout3.addItem(spacerItem7)
        self.label_Amount = QtWidgets.QLabel(parent=self.frame)
        self.label_Amount.setMinimumSize(QtCore.QSize(130, 25))
        self.label_Amount.setMaximumSize(QtCore.QSize(130, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_Amount.setFont(font)
        self.label_Amount.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_Amount.setObjectName("label_Amount")
        self.vLayout3.addWidget(self.label_Amount)
        self.hLayout.addLayout(self.vLayout3)
        self.vlLayout4 = QtWidgets.QVBoxLayout()
        self.vlLayout4.setObjectName("vlLayout4")
        self.ContracDate_NewOrder = QtWidgets.QLineEdit(parent=self.frame)
        self.ContracDate_NewOrder.setMinimumSize(QtCore.QSize(175, 25))
        self.ContracDate_NewOrder.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ContracDate_NewOrder.setFont(font)
        self.ContracDate_NewOrder.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ContracDate_NewOrder.setObjectName("ContracDate_NewOrder")
        self.vlLayout4.addWidget(self.ContracDate_NewOrder)
        spacerItem8 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vlLayout4.addItem(spacerItem8)
        self.NumItems_NewOrder = QtWidgets.QLineEdit(parent=self.frame)
        self.NumItems_NewOrder.setMinimumSize(QtCore.QSize(175, 25))
        self.NumItems_NewOrder.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NumItems_NewOrder.setFont(font)
        self.NumItems_NewOrder.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.NumItems_NewOrder.setObjectName("NumItems_NewOrder")
        self.vlLayout4.addWidget(self.NumItems_NewOrder)
        spacerItem9 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vlLayout4.addItem(spacerItem9)
        self.Amount_NewOrder = QtWidgets.QLineEdit(parent=self.frame)
        self.Amount_NewOrder.setMinimumSize(QtCore.QSize(175, 25))
        self.Amount_NewOrder.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Amount_NewOrder.setFont(font)
        self.Amount_NewOrder.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Amount_NewOrder.setObjectName("Amount_NewOrder")
        self.vlLayout4.addWidget(self.Amount_NewOrder)
        self.hLayout.addLayout(self.vlLayout4)
        self.verticalLayout.addLayout(self.hLayout)
        spacerItem10 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem10)
        self.hLayout1 = QtWidgets.QHBoxLayout()
        self.hLayout1.setObjectName("hLayout1")
        self.Button_NewOrder = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_NewOrder.sizePolicy().hasHeightForWidth())
        self.Button_NewOrder.setSizePolicy(sizePolicy)
        self.Button_NewOrder.setMinimumSize(QtCore.QSize(200, 30))
        self.Button_NewOrder.setMaximumSize(QtCore.QSize(200, 30))
        self.Button_NewOrder.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_NewOrder.setAutoDefault(True)
        self.Button_NewOrder.setObjectName("Button_NewOrder")
        self.hLayout1.addWidget(self.Button_NewOrder)
        self.Button_Cancel = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Cancel.sizePolicy().hasHeightForWidth())
        self.Button_Cancel.setSizePolicy(sizePolicy)
        self.Button_Cancel.setMinimumSize(QtCore.QSize(200, 30))
        self.Button_Cancel.setMaximumSize(QtCore.QSize(200, 30))
        self.Button_Cancel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Button_Cancel.setAutoDefault(True)
        self.Button_Cancel.setObjectName("Button_Cancel")
        self.hLayout1.addWidget(self.Button_Cancel)
        self.verticalLayout.addLayout(self.hLayout1)
        self.label_error_neworder = QtWidgets.QLabel(parent=self.frame)
        self.label_error_neworder.setMinimumSize(QtCore.QSize(0, 25))
        self.label_error_neworder.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_error_neworder.setStyleSheet("color: rgb(255, 0, 0);")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_error_neworder.setFont(font)
        self.label_error_neworder.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_error_neworder.setObjectName("label_error_neworder")
        self.verticalLayout.addWidget(self.label_error_neworder)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        New_Order.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=New_Order)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 22))
        self.menubar.setObjectName("menubar")
        New_Order.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=New_Order)
        self.statusbar.setObjectName("statusbar")
        New_Order.setStatusBar(self.statusbar)

        self.retranslateUi(New_Order)
        self.Button_Cancel.clicked.connect(New_Order.close) # type: ignore
        self.Button_NewOrder.clicked.connect(self.NewOrder)
        QtCore.QMetaObject.connectSlotsByName(New_Order)


    def retranslateUi(self, New_Order):
        _translate = QtCore.QCoreApplication.translate
        New_Order.setWindowTitle(_translate("New_Order", "Nuevo Pedido"))
        self.label_NumOrder.setText(_translate("New_Order", "Nº Pedido:"))
        self.label_NumOffer.setText(_translate("New_Order", "Nº Oferta:"))
        self.label_NumRef.setText(_translate("New_Order", "Nº Referencia:"))
        self.label_ContracDate.setText(_translate("New_Order", "Fecha Contractual:"))
        self.label_NumItems.setText(_translate("New_Order", "Nº Equipos:"))
        self.label_Amount.setText(_translate("New_Order", "Importe (€):"))
        self.Button_NewOrder.setText(_translate("New_Order", "Crear Pedido"))
        self.Button_Cancel.setText(_translate("New_Order", "Cancelar"))


    def NewOrder(self):
        numorder=self.NumOrder_NewOrder.text()
        numoffer=self.NumOffer_NewOrder.text()
        numref=self.NumRef_NewOrder.text()
        contractdate=self.ContracDate_NewOrder.text()
        numitems=self.NumItems_NewOrder.text()
        amount=self.Amount_NewOrder.text()
        state="Adjudicada"
        # self.responsible=Login_Window.login_username
        actual_date=date.today()
        year=actual_date.year
        month=actual_date.month
        actual_date= actual_date.strftime("%d/%m/%Y")

        if numorder=="" or (numoffer=="" or  (numref=="" or   (numitems=="" or amount==""))):
            self.label_error_neworder.setText('Rellene todos los campos. Solo el campo de fecha contractual puede estar en blanco')

        else:
            print(numorder, numoffer, numref, numref, contractdate, numitems, amount, state, actual_date, year, month)
            commands = ("""
                        SELECT *
                        FROM ofertas
                        WHERE "num_oferta" = %s
                        """)
            conn = None
            try:
            # read the connection parameters
                params = config()
            # connect to the PostgreSQL server
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
            # execution of commands one by one
                cur.execute(commands,(numoffer,))
                results=cur.fetchall()
                match=list(filter(lambda x:numoffer in x, results))
            # close communication with the PostgreSQL database server
                cur.close()
            # commit the changes
                conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()

            if len(match)==0:
                dlg = QtWidgets.QMessageBox()
                new_icon = QtGui.QIcon()
                new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                dlg.setWindowIcon(new_icon)
                dlg.setWindowTitle("Nuevo Pedido")
                dlg.setText("El número de oferta introducido no existe")
                dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                dlg.exec()
            
            else:
                commands = ("""
                            INSERT INTO pedidos (
                            "num_pedido","num_oferta","num_ref_pedido","fecha_pedido","fecha_contractual","num_equipos","importe"
                            )
                            VALUES (%s,%s,%s,%s,%s,%s,%s);
                            UPDATE ofertas
                            SET "estado" = %s
                            WHERE "num_oferta"=%s;
                            """)
                conn = None
                try:
                # read the connection parameters
                    params = config()
                # connect to the PostgreSQL server
                    conn = psycopg2.connect(**params)
                    cur = conn.cursor()
                # execution of commands
                    data=(numorder, numoffer, numref, actual_date, contractdate, numitems, amount, state, numoffer,)
                    cur.execute(commands, data)
                # close communication with the PostgreSQL database server
                    cur.close()
                # commit the changes
                    conn.commit()

                    dlg = QtWidgets.QMessageBox()
                    new_icon = QtGui.QIcon()
                    new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                    dlg.setWindowIcon(new_icon)
                    dlg.setWindowTitle("Crear Pedido")
                    dlg.setText("Pedido creado con éxito")
                    dlg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    dlg.exec()

                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if conn is not None:
                        conn.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    New_Order = QtWidgets.QMainWindow()
    ui = Ui_New_Order_Window()
    ui.setupUi(New_Order)
    New_Order.show()
    sys.exit(app.exec())
