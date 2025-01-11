import time
from PySide6.QtCore import QThread, Signal
from src.controllers.clear_process import CLEAR_AHK
from src.controllers.gameController import GameController
from src.controllers.windowController import WindowController
import keyboard
class CheckF11(QThread):
    loop = Signal()
    def __init__(self, mainWindowHandle):
        super().__init__()
        self.pressed=False
        self.mainWindowHandle=mainWindowHandle
    def run(self):
        self.control_thread()
    def control_thread(self):
        while True:
            if keyboard.read_key() == "f11":
                if hasattr(self.mainWindowHandle, "login_thread"):
                    self.mainWindowHandle.login_thread.stop()
                    self.loop.emit()
                    return
            if self.mainWindowHandle.login_thread.isFinished()==True:
                self.loop.emit()
                return

    def stop(self):
        self.terminate()
"""        if GameController().is_pressed("F11"):
            if keyboard.read_key() == "f11":
                if hasattr(self.mainWindowHandle, "login_thread"):
                    self.mainWindowHandle.login_thread.stop()
                    self.loop.emit()
                    return"""



class LoginThread(QThread):
    loop = Signal()

    def __init__(self,mainWindowHandle):
        QThread.__init__(self)
        self.mainWindowHandle = mainWindowHandle

    def run(self):
        self.login_accounts()

    def login_accounts(self):
        print("Login Thread started")
        self.loginAccounts = self.mainWindowHandle.loginAccounts
        loops = len(self.loginAccounts)
        self.gameController = GameController()
        self.windowController = WindowController()
        for i in range(loops):
            self.gameController.start_game()
            self.gameController.loginThread = self
            index, username, password, group, server = self.loginAccounts[i]
            print("Account: ", self.loginAccounts[i])
            self.mainWindowHandle.tableWidgetHandle.clear_highlight()
            self.mainWindowHandle.tableWidgetHandle.hightLightRow(index, True)
            print("Start select server")
            self.gameController.serverSelect(group, server)
            print("Start login")
            self.gameController.login(username, password)
            self.windowController.set_new_title("Conquer auto " + str(i + 1))
            self.windowController.minimize_current_window()
            self.mainWindowHandle.tableWidgetHandle.hightLightRow(index, True)
        CLEAR_AHK()
        self.loop.emit()

    def stop(self):
        self.terminate()