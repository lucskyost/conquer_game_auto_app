import re
from src.controllers.windowController import WindowController
from ReadWriteMemory import ReadWriteMemory
from ctypes import *
from ctypes.wintypes import *

# import windowController
from ahk import AHK 
class ReadMemory():
    def __init__(self):
        # self.self.ahk = AHK(executable_path=os.getcwd()+"/resources/files/AutoHotkey.exe".replace("/", "\\"),version="v1")
        self.ahk=None
        self.windowController = WindowController()
    def start_AHK(self):
        if not self.ahk:  # Nếu AHK chưa được khởi tạo
            self.ahk = AHK(executable_path="./resources/files/AutoHotkey.exe", version="v1")
    def read(self):
        windowGame=WindowController.find_window(self,"CO")
        print(windowGame.title)
        pid=windowGame.pid

        print(pid)


        PROCESS_ID = pid # From TaskManager for Notepad.exe
        # PROCESS_HEADER_ADDR = 0x0170FADD   # From SysInternals VMMap utility
        PROCESS_HEADER_ADDR = 0x16F36E2E #So vang trong game
        # read from addresses
        STRLEN = 255

        PROCESS_VM_READ = 0x0010

        k32 = WinDLL('kernel32')
        k32.OpenProcess.argtypes = DWORD,BOOL,DWORD
        k32.OpenProcess.restype = HANDLE
        k32.ReadProcessMemory.argtypes = HANDLE,LPVOID,LPVOID,c_size_t,POINTER(c_size_t)
        k32.ReadProcessMemory.restype = BOOL

        process = k32.OpenProcess(PROCESS_VM_READ, 0, PROCESS_ID)
        buf = create_string_buffer(STRLEN)
        s = c_size_t()
        if k32.ReadProcessMemory(process, PROCESS_HEADER_ADDR, buf, STRLEN, byref(s)):
            print(s.value,buf.raw)
        data=buf.raw
        if len(data) % 2 != 0:
            data += b'\x00'

        # Giải mã chuỗi UTF-16 với lỗi 'ignore' để bỏ qua các byte không hợp lệ
        decoded_data = data.decode('utf-16-le', errors='ignore')
        print(decoded_data)
        match = re.search(r'(\d+)]', decoded_data)

        match = re.search(r'([\d,]+)]', decoded_data)

        if match:
            number_before_bracket = match.group(1)
            print("Con số trước ký tự ]:", number_before_bracket)
        else:
            print("Không tìm thấy con số trước ký tự ] trong chuỗi.")
readMemory=ReadMemory()
readMemory.start_AHK()
readMemory.read()



