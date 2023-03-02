# Form implementation generated from reading ui file 'ImportTAG_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog


class Ui_ImportTAG_Window(object):
    def setupUi(self, ImportTAG_Window):
        ImportTAG_Window.setObjectName("ImportTAG_Window")
        ImportTAG_Window.resize(640, 330)
        ImportTAG_Window.setMinimumSize(QtCore.QSize(640, 330))
        ImportTAG_Window.setMaximumSize(QtCore.QSize(640, 330))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ImportTAG_Window.setWindowIcon(icon)
        ImportTAG_Window.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=ImportTAG_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hLayout = QtWidgets.QHBoxLayout()
        self.hLayout.setObjectName("hLayout")
        self.label_SelectFile = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_SelectFile.setFont(font)
        self.label_SelectFile.setObjectName("label_SelectFile")
        self.hLayout.addWidget(self.label_SelectFile)
        self.Button_Select = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Select.setMinimumSize(QtCore.QSize(250, 35))
        self.Button_Select.setMaximumSize(QtCore.QSize(250, 35))
        self.Button_Select.setObjectName("Button_Select")
        self.hLayout.addWidget(self.Button_Select)
        self.verticalLayout.addLayout(self.hLayout)
        self.label_name_file = QtWidgets.QLabel(parent=self.frame)
        self.label_name_file.setMinimumSize(QtCore.QSize(0, 25))
        self.label_name_file.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_name_file.setObjectName("label_name_file")
        self.verticalLayout.addWidget(self.label_name_file)
        self.hLayout1 = QtWidgets.QHBoxLayout()
        self.hLayout1.setObjectName("hLayout1")
        self.label_ItemType = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ItemType.setFont(font)
        self.label_ItemType.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_ItemType.setObjectName("label_ItemType")
        self.hLayout1.addWidget(self.label_ItemType)
        self.vLayout = QtWidgets.QVBoxLayout()
        self.vLayout.setObjectName("vLayout")
        self.radioFlow = QtWidgets.QRadioButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioFlow.setFont(font)
        self.radioFlow.setObjectName("radioFlow")
        self.vLayout.addWidget(self.radioFlow)
        self.radioTemp = QtWidgets.QRadioButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioTemp.setFont(font)
        self.radioTemp.setObjectName("radioTemp")
        self.vLayout.addWidget(self.radioTemp)
        self.radioLevel = QtWidgets.QRadioButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioLevel.setFont(font)
        self.radioLevel.setObjectName("radioLevel")
        self.vLayout.addWidget(self.radioLevel)
        self.radioOthers = QtWidgets.QRadioButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioOthers.setFont(font)
        self.radioOthers.setObjectName("radioOthers")
        self.vLayout.addWidget(self.radioOthers)
        self.hLayout1.addLayout(self.vLayout)
        self.verticalLayout.addLayout(self.hLayout1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.hLayout2 = QtWidgets.QHBoxLayout()
        self.hLayout2.setObjectName("hLayout2")
        self.Button_Import = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Import.setMinimumSize(QtCore.QSize(250, 35))
        self.Button_Import.setMaximumSize(QtCore.QSize(250, 35))
        self.Button_Import.setObjectName("Button_Import")
        self.hLayout2.addWidget(self.Button_Import)
        self.Button_Cancel = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Cancel.setMinimumSize(QtCore.QSize(250, 35))
        self.Button_Cancel.setMaximumSize(QtCore.QSize(250, 35))
        self.Button_Cancel.setObjectName("Button_Cancel")
        self.hLayout2.addWidget(self.Button_Cancel)
        self.verticalLayout.addLayout(self.hLayout2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        ImportTAG_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ImportTAG_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        ImportTAG_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ImportTAG_Window)
        self.statusbar.setObjectName("statusbar")
        ImportTAG_Window.setStatusBar(self.statusbar)

        self.retranslateUi(ImportTAG_Window)
        self.Button_Cancel.clicked.connect(ImportTAG_Window.close)
        self.Button_Select.clicked.connect(self.browsefiles) # type: ignore

        self.radioFlow.toggled.connect(lambda:self.btnstate(self.radioFlow))
        self.radioTemp.toggled.connect(lambda:self.btnstate(self.radioTemp))
        self.radioLevel.toggled.connect(lambda:self.btnstate(self.radioLevel))
        self.radioOthers.toggled.connect(lambda:self.btnstate(self.radioOthers))

        QtCore.QMetaObject.connectSlotsByName(ImportTAG_Window)


    def retranslateUi(self, ImportTAG_Window):
        _translate = QtCore.QCoreApplication.translate
        ImportTAG_Window.setWindowTitle(_translate("ImportTAG_Window", "Importar TAG"))
        self.label_SelectFile.setText(_translate("ImportTAG_Window", "Seleccionar archivo:"))
        self.Button_Select.setText(_translate("ImportTAG_Window", "Seleccionar"))
        self.label_name_file.setText(_translate("ImportTAG_Window", ""))
        self.label_ItemType.setText(_translate("ImportTAG_Window", "Tipo de equipo:"))
        self.radioFlow.setText(_translate("ImportTAG_Window", "Caudal"))
        self.radioTemp.setText(_translate("ImportTAG_Window", "Temperatura"))
        self.radioLevel.setText(_translate("ImportTAG_Window", "Nivel"))
        self.radioOthers.setText(_translate("ImportTAG_Window", "Otros"))
        self.Button_Import.setText(_translate("ImportTAG_Window", "Importar"))
        self.Button_Cancel.setText(_translate("ImportTAG_Window", "Cancelar"))


    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(None, 'Open File', 'C:')
        self.label_name_file.setText(fname[0])


    def btnstate(self,b):
        if b.text() == 'Caudal':
            if b.isChecked() == True:
                print('a')

        if b.text() == 'Temperatura':
            if b.isChecked() == True:
                print('b')

        if b.text() == 'Nivel':
            if b.isChecked() == True:
                print('c')

        if b.text() == 'Otros':
            if b.isChecked() == True:
                print('d')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ImportTAG_Window = QtWidgets.QMainWindow()
    ui = Ui_ImportTAG_Window()
    ui.setupUi(ImportTAG_Window)
    ImportTAG_Window.show()
    sys.exit(app.exec())
