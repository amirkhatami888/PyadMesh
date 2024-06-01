# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog,QLabel,QLineEdit,QComboBox,QMessageBox,QVBoxLayout, QRadioButton,QHBoxLayout
from PySide6 import QtGui
import os


def Tab_onePoint(first_layout):
    """ this function create the first tab in the GUI
    """
    global CSV_FIILE,INP_FILE,PROCOCESS,POINT_X,POINT_Y
    CSV_FIILE = ""
    INP_FILE = ""
    PROCOCESS = ""
    POINT_X=0
    POINT_Y=0

    #create layout for input csv file
    input_layout1 = QHBoxLayout()
    input_layout1.setSpacing(20)
    input_layout1.setContentsMargins(10, 10, 10, 10)
    first_layout.addLayout(input_layout1)
    
    #Create label csv
    label_browser_csv = QLabel("csv file path(result FEM):")
    #Create line edit
    lineEdit_browser_csv = QLineEdit()
    lineEdit_browser_csv.textChanged.connect(lambda: write_text(lineEdit_browser_csv.text(), "CSV_FIILE"))
    ### Create button to browser csv file
    button_browser_csv = QPushButton("browser")
    button_browser_csv.setFixedHeight(30)
    button_browser_csv.setFixedWidth(100)
    button_browser_csv.clicked.connect(lambda:  browse_csv_file())
    
    #Add widget to layout
    input_layout1.addWidget(label_browser_csv)
    input_layout1.addWidget(lineEdit_browser_csv)
    input_layout1.addWidget(button_browser_csv)
    
    #create layout for input inp file
    input_layout2 = QHBoxLayout()
    input_layout2.setSpacing(20)
    input_layout2.setContentsMargins(10, 10, 10, 10)
    first_layout.addLayout(input_layout2)
    
    # Create label inp
    label_browser_inp = QLabel("inp file path(first mesh):")
    
    #Create line edit
    lineEdit_browser_inp = QLineEdit()
    lineEdit_browser_inp.textChanged.connect(lambda: write_text(lineEdit_browser_inp.text(), "INP_FILE"))
    
    #Create button to browser inp file
    button_browser_inp = QPushButton("browser")
    button_browser_inp.setFixedHeight(30)
    button_browser_inp.setFixedWidth(100)
    button_browser_inp.clicked.connect(lambda:  browse_inp_file())
    
    #Add widget to layout
    input_layout2.addWidget(label_browser_inp)
    input_layout2.addWidget(lineEdit_browser_inp)
    input_layout2.addWidget(button_browser_inp)

    #create layout for input point data
    input_layout3 = QHBoxLayout()
    input_layout3.setSpacing(20)
    input_layout3.setContentsMargins(10, 10, 10, 10)
    first_layout.addLayout(input_layout3)
    
    #Create label point data x
    label_point_data_x = QLabel("x:")

    #Create line edit
    lineEdit_point_data_x = QLineEdit()
    lineEdit_point_data_x.setFixedWidth(100)
 
    lineEdit_point_data_x.textChanged.connect(lambda: write_text(lineEdit_point_data_x.text(), "POINT_X"))  
    #Create label point data y
    label_point_data_y = QLabel("y:")

    #Create line edit
    lineEdit_point_data_y = QLineEdit()
    lineEdit_point_data_y.setFixedWidth(100)
    lineEdit_point_data_y.textChanged.connect(lambda: write_text(lineEdit_point_data_y.text(), "POINT_Y"))
    
    #Add widget to layout
    input_layout3.addWidget(label_point_data_x)
    input_layout3.addWidget(lineEdit_point_data_x)
    input_layout3.addWidget(label_point_data_y)
    input_layout3.addWidget(lineEdit_point_data_y)
    input_layout3.addStretch(1)
    
    #radio button for type prosessor for calculation
    input_layout4 = QHBoxLayout()
    input_layout4.setSpacing(20)
    input_layout4.setContentsMargins(10, 10, 10, 10)
    first_layout.addLayout(input_layout4)
    
    #Create label type of processor
    label_type_processor = QLabel("type of processor:")

    #Create radio button
    radio_button1 = QRadioButton("CPU") 
    radio_button2 = QRadioButton("GPU")
    radio_button1.toggled.connect(lambda: write_text("CPU", "PROCOCESS"))
    radio_button2.toggled.connect(lambda: write_text("GPU", "PROCOCESS"))
    
    #Add widget to layout
    input_layout4.addWidget(label_type_processor)
    input_layout4.addWidget(radio_button1)
    input_layout4.addWidget(radio_button2)
    input_layout4.addStretch(1)
    
    #add stretch
    first_layout.addStretch(1)

    #create run button
    run_button = QPushButton("Run")
    run_button.setFixedHeight(50)
    run_button.setFixedWidth(150)
    run_button.clicked.connect(lambda: run())
    first_layout.addWidget(run_button)
    def write_text(text,var):

        global CSV_FIILE,INP_FILE,PROCOCESS,POINT_X,POINT_Y
        if var=="CSV_FIILE":
            CSV_FIILE=text
        elif var=="INP_FILE":
            INP_FILE=text
        elif var=="PROCOCESS":
            PROCOCESS=text
        elif var=="POINT_X":    
            POINT_X=text
        elif var=="POINT_Y":    
            POINT_Y=text

    def browse_csv_file():
        FILE,check=QFileDialog.getOpenFileName(None,"Open CSV File", "","CSV Files (*.csv)")
        if check:
            write_text(FILE,"CSV_FIILE")
            lineEdit_browser_csv.setText(FILE)
    
    def browse_inp_file():
        FILE,check=QFileDialog.getOpenFileName(None,"Open INP File", "","INP Files (*.inp)")
        if check:
            write_text(FILE,"INP_FILE")
            lineEdit_browser_inp.setText(FILE)
 
    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False  

    def run():
        if CSV_FIILE==""or not CSV_FIILE.endswith(".csv") or not os.path.exists(CSV_FIILE):
            QMessageBox.about(None,"Error","Please select CSV file correctlly")
        elif INP_FILE==""or not INP_FILE.endswith(".inp") or not os.path.exists(INP_FILE):
            QMessageBox.about(None,"Error","Please select INP file correctlly")
        elif PROCOCESS=="":
            QMessageBox.about(None,"Error","Please select type of processor")
        elif POINT_X=="" or not isfloat(POINT_X):
            QMessageBox.about(None,"Error","Please enter x coordinate correctlly")
        elif POINT_Y=="" or not isfloat(POINT_Y):
            QMessageBox.about(None,"Error","Please enter y coordinate correctlly")
        else:
            if PROCOCESS=="CPU":
                os.system(f"python main_CPU_transferpoint.py {CSV_FIILE} {INP_FILE} {POINT_X} {POINT_Y}")
                #call cpu function
            elif PROCOCESS=="GPU":

                os.system(f"python main_GPU_transferpoint.py {CSV_FIILE} {INP_FILE} {POINT_X} {POINT_Y}")
                #call gpu function
                
            