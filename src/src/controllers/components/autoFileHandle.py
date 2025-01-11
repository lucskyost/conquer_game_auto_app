# class AutoFileHandle:
#     def __init__(self, mainWindowHandle) -> None:
#         pass
from ahk import AHK
import time
import pyautogui
time.sleep(2)
# ahk=AHK()
# ahk.key
# # from pywinauto import application
# # from pywinauto.keyboard import send_keys
# from pywinauto.keyboard import send_keys, KeySequenceError
# time.sleep(2)
# send_keys('k', with_spaces=True)
# send_keys('@', with_spaces=True)
# send_keys('-', with_spaces=True)
self = type('Dummy', (), {})
self.ahk=AHK()
def enter_text( text):
    time.sleep(0.5)
    for char in text:
        time.sleep(0.1)
        if ord(char)==32:
            self.ahk.key_down("Space")
            continue
        elif (ord(char)>=33 and ord(char)<= 43) or (ord(char)>=58 and ord(char)<= 90) or (ord(char)>=94 and ord(char)<= 95) or (ord(char)>=123 and ord(char)<= 126): # @,#,? ABC,....
            self.ahk.key_down("Shift")
        elif (ord(char)>=44 and ord(char)<=57) or (ord(char)>=91 and ord(char)<=93) or (ord(char)>=96 and ord(char)<=122)  : #1,2,3,a,b,c,/,=,...
            pass
        self.ahk.key_down(char)
        downState = self.ahk.key_state(char)
        while downState is None:
            self.ahk.key_down(char)
            downState = self.ahk.key_state(char)
        time.sleep(0.02)
        self.ahk.key_up(char)
        upState = self.ahk.key_state(char)
        while upState is None:
            self.ahk.key_down(char)
            upState = self.ahk.key_state(char)
        self.ahk.key_up("Shift")
# enter_text("""  " #/  9?@SKY _^sky{|~'/""")
   #/  9?@SKY _^sky{|~}
# Tạo một đối tượng ứng dụng
# app = application.Application()
#  " #/  9?@SKY _^sky{|~"/"[]"
# # Kết nối với ứng dụng có tiêu đề chứa chuỗi "Notepad"  " #/  9?@SKY _^sky{|~"/"}"
# app.connect(ti)

# # Truy cập vào cửa sổ đầu tiên tìm thấy
# window = app.window()

# # Tương tác với các thành phần của cửa sổ
# edit = window.Edit
# edit.type_keys("Hello, world!")

# from ahk import AHK
# import time
# time.sleep(2)
# ahk=AHK()
# for char in text:
#     self.ahk.key_press(char)
#     time.sleep(0.05)
