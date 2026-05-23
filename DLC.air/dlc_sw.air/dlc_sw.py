# -*- encoding=utf8 -*-
__author__ = "ASUS"

from airtest.core.api import *

auto_setup(__file__)

def dlc_sw():
    touch(Template(r"tpl1775638583740.png", record_pos=(-0.416, -0.169), resolution=(2400, 1080)))
    sleep(5.0)
    link = "https://qr.kinder.com/VUE04"

    shell(f'am start -a android.intent.action.VIEW -d "{link}"')
    sleep(10)
    touch(Template(r"tpl1775618322860.png", record_pos=(0.015, 0.026), resolution=(2400, 1080)))
    sleep(15.0)
    touch(Template(r"tpl1775618375370.png", record_pos=(0.015, 0.168), resolution=(2400, 1080)))
    sleep(1.0)

dlc_sw()

touch(Template(r"tpl1775640011605.png", record_pos=(-0.414, -0.083), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1774942354699.png", record_pos=(0.309, -0.178), resolution=(2400, 1080)))
sleep(2.0)
touch(Template(r"tpl1774942398451.png", record_pos=(0.275, -0.048), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1774942417325.png", record_pos=(0.278, 0.172), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1774942417325.png", record_pos=(0.278, 0.172), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1774942417325.png", record_pos=(0.278, 0.172), resolution=(2400, 1080)))
sleep(3.0)
touch(Template(r"tpl1774942504082.png", record_pos=(-0.412, 0.194), resolution=(2400, 1080)))
sleep(1.0)
swipe((1200, 850), (1200, 250), duration=0.8)
sleep(0.5)
swipe((1200, 850), (1200, 250), duration=0.8)
sleep(1.0)
touch(Template(r"tpl1774942628631.png", record_pos=(-0.082, 0.022), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1774942681303.png", record_pos=(-0.412, -0.189), resolution=(2400, 1080)))
sleep(3.0)
touch(Template(r"tpl1774942719866.png", record_pos=(-0.417, -0.169), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1774942751039.png", record_pos=(-0.07, -0.054), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1774942787076.png", record_pos=(-0.25, 0.202), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1774942828221.png", record_pos=(0.088, 0.151), resolution=(2400, 1080)))
sleep(5.0)
wait(Template(r"tpl1774942878956.png", record_pos=(0.451, 0.17), resolution=(2400, 1080)))
touch(Template(r"tpl1774942894676.png", record_pos=(-0.415, -0.185), resolution=(2400, 1080)))
sleep(5.0)

