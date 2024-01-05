from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog,QLabel,QLineEdit,QComboBox,QMessageBox,QLCDNumber,QHBoxLayout,QRadioButton,QButtonGroup,QRadioButton
from PySide6 import QtGui


import os
def Tab_Mesh_generatorRefiner(sixth_layout):
    """this function create the third tab of GUI
    """
    global CSV_FIILE
    global INP_FILE
    global IGS_FILE
    global DISP_FILE 
    global SAVE_FILE
    global PROCOCESS
    global scalefactor
    global MAX_ITER
    CSV_FIILE = ""
    INP_FILE = ""
    IGS_FILE = ""
    DISP_FILE= ""
    SAVE_FILE = ""
    PROCOCESS = ""
    MAX_ITER=0
    scalefactor=0

   
    ##create layout for input inp file
    input_layout2 = QHBoxLayout()
    input_layout2.setSpacing(20)
    input_layout2.setContentsMargins(10, 10, 10, 10)
    sixth_layout.addLayout(input_layout2)
    ### Create label inp
    label_browser_inp = QLabel("inp file path( mesh):")
    ### Create line edit
    lineEdit_browser_inp = QLineEdit()
    lineEdit_browser_inp.textChanged.connect(lambda: write_text(lineEdit_browser_inp.text(), "INP_FILE"))
    ### Create button to browser inp file
    button_browser_inp = QPushButton("browser")

    button_browser_inp.setFixedWidth(100)
    button_browser_inp.setFixedHeight(30)
    button_browser_inp.clicked.connect(lambda: browse_inp_file())
    ### Add widget to layout
    input_layout2.addWidget(label_browser_inp)
    input_layout2.addWidget(lineEdit_browser_inp)
    input_layout2.addWidget(button_browser_inp)
    
    ## create layout for input igs file
    layout_igs = QHBoxLayout()
    layout_igs.setSpacing(20)
    layout_igs.setContentsMargins(10, 10, 10, 10)
    sixth_layout.addLayout(layout_igs)
    ### Create label igs
    label_browser_igs = QLabel("igs path(geo of mesh):")
    
    ### Create line edit
    lineEdit_browser_igs = QLineEdit()
    lineEdit_browser_igs.textChanged.connect(lambda: write_text(lineEdit_browser_igs.text(), "IGS_FILE"))
    ### Create button to browser igs file
    button_browser_igs = QPushButton("browser")

    button_browser_igs.setFixedWidth(100)
    button_browser_igs.setFixedHeight(30)
    button_browser_igs.clicked.connect(lambda: browse_igs_file())
    ### Add widget to layout
    layout_igs.addWidget(label_browser_igs)
    layout_igs.addWidget(lineEdit_browser_igs)
    layout_igs.addWidget(button_browser_igs)
    
    
    
    
    ##create layout for displacement file
    layout_disp = QHBoxLayout()
    layout_disp.setSpacing(20)
    layout_disp.setContentsMargins(10, 10, 10, 10)
    sixth_layout.addLayout(layout_disp)
    ### Create label igs
    label_browser_disp = QLabel("dispacement path:")
    ### Create line edit
    lineEdit_browser_disp=QLineEdit()
    lineEdit_browser_disp.textChanged.connect(lambda: write_text(lineEdit_browser_disp.text(),"DISP_FILE"))
    ### Create button to browser igs file
    button_browser_disp = QPushButton("browser")

    button_browser_disp.setFixedWidth(100)
    button_browser_disp.setFixedHeight(30)
    button_browser_disp.clicked.connect(lambda: browse_disp_file())
    ### Add widget to layout
    layout_disp.addWidget(label_browser_disp)
    layout_disp.addWidget(lineEdit_browser_disp)
    layout_disp.addWidget(button_browser_disp)
    ## create layout for input save path
    layout_save = QHBoxLayout()
    layout_save.setSpacing(20)
    layout_save.setContentsMargins(10, 10, 10, 10)
    sixth_layout.addLayout(layout_save)
    ### Create label save path
    label_browser_save = QLabel("save path:")
    ### Create line edit
    lineEdit_browser_save = QLineEdit()
    lineEdit_browser_save.textChanged.connect(lambda: write_text(lineEdit_browser_save.text(), "SAVE_FILE"))
    ### Create button to browser save path
    button_browser_save = QPushButton("browser")

    button_browser_save.setFixedWidth(100)
    button_browser_save.setFixedHeight(30)
    button_browser_save.clicked.connect(lambda: browse_save_path())
    ### Add widget to layout    
    layout_save.addWidget(label_browser_save)
    layout_save.addWidget(lineEdit_browser_save)
    layout_save.addWidget(button_browser_save)
    
    
    #radio button for type prosessor for calculation
    input_layout4 = QHBoxLayout()
    input_layout4.setSpacing(20)
    input_layout4.setContentsMargins(10, 10, 10, 10)
    sixth_layout.addLayout(input_layout4)
    ### Create label type of processor
    label_type_processor = QLabel("type of processor:")

    ### Create radio button
    radio_button1 = QRadioButton("CPU") 
    radio_button2 = QRadioButton("GPU")
    radio_button3 = QRadioButton("parallelCPU")
    radio_button1.toggled.connect(lambda: write_text("CPU","PROCOCESS"))
    radio_button2.toggled.connect(lambda: write_text("GPU","PROCOCESS"))

    ### Add widget to layout
    input_layout4.addWidget(label_type_processor)
    input_layout4.addWidget(radio_button1)
    input_layout4.addWidget(radio_button2)
    
    ### maximun ERROR and maximun iteration
    input_layout5 = QHBoxLayout()
    input_layout5.setSpacing(20)
    input_layout5.setContentsMargins(10, 10, 10, 10)
    sixth_layout.addLayout(input_layout5)
    ### Create label maximun ERROR


    ### Create label maximun iteration
    label_max_iteration = QLabel("max iteration:")

    ### Create line edit
    lineEdit_max_iteration = QLineEdit()
    lineEdit_max_iteration.textChanged.connect(lambda: write_text(lineEdit_max_iteration.text(), "MAX_ITER"))
    ### Add widget to layout
 
    input_layout5.addWidget(label_max_iteration)
    input_layout5.addWidget(lineEdit_max_iteration)


    ### Create label beta
    label_scalefactor = QLabel("<html> &beta;</html>")
    
    ### Create line edit
    lineEdit_scalefactor = QLineEdit()
    lineEdit_scalefactor.textChanged.connect(lambda: write_text(lineEdit_scalefactor.text(), "scalefactor"))

    ### Add widget to layout
    input_layout5.addWidget(label_scalefactor)
    input_layout5.addWidget(lineEdit_scalefactor)
    

    ## space 
    sixth_layout.addStretch(2)
    ## run button
    run_button = QPushButton("Run")
    run_button.setFixedHeight(50)
    run_button.setFixedWidth(150)

    sixth_layout.addWidget(run_button)
    run_button.clicked.connect(lambda: run())
    def write_text(text,var):
        global CSV_FIILE, INP_FILE, IGS_FILE,SAVE_FILE, PROCOCESS, scalefactor,MAX_ITER,DISP_FILE
        if var=="CSV_FIILE":
            CSV_FIILE = text
        elif var=="INP_FILE":
            INP_FILE = text
        elif var=="IGS_FILE":
            IGS_FILE = text
        elif var =="DISP_FILE":
            DISP_FILE = text
        elif var=="SAVE_FILE":
            SAVE_FILE = text
        elif var=="PROCOCESS":
            PROCOCESS = text
        elif var=="MAX_ITER":
            MAX_ITER = text
        elif var=="scalefactor":
            scalefactor = text


    
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
    
    def browse_igs_file():
        FILE,check=QFileDialog.getOpenFileName(None,"Open IGS File", "","IGS Files (*.igs)")
        if check:
            write_text(FILE,"IGS_FILE")
            lineEdit_browser_igs.setText(FILE)
            
            
            
    def browse_disp_file():
        FILE,check=QFileDialog.getOpenFileName(None,"Open DISP File", "","DISP Files (*.csv)")
        if check:
            write_text(FILE,"DISP_FILE")
            lineEdit_browser_disp.setText(FILE)
            DISP_FILE=FILE
    def browse_save_path():
        #select directory
        FILE=QFileDialog.getExistingDirectory(None,"Select Directory")
        if FILE:
            write_text(FILE,"SAVE_FILE")
            lineEdit_browser_save.setText(FILE)

    def radio_button_checked(text):
            if text == "CPU":
                    write_text(text,"PROCOCESS")
            elif text == "GPU":
                    write_text(text,"PROCOCESS")

                
                    
    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False                
    def run():


        if INP_FILE == ""or not INP_FILE.endswith(".inp")or not os.path.isfile(INP_FILE):
            QMessageBox.about(None,"Error","please select inp file correctlly")
        elif IGS_FILE == ""or not IGS_FILE.endswith(".igs")or not os.path.isfile(IGS_FILE):
            QMessageBox.about(None,"Error","please select igs file correctlly")
        elif DISP_FILE == ""or not DISP_FILE.endswith(".csv")or not os.path.isfile(DISP_FILE):
            print(DISP_FILE)
            QMessageBox.about(None,"Error","please select dispcament file correctlly")    
        elif SAVE_FILE == "" or os.path.isfile(SAVE_FILE) or not os.path.isdir(SAVE_FILE):
            QMessageBox.about(None,"Error","please select save file correctlly")
        elif MAX_ITER == 0 or not MAX_ITER.isnumeric():
            QMessageBox.about(None,"Error","please enter max iteration correctlly")

        elif PROCOCESS == "":
            QMessageBox.about(None,"Error","please select proccess correctlly")
        else:
            if PROCOCESS == "CPU":
                os.system(f"python main_CPU_Mesh_generatorRefiner.py  {INP_FILE} {IGS_FILE} {SAVE_FILE} {MAX_ITER} {scalefactor} {DISP_FILE} ")
            if PROCOCESS == "GPU":
                os.system(f"python main_GPU_Mesh_generatorRefiner.py  {INP_FILE} {IGS_FILE} {SAVE_FILE} {MAX_ITER} {scalefactor} {DISP_FILE} ")



