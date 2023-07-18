"""
 * @File       : DAQ_Model.py
 * @Version    : V1.2.0
 * @Date       : July 18, 2023
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
    CMD_Get_Trigger_Status = ""
    CMD_Measure_VNPLC   = "SENS:VOLT:DC:NPLC %f,(@%d)"
    CMD_Measure_Voltage = "MEAS:VOLT:%s? %s, %.6f,(@%d)"
    # CMD_Measure_Current = "MEAS:CURR:%s? %.6f, %.6f,(@%d)"
    CMD_Measure_Temp    = "MEAS:TEMP:%s? %s, MAX,(@%d)"
    CMD_Route_Add       = ""
    CMD_Set_Trigger_Channel = ""
    CMD_Set_Trigger_Limit_Lower = ""
    CMD_Set_Trigger_Limit_Upper = ""
    CMD_Set_Trigger_Mode = ""
    CMD_Set_Sense_Average_Count = ""
    CMD_Set_Sense_Average_State = ""
    CMD_Set_Sense_Average_Type = ""
    CMD_Set_Sense_Range = ""
    CMD_Set_Sense_VNPLC = "SENS:VOLT:DC:NPLC %s,(@%d)"

class Keithley_DAQ6510(DAQ):
    Model_Name          = "Keithley_DAQ6510"
    CMD_Config_VMode    = "SENS:FUNC 'VOLT:%s',(@%d)"
    CMD_Config_IMode    = "SENS:FUNC 'CURR:%s',(@%d)"
    CMD_Config_TMode    = "CONF:TEMP:%s %s, %.6f,(@%d)"
    CMD_Get_Trigger_Status = "ROUTe:SCAN:STATe?"
    CMD_Measure_VNPLC   = ""
    CMD_Measure_Voltage = "MEAS:VOLT:%s? %.1f, %.6f,(@%d)"
    CMD_Measure_Current = "MEAS:CURR:%s? %.1f, %.6f,(@%d)"
    CMD_Measure_Temp    = "MEAS:TEMP:%s? %s, MAX,(@%d)"
    CMD_Route_Add       = "ROUTe:SCAN:Add (@%d)"
    CMD_Set_Trigger_Channel = "ROUTe:SCAN:MONitor:CHANnel (@%d)"
    CMD_Set_Trigger_Limit_Lower = "ROUTe:SCAN:MONitor:LIMit:LOWer %f"
    CMD_Set_Trigger_Limit_Upper = "ROUTe:SCAN:MONitor:LIMit:UPPer %f"
    CMD_Set_Trigger_Mode = "ROUTe:SCAN:MONitor:MODE %s"
    CMD_Set_Sense_Average_Count = "VOLT:AVER:COUNT %d, (@%d)"
    CMD_Set_Sense_Average_State = "VOLT:AVER %s, (@%d)"
    CMD_Set_Sense_Average_Type = "VOLT:AVER:TCON %s"
    CMD_Set_Sense_Range = ":SENS:CURR:RANG %.6f"
    CMD_Set_Sense_VNPLC = "SENS:VOLT:NPLC %s, (@%d)"
    CMD_Set_Sense_INPLC = "SENS:CURR:NPLC %s, (@%d)"