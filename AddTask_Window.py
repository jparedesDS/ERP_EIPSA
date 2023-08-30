# Form implementation generated from reading ui file 'AddTask_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from config import config
import psycopg2


class Ui_AddTask_Window(object):
    def __init__(self, name, date):
        self.name=name
        self.dateselected = date
    # def __init__(self):
    #     self.name="Luis Bravo"

    def setupUi(self, AddTask_Window):
        AddTask_Window.setObjectName("AddTask_Window")
        AddTask_Window.resize(400, 561)
        AddTask_Window.setMinimumSize(QtCore.QSize(400, 375))
        AddTask_Window.setMaximumSize(QtCore.QSize(400, 375))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Recursos/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        AddTask_Window.setWindowIcon(icon)
        AddTask_Window.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=AddTask_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(350, 300))
        self.frame.setMaximumSize(QtCore.QSize(350, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        if self.name == 'Luis Bravo':
            self.hLayout1 = QtWidgets.QHBoxLayout()
            self.hLayout1.setObjectName("hLayout2")
            self.labelResponsible = QtWidgets.QLabel(parent=self.frame)
            self.labelResponsible.setMinimumSize(QtCore.QSize(100, 25))
            self.labelResponsible.setMaximumSize(QtCore.QSize(100, 25))
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            self.labelResponsible.setText("Responsable:")
            self.labelResponsible.setFont(font)
            self.labelResponsible.setObjectName("labelResponsible")
            self.hLayout1.addWidget(self.labelResponsible)
            self.Responsible_Task = QtWidgets.QComboBox(parent=self.frame)
            self.Responsible_Task.setMinimumSize(QtCore.QSize(220, 25))
            self.Responsible_Task.setMaximumSize(QtCore.QSize(220, 25))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.Responsible_Task.setFont(font)
            self.Responsible_Task.setObjectName("Responsible_Task")
            self.Responsible_Task.addItems(["Luis Bravo","Carlos Crespo","Sandra Sanz"])
            self.hLayout1.addWidget(self.Responsible_Task)
            self.gridLayout_2.addLayout(self.hLayout1, 1, 0, 1, 1)
            spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
            self.gridLayout_2.addItem(spacerItem4, 2, 0, 1, 1)
        self.hLayout2 = QtWidgets.QHBoxLayout()
        self.hLayout2.setObjectName("hLayout2")
        self.labelDate = QtWidgets.QLabel(parent=self.frame)
        self.labelDate.setMinimumSize(QtCore.QSize(90, 25))
        self.labelDate.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.labelDate.setFont(font)
        self.labelDate.setObjectName("labelDate")
        self.hLayout2.addWidget(self.labelDate)
        self.checkbox = QtWidgets.QCheckBox(parent=self.frame)
        self.checkbox.setMinimumSize(QtCore.QSize(20, 20))
        self.checkbox.setMaximumSize(QtCore.QSize(20, 20))
        self.hLayout2.addWidget(self.checkbox)
        self.spacerItem = QtWidgets.QSpacerItem(1, 1, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hLayout2.addItem(self.spacerItem)
        self.comboBox = QtWidgets.QDateEdit(calendarPopup=True)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 25))
        self.comboBox.setMaximumSize(QtCore.QSize(200, 25))
        self.comboBox.setDate(self.dateselected)#QtCore.QDate.currentDate())
        self.comboBox.setStyleSheet("QCalendarWidget QWidget{\n"
"background-color: rgb(3, 174, 236);\n"
"}\n"
"\n"
"QCalendarWidget QTableView{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    color: white;\n"
"    font-size:15px;\n"
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
"    qproperty-icon: url(//nas01/DATOS/Comunes/EIPSA-ERP/Recursos/Iconos/back_arrow.png);\n"
"}\n"
"#qt_calendar_nextmonth {\n"
"    qproperty-icon: url(//nas01/DATOS/Comunes/EIPSA-ERP/Recursos/Iconos/forward_arrow.png);\n"
"}")
        self.hLayout2.addWidget(self.comboBox)
        self.comboBox.setVisible(False)
        self.gridLayout_2.addLayout(self.hLayout2, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        self.hLayout3 = QtWidgets.QHBoxLayout()
        self.hLayout3.setObjectName("hLayout3")
        self.labelValue = QtWidgets.QLabel(parent=self.frame)
        self.labelValue.setMinimumSize(QtCore.QSize(90, 25))
        self.labelValue.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.labelValue.setFont(font)
        self.labelValue.setObjectName("labelValue")
        self.hLayout3.addWidget(self.labelValue)
        self.lineEdit = QtWidgets.QTextEdit(parent=self.frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(225, 75))
        self.lineEdit.setMaximumSize(QtCore.QSize(225, 75))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.hLayout3.addWidget(self.lineEdit)
        self.gridLayout_2.addLayout(self.hLayout3, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 6, 0, 1, 1)
        self.hLayout3 = QtWidgets.QHBoxLayout()
        self.hLayout3.setObjectName("hLayout3")
        self.Button_AddTask = QtWidgets.QPushButton(parent=self.frame)
        self.Button_AddTask.setMinimumSize(QtCore.QSize(100, 35))
        self.Button_AddTask.setMaximumSize(QtCore.QSize(100, 35))
        self.Button_AddTask.setObjectName("Button_AddTask")
        self.hLayout3.addWidget(self.Button_AddTask)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hLayout3.addItem(spacerItem3)
        self.Button_Cancel = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Cancel.setMinimumSize(QtCore.QSize(100, 35))
        self.Button_Cancel.setMaximumSize(QtCore.QSize(100, 35))
        self.Button_Cancel.setObjectName("Button_Cancel")
        self.hLayout3.addWidget(self.Button_Cancel)
        self.gridLayout_2.addLayout(self.hLayout3, 7, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        AddTask_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=AddTask_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        AddTask_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=AddTask_Window)
        self.statusbar.setObjectName("statusbar")
        AddTask_Window.setStatusBar(self.statusbar)
        AddTask_Window.setWindowFlags(QtCore.Qt.WindowType.WindowMinimizeButtonHint)

        self.retranslateUi(AddTask_Window)
        self.Button_Cancel.clicked.connect(AddTask_Window.close) # type: ignore
        self.Button_AddTask.clicked.connect(self.AddTask)
        self.checkbox.stateChanged.connect(self.toggle_combo_box)
        QtCore.QMetaObject.connectSlotsByName(AddTask_Window)


    def retranslateUi(self, AddTask_Window):
        _translate = QtCore.QCoreApplication.translate
        AddTask_Window.setWindowTitle(_translate("AddTask_Window", "Crear Tarea"))
        self.labelValue.setText(_translate("AddTask_Window", "Tarea:"))
        self.labelDate.setText(_translate("AddTask_Window", "Fecha Fin:"))
        self.Button_AddTask.setText(_translate("AddTask_Window", "Agregar"))
        self.Button_Cancel.setText(_translate("AddTask_Window", "Cancelar"))


    def AddTask(self):
        task_value = self.lineEdit.toPlainText()
        state_checkbox = "Checked" if self.checkbox.isChecked() else "Unchecked"

        date_task = self.comboBox.date().toString(QtCore.Qt.DateFormat.ISODate) if state_checkbox == "Checked" else None

        if self.name=='Luis Bravo':
            responsible = self.Responsible_Task.currentText()

        else:
            responsible = self.name

        if self.name=='Carlos Crespo':
            creator=self.name[0] + self.name[self.name.find(' ')+1]+'H'
        else:
            creator=self.name[0] + self.name[self.name.find(' ')+1]

        if date_task == "" or task_value == "":
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Recursos/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("ERP EIPSA")
            dlg.setText("Los campos deben estar rellenos")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            dlg.exec()
            del dlg, new_icon

        else:
            commands_AddTask = f"INSERT INTO tasks VALUES (default, '{creator}', '{responsible}', '{date_task}', '{task_value}', 'Pendiente')"
            conn = None
            try:
            # read the connection parameters
                params = config()
            # connect to the PostgreSQL server
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
            # execution of commands one by one
                cur.execute(commands_AddTask)
            # close communication with the PostgreSQL database server
                cur.close()
            # commit the changes
                conn.commit()

                dlg = QtWidgets.QMessageBox()
                new_icon = QtGui.QIcon()
                new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Recursos/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                dlg.setWindowIcon(new_icon)
                dlg.setWindowTitle("ERP EIPSA")
                dlg.setText("Tarea creada con éxito")
                dlg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                dlg.exec()
                del dlg, new_icon

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()

    def toggle_combo_box(self, state):
        if state == 2:
            self.comboBox.setVisible(True)
        else:
            self.comboBox.setVisible(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddTask_Window = QtWidgets.QMainWindow()
    ui = Ui_AddTask_Window()
    ui.setupUi(AddTask_Window)
    AddTask_Window.show()
    sys.exit(app.exec())