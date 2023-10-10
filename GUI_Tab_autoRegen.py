from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog,QLabel,QLineEdit,QComboBox,QMessageBox,QLCDNumber,QHBoxLayout,QRadioButton,QButtonGroup,QRadioButton
from PySide6 import QtGui


import os
def Tab_autoRegen(third_layout):
    global CSV_FIILE, INP_FILE, IGS_FILE,SAVE_FILE, PROCOCESS, MAX_ERROR, scalefactor, ratio_selection,MAX_ITER
    CSV_FIILE = ""
    INP_FILE = ""
    IGS_FILE = ""
    SAVE_FILE = ""
    PROCOCESS = ""
    MAX_ITER=0
    scalefactor=0
    ratio_selection=0
    ##create layout for input csv file
    input_layout1 = QHBoxLayout()
    input_layout1.setSpacing(20)
    input_layout1.setContentsMargins(10, 10, 10, 10)
    third_layout.addLayout(input_layout1)
    ### Create label csv
    label_browser_csv = QLabel("csv file path(result FEM):")
    ### Create line edit
    lineEdit_browser_csv = QLineEdit()
    lineEdit_browser_csv.textChanged.connect(lambda: write_text(lineEdit_browser_csv.text(), "CSV_FIILE"))
    ### Create button to browser csv file
    button_browser_csv = QPushButton("browser")

    button_browser_csv.setFixedWidth(100)
    button_browser_csv.setFixedHeight(30)
    button_browser_csv.clicked.connect(lambda: browse_csv_file())
    ### Add widget to layout
    input_layout1.addWidget(label_browser_csv)
    input_layout1.addWidget(lineEdit_browser_csv)
    input_layout1.addWidget(button_browser_csv)
    
    ##create layout for input inp file
    input_layout2 = QHBoxLayout()
    input_layout2.setSpacing(20)
    input_layout2.setContentsMargins(10, 10, 10, 10)
    third_layout.addLayout(input_layout2)
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
    third_layout.addLayout(layout_igs)
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

    ## create layout for input save path
    layout_save = QHBoxLayout()
    layout_save.setSpacing(20)
    layout_save.setContentsMargins(10, 10, 10, 10)
    third_layout.addLayout(layout_save)
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
    third_layout.addLayout(input_layout4)
    ### Create label type of processor
    label_type_processor = QLabel("type of processor:")

    ### Create radio button
    radio_button1 = QRadioButton("CPU") 
    radio_button2 = QRadioButton("GPU")
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
    third_layout.addLayout(input_layout5)
    ### Create label maximun ERROR


    ### Create label maximun iteration
    label_max_iteration = QLabel("max iteration:")

    ### Create line edit
    lineEdit_max_iteration = QLineEdit()
    lineEdit_max_iteration.textChanged.connect(lambda: write_text(lineEdit_max_iteration.text(), "MAX_ITER"))
    ### Add widget to layout
 
    input_layout5.addWidget(label_max_iteration)
    input_layout5.addWidget(lineEdit_max_iteration)

    ### Create maximun stepSize and minimun stepSize
    input_layout6 = QHBoxLayout()
    input_layout6.setSpacing(20)
    input_layout6.setContentsMargins(10, 10, 10, 10)
    third_layout.addLayout(input_layout6)

    ### Create label maximun stepSize
    label_scalefactor = QLabel("scalefactor:")
    
    ### Create line edit
    lineEdit_scalefactor = QLineEdit()
    lineEdit_scalefactor.textChanged.connect(lambda: write_text(lineEdit_scalefactor.text(), "scalefactor"))
    ### Create label minimun stepSize
    label_ratio_selection = QLabel("selection_ratio:")

    ### Create line edit
    lineEdit_ratio_selection = QLineEdit()
    lineEdit_ratio_selection.textChanged.connect(lambda: write_text(lineEdit_ratio_selection.text(), "ratio_selection"))
    ### Add widget to layout
    input_layout6.addWidget(label_scalefactor)
    input_layout6.addWidget(lineEdit_scalefactor)
    input_layout6.addWidget(label_ratio_selection)
    input_layout6.addWidget(lineEdit_ratio_selection)


    ## space 
    third_layout.addStretch(2)
    ## run button
    run_button = QPushButton("Run")
    run_button.setFixedHeight(50)
    run_button.setFixedWidth(150)

    third_layout.addWidget(run_button)
    run_button.clicked.connect(lambda: run())
    def write_text(text,var):
        global CSV_FIILE, INP_FILE, IGS_FILE,SAVE_FILE, PROCOCESS, scalefactor, ratio_selection,MAX_ITER
        if var=="CSV_FIILE":
            CSV_FIILE = text
        elif var=="INP_FILE":
            INP_FILE = text
        elif var=="IGS_FILE":
            IGS_FILE = text
        elif var=="SAVE_FILE":
            SAVE_FILE = text
        elif var=="PROCOCESS":
            PROCOCESS = text
        elif var=="MAX_ITER":
            MAX_ITER = text
        elif var=="scalefactor":
            scalefactor = text
        elif var=="ratio_selection":
            ratio_selection = text

    
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
        if CSV_FIILE == ""or not CSV_FIILE.endswith(".csv") or not os.path.isfile(CSV_FIILE):
            QMessageBox.about(None,"Error","please select csv file correctlly")
        elif INP_FILE == ""or not INP_FILE.endswith(".inp")or not os.path.isfile(INP_FILE):
            QMessageBox.about(None,"Error","please select inp file correctlly")
        elif IGS_FILE == ""or not IGS_FILE.endswith(".igs")or not os.path.isfile(IGS_FILE):
            QMessageBox.about(None,"Error","please select igs file correctlly")
        elif SAVE_FILE == "" or os.path.isfile(SAVE_FILE) or not os.path.isdir(SAVE_FILE):
            QMessageBox.about(None,"Error","please select save file correctlly")
        elif MAX_ITER == 0 or not MAX_ITER.isnumeric():
            QMessageBox.about(None,"Error","please enter max iteration correctlly")
        elif scalefactor == 0 or not isfloat(scalefactor):
            QMessageBox.about(None,"Error","please enter max stepsize correctlly")
        elif ratio_selection == 0 or not isfloat(ratio_selection):
            QMessageBox.about(None,"Error","please enter min stepsize correctlly")
        elif PROCOCESS == "":
            QMessageBox.about(None,"Error","please select proccess correctlly")
        else:
            if PROCOCESS == "CPU":
                os.system(f"python main_CPU_auto_generateMesh.py {CSV_FIILE} {INP_FILE} {IGS_FILE} {SAVE_FILE} {MAX_ITER} {scalefactor} {ratio_selection} ")
            if PROCOCESS == "GPU":
                os.system(f"python main_GPU_auto_generateMesh.py {CSV_FIILE} {INP_FILE} {IGS_FILE} {SAVE_FILE} {MAX_ITER} {scalefactor} {ratio_selection} ")



