"""
 * @File       : DC_Source_Model.py
 * @Version    : V1.0.0
 * @Date       : April 27, 2022
 * @Brief      : Child class of DC Source.
 * @Author     : Rex Wang
 * @Last editor: Rex Wang
 * Copyright (C) 2022 Alpha & Omega Semiconductor Ltd. All rights reserved.
"""

from Library.INSTR import DC_Source

class Chroma_62000P_Series(DC_Source):
    Model_Name                       = "Chroma_62000P_Series"
    CMD_Set_Output_Channel           = ""
    CMD_Set_Voltage                  = "SOURce:VOLTage %.3f"
    CMD_Set_Voltage_Limit_State_On   = ""
    CMD_Set_Voltage_Limit_State_Off  = ""
    CMD_Set_Voltage_Limit            = "SOURce:VOLTage:PROTect:HIGH %.3f"
    CMD_Set_Voltage_Slew_Rate        = "SOURce:VOLTage:SLEW %.3f"
    CMD_Set_Current                  = "SOURce:CURRent %.3f"
    CMD_Set_Current_Limit_State_On   = ""
    CMD_Set_Current_Limit_State_Off  = ""
    CMD_Set_Current_Limit            = "SOURce:CURRent:PROTect:HIGH %.3f"
    CMD_Set_Current_Slew_Rate        = "SOURce:CURRent:SLEW %.3f"
    CMD_Set_Remote_Sense_On          = ""
    CMD_Set_Remote_Sense_Off         = ""

    CMD_Measure_Voltage              = "MEASure:VOLTage?"
    CMD_Measure_Current              = "MEASure:CURRent?"
    CMD_Measure_Power                = "MEASure:POWer?"

    CMD_Set_Output_State_On          = "CONFigure:OUTPut ON"
    CMD_Set_Output_State_Off         = "CONFigure:OUTPut OFF"
    CMD_Get_Output_State             = "CONFigure: OUTPut?"
    CMD_Set_Output_Channel_State_On  = ""
    CMD_Set_Output_Channel_State_Off = ""
    CMD_Set_Output_Series_State_On   = ""
    CMD_Set_Output_Series_State_Off  = ""

class Keithley_2200_Series(DC_Source):
    Model_Name                       = "Keithley_2200_Series"
    CMD_Set_Output_Channel           = "INSTrument:SELect CH%d"
    CMD_Set_Voltage                  = "SOURce:VOLTage %.3f"
    CMD_Set_Voltage_Limit_State_On   = "SOURce:VOLTage:LIMit:STATe 1"
    CMD_Set_Voltage_Limit_State_Off  = "SOURce:VOLTage:LIMit:STATe 0"
    CMD_Set_Voltage_Limit            = "SOURce:VOLTage:LIMit %.3f"
    CMD_Set_Voltage_Slew_Rate        = ""
    CMD_Set_Current                  = "SOURce:CURRent %.3f"
    CMD_Set_Current_Limit_State_On   = ""
    CMD_Set_Current_Limit_State_Off  = ""
    CMD_Set_Current_Limit            = ""
    CMD_Set_Current_Slew_Rate        = ""
    CMD_Set_Remote_Sense_On          = ""
    CMD_Set_Remote_Sense_Off         = ""

    CMD_Measure_Voltage              = "MEASure:VOLTage? CH%d"
    CMD_Measure_Current              = "MEASure:CURRent? CH%d"
    CMD_Measure_Power                = "MEASure:POWer? CH%d"

    CMD_Set_Output_State_On          = "SOURce:OUTPut ON"
    CMD_Set_Output_State_Off         = "SOURce:OUTPut OFF"
    CMD_Get_Output_State             = "SOURce:OUTPut?"
    CMD_Set_Output_Channel_State_On  = "SOURce:CHANNEL:OUTPUT 1"
    CMD_Set_Output_Channel_State_Off = "SOURce:CHANNEL:OUTPUT 0"
    CMD_Set_Output_Series_State_On   = "INSTrument:COMbine:SERies"
    CMD_Set_Output_Series_State_Off  = "INSTrument:COMbine:OFF"

class Keysight_E36300_Series(DC_Source):
    Model_Name                       = "Keysight_E36300_Series"
    CMD_Set_Output_Channel           = ""
    CMD_Set_Voltage                  = "SOURce:VOLTage %.3f , (@%d)"
    CMD_Set_Voltage_Limit_State_On   = ""
    CMD_Set_Voltage_Limit_State_Off  = ""
    CMD_Set_Voltage_Limit            = "SOURce:VOLTage:PROTection %.3f, (@%d)"
    CMD_Set_Voltage_Slew_Rate        = ""
    CMD_Set_Current                  = "SOURce:CURRent %.3f, (@%d)"
    CMD_Set_Current_Limit_State_On   = "SOURce:CURRent:PROTection:STATe ON, (@%d)"
    CMD_Set_Current_Limit_State_Off  = "SOURce:CURRent:PROTection:STATe OFF, (@%d)"
    CMD_Set_Current_Limit            = ""
    CMD_Set_Current_Slew_Rate        = ""
    CMD_Set_Remote_Sense_On          = "SOURce:VOLTage:SENSe:SOURce EXTernal, (@%d)"
    CMD_Set_Remote_Sense_Off         = "SOURce:VOLTage:SENSe:SOURce INTernal, (@%d)"

    CMD_Measure_Voltage              = "MEASure:VOLTage? (@%d)"
    CMD_Measure_Current              = "MEASure:CURRent? (@%d)"
    CMD_Measure_Power                = ""

    CMD_Set_Output_State_On          = "OUTPut:STATe ON, (@%d)"
    CMD_Set_Output_State_Off         = "OUTPut:STATe OFF, (@%d)"
    CMD_Get_Output_State             = ""
    CMD_Set_Output_Channel_State_On  = ""
    CMD_Set_Output_Channel_State_Off = ""
    CMD_Set_Output_Series_State_On   = ""
    CMD_Set_Output_Series_State_Off  = ""

class Ametek_AST200_17AR(DC_Source):
    Model_Name                       = "Ametek_AST200_17AR"
    CMD_Set_Output_Channel           = ""
    CMD_Set_Voltage                  = "SOURce:VOLTage %.6f"
    CMD_Set_Voltage_Limit_State_On   = ""
    CMD_Set_Voltage_Limit_State_Off  = ""
    CMD_Set_Voltage_Limit            = "SOURce:VOLTage:LIMit %.6f"
    CMD_Set_Voltage_Slew_Rate        = ""
    CMD_Set_Current                  = "SOURce:CURRent %.6f"
    CMD_Set_Current_Limit_State_On   = ""
    CMD_Set_Current_Limit_State_Off  = ""
    CMD_Set_Current_Limit            = "SOURce:CURRent:LIMit %.6f"
    CMD_Set_Current_Slew_Rate        = ""
    CMD_Set_Remote_Sense_On          = "SYSTem:LOCAL OFF"
    CMD_Set_Remote_Sense_Off         = "SYSTem:LOCAL ON"

    CMD_Measure_Voltage              = "MEASure:VOLTage?"
    CMD_Measure_Current              = "MEASure:CURRent?"
    CMD_Measure_Power                = ""

    CMD_Set_Output_State_On          = "OUTPut:STATe ON"
    CMD_Set_Output_State_Off         = "OUTPut:STATe OFF"
    CMD_Get_Output_State             = ""
    CMD_Set_Output_Channel_State_On  = ""
    CMD_Set_Output_Channel_State_Off = ""
    CMD_Set_Output_Series_State_On   = ""
    CMD_Set_Output_Series_State_Off  = ""
