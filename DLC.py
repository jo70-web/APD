# -*- encoding=utf8 -*-
__author__ = "ASUS"

from airtest.core.api import *

auto_setup(__file__)

using("dlc_dino.air") 
using("dlc_we.air")
using("dlc_sw.air")
using("dlc_ls.air")
using("dlc_kin.air")
using("dlc_nat.air")
using("dlc_ink.air")
import dlc_dino
import dlc_we
import dlc_sw
import dlc_ls
import dlc_nat
import dlc_ink

dlc_dino()
dlc_we()
dlc_sw()
dlc_ls()
dlc_kin()
dlc_nat()
dlc_ink()