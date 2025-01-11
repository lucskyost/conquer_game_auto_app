import sys
from PySide6.QtWidgets import QApplication
from src.controllers.main_window_handle import MainWindowHandle
import pyuac
import sys
def main():
    app = QApplication(sys.argv)
    window = MainWindowHandle()
    window.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:   
        print("As Admin")     
        main()  # Already an admin here.