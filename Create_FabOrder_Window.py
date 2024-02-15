# Form implementation generated from reading ui file 'ElementsFabOrder_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import pandas as pd
from OTFabOrder_Window import Ui_OTFabOrder_Window
import os

basedir = r"\\nas01\DATOS\Comunes\EIPSA-ERP"


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignmentFlag.AlignCenter


class Ui_CreateFabOrder_Window(object):
    def __init__(self, variable, proxy, model):
        self.variable = variable
        self.proxy = proxy
        self.model = model

    def setupUi(self, ElementsFabOrder_Window):
        self.id_list = []
        data_list = []
        ElementsFabOrder_Window.setObjectName("ElementsFabOrder_Window")
        ElementsFabOrder_Window.resize(400, 561)
        ElementsFabOrder_Window.setMinimumSize(QtCore.QSize(600, 575))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ElementsFabOrder_Window.setWindowIcon(icon)
        ElementsFabOrder_Window.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=ElementsFabOrder_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
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
        self.Button_Generate = QtWidgets.QPushButton(parent=self.frame)
        self.Button_Generate.setMinimumSize(QtCore.QSize(120, 35))
        self.Button_Generate.setMaximumSize(QtCore.QSize(120, 35))
        self.Button_Generate.setObjectName("Button_Generate")
        self.gridLayout_2.addWidget(self.Button_Generate, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem4, 2, 0, 1, 2)
        if self.variable == "Caudal":
            self.columns_number = 27
            headers_labels = ["Tag", "PTTAG", "CFabEq", "CFabBrOr", "QBrOr", "CFabBrLin",
                                "QBrLin", "CFabJunta", "QJunta", "CFabTorn", "QTorn",
                                "CFabTapón", "QTapón", "CFabExt", "QExt", "CFabPlaca",
                                "QPlaca", "CFabNiplo", "QNiplo", "CFabMango", "QMango",
                                "CodFabChRing", "QChRing", "CFabTubo", "QTubo", "CFabCuña", "QCuña"]
        elif self.variable == "Temperatura":
            self.columns_number = 27
            headers_labels = ["Tag", "PTTAG", "CFabEq", "CFabBarra", "QBarra", "CFabTubo",
                                "QTubo", "CFabBrida", "QBrida", "CFabSensor", "QSensor",
                                "CFabCabeza", "QCabeza", "CFabBTB", "QBTB", "CFabNiplo",
                                "QNiplo", "CFabMuelle", "QMuelle", "CFabpuntal", "QPuntal",
                                "CodFabTapón", "QTapón", "CFabVaina", "QVaina", "CFabCable", "QCable"]
        elif self.variable == "Nivel":
            self.columns_number = 37
            headers_labels = ["Tag", "PTTAG", "CFabEq", "CFabCuerpo", "QCuerpo", "CFabCubierta",
                                "QCubierta", "CFabTorn", "QTorn", "CFabNipHex", "QNipHex",
                                "CFabVálv", "QVálv", "CFabBrida", "QBrida", "CFabDV",
                                "QDV", "CFabEscala", "QEscala", "CFabIlum", "QIlum",
                                "CodFabJunta", "QJunta", "CFabVidrio", "QVidrio", "CFabFlot",
                                "QFlot", "CFabMica", "QMica", "CFabFlags", "QFlags",
                                "CodFabJuntaBrida", "QJuntaBrida", "CFabNipTub", "QNipTub", "CFabFrost", "QFrost"]
        self.hLayout2 = QtWidgets.QHBoxLayout()
        self.hLayout2.setObjectName("hLayout2")
        self.hLayout2.setSpacing(0)
        self.gridLayout_2.addLayout(self.hLayout2, 3, 0, 1, 3)
        self.tableElements = QtWidgets.QTableWidget(parent=self.frame)
        self.tableElements.setObjectName("tableWidget")
        self.tableElements.setColumnCount(self.columns_number)
        self.tableElements.setRowCount(0)
        for i in range(self.columns_number):
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            item.setFont(font)
            self.tableElements.setHorizontalHeaderItem(i, item)
        self.gridLayout_2.addWidget(self.tableElements, 4, 0, 1, 3)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        ElementsFabOrder_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ElementsFabOrder_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        ElementsFabOrder_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ElementsFabOrder_Window)
        self.statusbar.setObjectName("statusbar")
        ElementsFabOrder_Window.setStatusBar(self.statusbar)
        self.tableElements.setSortingEnabled(True)
        self.tableElements.horizontalHeader().setStyleSheet("QHeaderView::section {background-color: #33bdef; border: 1px solid black;}")
        # ElementsFabOrder_Window.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint, False)

        self.retranslateUi(ElementsFabOrder_Window)
        QtCore.QMetaObject.connectSlotsByName(ElementsFabOrder_Window)

        for row in range(self.proxy.rowCount()):
            first_column_value = self.proxy.data(self.proxy.index(row, 0))
            self.id_list.append(first_column_value)

        for element in self.id_list:
            for row in range(self.model.rowCount()):
                if self.model.data(self.model.index(row, 0)) == element:
                    target_row = row
                    break
            if target_row is not None:
                if self.variable == "Caudal":
                    tag = self.model.data(self.model.index(target_row, 1))
                    ped_type_tag = self.model.data(self.model.index(target_row, 110))
                    code_fab_equipment = self.model.data(self.model.index(target_row, 71))
                    codefab_orifice_flange = self.model.data(self.model.index(target_row, 74))
                    qty_orifice_flange = self.model.data(self.model.index(target_row, 75))
                    codefab_line_flange = self.model.data(self.model.index(target_row, 77))
                    qty_line_flange = self.model.data(self.model.index(target_row, 78))
                    codefab_gasket = self.model.data(self.model.index(target_row, 80))
                    qty_gasket = self.model.data(self.model.index(target_row, 81))
                    codefab_bolts = self.model.data(self.model.index(target_row, 83))
                    qty_bolts = self.model.data(self.model.index(target_row, 84))
                    codefab_plugs = self.model.data(self.model.index(target_row, 86))
                    qty_plugs = self.model.data(self.model.index(target_row, 87))
                    codefab_extractor = self.model.data(self.model.index(target_row, 89))
                    qty_extractor = self.model.data(self.model.index(target_row, 90))
                    codefab_plate = self.model.data(self.model.index(target_row, 92))
                    qty_plate = self.model.data(self.model.index(target_row, 93))
                    codefab_nipple = self.model.data(self.model.index(target_row, 95))
                    qty_nipple = self.model.data(self.model.index(target_row, 96))
                    codefab_handle = self.model.data(self.model.index(target_row, 98))
                    qty_handle = self.model.data(self.model.index(target_row, 99))
                    codefab_chring = self.model.data(self.model.index(target_row, 101))
                    qty_chring = self.model.data(self.model.index(target_row, 102))
                    codefab_tube = self.model.data(self.model.index(target_row, 104))
                    qty_tube = self.model.data(self.model.index(target_row, 105))
                    codefab_piece2 = self.model.data(self.model.index(target_row, 107))
                    qty_piece2 = self.model.data(self.model.index(target_row, 108))
                    data_list.append([tag, ped_type_tag, code_fab_equipment, codefab_orifice_flange, qty_orifice_flange, codefab_line_flange,
                                        qty_line_flange, codefab_gasket, qty_gasket, codefab_bolts, qty_bolts,
                                        codefab_plugs, qty_plugs, codefab_extractor, qty_extractor, codefab_plate,
                                        qty_plate, codefab_nipple, qty_nipple, codefab_handle, qty_handle,
                                        codefab_chring, qty_chring, codefab_tube, qty_tube, codefab_piece2, qty_piece2])

                elif self.variable == "Temperatura":
                    tag = self.model.data(self.model.index(target_row, 1))
                    ped_type_tag = self.model.data(self.model.index(target_row, 117))
                    code_fab_equipment = self.model.data(self.model.index(target_row, 79))
                    codefab_bar = self.model.data(self.model.index(target_row, 82))
                    qty_bar = self.model.data(self.model.index(target_row, 83))
                    codefab_tube = self.model.data(self.model.index(target_row, 85))
                    qty_tube = self.model.data(self.model.index(target_row, 86))
                    codefab_flange = self.model.data(self.model.index(target_row, 88))
                    qty_flange = self.model.data(self.model.index(target_row, 89))
                    codefab_sensor = self.model.data(self.model.index(target_row, 91))
                    qty_sensor = self.model.data(self.model.index(target_row, 92))
                    codefab_head = self.model.data(self.model.index(target_row, 94))
                    qty_head = self.model.data(self.model.index(target_row, 95))
                    codefab_btb = self.model.data(self.model.index(target_row, 97))
                    qty_btb = self.model.data(self.model.index(target_row, 98))
                    codefab_nipple = self.model.data(self.model.index(target_row, 100))
                    qty_nipple = self.model.data(self.model.index(target_row, 101))
                    codefab_spring = self.model.data(self.model.index(target_row, 103))
                    qty_spring = self.model.data(self.model.index(target_row, 104))
                    codefab_puntal = self.model.data(self.model.index(target_row, 106))
                    qty_puntal = self.model.data(self.model.index(target_row, 107))
                    codefab_plug = self.model.data(self.model.index(target_row, 109))
                    qty_plug = self.model.data(self.model.index(target_row, 110))
                    codefab_tw = self.model.data(self.model.index(target_row, 112))
                    qty_tw = self.model.data(self.model.index(target_row, 113))
                    codefab_cable = self.model.data(self.model.index(target_row, 115))
                    qty_cable = self.model.data(self.model.index(target_row, 116))
                    data_list.append([tag, ped_type_tag, code_fab_equipment, codefab_bar, qty_bar, codefab_tube,
                                        qty_tube, codefab_flange, qty_flange, codefab_sensor, qty_sensor,
                                        codefab_head, qty_head, codefab_btb, qty_btb, codefab_nipple,
                                        qty_nipple, codefab_spring, qty_spring, codefab_puntal, qty_puntal,
                                        codefab_plug, qty_plug, codefab_tw, qty_tw, codefab_cable, qty_cable])

                elif self.variable == "Nivel":
                    tag = self.model.data(self.model.index(target_row, 1))
                    ped_type_tag = self.model.data(self.model.index(target_row, 118))
                    code_fab_equipment = self.model.data(self.model.index(target_row, 65))
                    codefab_body = self.model.data(self.model.index(target_row, 68))
                    qty_body = self.model.data(self.model.index(target_row, 69))
                    codefab_cover = self.model.data(self.model.index(target_row, 71))
                    qty_cover = self.model.data(self.model.index(target_row, 72))
                    codefab_stud = self.model.data(self.model.index(target_row, 74))
                    qty_stud = self.model.data(self.model.index(target_row, 75))
                    codefab_niphex = self.model.data(self.model.index(target_row, 77))
                    qty_niphex= self.model.data(self.model.index(target_row, 78))
                    codefab_valve = self.model.data(self.model.index(target_row, 80))
                    qty_valve = self.model.data(self.model.index(target_row, 81))
                    codefab_flange = self.model.data(self.model.index(target_row, 83))
                    qty_flange = self.model.data(self.model.index(target_row, 84))
                    codefab_dv = self.model.data(self.model.index(target_row, 86))
                    qty_dv = self.model.data(self.model.index(target_row, 87))
                    codefab_scale = self.model.data(self.model.index(target_row, 89))
                    qty_scale = self.model.data(self.model.index(target_row, 90))
                    codefab_illum = self.model.data(self.model.index(target_row, 92))
                    qty_illum = self.model.data(self.model.index(target_row, 93))
                    codefab_gasketglass = self.model.data(self.model.index(target_row, 95))
                    qty_gasketglass = self.model.data(self.model.index(target_row, 96))
                    codefab_glass = self.model.data(self.model.index(target_row, 98))
                    qty_glass = self.model.data(self.model.index(target_row, 99))
                    codefab_float = self.model.data(self.model.index(target_row, 101))
                    qty_float = self.model.data(self.model.index(target_row, 102))
                    codefab_mica = self.model.data(self.model.index(target_row, 104))
                    qty_mica = self.model.data(self.model.index(target_row, 105))
                    codefab_flags = self.model.data(self.model.index(target_row, 107))
                    qty_flags = self.model.data(self.model.index(target_row, 108))
                    codefab_gasketflange = self.model.data(self.model.index(target_row, 110))
                    qty_gasketflange = self.model.data(self.model.index(target_row, 111))
                    codefab_niptub = self.model.data(self.model.index(target_row, 112))
                    qty_niptub = self.model.data(self.model.index(target_row, 114))
                    codefab_antifrost = self.model.data(self.model.index(target_row, 116))
                    qty_antifrost = self.model.data(self.model.index(target_row, 117))
                    data_list.append([tag, ped_type_tag, code_fab_equipment, codefab_body, qty_body, codefab_cover,
                                        qty_cover, codefab_stud, qty_stud, codefab_niphex, qty_niphex,
                                        codefab_valve, qty_valve, codefab_flange, qty_flange, codefab_dv,
                                        qty_dv, codefab_scale, qty_scale, codefab_illum, qty_illum,
                                        codefab_gasketglass, qty_gasketglass, codefab_glass, qty_glass, codefab_float,
                                        qty_float, codefab_mica, qty_mica, codefab_flags, qty_flags,
                                        codefab_gasketflange, qty_gasketflange, codefab_niptub, qty_niptub, codefab_antifrost, qty_antifrost])

        self.tableElements.setRowCount(len(self.id_list) + 1)
        tablerow=1

        if self.variable in ['Caudal', 'Temperatura']:
            list_columns = [2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
        elif self.variable in ['Nivel']:
            list_columns = [2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]

    # fill the Qt Table with the results
        for column in range(self.columns_number):
            if column in list_columns:
                # chkBox = QtWidgets.QCheckBox()
                # chkBox.setCheckState(QtCore.Qt.CheckState.Unchecked)

                # cell_widget = QtWidgets.QWidget()
                # cell_layout = QtWidgets.QHBoxLayout()
                # cell_layout.addWidget(chkBox)
                # cell_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                # cell_widget.setLayout(cell_layout)
                # self.tableElements.setCellWidget(0, column, cell_widget)

                chkBoxItem  = QtWidgets.QTableWidgetItem()
                chkBoxItem.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                chkBoxItem.setCheckState(QtCore.Qt.CheckState.Unchecked)
                size = QtCore.QSize(0, 0)
                chkBoxItem.setSizeHint(size)
                self.tableElements.setItem(0, column, chkBoxItem)

        for row in data_list:
            for column in range(self.columns_number):
                value = row[column]
                if value is None or value == 0:
                    value = ''
                it = QtWidgets.QTableWidgetItem(str(value))
                it.setFlags(it.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                self.tableElements.setItem(tablerow, column, it)

            self.tableElements.setItemDelegateForRow(tablerow, AlignDelegate(self.tableElements))
            tablerow+=1

        self.tableElements.verticalHeader().hide()
        self.tableElements.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableElements.setHorizontalHeaderLabels(headers_labels)

        self.Button_Cancel.clicked.connect(ElementsFabOrder_Window.close)
        self.Button_Generate.clicked.connect(self.generate_ot)


    def retranslateUi(self, ElementsFabOrder_Window):
        _translate = QtCore.QCoreApplication.translate
        ElementsFabOrder_Window.setWindowTitle(_translate("ElementsFabOrder_Window", "Orden de Fabricación"))
        self.Button_Cancel.setText(_translate("ElementsFabOrder_Window", "Salir"))
        self.Button_Generate.setText(_translate("ElementsFabOrder_Window", "Generar OT"))


    def generate_ot(self):
        column_list = []
        otdata_list = []
        for column in range(self.tableElements.columnCount()):
            item = self.tableElements.item(0, column)
            if item is not None:
                if item.checkState() == QtCore.Qt.CheckState.Checked:
                    column_list.append(column)

        if len(column_list) == 0:
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(basedir, "Resources/Iconos/icon.ico"))), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("Orden de Fabricación")
            dlg.setText("Debe seleccionar al menos una columna para generar OT")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            dlg.exec()
            del dlg, new_icon
        else:
            for row in range(self.tableElements.rowCount()):
                if row != 0:
                    for column in column_list:
                        id_ot = self.tableElements.item(row, 1).text() + ' # ' + self.tableElements.item(row, column).text()
                        ped_type_tag = self.tableElements.item(row, 1).text()
                        item_text = self.tableElements.item(row, column).text()
                        if column == 2:
                            qty_item = 1
                        else:
                            qty_item = self.tableElements.item(row, column + 1).text()
                        if item_text != '':
                            otdata_list.append([id_ot, ped_type_tag, item_text, qty_item])

            df_otdata = pd.DataFrame(otdata_list)
            df_otdata = df_otdata.sort_values(by=2)
            df_otdata = df_otdata.reset_index(drop=True)

            self.otfaborder_window=QtWidgets.QMainWindow()
            self.ui=Ui_OTFabOrder_Window(df_otdata, self.id_list, self.model, self.variable)
            self.ui.setupUi(self.otfaborder_window)
            self.otfaborder_window.showMaximized()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ElementsFabOrder_Window = QtWidgets.QMainWindow()
    ui = Ui_CreateFabOrder_Window()
    ui.setupUi(ElementsFabOrder_Window)
    ElementsFabOrder_Window.show()
    sys.exit(app.exec())