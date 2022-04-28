"""
 * @File       : DMM_Model.py
 * @Version    : V1.0.0
 * @Date       : April 27, 2022
 * @Brief      : Child class of DMM.
 * @Author     : Rex Wang
 * @Last editor: Rex Wang
 * Copyright (C) 2022 Alpha & Omega Semiconductor Ltd. All rights reserved.
"""

from Library.INSTR import DMM_2

class Keysight_34461(DMM_2):
    CMD_Config_VMode    = "CONF:VOLT:%s %s, %.3f"
    CMD_Config_IMode    = "CONF:CURR:%s %.4f, %.3f"
    CMD_Measure_Voltage = "MEAS:VOLT:%s?"
    CMD_Measure_Current = "MEAS:CURR:%s?"
    #CMD_MEAS_TEMP = "MEAS:TEMP:%s? %s, MAX,(@%d)"
