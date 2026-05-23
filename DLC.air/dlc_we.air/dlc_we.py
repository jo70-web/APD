# -*- encoding=utf8 -*-
__author__ = "ASUS"

from airtest.core.api import *

auto_setup(__file__)

def dlc_we():
    sleep(5.0)
    wait(Template(r"tpl1773306717664.png", record_pos=(-0.414, 0.165), resolution=(2400, 1080)))
    touch(Template(r"tpl1773306724135.png", record_pos=(-0.413, 0.165), resolution=(2400, 1080)))
    sleep(1.0)
dlc_we()
   
def search_we():
    
    target_icon = Template(r"tpl1773307427070.png", record_pos=(0.0, 0.0), resolution=(1080, 1920))

    while True:
        sleep(1.0)
        pos = exists(target_icon)
        
        if pos:
            print("Word Explorer ditemukan! Melakukan Touch...")
            sleep(1.0)
            touch(pos)
            sleep(1.0)
            break # Keluar dari loop karena sudah berhasil pencet

        else:
            print("Belum ketemu, swipe ke kiri untuk mencari...")
            swipe((0.8, 0.39), (0.2, 0.39), duration=1.0)
            sleep(3)
search_we()           

print("Berhasil masuk, sekarang klik tombol selanjutnya...")
sleep(2.0) 
touch(Template(r"tpl1773392236672.png", record_pos=(0.089, 0.151), resolution=(2400, 1080)))
sleep(30.0)
wait(Template(r"tpl1773392431216.png", record_pos=(0.467, 0.182), resolution=(2400, 1080)))
touch(Template(r"tpl1773392440750.png", record_pos=(0.468, 0.18), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1773392480858.png", record_pos=(-0.426, -0.186), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1773392512166.png", record_pos=(-0.42, -0.186), resolution=(2400, 1080)))





