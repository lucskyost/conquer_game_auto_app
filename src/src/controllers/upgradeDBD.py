import os
import random
import time
from ahk import AHK

ahk = AHK()

def upgrade(position):
    while True:
        # ahk.click(( 0,0),coord_mode='Screen',click_count=3)
        # ahk.click((184, 158),coord_mode='Relative',click_count=3) #Nhan vao cua so de lay toa do tuong doi cua cua so do
        ahk.click(position,coord_mode='Relative',click_count=3) #Nhan vao cua so de lay toa do tuong doi cua cua so do
        if (ahk.key_state("F2")==True):
            time.sleep(0.5)
            print("Pause upgrading")
            check=ahk.key_state("F2")
            while check==False:
                check=ahk.key_state("F2")
            print("Continue upgrading")
            ahk.key_up("F2")
        if (ahk.key_state("F3")==True):
            print("Exit upgrade")
            break
def get_position():
    while True:
        coordinates= ahk.get_mouse_position(coord_mode="Relative") 
        # coordinates= ahk.get_mouse_position() 
        if ahk.key_state("enter"):
            print("Coordinates:",coordinates)
            print("""    
            #F1: Start upgrading...
            #F2: Pause / continute
            #F3: Stop upgrading""")
            time.sleep(0.5)
        if ahk.key_state("F1"):
            print("To be upgrading...")
            return coordinates
def get_title_current_window():
    
    for window in ahk.list_windows():  
        if window.is_active()==True:
            return window.title
def app():
    print("""The first, click to inside DBD window, 
then moving the mouse to the point need click, 
and then clicking enter to get position!""")
    position=get_position()
    upgrade(position)
app()
#F1: Start upgrading
#F2: Pause / continute
#F3: Stop upgrading
