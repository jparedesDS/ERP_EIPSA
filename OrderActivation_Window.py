# Form implementation generated from reading ui file 'OrderActivation_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import psycopg2
from config import config  
import os
from Email_Styles import email_order_activation
from datetime import *


basedir = r"\\nas01\DATOS\Comunes\EIPSA-ERP"


class Ui_OrderActivation_Window(object):
    def setupUi(self, OrderActivation_Window):
        OrderActivation_Window.setObjectName("OrderActivation_Window")
        OrderActivation_Window.resize(300, 450)
        OrderActivation_Window.setMinimumSize(QtCore.QSize(300, 450))
        OrderActivation_Window.setMaximumSize(QtCore.QSize(300, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        OrderActivation_Window.setWindowIcon(icon)
        OrderActivation_Window.setAutoFillBackground(False)
        OrderActivation_Window.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=OrderActivation_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_numorder_orderactivation = QtWidgets.QLabel(parent=self.frame)
        self.label_numorder_orderactivation.setEnabled(True)
        self.label_numorder_orderactivation.setMinimumSize(QtCore.QSize(200, 25))
        self.label_numorder_orderactivation.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_numorder_orderactivation.setFont(font)
        self.label_numorder_orderactivation.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_numorder_orderactivation.setObjectName("label_numorder_orderactivation")
        self.verticalLayout.addWidget(self.label_numorder_orderactivation, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.numorder_orderactivation = QtWidgets.QLineEdit(parent=self.frame)
        self.numorder_orderactivation.setEnabled(True)
        self.numorder_orderactivation.setMinimumSize(QtCore.QSize(200, 25))
        self.numorder_orderactivation.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.numorder_orderactivation.setFont(font)
        self.numorder_orderactivation.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.numorder_orderactivation.setObjectName("numorder_orderactivation")
        self.verticalLayout.addWidget(self.numorder_orderactivation, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_info_orderactivation = QtWidgets.QLabel(parent=self.frame)
        self.label_info_orderactivation.setEnabled(True)
        self.label_info_orderactivation.setMinimumSize(QtCore.QSize(200, 25))
        self.label_info_orderactivation.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_info_orderactivation.setFont(font)
        self.label_info_orderactivation.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_orderactivation.setObjectName("label_info_orderactivation")
        self.verticalLayout.addWidget(self.label_info_orderactivation, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.info_orderactivation = QtWidgets.QTextEdit(parent=self.frame)
        self.info_orderactivation.setEnabled(True)
        self.info_orderactivation.setMinimumSize(QtCore.QSize(200, 100))
        self.info_orderactivation.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.info_orderactivation.setFont(font)
        self.info_orderactivation.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.info_orderactivation.setObjectName("info_orderactivation")
        self.verticalLayout.addWidget(self.info_orderactivation, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.generate_orderactivation = QtWidgets.QPushButton(parent=self.frame)
        self.generate_orderactivation.setEnabled(True)
        self.generate_orderactivation.setMinimumSize(QtCore.QSize(200, 35))
        self.generate_orderactivation.setMaximumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.generate_orderactivation.setFont(font)
        self.generate_orderactivation.setStyleSheet("QPushButton {\n"
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
        self.generate_orderactivation.setAutoDefault(True)
        self.generate_orderactivation.setObjectName("generate_orderactivation")
        self.verticalLayout.addWidget(self.generate_orderactivation, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        OrderActivation_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=OrderActivation_Window)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 275, 22))
        self.menubar.setObjectName("menubar")
        OrderActivation_Window.setMenuBar(self.menubar)

        self.retranslateUi(OrderActivation_Window)
        self.generate_orderactivation.clicked.connect(self.activateorder)
        QtCore.QMetaObject.connectSlotsByName(OrderActivation_Window)


    def retranslateUi(self, OrderActivation_Window):
        _translate = QtCore.QCoreApplication.translate
        OrderActivation_Window.setWindowTitle(_translate("OrderActivation_Window", "Activar Pedido"))
        self.label_numorder_orderactivation.setText(_translate("OrderActivation_Window", "Número Pedido:"))
        self.label_info_orderactivation.setText(_translate("OrderActivation_Window", "Info adicional:"))
        self.generate_orderactivation.setText(_translate("OrderActivation_Window", "Activar"))


    def activateorder(self):
        numorder=self.numorder_orderactivation.text()
        adit_info=self.info_orderactivation.toPlainText()

        actual_date=date.today()
        actual_date= actual_date.strftime("%d/%m/%Y")

        commands_responsible = ("""SELECT name, surname, email FROM users_data.registration
                                    WHERE username = %s
                                    """)
        commands_mail_sendto = ("""SELECT username, email FROM users_data.registration
                            WHERE (profile = 'Técnico'
                            OR
                            profile = 'Compras'
                            OR
                            profile = 'Taller'
                            )
                            """)
        commands_mail_copy = ("""SELECT email FROM users_data.registration
                            WHERE (profile = 'Dirección'
                            OR
                            profile = 'DirecciónF'
                            )
                            """)
        commands_queryorder = ("""
                                SELECT orders."num_order",offers."responsible", orders."num_ref_order", offers."client", offers."final_client", TO_CHAR(orders."expected_date", 'DD-MM-YYYY')
                                FROM offers
                                INNER JOIN orders ON (offers."num_offer"=orders."num_offer")
                                WHERE orders."num_order" = %s
                                ORDER BY orders."num_order"
                                """)
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cursor = conn.cursor()

            cursor.execute(commands_queryorder, (numorder,))
            results_queryorder=cursor.fetchall()
            if not len(results_queryorder) > 0:
                dlg = QtWidgets.QMessageBox()
                new_icon = QtGui.QIcon()
                new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                dlg.setWindowIcon(new_icon)
                dlg.setWindowTitle("TAGS pedido")
                dlg.setText("El pedido no se encuentra registrado en el sistema")
                dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                dlg.exec()
            # Closing cursor and database connection
                conn.commit()
                cursor.close()

            else:
                conn = None
                try:
                # read the connection parameters
                    params = config()
                # connect to the PostgreSQL server
                    conn = psycopg2.connect(**params)
                    cur = conn.cursor()

                    username_responsible = results_queryorder[0][1]
                    num_ref_order = results_queryorder[0][2]
                    client = results_queryorder[0][3]
                    final_client = results_queryorder[0][4]
                    expected_date = results_queryorder[0][5]
                # execution of commands
                    cur.execute(commands_responsible, (username_responsible,))
                    results_responsible=cur.fetchall()
                    name_responsible = results_responsible[0][0] + " " + results_responsible[0][1]
                    email_responsible = results_responsible[0][2]

                    cur.execute(commands_mail_sendto)
                    results_mailto=cur.fetchall()
                    mails_sendto = [x[1] for x in results_mailto]

                    cur.execute(commands_mail_copy)
                    results_mailcopy=cur.fetchall()
                    mails_copy = [x[0] for x in results_mailcopy]
                    mails_copy.append(email_responsible)

                    mail = email_order_activation(numorder, num_ref_order, client, final_client, expected_date, name_responsible, mails_sendto, mails_copy, adit_info)
                    mail.send_email()
                    
                    commands_usernames = ("""SELECT username FROM users_data.registration
                        WHERE (profile = 'Técnico'
                        OR
                        profile = 'Compras'
                        )
                        """)
                    commands_notification_neworder = ("""INSERT INTO notifications.notifications_orders (
                                            "username","message","state","date_creation"
                                            )
                                            VALUES (%s,%s,%s,%s)
                                            """)

                    cur.execute(commands_usernames)
                    results_usernames=cur.fetchall()

                    for user_data in results_usernames:
                        data = (user_data[0], "Nuevo pedido: " + numorder, "Pendiente", actual_date)
                        cur.execute(commands_notification_neworder, data)

                # close communication with the PostgreSQL database server
                    cur.close()
                # commit the changes
                    conn.commit()

                    dlg = QtWidgets.QMessageBox()
                    new_icon = QtGui.QIcon()
                    new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                    dlg.setWindowIcon(new_icon)
                    dlg.setWindowTitle("Activar Pedido")
                    dlg.setText("Pedido activado con éxito")
                    dlg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    dlg.exec()

                    OrderActivation_Window.close()

                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if conn is not None:
                        conn.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OrderActivation_Window = QtWidgets.QMainWindow()
    ui = Ui_OrderActivation_Window()
    ui.setupUi(OrderActivation_Window)
    OrderActivation_Window.show()
    sys.exit(app.exec())