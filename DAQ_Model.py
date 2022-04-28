"""
 * @File       : DAQ_Model.py
 * @Version    : V1.0.0
 * @Date       : April 27, 2022
 * @Brief      : Child class of DAQ.
 * @Author     : Rex Wang
 * @Last editor: Rex Wang
 * Copyright (C) 2022 Alpha & Omega Semiconductor Ltd. All rights reserved.
"""

from Library.INSTR import DAQ

class Keysight_DAQ970A(DAQ):
    Model_Name          = "Keysight_DAQ970A"
    CMD_Config_VMode    = "CONF:VOLT:%s %.1f, %.6f,(@%d)"
    # CMD_Config_IMode = "CONF:CURR:%s %.6f, %.6f,(@%d)"
    CMD_Config_TMode    = "CONF:TEMP:%s %s, %.6f,(@%d)"
    CMD_Measure_Voltage = "MEAS:VOLT:%s? %s, %.6f,(@%d)"
    # CMD_Measure_Current = "MEAS:CURR:%s? %.6f, %.6f,(@%d)"
    CMD_Measure_Temp    = "MEAS:TEMP:%s? %s, MAX,(@%d)"
    CMD_Route_Add    = ""
    CMD_Set_Sense_Range = ""

class Keithley_DAQ6510(DAQ):
    Model_Name          = "Keithley_DAQ6510"
    CMD_Config_VMode    = "SENS:FUNC 'VOLT:%s',(@%d)"
    # CMD_Config_IMode = "CONF:CURR:%s %.6f, %.6f,(@%d)"
    CMD_Config_TMode    = "CONF:TEMP:%s %s, %.6f,(@%d)"
    CMD_Measure_Voltage = "MEAS:VOLT:%s? %.1f, %.6f,(@%d)"
    # CMD_Measure_Current = "MEAS:CURR:%s? %.6f, %.6f,(@%d)"
    CMD_Measure_Temp    = "MEAS:TEMP:%s? %s, MAX,(@%d)"
    CMD_Route_Add    = "ROUTe:SCAN:Add (@%d)"
    CMD_Set_Sense_Range = ":SENS:CURR:RANG %.6f"     