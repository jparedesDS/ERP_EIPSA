# Form implementation generated from reading ui file 'EditOffer_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Edit_Offer_Window(object):
    def setupUi(self, Edit_Offer_Window):
        Edit_Offer_Window.setObjectName("Edit_Offer_Window")
        Edit_Offer_Window.resize(670, 425)
        Edit_Offer_Window.setMinimumSize(QtCore.QSize(670, 425))
        Edit_Offer_Window.setMaximumSize(QtCore.QSize(670, 425))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Edit_Offer_Window.setWindowIcon(icon)
        Edit_Offer_Window.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=Edit_Offer_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.hLayout = QtWidgets.QHBoxLayout()
        self.hLayout.setObjectName("hLayout")
        self.vLayout1 = QtWidgets.QVBoxLayout()
        self.vLayout1.setContentsMargins(0, -1, 0, -1)
        self.vLayout1.setObjectName("vLayout1")
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
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout1.addItem(spacerItem1)
        self.label_Client = QtWidgets.QLabel(parent=self.frame)
        self.label_Client.setMinimumSize(QtCore.QSize(105, 25))
        self.label_Client.setMaximumSize(QtCore.QSize(105, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_Client.setFont(font)
        self.label_Client.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_Client.setObjectName("label_Client")
        self.vLayout1.addWidget(self.label_Client)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout1.addItem(spacerItem2)
        self.label_FinalClient = QtWidgets.QLabel(parent=self.frame)
        self.label_FinalClient.setMinimumSize(QtCore.QSize(105, 25))
        self.label_FinalClient.setMaximumSize(QtCore.QSize(105, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_FinalClient.setFont(font)
        self.label_FinalClient.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_FinalClient.setObjectName("label_FinalClient")
        self.vLayout1.addWidget(self.label_FinalClient)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout1.addItem(spacerItem3)
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
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout1.addItem(spacerItem4)
        self.label_State = QtWidgets.QLabel(parent=self.frame)
        self.label_State.setMinimumSize(QtCore.QSize(105, 25))
        self.label_State.setMaximumSize(QtCore.QSize(105, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_State.setFont(font)
        self.label_State.setObjectName("label_State")
        self.vLayout1.addWidget(self.label_State)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout1.addItem(spacerItem5)
        self.hLayout.addLayout(self.vLayout1)
        self.vLayout2 = QtWidgets.QVBoxLayout()
        self.vLayout2.setObjectName("vLayout2")
        self.NumOffer_EditOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.NumOffer_EditOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.NumOffer_EditOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NumOffer_EditOffer.setFont(font)
        self.NumOffer_EditOffer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.NumOffer_EditOffer.setObjectName("NumOffer_EditOffer")
        self.vLayout2.addWidget(self.NumOffer_EditOffer)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout2.addItem(spacerItem6)
        self.Client_EditOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.Client_EditOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.Client_EditOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Client_EditOffer.setFont(font)
        self.Client_EditOffer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Client_EditOffer.setObjectName("Client_EditOffer")
        self.vLayout2.addWidget(self.Client_EditOffer)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout2.addItem(spacerItem7)
        self.FinalClient_EditOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.FinalClient_EditOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.FinalClient_EditOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FinalClient_EditOffer.setFont(font)
        self.FinalClient_EditOffer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.FinalClient_EditOffer.setObjectName("FinalClient_EditOffer")
        self.vLayout2.addWidget(self.FinalClient_EditOffer)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout2.addItem(spacerItem8)
        self.NumRef_EditOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.NumRef_EditOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.NumRef_EditOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NumRef_EditOffer.setFont(font)
        self.NumRef_EditOffer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.NumRef_EditOffer.setObjectName("NumRef_EditOffer")
        self.vLayout2.addWidget(self.NumRef_EditOffer)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout2.addItem(spacerItem9)
        self.State_EditOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.State_EditOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.State_EditOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.State_EditOffer.setFont(font)
        self.State_EditOffer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.State_EditOffer.setObjectName("State_EditOffer")
        self.vLayout2.addWidget(self.State_EditOffer)
        spacerItem10 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout2.addItem(spacerItem10)
        self.hLayout.addLayout(self.vLayout2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hLayout.addItem(spacerItem11)
        self.vLayout3 = QtWidgets.QVBoxLayout()
        self.vLayout3.setObjectName("vLayout3")
        self.label_NacExt = QtWidgets.QLabel(parent=self.frame)
        self.label_NacExt.setMinimumSize(QtCore.QSize(130, 25))
        self.label_NacExt.setMaximumSize(QtCore.QSize(130, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_NacExt.setFont(font)
        self.label_NacExt.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_NacExt.setObjectName("label_NacExt")
        self.vLayout3.addWidget(self.label_NacExt)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout3.addItem(spacerItem12)
        self.label_Buyer = QtWidgets.QLabel(parent=self.frame)
        self.label_Buyer.setMinimumSize(QtCore.QSize(130, 25))
        self.label_Buyer.setMaximumSize(QtCore.QSize(130, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_Buyer.setFont(font)
        self.label_Buyer.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_Buyer.setObjectName("label_Buyer")
        self.vLayout3.addWidget(self.label_Buyer)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout3.addItem(spacerItem13)
        self.label_Material = QtWidgets.QLabel(parent=self.frame)
        self.label_Material.setMinimumSize(QtCore.QSize(130, 25))
        self.label_Material.setMaximumSize(QtCore.QSize(130, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_Material.setFont(font)
        self.label_Material.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_Material.setObjectName("label_Material")
        self.vLayout3.addWidget(self.label_Material)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout3.addItem(spacerItem14)
        self.label_Notes = QtWidgets.QLabel(parent=self.frame)
        self.label_Notes.setMinimumSize(QtCore.QSize(130, 25))
        self.label_Notes.setMaximumSize(QtCore.QSize(130, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_Notes.setFont(font)
        self.label_Notes.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_Notes.setObjectName("label_Notes")
        self.vLayout3.addWidget(self.label_Notes)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout3.addItem(spacerItem15)
        self.label_Amount = QtWidgets.QLabel(parent=self.frame)
        self.label_Amount.setMinimumSize(QtCore.QSize(130, 25))
        self.label_Amount.setMaximumSize(QtCore.QSize(130, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_Amount.setFont(font)
        self.label_Amount.setObjectName("label_Amount")
        self.vLayout3.addWidget(self.label_Amount)
        spacerItem16 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout3.addItem(spacerItem16)
        self.hLayout.addLayout(self.vLayout3)
        self.vlLayout4 = QtWidgets.QVBoxLayout()
        self.vlLayout4.setObjectName("vlLayout4")
        self.NacExt_EditOffer = QtWidgets.QComboBox(parent=self.frame)
        self.NacExt_EditOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.NacExt_EditOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NacExt_EditOffer.setFont(font)
        self.NacExt_EditOffer.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.NacExt_EditOffer.setObjectName("NacExt_EditOffer")
        list_nacext=['Exterior','Nacional']
        self.NacExt_EditOffer.addItems(list_nacext)
        self.vlLayout4.addWidget(self.NacExt_EditOffer)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vlLayout4.addItem(spacerItem17)
        self.Buyer_EditOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.Buyer_EditOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.Buyer_EditOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Buyer_EditOffer.setFont(font)
        self.Buyer_EditOffer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Buyer_EditOffer.setObjectName("Buyer_EditOffer")
        self.vlLayout4.addWidget(self.Buyer_EditOffer)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vlLayout4.addItem(spacerItem18)
        self.Material_EditOffer = QtWidgets.QComboBox(parent=self.frame)
        self.Material_EditOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.Material_EditOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Material_EditOffer.setFont(font)
        self.Material_EditOffer.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.Material_EditOffer.setObjectName("Material_EditOffer")
        self.Material_EditOffer.addItem("")
        self.Material_EditOffer.addItem("")
        self.vlLayout4.addWidget(self.Material_EditOffer)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vlLayout4.addItem(spacerItem19)
        self.Notes_EditOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.Notes_EditOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.Notes_EditOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Notes_EditOffer.setFont(font)
        self.Notes_EditOffer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Notes_EditOffer.setObjectName("Notes_EditOffer")
        self.vlLayout4.addWidget(self.Notes_EditOffer)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vlLayout4.addItem(spacerItem20)
        self.Amount_EditOffer = QtWidgets.QLineEdit(parent=self.frame)
        self.Amount_EditOffer.setMinimumSize(QtCore.QSize(175, 25))
        self.Amount_EditOffer.setMaximumSize(QtCore.QSize(175, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Amount_EditOffer.setFont(font)
        self.Amount_EditOffer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Amount_EditOffer.setObjectName("Amount_EditOffer")
        self.vlLayout4.addWidget(self.Amount_EditOffer)
        spacerItem21 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vlLayout4.addItem(spacerItem21)
        self.hLayout.addLayout(self.vlLayout4)
        self.verticalLayout.addLayout(self.hLayout)
        spacerItem22 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem22)
        self.hLayout1 = QtWidgets.QHBoxLayout()
        self.hLayout1.setObjectName("hLayout1")
        self.Button_EditOffer = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_EditOffer.sizePolicy().hasHeightForWidth())
        self.Button_EditOffer.setSizePolicy(sizePolicy)
        self.Button_EditOffer.setMinimumSize(QtCore.QSize(200, 30))
        self.Button_EditOffer.setMaximumSize(QtCore.QSize(200, 30))
        self.Button_EditOffer.setStyleSheet("QPushButton:focus{\n"
"    background-color: #019ad2;\n"
"    border-color: rgb(0, 0, 0);\n"
"}"
)
        self.Button_EditOffer.setAutoDefault(True)
        self.Button_EditOffer.setObjectName("Button_EditOffer")
        self.hLayout1.addWidget(self.Button_EditOffer)
        self.Button_Cancel = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Cancel.sizePolicy().hasHeightForWidth())
        self.Button_Cancel.setSizePolicy(sizePolicy)
        self.Button_Cancel.setMinimumSize(QtCore.QSize(200, 30))
        self.Button_Cancel.setMaximumSize(QtCore.QSize(200, 30))
        self.Button_Cancel.setStyleSheet("QPushButton:focus{\n"
"    background-color: #019ad2;\n"
"    border-color: rgb(0, 0, 0);\n"
"}"
)
        self.Button_Cancel.setAutoDefault(True)
        self.Button_Cancel.setObjectName("Button_Cancel")
        self.hLayout1.addWidget(self.Button_Cancel)
        self.verticalLayout.addLayout(self.hLayout1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        Edit_Offer_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Edit_Offer_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 22))
        self.menubar.setObjectName("menubar")
        Edit_Offer_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Edit_Offer_Window)
        self.statusbar.setObjectName("statusbar")
        Edit_Offer_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Edit_Offer_Window)
        self.Button_Cancel.clicked.connect(Edit_Offer_Window.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Edit_Offer_Window)


    def retranslateUi(self, Edit_Offer_Window):
        _translate = QtCore.QCoreApplication.translate
        Edit_Offer_Window.setWindowTitle(_translate("Edit_Offer_Window", "Editar Oferta"))
        self.label_NumOffer.setText(_translate("Edit_Offer_Window", "Nº Oferta:"))
        self.label_Client.setText(_translate("Edit_Offer_Window", "Cliente:"))
        self.label_FinalClient.setText(_translate("Edit_Offer_Window", "Cliente Final:"))
        self.label_NumRef.setText(_translate("Edit_Offer_Window", "Nº Referencia:"))
        self.label_State.setText(_translate("Edit_Offer_Window", "Estado:"))
        self.label_NacExt.setText(_translate("Edit_Offer_Window", "Nacional/Exterior:"))
        self.label_Buyer.setText(_translate("Edit_Offer_Window", "Comprador:"))
        self.label_Material.setText(_translate("Edit_Offer_Window", "Material:"))
        self.label_Notes.setText(_translate("Edit_Offer_Window", "Notas:"))
        self.label_Amount.setText(_translate("Edit_Offer_Window", "Importe (€):"))


        self.Material_EditOffer.setItemText(0, _translate("Edit_Offer_Window", "Material1"))
        self.Material_EditOffer.setItemText(1, _translate("Edit_Offer_Window", "Material2"))
        self.Button_EditOffer.setText(_translate("Edit_Offer_Window", "Editar Oferta"))
        self.Button_Cancel.setText(_translate("Edit_Offer_Window", "Cancelar"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Edit_Offer_Window = QtWidgets.QMainWindow()
    ui = Ui_Edit_Offer_Window()
    ui.setupUi(Edit_Offer_Window)
    Edit_Offer_Window.show()
    sys.exit(app.exec())