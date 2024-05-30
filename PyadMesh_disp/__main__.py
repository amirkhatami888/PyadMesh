# author: amirhossein khatami
# mail: amirkhatami@gmail.com

# importing libraries
import sys
from PySide6.QtWidgets import QApplication
from GUI_mainWindow  import mainFrameGUI
import sys

def main():
    """ 
    The main function of the GUI application.
    
    This function initializes the Qt application, creates an instance of the main
    window, shows it, and starts the application's event loop.
    """
    # Initialize the Qt application
    app = QApplication(sys.argv)
    
    # Create an instance of the main window
    main_window = mainFrameGUI()
    
    # Show the main window
    main_window.show()
    
    # Start the event loop
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()