from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog,QLabel,QLineEdit,QComboBox,QMessageBox,QLCDNumber,QHBoxLayout,QRadioButton,QButtonGroup
from PySide6 import QtGui
import os

def Tab_wholeMesh(second_layout):
    """ this function create the second tab in the GUI
    """
    global CSV_FIILE, INP_FILE, DAT_FILE, SAVE_FILE, PROCOCESS, THREAD_X, THREAD_Y, CORE
    CSV_FIILE = ""
    INP_FILE = ""
    DAT_FILE = ""
    SAVE_FILE = ""
    PROCOCESS = ""
    THREAD_X = 0
    THREAD_Y = 0
    CORE = 0
    ##create layout for input csv file
    input_layout1 = QHBoxLayout()
    input_layout1.setSpacing(20)
    input_layout1.setContentsMargins(10, 10, 10, 10)
    second_layout.addLayout(input_layout1)
    ### Create label csv
    label_browser_csv = QLabel("csv file path(result FEM):")

    ### Create line edit
    lineEdit_browser_csv = QLineEdit()

    lineEdit_browser_csv.textChanged.connect(lambda: write_text(lineEdit_browser_csv.text(), "CSV_FIILE"))
    ### Create button to browser csv file
    button_browser_csv = QPushButton("browser")

    button_browser_csv.setFixedHeight(30)
    button_browser_csv.setFixedWidth(100)
    button_browser_csv.clicked.connect(lambda: browse_csv_file())
    ### Add widget to layout
    ## add widget to input_layout1 to top to bottom
    input_layout1.addWidget(label_browser_csv)
    input_layout1.addWidget(lineEdit_browser_csv)
    input_layout1.addWidget(button_browser_csv)
    
    
    ##create layout for input inp file
    input_layout2 = QHBoxLayout()
    input_layout2.setSpacing(20)
    input_layout2.setContentsMargins(10, 10, 10, 10)
    second_layout.addLayout(input_layout2)
    ### Create label inp
    label_browser_inp = QLabel("inp file path(first mesh):")

    ### Create line edit
    lineEdit_browser_inp = QLineEdit()

    lineEdit_browser_inp.textChanged.connect(lambda: write_text(lineEdit_browser_inp.text(), "INP_FILE"))
    ### Create button to browser inp file
    button_browser_inp = QPushButton("browser")

    button_browser_inp.setFixedHeight(30)
    button_browser_inp.setFixedWidth(100)
    button_browser_inp.clicked.connect(lambda: browse_inp_file())
    ### Add widget to layout
    input_layout2.addWidget(label_browser_inp)
    input_layout2.addWidget(lineEdit_browser_inp)
    input_layout2.addWidget(button_browser_inp)

    ##create layout for input dat file
    input_layout3 = QHBoxLayout()
    input_layout3.setSpacing(20)
    input_layout3.setContentsMargins(10, 10, 10, 10)
    second_layout.addLayout(input_layout3)
    ### Create label dat
    label_browser_dat = QLabel("dat file path(second mesh):")

    ### Create line edit    
    lineEdit_browser_dat = QLineEdit()

    lineEdit_browser_dat.textChanged.connect(lambda: write_text(lineEdit_browser_dat.text(), "DAT_FILE"))
    ### Create button to browser dat file
    button_browser_dat = QPushButton("browser")

    button_browser_dat.setFixedHeight(30)
    button_browser_dat.setFixedWidth(100)
    button_browser_dat.clicked.connect(lambda: browse_dat_file())
    ### Add widget to layout
    input_layout3.addWidget(label_browser_dat)
    input_layout3.addWidget(lineEdit_browser_dat)
    input_layout3.addWidget(button_browser_dat)
    
    ## create layout for input save path
    input_layout4 = QHBoxLayout()
    input_layout4.setSpacing(20)
    input_layout4.setContentsMargins(10, 10, 10, 10)
    second_layout.addLayout(input_layout4)
    ### Create label save path
    label_browser_save = QLabel("save path:")

    ### Create line edit
    lineEdit_browser_save = QLineEdit()

    lineEdit_browser_save.textChanged.connect(lambda: write_text(lineEdit_browser_save.text(), "SAVE_FILE"))
    ### Create button to browser save path
    button_browser_save = QPushButton("browser")

    button_browser_save.setFixedHeight(30)
    button_browser_save.setFixedWidth(100)
    button_browser_save.clicked.connect(lambda: browse_save_path())
    ### Add widget to layout
    input_layout4.addWidget(label_browser_save)
    input_layout4.addWidget(lineEdit_browser_save)
    input_layout4.addWidget(button_browser_save)

    
    ##radio button for type prosessor for calculation
    input_layout5 = QHBoxLayout()
    input_layout5.setSpacing(20)
    input_layout5.setContentsMargins(10, 10, 10, 10)
    second_layout.addLayout(input_layout5)
    ### Create label type prosessor
    label_type_prosessor = QLabel("type prosessor:")


    ### Create radio button
    radio_group_type_prosessor = QButtonGroup()
    radio_group_type_prosessor.setExclusive(True)
    radio_group_type_prosessor.addButton(QRadioButton("serial CPU"))
    radio_group_type_prosessor.addButton(QRadioButton("GPU"))
    radio_group_type_prosessor.addButton(QRadioButton("parallel CPU"))
    radio_group_type_prosessor.addButton(QRadioButton("parallel CPU and GPU"))
    radio_group_type_prosessor.buttonClicked.connect(lambda: conditional_layout_serialCPU(second_layout)  if radio_group_type_prosessor.buttons()[0].isChecked() else None)
    radio_group_type_prosessor.buttonClicked.connect(lambda: conditional_layout_GPU(second_layout)        if radio_group_type_prosessor.buttons()[1].isChecked() else None)
    radio_group_type_prosessor.buttonClicked.connect(lambda: conditional_layout_parallelCPU(second_layout)  if radio_group_type_prosessor.buttons()[2].isChecked() else None)
    radio_group_type_prosessor.buttonClicked.connect(lambda: conditional_layout_serialCPUGPU(second_layout)  if radio_group_type_prosessor.buttons()[3].isChecked() else None)
    

    ### Add widget to layout
    input_layout5.addWidget(label_type_prosessor)
    input_layout5.addWidget(radio_group_type_prosessor.buttons()[0])
    input_layout5.addWidget(radio_group_type_prosessor.buttons()[1])
    input_layout5.addWidget(radio_group_type_prosessor.buttons()[2])
    input_layout5.addWidget(radio_group_type_prosessor.buttons()[3])
    
    input_layout6 = QHBoxLayout()
    input_layout6.setSpacing(20)
    input_layout6.setContentsMargins(10, 10, 10, 10)
    second_layout.addLayout(input_layout6)
    ### Create label thread per block
    label_thread_per_block = QLabel("thread per block: (")

    
    ### Create line edit
    lineEdit_thread_per_block = QLineEdit()
    lineEdit_thread_per_block.setDisabled(True)
    lineEdit_thread_per_block.setFixedWidth(20)
    lineEdit_thread_per_block.setFixedHeight(30)

    lineEdit_thread_per_block.textChanged.connect(lambda: write_text(lineEdit_thread_per_block.text(), "THREAD_X"))

    ### creat label ,
    label_comma = QLabel(",")

    ### Create line edit
    lineEdit_thread_per_block2 = QLineEdit()
    lineEdit_thread_per_block2.setDisabled(True)
    lineEdit_thread_per_block2.setFixedWidth(20)
    lineEdit_thread_per_block2.setFixedHeight(30)

    lineEdit_thread_per_block2.textChanged.connect(lambda: write_text(lineEdit_thread_per_block2.text(), "THREAD_Y"))
    ### creat label )
    label_comma2 = QLabel(")")


    
    ### Add widget to layout
    input_layout6.addWidget(label_thread_per_block)
    input_layout6.addWidget(lineEdit_thread_per_block)
    input_layout6.addWidget(label_comma)
    input_layout6.addWidget(lineEdit_thread_per_block2)
    input_layout6.addWidget(label_comma2)
    input_layout6.addStretch(2)
    
    ##create layout for input number of core
    input_layout7 = QHBoxLayout()
    input_layout7.setSpacing(20)
    input_layout7.setSpacing(20)
    input_layout7.setContentsMargins(10, 10, 10, 10)
    second_layout.addLayout(input_layout7)
    ### Create label for number of core
    label_number_of_core = QLabel("number of core:")

    
    ### Create line edit
    lineEdit_number_of_core = QLineEdit()
    lineEdit_number_of_core.setDisabled(True)
    lineEdit_number_of_core.setFixedWidth(20)

    lineEdit_number_of_core.textChanged.connect(lambda: write_text(lineEdit_number_of_core.text(),"CORE"))
    ### Add widget to layout
    input_layout7.addWidget(label_number_of_core)
    input_layout7.addWidget(lineEdit_number_of_core)
    
    input_layout7.addStretch(2)
    
    second_layout.addStretch(2)
    ##create run button
    run_button = QPushButton("Run")
    run_button.setFixedHeight(50)
    run_button.setFixedWidth(150)
    second_layout.addWidget(run_button)


    run_button.clicked.connect(lambda: run())
    def conditional_layout_serialCPU(second_layout)  :
        label_thread_per_block.setStyleSheet("color: gray")
        label_comma.setStyleSheet("color: gray")
        label_comma2.setStyleSheet("color: gray")
        label_number_of_core.setStyleSheet("color: gray")
        lineEdit_number_of_core.setDisabled(True)
        lineEdit_thread_per_block.setDisabled(True)
        lineEdit_thread_per_block2.setDisabled(True)
        write_text("serialCPU",'PROCOCESS')
    def conditional_layout_GPU(second_layout)        :
        lineEdit_thread_per_block2.setDisabled(False)
        lineEdit_thread_per_block.setDisabled(False)
        label_thread_per_block.setStyleSheet("color: black")
        label_comma.setStyleSheet("color: black")
        label_comma2.setStyleSheet("color: black")
        label_number_of_core.setStyleSheet("color: gray")
        lineEdit_number_of_core.setDisabled(True)
        write_text("GPU",'PROCOCESS')
    def conditional_layout_parallelCPU(second_layout):
        label_thread_per_block.setStyleSheet("color: gray")
        label_comma.setStyleSheet("color: gray")
        label_comma2.setStyleSheet("color: gray")
        label_number_of_core.setStyleSheet("color: black")
        lineEdit_number_of_core.setDisabled(False)
        lineEdit_thread_per_block.setDisabled(True)
        lineEdit_thread_per_block2.setDisabled(True)
        write_text("parallelCPU",'PROCOCESS')
    def conditional_layout_serialCPUGPU(second_layout):
        label_thread_per_block.setStyleSheet("color: black")
        label_comma.setStyleSheet("color: black")
        label_comma2.setStyleSheet("color: black")
        label_number_of_core.setStyleSheet("color: black")
        lineEdit_number_of_core.setDisabled(False)
        lineEdit_thread_per_block.setDisabled(False)
        lineEdit_thread_per_block2.setDisabled(False)
        write_text("CPUGPU",'PROCOCESS')
    def write_text(text,var):
        global CSV_FIILE, INP_FILE, DAT_FILE, SAVE_FILE, PROCOCESS, THREAD_X, THREAD_Y, CORE
        if var == "CSV_FIILE":
            CSV_FIILE = text
        elif var == "INP_FILE":
            INP_FILE = text
        elif var == "DAT_FILE":
            DAT_FILE = text
        elif var == "SAVE_FILE":
            SAVE_FILE = text
        elif var == "PROCOCESS":
            PROCOCESS = text
        elif var == "THREAD_X":
            THREAD_X = text
        elif var == "THREAD_Y":
            THREAD_Y = text
        elif var == "CORE":
            CORE = text
    
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
    
    def browse_dat_file():
        FILE,check=QFileDialog.getOpenFileName(None,"Open DAT File", "","DAT Files (*.dat)")
        if check:
            write_text(FILE,"DAT_FILE")
            lineEdit_browser_dat.setText(FILE) 
    
    def browse_save_path():
        FILE=QFileDialog.getExistingDirectory(None,"Select Directory")
        if FILE:
            write_text(FILE,"SAVE_FILE")
            lineEdit_browser_save.setText(FILE)
    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False         
    def run():
        global CSV_FIILE, INP_FILE, DAT_FILE, SAVE_FILE, PROCOCESS, THREAD_X, THREAD_Y, CORE
        if CSV_FIILE =="" or not CSV_FIILE.endswith(".csv") or not os.path.isfile( CSV_FIILE):
            QMessageBox.about(None, "Error", "CSV file is not valid")
        elif INP_FILE =="" or not INP_FILE.endswith(".inp") or not os.path.isfile( INP_FILE):
            QMessageBox.about(None, "Error", "INP file is not valid")
        elif DAT_FILE =="" or not DAT_FILE.endswith(".dat") or  not os.path.isfile( DAT_FILE):
            QMessageBox.about(None, "Error", "DAT file is not valid")
        elif SAVE_FILE =="" or not os.path.isdir( SAVE_FILE):
            QMessageBox.about(None, "Error", "Save path is not valid")
        elif PROCOCESS == "":
            QMessageBox.about(None, "Error", "Please select process type")
        else:
            if PROCOCESS=="serialCPU":
                os.system(f"python main_CPU_transferMesh.py {CSV_FIILE} {INP_FILE} {DAT_FILE} {SAVE_FILE} ")
            elif PROCOCESS=="GPU":
                if THREAD_X ==0 or not THREAD_X.isnumeric():
                    QMessageBox.about(None, "Error", "Please enter valid number of thread x")
                elif THREAD_Y ==0 or not THREAD_Y.isnumeric():
                    QMessageBox.about(None, "Error", "Please enter valid number of thread y")
                else:
                    os.system(f"python main_GPU_transferMesh.py {CSV_FIILE} {INP_FILE} {DAT_FILE} {SAVE_FILE} {THREAD_X} {THREAD_Y}")

            elif PROCOCESS=="parallelCPU":
                if  CORE ==0 or not CORE.isnumeric():
                    QMessageBox.about(None, "Error", "Please enter valid number of core")
                else :
                    os.system(f"python main_CPU_parallel_transferMesh.py {CSV_FIILE} {INP_FILE} {DAT_FILE} {SAVE_FILE} {CORE}")

