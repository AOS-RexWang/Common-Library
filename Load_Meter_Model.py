"""
 * @File       : Load_Meter_Model.py
 * @Version    : V1.0.0
 * @Date       : April 27, 2022
 * @Brief      : Child class of Load Meter
 * @Author     : Rex Wang
 * @Last editor: Rex Wang
 * Copyright (C) 2022 Alpha & Omega Semiconductor Ltd. All rights reserved.
"""
from Library.INSTR import Load_Meter

class Keithley_2400(Load_Meter):
    CMD_Get_Output_State = ":OUTPut?"
    CMD_Initiate_Measurement = ":INITiate"
    CMD_Set_All_Measurement_Off = ":SENSe:FUNCtion:OFF:ALL"
    CMD_Set_All_Measurement_On = ":SENSe:FUNCtion:ON:ALL"
    CMD_Set_Arm_Count = ":ARM:COUNt %d"
    CMD_Set_Arm_Count_Infinite = ":ARM:COUNt INFinite"
    CMD_Set_Beeper_State = ":SYSTem:BEEPer:STATe %d"
    CMD_Set_Concurrent_Measurement_State_Off = ":SENSe:FUNCtion:CONCurrent OFF"
    CMD_Set_Concurrent_Measurement_State_On = ":SENSe:FUNCtion:CONCurrent ON"
    CMD_Set_Idle = ":ABORt"
    CMD_Set_Measurement_Off = ":SENSe:FUNCtion:OFF '%s'"
    CMD_Set_Measurement_On = ":FUNCtion '%s'"
    CMD_Set_Output_State_Off = ":OUTPut:STATe OFF"
    CMD_Set_Output_State_On = ":OUTPut:STATe ON"
    CMD_Set_Remote_Sense_Off = ":SYSTem:RSENse 0"
    CMD_Set_Remote_Sense_On = ":SYSTem:RSENse 1"
    CMD_Set_Sense_Averaging_Count = ":SENSe:AVERage:COUNt %d"
    CMD_Set_Sense_Averaging_State = ":SENSe:AVERage:STATe %d"
    CMD_Set_Sense_Averaging_Type = ":SENSe:AVERage:TCONtrol %s"
    CMD_Set_Sense_Current_Limit = ":SENSe:CURRent:DC:PROTection %f"
    CMD_Set_Sense_Current_Range = ":SENSe:CURRent:DC:RANGe %f"
    CMD_Set_Sense_Current_Range_Auto_State = ":SENSe:CURRent:DC:RANGe:AUTO %d"
    CMD_Set_Sense_Voltage_Limit = ":SENSe:VOLTage:DC:PROTection %f"
    CMD_Set_Sense_Voltage_Range = ":SENSe:VOLTage:DC:RANGe %f"
    CMD_Set_Sense_Voltage_Range_Auto_State = ":SENSe:VOLTage:DC:RANGe:AUTO %d"
    CMD_Set_Source_Current_Amplitude = ":SOURce:CURRent:LEVel:IMMediate:AMPLitude %.4f"
    CMD_Set_Source_Current_Limit = ":SOURce:CURRent:PROTection %f"
    CMD_Set_Source_Current_Range = ":SOURce:CURRent:RANGe %f"
    CMD_Set_Source_Mode = ":SOURce:FUNCtion:MODE %s"
    CMD_Set_Source_Voltage_Amplitude = ":SOURce:VOLTage:LEVel:IMMediate:AMPLitude %.4f"
    CMD_Set_Source_Voltage_Limit = ":SOURce:VOLTage:PROTection %f"
    CMD_Set_Source_Voltage_Range = ":SOURce:VOLTage:RANGe %f"
