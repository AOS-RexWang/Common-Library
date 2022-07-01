"""
 * @File       : Function_Generator_Model.py
 * @Version    : V1.1.0
 * @Date       : July 01, 2022
 * @Brief      : Child class of Function_Gernerator.
 * @Author     : Rex Wang
 * @Last editor: Rex Wang
 * Copyright (C) 2022 Alpha & Omega Semiconductor Ltd. All rights reserved.
"""

from Library.INSTR import Function_Generator

class AFG31000_Series(Function_Generator):
    CMD_Set_Amplitude       = "SOURce%d:VOLTage:LEVel:IMMediate:AMPLitude %.3f%s"
    CMD_Set_Frequency       = "SOURce%d:FREQuency %.6fHz"
    CMD_Set_Function        = "SOURce%d:FUNCtion:SHAPe %s"
    VAR_Set_Function        = {"DC":"DC", "SIN":"SINusoid", "SQU":"SQUare", "RAMP":"Ramp", "PULSE":"PULSe"}
    CMD_Set_Impedance       = "OUTPut%d:IMPedance %s"
    CMD_Set_Offset          = "SOURce%d:VOLTage:LEVel:IMMediate:OFFSet %fV"
    CMD_Set_Output_State    = "OUTPut%d:STATe %d"
    CMD_Set_Phase           = "SOURce%d:PHASe:ADJust %.2fDEG"
    CMD_Set_Pulse_Duty      = "SOURce%d:PULSe:DCYCle %.1f"
    CMD_Set_Ramp_Symmetry   = "SOURce%d:FUNCtion:RAMP:SYMMetry %.1f"
    CMD_Set_Unit            = "SOURce%d:VOLTage:UNIT %s"
    
    
