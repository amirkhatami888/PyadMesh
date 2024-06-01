# author: amirhossein khatami
# mail: amirkhatami@gmail.com
#importing libraries
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QPushButton, QVBoxLayout
from PySide6 import QtGui
from gui.GUI_Tab_onePoint import Tab_onePoint
from gui.GUI_Tab_wholeMesh import Tab_wholeMesh
from gui.GUI_Tab_autoRegen import Tab_autoRegen
from gui.GUI_Tab_plotError import Tab_plotError

class mainFrameGUI(QWidget):
    """this class is the main frame of the GUI
    """
    def __init__(self):
        super().__init__()
        self.setGeometry(15, 30, 700, 500)
        self.setWindowTitle("Transfer Operator HighPerformance SRP")
        self.setStyleSheet("QWidget {background-color:  rgb(32, 32, 32);}"
                            "QTabWidget {background-color:  rgb(32, 32, 32);}"
                            "QTabBar::tab {background-color: rgb(64, 64, 64); color: rgb(255, 255, 255);}"
                            "QTabBar::tab:selected {background-color: rgb(64, 64, 64); color: rgb(255, 255, 255);}"
                            "QTabBar::tab:!selected {background-color: rgb(128, 128, 128); color: rgb(255, 255, 255);}"
                            "QTabBar::tab:hover {background-color: rgb(64, 64, 64); color: rgb(255, 255, 255);}")

        # Create the tab widget
        tab_widget = QTabWidget()
        tab_widget.setStyleSheet("background-color:  rgb(32, 32, 32);")
        
        
        
        tab_bar = tab_widget.tabBar()
        tab_bar.setStyleSheet("background-color: rgb(64, 64, 64); color: rgb(255, 255, 255);")
        # Create the first tab
        first_tab = QWidget()
        first_tab.setStyleSheet("background-color:  rgb(32, 32, 32);")


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
        tab_widget.addTab(fourth_tab,'plot ERROR countour')
        
        # Create te button to close the main frame
        close_button = QPushButton('Close')
        close_button.clicked.connect(self.close_main_frame)
        close_button.setFixedWidth(100)
        close_button.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        close_button.setStyleSheet("""
                                              QPushButton {background-color:  rgb(64, 64, 64);color: rgb(255, 255, 255);border: none;}
                                              QPushButton:hover {background-color:  rgb(128, 128, 128);color: rgb(255, 255, 255);}
                                                  
                                                  """)
        close_button.setFixedHeight(50)
    
            

        # Layout the widgets
        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        layout.addWidget(close_button)
        self.setLayout(layout)
    
    def close_main_frame(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainFrameGUI()
    ex.show()
    sys.exit(app.exec())
        

        
        
        