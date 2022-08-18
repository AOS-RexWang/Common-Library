"""
 * @File       : DMM_Model.py
 * @Version    : V1.0.1
 * @Date       : Aug 16, 2022
 * @Brief      : Child class of DMM.
 * @Author     : Rex Wang
 * @Last editor: Ivan Chen
 * Copyright (C) 2022 Alpha & Omega Semiconductor Ltd. All rights reserved.
"""

from Library.INSTR import DMM

class Keysight_34461(DMM):
    CMD_Config_VMode    = "CONF:VOLT:%s %s, %.3f"
    CMD_Config_IMode    = "CONF:CURR:%s %.4f, %.3f"
    CMD_Measure_VNPLC    = "SENS:VOLT:DC:NPLC %d"
    CMD_Measure_INPLC    = "SENS:CURR:DC:NPLC %d"
    CMD_Measure_Voltage = "MEAS:VOLT:%s?"
    CMD_Measure_Current = "MEAS:CURR:%s?"
    #CMD_MEAS_TEMP = "MEAS:TEMP:%s? %s, MAX,(@%d)"
