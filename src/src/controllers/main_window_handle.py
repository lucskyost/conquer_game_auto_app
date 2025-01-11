import atexit
import os
import threading
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QTableWidgetItem,QHBoxLayout, QTableWidget, QWidget, QHeaderView, QCheckBox, QMenu, QFileDialog, QMessageBox
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap, QMovie
from openpyxl import load_workbook
from src.controllers.components.table_widget_handle import TableWidgetHandle
from src.controllers.login_thread import CheckF11, LoginThread
from src.controllers.windowController import WindowController
from ui.main_window_ui import Ui_MainWindow
from src.models.account import Account
from src.controllers.gameController import GameController
from PySide6.QtCore import QThread, Signal
from src.controllers.update import UpdateChecker, on_exit
from src.controllers.clear_process import CLEAR_CONQUER


class MainWindowHandle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.update_ui()
        self.update_checker = UpdateChecker()
        # self.windowController=WindowController()
        self.setWindowTitle("Conquer Auto App " + self.update_checker.app_version)
        self.setWindowIcon(QIcon("./resources/icons/rocket_icon.png"))
        self.accounts = []
        self.gameWindows = []
        self.data_path=""
        # self.data_path = os.path.join(os.getcwd(), 'resources', 'data', 'data.xlsx')
        self.getDataPath()
        # self.load_data_from_excel(self.data_path)
        # self.ui.tableWidget.clicked.connect(self.on_tableWidget_clicked)
        self.tableWidgetHandle=TableWidgetHandle(self)
        # self.ui.sellectAllCheckBox.stateChanged.connect(self.select_all_checkbox_handle)
        self.ui.importButton.clicked.connect(self.importFileDialog)
        self.ui.reloadButton.clicked.connect(self.on_reload_button_clicked)
        self.ui.sortButton.setMenu(self.setup_sort_button_menu())
        # self.ui.chosseFileButton1.clicked.connect(self.openFileDialog(self.ui.autoFileLabel1) )
        # self.ui.chosseFileButton2.clicked.connect(self.openFileDialog(self.ui.autoFileLabel2) )
        self.ui.runButton.clicked.connect(self.executeTasks)
        # self.ui.runButton.clicked.connect(self.startAnimation)
        self.ui.closeAllButon.clicked.connect(self.closeAllTask)
        self.ui.updateButton.clicked.connect(self.setup_update_button)

        # Loading the GIF 
        self.movie = QMovie("./resources/images/loading.gif") 
        self.movie.setScaledSize(self.ui.waitingSpinnerLabel.size())
        self.ui.waitingSpinnerLabel.setMovie(self.movie)

        
        
    def update_ui(self):
        self.shadow_effect = QGraphicsDropShadowEffect()
        self.shadow_effect.setBlurRadius(30)
        self.shadow_effect.setColor(Qt.black)
        self.shadow_effect.setOffset(10, 12)
        self.ui.graphicsView.setGraphicsEffect(self.shadow_effect)
    def setup_update_button(self):
        self.update_checker.check_for_updates()
        if self.update_checker.updated==True:
            print("Close App")
            atexit.register(on_exit)
            QApplication.quit()
            print("Close App")

    def setup_sort_button_menu(self):
        menu = QMenu(self.ui.sortButton)
        menu.addAction("Password", self.on_option1_clicked)
        menu.addAction("Level", self.on_option2_clicked)
        menu.addAction("Gold", self.on_option2_clicked)
        menu.addAction("Status", self.on_option2_clicked)
        return menu
        

    def on_option1_clicked(self):
        print("Option 1 clicked")

    def on_option2_clicked(self):
        print("Option 2 clicked")

    def on_reload_button_clicked(self):
        self.tableWidgetHandle.load_data_to_tableWidget(self.data_path)
    def getDataPath(self):
        try:
            file = open("./resources/data/dataPath.txt", "r+") 
            self.data_path=file.read()
            file.close()
        except:
            file = open("./resources/data/dataPath.txt", "w") 
            file.write("./resources/data/data.xlsx")
            file = open("./resources/data/dataPath.txt", "r+") 
            self.data_path=file.read()
            file.close()
        self.ui.importFileLabel.setText("Import File: " + self.data_path)
        self.ui.importFileLabel.setMinimumWidth(self.ui.importFileLabel.sizeHint().width())
        
    def saveDataPath(self):
        file = open("./resources/data/dataPath.txt", "w") 
        file.write(self.data_path)
        file.close()

    def importFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Chọn file", "", "Excel Files (*.xlsx)", options=options)
        if fileName:
            self.ui.importFileLabel.setText("Import File: " + fileName)
            self.ui.importFileLabel.setMinimumWidth(self.ui.importFileLabel.sizeHint().width())
            self.data_path=fileName
            self.saveDataPath()
            self.tableWidgetHandle.load_data_to_tableWidget(self.data_path)
            
    def openFileDialog(self, autoFileLabel):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Chọn file", "", "TMaKs Files (*.TMaKs)", options=options)
        if fileName:
            self.run_auto_file=fileName
            autoFileLabel.setText("File sellected: " + fileName)


   
    def getPath(self,fileName):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), fileName)
    
  
    # Start Animation 
    def startAnimation(self):
        self.ui.waitingSpinnerLabel.show() 
        self.movie.start() 
    
    # Stop Animation(According to need) 
    def stopAnimation(self): 
        self.movie.stop()
        self.ui.waitingSpinnerLabel.hide()

    def getLoginAccounts(self):
        # self.startAnimation()
        loginAccounts=[]
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.cellWidget(row, 0)
            checkbox = item.findChild(QCheckBox)
            if checkbox.isChecked()==True:
                index=row
                username=self.ui.tableWidget.item(row, 1).text()
                password=self.ui.tableWidget.item(row, 2).text()
                group=self.ui.tableWidget.item(row, 3).text()
                server=self.ui.tableWidget.item(row, 4).text()
                loginAccounts.append((index,username,password,group,server))
        self.loginAccounts=loginAccounts
    def runAutoFileTask(self, filename):
        try:
            os.startfile(filename)
        except Exception as e:
            QMessageBox.critical(self,"Lỗi khi chạy file:", e)

    def buyItemTask(self):
        pass
    def closeAllTask(self):
        CLEAR_CONQUER()
        self.clear_threads()
        self.stopAnimation()
    def clear_threads(self):
        if hasattr(self, "login_thread"):
            if self.login_thread!=None:
                self.login_thread.terminate()
                self.login_thread=None
                print("Terminated  thread from main")
        if hasattr(self, "check_F11"):
            if self.check_F11!=None:
                self.check_F11.terminate()
                self.check_F11=None
                print("Terminated F11 thread from main")
    def executeTasks(self):
        self.closeAllTask()
        if self.ui.loginCheckBox.isChecked():
            self.getLoginAccounts()
            if len(self.loginAccounts)>0:
                self.login_thread = LoginThread(self)
                self.login_thread.started.connect(self.startAnimation)
                self.login_thread.finished.connect(self.stopAnimation)
                self.login_thread.start()
                self.check_F11=CheckF11(self)
                self.check_F11.start()
                

        if self.ui.runAutoFileCheckBox1.isChecked():
            print(f"Running auto file for user")
            # Thực hiện hành động chạy tệp tự động ở đây
            self.runAutoFileTask(self.ui.autoFileLabel1.text())

        if self.ui.buyItemCheckBox.isChecked():
            print(f"Buying item for user")
            # Thực hiện hành động mua hàng cho người dùng ở đây
            self.buyItemTask()
        if self.ui.runAutoFileCheckBox2.isChecked():
            print(f"Running auto file for user")
            # Thực hiện hành động chạy tệp tự động ở đây
            self.runAutoFileTask(self.ui.autoFileLabel2.text())
        

