import psutil
def CLEAR_PROCESS(PROCNAME):
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            proc.kill()
    print("Cleaned:", PROCNAME)
def CLEAR_AHK():
    CLEAR_PROCESS("AutoHotkey.exe")
    
def CLEAR_CONQUER():
    CLEAR_PROCESS("Conquer.exe")
        


