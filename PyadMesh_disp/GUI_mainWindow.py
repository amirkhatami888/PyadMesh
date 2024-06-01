# author: amirhossein khatami
# mail: amirkhatami@gmail.com

# importing libraries
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QPushButton, QVBoxLayout
from PySide6 import QtGui
from GUI_Tab_onePoint import Tab_onePoint
from GUI_Tab_wholeMesh import Tab_wholeMesh
from PySide6.QtGui import QIcon, QScreen
class mainFrameGUI(QWidget):
    """this class is the main frame of the GUI
    """
    def __init__(self):
        super().__init__()
        self.setGeometry(15, 30, 950, 950)
        self.setWindowTitle("PyadptiMesh-disp")
        self.setWindowIcon(QIcon('pyadaptimesh.svg'))
        # Create the tab widget
        tab_widget = QTabWidget()
        
        tab_bar = tab_widget.tabBar()
        # Create the first tab
        first_tab = QWidget()

        first_layout = QVBoxLayout(first_tab)
        Tab_onePoint(first_layout)
        tab_widget.addTab(first_tab, 'point claculator  ')
        
        # Create the second tab
        second_tab = QWidget()
        second_layout = QVBoxLayout(second_tab)
        ## obj top to bottom in second tab
        second_layout.addStretch(0.5)

        Tab_wholeMesh(second_layout)    
        tab_widget.addTab(second_tab,'mesh Transfer  ')
     
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
        """
        """
        self.close()
