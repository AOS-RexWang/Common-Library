"""
 * @File       : DMM_Model.py
 * @Version    : V1.0.3
 * @Date       : Aug 26, 2022
 * @Brief      : Child class of DMM.
 * @Author     : Rex Wang
 * @Last editor: Rex Wang
 * Copyright (C) 2022 Alpha & Omega Semiconductor Ltd. All rights reserved.
"""

from Library.INSTR import DMM

class Keysight_34461(DMM):
    Model_Name                     = "Keysight_34461"
    CMD_Config_IMode               = "CONF:CURR:%s %.4f, %.3f"
    CMD_Config_IMode_Auto_Range    = "CONF:CURR:%s AUTO"    
    CMD_Config_VMode               = "CONF:VOLT:%s %s, %.3f"
    CMD_Config_VMode_Auto_Range    = "CONF:VOLT:%s AUTO"
    CMD_Measure_VNPLC              = "SENS:VOLT:DC:NPLC %d"
    CMD_Measure_INPLC              = "SENS:CURR:DC:NPLC %d"
    CMD_Measure_Voltage            = "MEAS:VOLT:%s?"
    CMD_Measure_Current            = "MEAS:CURR:%s?"
    CMD_Set_Current_Terminals      = "SENSe:CURRent:%s:TERMinals %d"
