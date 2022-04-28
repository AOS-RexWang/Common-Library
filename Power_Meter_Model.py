"""
 * @File       : Power_Meter_Model.py
 * @Version    : V1.0.0
 * @Date       : April 27, 2022
 * @Brief      : Child class of Power Meter.
 * @Author     : Rex Wang
 * @Last editor: Rex Wang
 * Copyright (C) 2022 Alpha & Omega Semiconductor Ltd. All rights reserved.
"""

from Library.INSTR import Power_Meter

class Yokogawa_WT310E(Power_Meter):
    CMD_Set_Display_Item                = ":DISPLAY:NORMAL:ITEM%d %s"
    CMD_Set_Mode                        = ":INPut:MODE %s"
    CMD_Set_Voltage_Auto_Range          = ":INPUT:VOLTAGE:RANGe AUTO"
    CMD_Set_Voltage_Range               = ":INPUT:VOLTAGE:RANGe %d"
    CMD_Set_Current_Auto_Range          = ":INPUT:CURRent:RANGe AUTO"
    CMD_Set_Current_Range               = ":INPUT:CURRent:RANGe %.4f"
    CMD_Set_Measure_Averaging_State     = ":MEASure:AVERaging:STATe %s"
    CMD_Set_Measure_Averaging_Type      = ":MEASure:AVERaging:TYPE %s"
    CMD_Set_Measure_Averaging_Count     = ":MEASure:AVERaging:COUNt %d"
    CMD_Set_Numeric_Format              = ":NUMeric:FORMat %s"
    CMD_Set_Numeric_Item                = ":NUMERIC:NORMAL:ITEM%d %s,1"
    CMD_Preset_Numeric_Item             = ":NUMeric:NORMal:PRESet %d"
    CMD_Clear_Numeric_Item              = ":NUMeric:NORMal:CLEar %d"
    CMD_Measure_Numeric_Item            = ":NUMeric:NORMal:VALue? %d"
