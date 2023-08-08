"""
 * @File       : Function_Generator_Model.py
 * @Version    : V1.3.0
 * @Date       : Aug 8, 2023
 * @Brief      : Child class of Function_Gernerator.
 * @Author     : Rex Wang
 * @Last editor: Rex Wang
 * Copyright (C) 2023 Alpha & Omega Semiconductor Ltd. All rights reserved.
"""

from Library.INSTR import Function_Generator

class AFG31000_Series(Function_Generator):
    CMD_Load_Memory_Trace   = "MMEMory:LOAD:TRACe EMEMory%d,'%s'"
    CMD_Manual_Trigger      = "*TRG"
    CMD_Set_Burst_Cycle     = "SOURce%d:BURSt:NCYCles %d"
    CMD_Set_Burst_Idle_End  = "SOURce%d:BURSt:IDLE END"
    CMD_Set_Burst_Idle_Start= "SOURce%d:BURSt:IDLE START"
    CMD_Set_Burst_Off       = "SOURce%d:BURSt OFF"
    CMD_Set_Burst_On        = "SOURce%d:BURSt ON"
    CMD_Set_Burst_Trigger_Delay = "SOURce%d:BURSt:TDELay %f"
    CMD_Set_Frequency       = "SOURce%d:FREQuency %.6fHz"
    CMD_Set_Function        = "SOURce%d:FUNCtion:SHAPe %s"
    VAR_Set_Function        = {"DC":"DC", "SIN":"SINusoid", "SQU":"SQUare", "RAMP":"Ramp", "PULSE":"PULSe", "MEMORY1":"EMEMory1", "MEMORY2":"EMEMory2"}
    CMD_Set_Impedance       = "OUTPut%d:IMPedance %s"
    CMD_Set_Output_State    = "OUTPut%d:STATe %d"
    CMD_Set_Phase           = "SOURce%d:PHASe:ADJust %.2fDEG"
    CMD_Set_Pulse_Duty      = "SOURce%d:PULSe:DCYCle %.1f"
    CMD_Set_Pulse_Hold      = "SOURce%d:PULSe:HOLD %s"
    CMD_Set_Pulse_Lead_Delay = "SOURce%d:PULSe:DELay %.10f"
    CMD_Set_Pulse_Leading   = "SOURce%d:PULSe:TRANsition:LEADing %.10f"
    CMD_Set_Pulse_Period    = "SOURce%d:PULSe:PERiod %.10f"
    CMD_Set_Pulse_Trailing  = "SOURce%d:PULSe:TRANsition:Trailing %.10f"
    CMD_Set_Pulse_Width     = "SOURce%d:PULSe:WIDTh %.10f"
    CMD_Set_Ramp_Symmetry   = "SOURce%d:FUNCtion:RAMP:SYMMetry %.1f"
    CMD_Set_Trigger_Slope   = "TRIGger:SLOPe %s"
    CMD_Set_Trigger_Source  = "TRIGger:SOURce %s"
    CMD_Set_Trigger_Timer   = "TRIGger:TIMer %f"
    CMD_Set_Unit            = "SOURce%d:VOLTage:UNIT %s"
    CMD_Set_Voltage_Amplitude       = "SOURce%d:VOLTage:LEVel:IMMediate:AMPLitude %.3f%s"
    CMD_Set_Voltage_High            = "SOURce%d:VOLTage:LEVel:IMMediate:HIGH %.9fV"
    CMD_Set_Voltage_Low             = "SOURce%d:VOLTage:LEVel:IMMediate:LOW %.9fV"
    CMD_Set_Voltage_Offset          = "SOURce%d:VOLTage:LEVel:IMMediate:OFFSet %fV"