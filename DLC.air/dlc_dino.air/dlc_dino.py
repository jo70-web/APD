# -*- encoding=utf8 -*-
__author__ = "ASUS"

from airtest.core.api import *

auto_setup(__file__)

import time

def dlc_dino():
    stop_app("com.ferrero.applayduGP")
    start_app("com.ferrero.applayduGP")
    sleep(5.0)
    wait(Template(r"tpl1773305966050.png", record_pos=(-0.415, -0.085), resolution=(2400, 1080)))
    touch(Template(r"tpl1773305978566.png", record_pos=(-0.41, -0.169), resolution=(2400, 1080)))
    sleep(1.0)
    touch(Template(r"tpl1773306046361.png", record_pos=(-0.069, 0.045), resolution=(2400, 1080)))
    sleep(1.0)
    touch(Template(r"tpl1773306107271.png", record_pos=(-0.25, 0.199), resolution=(2400, 1080)))
    sleep(3.0)
    touch(Template(r"tpl1773306141287.png", record_pos=(0.316, 0.101), resolution=(2400, 1080)))
    sleep(1.0)
    touch(Template(r"tpl1773306172308.png", record_pos=(-0.002, 0.184), resolution=(2400, 1080)))
    sleep(1.0)
    touch(Template(r"tpl1773306194070.png", record_pos=(-0.006, 0.154), resolution=(2400, 1080)))
    sleep(5.0)

dlc_dino()

def timeout_dlc():
    start_time = time.time()
    timeout = 180
    
    while exists(Template(r"tpl1775633265625.png")):
        if time.time() - start_time > timeout:
            snapshot(filename="dlc_failed_dino.png", msg="DLC timeout")
            print("FAILED: DLC tidak jalan (timeout)")
            touch(Template(r"tpl1776238463953.png", record_pos=(-0.416, -0.185), resolution=(2400, 1080)))
            sleep(1.0)
            touch(Template(r"tpl1776238440268.png", record_pos=(-0.098, 0.117), resolution=(2400, 1080)))
            sleep(1.0)
            touch(Template(r"tpl1776238535122.png", record_pos=(-0.417, -0.185), resolution=(2400, 1080)))
            sleep(1.0)
            touch(Template(r"tpl1776238620051.png", record_pos=(-0.416, -0.182), resolution=(2400, 1080)))
            sleep(1.0)
            touch(Template(r"tpl1776238652261.png", record_pos=(-0.416, -0.178), resolution=(2400, 1080)))
            break
            
timeout_dlc()
sleep(1)
  
    
wait(Template(r"tpl1773306367073.png", record_pos=(-0.416, -0.186), resolution=(2400, 1080)), timeout=120)
touch(Template(r"tpl1773306380474.png", record_pos=(-0.416, -0.186), resolution=(2400, 1080)))
sleep(2.0)
touch(Template(r"tpl1773306441459.png", record_pos=(-0.415, -0.179), resolution=(2400, 1080)))