import os
import random
import string
import time
from src.controllers.windowController import WindowController
from src.controllers.game_window_name import GAME_WINDOW_NAME
from ahk import AHK 
# from windowController import WindowController

class GameController:
    def __init__(self):
        # self.self.ahk = AHK(executable_path=os.getcwd()+"/resources/files/AutoHotkey.exe".replace("/", "\\"),version="v1")
        self.ahk=None
        self.windowController = WindowController()
    def start_AHK(self):
        if not self.ahk:  # Nếu AHK chưa được khởi tạo
            self.ahk = AHK(executable_path="./resources/files/AutoHotkey.exe", version="v1")
    def close_AHK(self):
        if self.ahk:  # Nếu AHK đã được khởi tạo
            # subprocess.call("taskkill /f /im AutoHotkey.exe",shell=True)
            self.ahk = None  # Đặt AHK thành None
    def start_game(self):
        
        folder_path = os.getcwd()
        for filename in os.listdir(folder_path):
            if "Conquer - Shortcut" in filename:
                folder_path = os.getcwd()
                # os.startfile(os.path.join(folder_path, filename))
                file_path=os.path.join(folder_path, filename)
                break
        try:
            # subprocess.run(["runas", "/user:Administrator", file_path])
            os.startfile(file_path)
        except Exception as e:
            print("Error:", e)
    def click_image(self, image_path):
        self.start_AHK()
        btn = self.ahk.image_search(image_path,color_variation=30)
        while btn is None:
            # self.control_thread()
            print("Don't exits")
            btn = self.ahk.image_search(image_path,color_variation=30)
        x,y=btn
        self.human_click(x + 10, y + 10)
        print("Clicked", image_path)
    def replay_unpressed_key(self, key, func):
        self.start_AHK()
        method = getattr(self.ahk, func)
        
        method(key)
        # state = self.ahk.function_call(func,[key])
        state=self.ahk.key_state(key)
        while state is None:
            state=self.ahk.key_state(key)
    def enter_text(self, text):
        self.start_AHK()
        for char in text:
            time.sleep(0.2)
            if ord(char)==32:
               
                # self.replay_unpressed_key("Space","key_down")
                self.ahk.key_down("Space")
                downState = self.ahk.key_state("Space")
                while downState is None:
                    self.ahk.key_down("Space")
                    downState = self.ahk.key_state("Space")
                continue
            elif (ord(char)>=33 and ord(char)<= 43) or (ord(char)>=58 and ord(char)<= 90) or (ord(char)>=94 and ord(char)<= 95) or (ord(char)>=123 and ord(char)<= 126): # @,#,? ABC,....
                self.ahk.key_down("Shift")
                downState = self.ahk.key_state("Shift")
                while downState is None:
                    self.ahk.key_down("Shift")
                    downState = self.ahk.key_state("Shift")
                time.sleep(0.1)
            elif (ord(char)>=44 and ord(char)<=57) or (ord(char)>=91 and ord(char)<=93) or (ord(char)>=96 and ord(char)<=122)  : #1,2,3,a,b,c,/,=,...
                pass
            # self.replay_unpressed_key(char,"key_down")
            self.ahk.key_down(char)
            downState = self.ahk.key_state(char)
            while downState is None:
                self.ahk.key_down(char)
                downState = self.ahk.key_state(char)
            time.sleep(0.1)
            # self.replay_unpressed_key(char,"key_up")
            self.ahk.key_up(char)
            upState = self.ahk.key_state(char)
            while upState is None:
                self.ahk.key_up(char)
                upState = self.ahk.key_state(char)
            time.sleep(0.1)
            self.ahk.key_up("Shift")
            upState = self.ahk.key_state("Shift")
            while upState is None:
                self.ahk.key_up("Shift")
                upState = self.ahk.key_state("Shift")
            # self.replay_unpressed_key("Shift","key_up")
    def human_click(self, x,y):
        self.start_AHK()
        # self.control_thread()
        self.ahk.mouse_move(x,y,relative=False,speed=4)
        self.ahk.click()
        # self.ahk.click(x, y,coord_mode='Relative',click_count=1)
    def focusWindow(self):
        self.start_AHK()
        if GAME_WINDOW_NAME not in str(self.windowController.get_title_current_window()):
            self.windowController.focus_conquer_window()
            print("change window current")
        if self.ahk.get_mouse_position()!=(0,0):
            print("change mouse position")
            self.ahk.mouse_move(0, 0,speed=4)
    def waitingScreen(self, image_path):
        self.start_AHK()
        print("waiting",image_path)
        self.focusWindow()
        btn = self.ahk.image_search(image_path,color_variation=30) 
        while btn == None:
            self.focusWindow()
            btn = self.ahk.image_search(image_path,color_variation=30) 
        print("loaded",image_path)
        time.sleep(1)

    def waitingSuccessLogin(self, image_path, username, password):
        self.start_AHK()
        print("waiting",image_path)
        self.focusWindow()
        btn = self.ahk.image_search(image_path,color_variation=30) 
        while btn == None:
            self.focusWindow()
            btn = self.ahk.image_search(image_path,color_variation=30) 
            errorLogin=self.ahk.image_search("./resources/images/confirmButton.png",color_variation=30) 
            if errorLogin != None:
                self.click_image("./resources/images/confirmButton.png")
                self.loginAgain(username, password)
                return
            registerScreen=self.ahk.image_search("./resources/images/returnButton.png",color_variation=30) 
            if registerScreen != None:
                self.characterSelect()
                self.register()
            
        print("loaded",image_path)
        time.sleep(1)
    def loginAgain(self, username, password):
        self.click_image("./resources/images/usernameField.png")
        self.enter_text("\b"*len(username))
        self.login(username, password)
    
    def login(self, username, password):
        self.click_image("./resources/images/usernameField.png")
        self.enter_text(username)
        self.human_click(378, 717)
        self.enter_text(password)
        self.human_click(795, 716)
        self.waitingSuccessLogin("./resources/images/taskbarMenu.png", username, password)
        self.initAction()



    def registerAgain(self, username):
        self.click_image("./resources/images/blueConfirmButton.png")
        self.click_image("./resources/images/yellowCancelButton.png")
        nameEditText=self.human_click(680, 720)
        self.click_image("./resources/images/usernameField.png")
        self.enter_text("\b"*len(username))
        self.register()
    def waitingSuccessRegister(self, image_path, ):
        self.start_AHK()
        print("waiting",image_path)
        self.focusWindow()
        btn = self.ahk.image_search(image_path,color_variation=30) 
        while btn == None:
            self.focusWindow()
            btn = self.ahk.image_search(image_path,color_variation=30) 
            charNameExisted=self.ahk.image_search("./resources/images/nameExisted.png",color_variation=30) 
            if charNameExisted != None:
                self.registerAgain()
                return
    def characterSelect(self, char="1"):
        self.start_AHK()
        via_page=self.human_click(980, 333)
        if char=="1":
            self.human_click(250, 285)
        else:
            self.human_click(770, 285)  
    def register(self, char="1"):
        self.start_AHK()
        nameEditText=self.human_click(680, 720)
        random_string = self.generate_random_string().lower()
        self.enter_text(random_string)
        confirmButton=self.human_click(860, 720)
        self.waitingScreen("./resources/images/yellowConfirmButton.png")
        confirmButton=self.human_click(436, 438)
        self.waitingSuccessRegister("./resources/images/successRegister.png")
        confirmButton=self.human_click(440, 420)
    def generate_random_string(self, length=11):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))
        # random_string = generate_random_string()
        # print("Chuỗi ngẫu nhiên:", random_string.lower())

    def initAction(self):
        self.start_AHK()
        time.sleep(3)
        tabPress=self.ahk.key_press("Esc")
        self.ahk.key_up("Esc")
        upState = self.ahk.key_state("Esc")
        while upState is None:
            self.ahk.key_up("Esc")
            upState = self.ahk.key_state("Esc")

        # hideButton=self.human_click(779, 677)  
        hideButton=self.human_click(595, 539)
        tabPress=self.ahk.key_press("Tab")
        

    def serverSelect(self, group, server):
        self.start_AHK()
        self.waitingScreen("./resources/images/loginButton.png")
        group=int(group)
        server=int(server)
        print("Group:", group, "Server:", server)
        if group <=17:
            # self.human_click(170, 550)
            print("Back page")
            # self.click_image("./resources/images/backServer.png")
            self.human_click(165, 552)
        elif group  <= 35:
            print("Next page")
            self.human_click(265, 552)
            # self.click_image("./resources/images/nextServer.png")
        xG=0; yG=0
        group=group - int(group/18)*18 #Quy về 1 bảng 18 ô( 0-17), gồm 2 cột để tính x
        if group<=8: xG = 100 #server<=9 la cot trai
        elif group<=17: xG = 300#server<=17 la cot phai
        group=group - int(group/9)*9 #Quy đổi về 9 hàng(0-8), 1 hàng 2 ô để tính y 
        print("group",group)
        yG= 180+group*40
        self.human_click(xG, yG)
        print(xG, yG)
        print("Click group", xG, yG )
        yS = 180 + int(server/3)*100 #Quy đổi về  4 dòng(0-3) từ trên xuống, 1 dòng 3 ô để tính y
        server=server - int(server/3)*3
        xS = 500 + server*200  #Quy đổi về 3 cột từ trái sang phải, 1 cột 4 ô để tính x
        self.human_click(xS, yS)
        print("Click server", xS, yS)
    def is_pressed(self, key="F11"):
        self.start_AHK()
        self.ahk.key_wait(key)
        return True
    def closeAll(self):
        self.start_AHK()
        try:
            self.ahk=self.ahk
            for window in self.ahk.list_windows():
                if GAME_WINDOW_NAME in window.title and  "Conquer Auto App" not in window.title:
                    window.close()
        except Exception as e: 
            print(e)
        print("closed all")
# game=GameController()
# # game.start_game()
# game.login("kimbao1", "kimbao123")
# game.serverSellect("6","3")

