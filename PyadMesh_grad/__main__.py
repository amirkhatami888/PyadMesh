import sys
from PySide6.QtWidgets import QApplication
from GUI_mainWindow  import mainFrameGUI
import sys

def main():
    """
    Main function to initialize and run the GUI application.

    This function sets up the QApplication, creates an instance of the main window (mainFrameGUI), 
    displays it, and starts the application's event loop.
    """
    app = QApplication(sys.argv)
    main_window = mainFrameGUI()
    main_window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    """
    Entry point of the script.

    This block ensures that the main function is called when the script is executed directly.
    """

    main()