import sys
from PySide6.QtWidgets import QApplication
from GUI_mainWindow  import mainFrameGUI
import sys

def main():
    """ this function is the main function of the GUI
    """
    app = QApplication(sys.argv)
    main_window = mainFrameGUI()
    main_window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()