# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog,QLabel,QLineEdit,QComboBox,QMessageBox,QLCDNumber,QHBoxLayout,QRadioButton,QButtonGroup, QFileDialog
from PySide6 import QtGui
import os

def Tab_plotError(fourth_layout):
        """ this function create the fourth tab in the GUI
        """
        global CSV_FIILE, INP_FILE, SAVE_FILE, PROCOCESS,error_thereshold
        CSV_FIILE = ""
        INP_FILE = ""
        SAVE_FILE = ""
        PROCOCESS = ""
        error_thereshold=0.001


        ##create layout for input csv file
        input_layout1 = QHBoxLayout()
        input_layout1.setSpacing(20)
        input_layout1.setContentsMargins(10, 10, 10, 10)
        fourth_layout.addLayout(input_layout1)
        ### Create label csv
        label_browser_csv = QLabel("csv file path(result FEM):")


        ### Create line edit
        lineEdit_browser_csv = QLineEdit()
        lineEdit_browser_csv.textChanged.connect(lambda: write_text(lineEdit_browser_csv.text(),"CSV_FIILE"))
        ### Create button to browser csv file
        button_browser_csv = QPushButton("browser")
        
        button_browser_csv.setFixedHeight(30)
        button_browser_csv.setFixedWidth(100)
        button_browser_csv.clicked.connect(lambda: browse_csv_file())
        ### Add widget to layout
        input_layout1.addWidget(label_browser_csv)
        input_layout1.addWidget(lineEdit_browser_csv)
        input_layout1.addWidget(button_browser_csv)

        ##create layout for input inp file
        input_layout2 = QHBoxLayout()
        input_layout2.setSpacing(20)
        input_layout2.setContentsMargins(10, 10, 10, 10)
        fourth_layout.addLayout(input_layout2)
        ### Create label inp
        label_browser_inp = QLabel("inp file path(first mesh):")

        ### Create line edit
        lineEdit_browser_inp = QLineEdit()

        lineEdit_browser_inp.textChanged.connect(lambda: write_text(lineEdit_browser_inp.text(),"INP_FILE"))
        ### Create button to browser inp file
        button_browser_inp = QPushButton("browser")

        button_browser_inp.setFixedHeight(30)
        button_browser_inp.setFixedWidth(100)
        button_browser_inp.clicked.connect(lambda: browse_inp_file())
        ### Add widget to layout
        input_layout2.addWidget(label_browser_inp)
        input_layout2.addWidget(lineEdit_browser_inp)
        input_layout2.addWidget(button_browser_inp)

        ##create layout for input  save path
        input_layout3 = QHBoxLayout()
        input_layout3.setSpacing(20)
        input_layout3.setContentsMargins(10, 10, 10, 10)
        fourth_layout.addLayout(input_layout3)
        ### Create label save path
        label_browser_save = QLabel("save path:")

        ### Create line edit
        lineEdit_browser_save = QLineEdit()

        lineEdit_browser_save.textChanged.connect(lambda: write_text(lineEdit_browser_save.text(),"SAVE_FILE"))
        ### Create button to browser save path
        button_browser_save = QPushButton("browser")

        button_browser_save.setFixedHeight(30)
        button_browser_save.setFixedWidth(100)
        button_browser_save.clicked.connect(lambda: browse_save_path())
        ### Add widget to layout
        input_layout3.addWidget(label_browser_save)
        input_layout3.addWidget(lineEdit_browser_save)
        input_layout3.addWidget(button_browser_save)

        #radio button for type prosessor for calculation
        input_layout4 = QHBoxLayout()
        input_layout4.setSpacing(20)
        input_layout4.setContentsMargins(10, 10, 10, 10)
        fourth_layout.addLayout(input_layout4)
        ### Create label type of processor
        label_type_processor = QLabel("type of processor:")

        ### Create radio button
        radio_button1 = QRadioButton("CPU") 

        radio_button2 = QRadioButton("GPU")
     
        radio_button1.toggled.connect(lambda: radio_button_checked("CPU"))
        radio_button2.toggled.connect(lambda: radio_button_checked("GPU"))

        ### Add widget to layout
        input_layout4.addWidget(label_type_processor)
        input_layout4.addWidget(radio_button1)
        input_layout4.addWidget(radio_button2)




        ### Create label  ERROR threashold
        
        input_layout5 = QHBoxLayout()
        input_layout5.setSpacing(20)
        input_layout5.setContentsMargins(10, 10, 10, 10)
        fourth_layout.addLayout(input_layout5)



        ### Create label ERROR threshold
        label_error_threshold = QLabel("Error threshold:")

        ### Create line edit
        lineEdit_error_threshold = QLineEdit()
        lineEdit_error_threshold.textChanged.connect(lambda: write_text(lineEdit_error_threshold.text(), "error_thereshold"))
        ### Add widget to layout
        
        input_layout5.addWidget(label_error_threshold)
        input_layout5.addWidget(lineEdit_error_threshold)
        
        ###add space
        input_layout5.addStretch(1)






        ##space empty
        fourth_layout.addStretch(1)
        ##create run button
        run_button = QPushButton("Run")
        run_button.setFixedHeight(50)
        run_button.setFixedWidth(150)


        fourth_layout.addWidget(run_button)
        run_button.clicked.connect( lambda: run_button_clicked())
        def isfloat(value):
                try:
                        float(value)
                        return True
                except ValueError:
                        return False         
        def write_text(text, var):
                global CSV_FIILE, INP_FILE, SAVE_FILE, PROCOCESS

                if var == "CSV_FIILE":
                        CSV_FIILE = text
                elif var == "INP_FILE":
                        INP_FILE = text
                elif var == "SAVE_FILE":
                        SAVE_FILE = text
                elif var == "PROCOCESS":
                        PROCOCESS = text
                elif var=="error_thereshold":
                        error_thereshold=text
        def browse_csv_file():
                FILE,check=QFileDialog.getOpenFileName(None,"Open CSV File", "","CSV Files (*.csv)")
                if check:
                        lineEdit_browser_csv.setText(FILE)
                        write_text(FILE,"CSV_FIILE")
                        
        def browse_inp_file():
                FILE,check=QFileDialog.getOpenFileName(None,"Open INP or dat File", "", "INP Files (*.inp);;dat Files (*.dat)")
                if check:
                        lineEdit_browser_inp.setText(FILE)
                        write_text(FILE,"INP_FILE")
        def browse_save_path():
                SPATH=QFileDialog.getExistingDirectory(None,"Select Directory")
                if SPATH:
                        lineEdit_browser_save.setText(SPATH)
                        write_text(SPATH,"SAVE_FILE")
        def radio_button_checked(text):
                if text == "CPU":
                        write_text(text,"PROCOCESS")
                elif text == "GPU":
                        write_text(text,"PROCOCESS")

        def run_button_clicked():
                if CSV_FIILE == ""or not CSV_FIILE.endswith(".csv") or isfloat(CSV_FIILE) == True:
                        QMessageBox.about(None,"Error","please select csv file correctlly")
                elif INP_FILE == ""or not(INP_FILE.endswith(".inp") or INP_FILE.endswith(".dat")) or isfloat(INP_FILE) == True:

                        QMessageBox.about(None,"Error","please select inp file correctlly")
                elif SAVE_FILE == ""or os.path.isdir(SAVE_FILE) == False:
                       QMessageBox.about(None,"Error","please select save path")
                elif PROCOCESS == "":   
                       QMessageBox.about(None,"Error","please select type of processor")
                else:
                        if PROCOCESS=="CPU":
                                os.system(f"python main_CPU_plotError.py {CSV_FIILE} {INP_FILE} {SAVE_FILE} {error_thereshold}")

                        elif PROCOCESS=="GPU":
                                os.system(f"python main_GPU_plotError.py {CSV_FIILE} {INP_FILE} {SAVE_FILE} {error_thereshold}")


                
        