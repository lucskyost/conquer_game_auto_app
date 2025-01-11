import os
import subprocess
from src.controllers.game_window_name import GAME_WINDOW_NAME
from ahk import AHK

class WindowController:
    def __init__(self):
        self.windownCount=0
        self.ahk=None
    def start_AHK(self):
        if not self.ahk:  # Nếu AHK chưa được khởi tạo
            self.ahk = AHK(executable_path="./resources/files/AutoHotkey.exe", version="v1")
    def close_AHK(self):
        if self.ahk:  # Nếu AHK đã được khởi tạo
            # subprocess.call("taskkill /f /im AutoHotkey.exe",shell=True)
            self.ahk = None  # Đặt AHK thành None
    def add_new_title(self):
        self.start_AHK()
        for window in self.ahk.list_windows():  
            if "Conquer Online" in window.title:
                self.windownCount+=1
                window.set_title("Conquer auto "+str(self.windownCount))
                break
    def set_new_title(self, newTitle):
        self.start_AHK()
        for window in self.ahk.list_windows():  
            if "Conquer Online" in window.title and window.active==True:
                self.windownCount+=1
                # window.set_title("Conquer auto "+str(self.windownCount))
                window.set_title(newTitle)
                break
    def get_title_current_window(self):
        self.start_AHK()
        for window in self.ahk.list_windows():  
            if window.is_active()==True:
                return window.title
    def print_title_all_windows(self):
        self.start_AHK()
        for window in self.ahk.list_windows():  
            print(window.title)
    def minimize_current_window(self):
        self.start_AHK()
        win = self.ahk.find_window(title=self.get_title_current_window())
        win.minimize()
    def minimize_window(self, title):
        self.start_AHK()
        win = self.ahk.find_window_by_title(str(title))
        win.minimize()
    def find_window(self, windowName):
        self.start_AHK()
        for window in self.ahk.list_windows():  
            if windowName in window.title:
                # print(window.title)
                return window
    def activate_window(self, windowName):
        self.start_AHK()
        for window in self.ahk.list_windows():  
            if windowName == window.title:
                window.activate()
    def focus_conquer_window(self, windowName=GAME_WINDOW_NAME):
        self.start_AHK()
        while True:
            for window in self.ahk.list_windows():  
                if windowName in window.title:
                    window.activate()
                    return

# time.sleep(3)
# windowController.minimize_current_window()
# print(windowController.get_current_window())
# Sử dụng lớp GameController
# controller = WindowController()
# controller.print_title_all_windows()

