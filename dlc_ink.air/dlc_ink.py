# -*- encoding=utf8 -*-
__author__ = "ASUS"

from airtest.core.api import *

auto_setup(__file__)

def dlc_ink():
    sleep(5.0)
    touch(Template(r"tpl1775628327885.png", record_pos=(-0.412, 0.168), resolution=(2400, 1080)))

dlc_ink()

def search_ink():
    
    target_icon = Template(r"tpl1775628225113.png", record_pos=(0.0, 0.0), resolution=(1080, 1920))

    while True:
        sleep(1.0)
        pos = exists(target_icon)
        
        if pos:
            print("Inkmagination ditemukan! Melakukan Touch...")
            sleep(1.0)
            touch(pos)
            sleep(1.0)
            break # Keluar dari loop karena sudah berhasil pencet

        else:
            print("Belum ketemu, swipe ke kiri untuk mencari...")
            swipe((0.2, 0.39), (0.8, 0.39), duration=1.0)
            sleep(3)
search_ink() 

sleep(1.0)
touch(Template(r"tpl1775628647273.png", record_pos=(-0.221, -0.182), resolution=(2400, 1080)))
sleep(60.0)
wait(Template(r"tpl1775628961531.png", record_pos=(-0.308, -0.183), resolution=(2400, 1080)))
touch(Template(r"tpl1775628762351.png", record_pos=(-0.375, -0.001), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1775628813836.png", record_pos=(0.086, 0.15), resolution=(2400, 1080)))
sleep(30.0)
touch(Template(r"tpl1775628875909.png", record_pos=(-0.416, -0.185), resolution=(2400, 1080)))

