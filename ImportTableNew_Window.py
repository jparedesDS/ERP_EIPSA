# Form implementation generated from reading ui file 'ImportTableNew_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from tkinter.filedialog import askopenfilename
import sys
import psycopg2
from config import config
import re
import pandas as pd


class Ui_ImportTableNew_Window(object):
    def setupUi(self, ImportTableNew_Window):
        ImportTableNew_Window.setObjectName("ImportTableNew_Window")
        ImportTableNew_Window.resize(640, 330)
        ImportTableNew_Window.setMinimumSize(QtCore.QSize(640, 330))
        ImportTableNew_Window.setMaximumSize(QtCore.QSize(640, 330))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ImportTableNew_Window.setWindowIcon(icon)
        ImportTableNew_Window.setStyleSheet("QWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=ImportTableNew_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hLayout1 = QtWidgets.QHBoxLayout()
        self.hLayout1.setObjectName("hLayout1")
        self.label_TableName = QtWidgets.QLabel(parent=self.frame)
        self.label_TableName.setMinimumSize(QtCore.QSize(200, 55))
        self.label_TableName.setMaximumSize(QtCore.QSize(200, 55))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_TableName.setFont(font)
        self.label_TableName.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_TableName.setObjectName("label_TableName")
        self.hLayout1.addWidget(self.label_TableName)
        self.TableName_ImportTableNew = QtWidgets.QLineEdit(parent=self.frame)
        self.TableName_ImportTableNew.setMinimumSize(QtCore.QSize(250, 25))
        self.TableName_ImportTableNew.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TableName_ImportTableNew.setFont(font)
        self.TableName_ImportTableNew.setObjectName("TableName_ImportTableNew")
        self.hLayout1.addWidget(self.TableName_ImportTableNew)
        self.verticalLayout.addLayout(self.hLayout1)
        self.hLayout = QtWidgets.QHBoxLayout()
        self.hLayout.setObjectName("hLayout")
        self.label_SelectFile = QtWidgets.QLabel(parent=self.frame)
        self.label_SelectFile.setMinimumSize(QtCore.QSize(200, 55))
        self.label_SelectFile.setMaximumSize(QtCore.QSize(200, 55))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
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
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_name_file.setFont(font)
        self.label_name_file.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_name_file.setObjectName("label_name_file")
        self.verticalLayout.addWidget(self.label_name_file)
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
        ImportTableNew_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ImportTableNew_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        ImportTableNew_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ImportTableNew_Window)
        self.statusbar.setObjectName("statusbar")
        ImportTableNew_Window.setStatusBar(self.statusbar)

        self.retranslateUi(ImportTableNew_Window)
        self.Button_Cancel.clicked.connect(ImportTableNew_Window.close) # type: ignore
        self.Button_Import.clicked.connect(self.importtablenew)
        self.Button_Select.clicked.connect(self.fileselection)
        QtCore.QMetaObject.connectSlotsByName(ImportTableNew_Window)


    def retranslateUi(self, ImportTableNew_Window):
        _translate = QtCore.QCoreApplication.translate
        ImportTableNew_Window.setWindowTitle(_translate("ImportTableNew_Window", "Importar Tabla Nueva"))
        self.label_TableName.setText(_translate("ImportTableNew_Window", "Nombre Tabla:"))
        self.label_SelectFile.setText(_translate("ImportTableNew_Window", "Seleccionar Archivo:"))
        self.Button_Select.setText(_translate("ImportTableNew_Window", "Seleccionar"))
        self.label_name_file.setText(_translate("ImportTableNew_Window", ""))
        self.Button_Import.setText(_translate("ImportTableNew_Window", "Importar"))
        self.Button_Cancel.setText(_translate("ImportTableNew_Window", "Cancelar"))

#Function to create new table and import data from and Excel where first row is datatype and second row is column name
    def importtablenew(self):
        table_name=self.TableName_ImportTableNew.text()

        query_databasetables = """SELECT table_name
                                FROM information_schema.tables
                                WHERE table_schema = 'public' AND table_type = 'BASE TABLE';"""

        conn = None
        try:
        # read the connection parameters
            params = config()
        # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # execution of commands one by one
            cur.execute(query_databasetables)
            results=cur.fetchall()
        # close communication with the PostgreSQL database server
            cur.close()
        # commit the changes
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        tablesdatabase_names=[x[0] for x in results]

        if table_name == "":
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("ERP EIPSA")
            dlg.setText("Rellena el campo del nombre de la tabla")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            dlg.exec()
            del dlg, new_icon

        elif not re.match(r"^[a-z_]+$",table_name):
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("ERP EIPSA")
            dlg.setText("El formato del nombre de tabla no es correcto\n"
                        "Sólo pueden utilizarse minúsculas y guiones bajos")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            dlg.exec()
            del dlg, new_icon

        elif table_name in tablesdatabase_names:
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("ERP EIPSA")
            dlg.setText("El nombre de tabla introducido ya existe en la base de datos")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            dlg.exec()
            del dlg, new_icon

        elif self.label_name_file.text() == "":
            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("ERP EIPSA")
            dlg.setText("Selecciona un archivo para importar")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            dlg.exec()
            del dlg, new_icon

        else:
            excel_file=self.label_name_file.text().split("Archivo: ")[1]

            params = config()
            conn = psycopg2.connect(**params)
            cursor = conn.cursor()

        #Importing excel file into dataframes
            df_raw=pd.read_excel(excel_file)
            df_table = pd.read_excel(excel_file, skiprows=1)

        # Getting columns names and datatype for database table
            columns_datatypes = list(df_raw.columns)
            columns_names = list(df_table.columns)
            
        # Creating list of pairs (name, dataype) for each column
            columns_definition = [f"{name} {datatype}" for name, datatype in zip(columns_names, columns_datatypes)]
            
        # Creating query and executing it
            sql_create_table = f"CREATE TABLE {table_name} ({', '.join(columns_definition)})"
            cursor.execute(sql_create_table)

        # Loop through each row of the DataFrame and insert the data into the table
            for index, row in df_table.iterrows():
            # Create a list of pairs (column_name, column_value) for each column with value
                columns_values = [(column, str(row[column])) for column in df_table.columns if not pd.isnull(row[column])]

            # Wrap values with double quotes if they contain double quotes or spaces
                columns_values = [(column, f"'{values}'") for column, values in columns_values]

            # Creating string for columns names
                columns = ', '.join([column for column, _ in columns_values])

            # Creating string for columns values
                values = ', '.join([values for _, values in columns_values])

            # Creating insertion query and executing it
                sql_insertion = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
                cursor.execute(sql_insertion)

        # Closing cursor and database connection
            conn.commit()
            cursor.close()
            conn.close()

            dlg = QtWidgets.QMessageBox()
            new_icon = QtGui.QIcon()
            new_icon.addPixmap(QtGui.QPixmap("//nas01/DATOS/Comunes/EIPSA-ERP/Iconos/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            dlg.setWindowIcon(new_icon)
            dlg.setWindowTitle("ERP EIPSA")
            dlg.setText("Tabla creada y datos importados con éxito")
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            dlg.exec()
            del dlg, new_icon

            self.TableName_ImportTableNew.setText("")
            self.label_name_file.setText("")


#Function for selecting file to import
    def fileselection(self):
        fname = askopenfilename(filetypes=[("Archivos de Excel", "*.xlsx")],
                            title="Seleccionar archivo Excel")
        if fname:
            self.label_name_file.setText("Archivo: " + fname)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImportTableNew_Window = QtWidgets.QMainWindow()
    ui = Ui_ImportTableNew_Window()
    ui.setupUi(ImportTableNew_Window)
    ImportTableNew_Window.show()
    sys.exit(app.exec())