# -*- encoding=utf8 -*-
__author__ = "ASUS"

from airtest.core.api import *

auto_setup(__file__)

def reset_to_scanner():
    stop_app("com.ferrero.applayduGP")
    stop_app("com.gamma.scan")
    start_app("com.ferrero.applayduGP")
    sleep(10.0)
    start_app("com.gamma.scan")
    sleep(5.0)
    touch(Template(r"tpl1769398280756.png", record_pos=(-0.166, -0.959), resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1769398327766.png", record_pos=(-0.38, 0.369), resolution=(1080, 2400)))
    sleep(1.0)

def main():
    # ===== START =====
    reset_to_scanner()

    positions = [
        (0.139, 0.186), (0.374, 0.188), (0.617, 0.186), (0.86, 0.187), (0.137, 0.296),
        (0.385, 0.294), (0.617, 0.291), (0.869, 0.293), (0.137, 0.399), (0.377, 0.402),
]


    for idx, pos in enumerate(positions, start=1):
        
        if idx == 11:
            print("Scan 10, stop script")
            log("Scan 10x, stop script")
            break
            
        touch(pos)
        sleep(2)

        touch(Template(r"tpl1769399197552.png", record_pos=(-0.381, -0.66), resolution=(1080, 2400)))
        sleep(15.0)
        if exists (Template(r"tpl1769409480449.png", record_pos=(0.407, 0.166), resolution=(2400, 1080))):
            touch(Template(r"tpl1769409505733.png", record_pos=(0.455, -0.18), resolution=(2400, 1080)))
            sleep(10.0)

        
        if exists(Template(r"tpl1769419248273.png", record_pos=(-0.418, -0.175), resolution=(2400, 1080))):
            reset_to_scanner()
        else:
            sleep(1.0)
            touch(Template(r"tpl1769409669024.png", record_pos=(0.044, 0.047), resolution=(2400, 1080)))
            sleep(15.0)
            wait(Template(r"tpl1769399703092.png", record_pos=(0.017, 0.174), resolution=(2400, 1080)))
            touch(Template(r"tpl1769399738877.png", record_pos=(0.017, 0.172), resolution=(2400, 1080)))
            sleep(1.0)
            touch(Template(r"tpl1772010732207.png", record_pos=(-0.42, -0.175), resolution=(2400, 1080)))
            sleep(2.0)
            # Bagian snapshot dinamis
            save_path = f"D:/Screenshot/toy{idx:02d}.jpg"
            snapshot(filename=save_path, msg=f"Screenshot urutan ke-{idx}")
        reset_to_scanner()

# Panggil fungsi utama
main()