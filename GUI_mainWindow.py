import sys
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QPushButton, QVBoxLayout
from PySide6 import QtGui
from GUI_Tab_onePoint import Tab_onePoint
from GUI_Tab_wholeMesh import Tab_wholeMesh
from GUI_Tab_autoRegen import Tab_autoRegen
from GUI_Tab_plotError import Tab_plotError
from GUI_Tab_plotError_fineMesh import Tab_plotError_fineMesh


class mainFrameGUI(QWidget):
    """this class
    """
    def __init__(self):
        super().__init__()
        self.setGeometry(15, 30, 700, 500)
        self.setWindowTitle("Transfer Operator HighPerformance SRP")

        # Create the tab widget
        tab_widget = QTabWidget()
        
        
        
        tab_bar = tab_widget.tabBar()
        # Create the first tab
        first_tab = QWidget()


        first_layout = QVBoxLayout(first_tab)
        Tab_onePoint(first_layout)
        tab_widget.addTab(first_tab, 'Transfer one point')
        
    
        
        # Create the second tab
        second_tab = QWidget()
        second_layout = QVBoxLayout(second_tab)
        ## obj top to bottom in second tab
        second_layout.addStretch(0.5)

        
    
        Tab_wholeMesh(second_layout)    
        tab_widget.addTab(second_tab,'Transfer whole mesh')
    
        
        # Create the third tab
        third_tab = QWidget()
        third_layout = QVBoxLayout(third_tab)
        Tab_autoRegen(third_layout)
        tab_widget.addTab(third_tab,'AUTO regenration of mesh')
    
        # Create the fourth tab
        fourth_tab = QWidget()
        fourth_layout = QVBoxLayout(fourth_tab)
        Tab_plotError(fourth_layout)
        tab_widget.addTab(fourth_tab,'calculate and plot ERROR countour ZZ')
        
        # Create the fifth tab
        fifth_tab = QWidget()
        fifth_layout = QVBoxLayout(fifth_tab)
        Tab_plotError_fineMesh(fifth_layout)
        tab_widget.addTab(fifth_tab,'calculate and plot ERROR countour from fine mesh')
        
        # Create te button to close the main frame
        close_button = QPushButton('Close')
        close_button.clicked.connect(self.close_main_frame)
        close_button.setFixedWidth(100)

        close_button.setFixedHeight(50)
    
            

        # Layout the widgets
        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        layout.addWidget(close_button)
        self.setLayout(layout)
    
    def close_main_frame(self):
        self.close()



        
        
        