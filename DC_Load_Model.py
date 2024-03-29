"""
 * @File       : DC_Load_Model.py
 * @Version    : V1.2.0
 * @Date       : July 18, 2023
 * @Brief      : Child class of DC Load.
 * @Author     : Rex Wang
 * @Last editor: Rex Wang
 * Copyright (C) 2023 Alpha & Omega Semiconductor Ltd. All rights reserved.
"""

from Library.INSTR import DC_Load

class Chroma_63103(DC_Load):
    Model_Name                              = "Chroma_63103"
    Current_Range                           = {"CCL": 6, "CCH": 60}
    CMD_Get_Load_State                      = "LOAD?"
    CMD_Measure_Voltage                     = "MEASure:VOLTage?"
    CMD_Measure_Current                     = "MEASure:CURRent?"
    CMD_Set_Mode                            = "MODE %s"
    CMD_Set_Channel                         = "CHANnel %d"
    CMD_Set_Dynamic_Current                 = "CURRent:DYNamic:L%d %.3f"
    CMD_Set_Dynamic_Current_Slew_Rate       = "CURRent:DYNamic:%s %.3f"
    CMD_Set_Dynamic_Current_Period          = "CURRent:DYNamic:T%d %f"
    CMD_Set_Load_Short_Off                  = "LOAD:SHORt OFF"
    CMD_Set_Load_Short_On                   = "LOAD:SHORt ON"
    CMD_Set_Load_State_Off                  = "Load OFF"
    CMD_Set_Load_State_On                   = "LOAD ON"
    CMD_Set_Load_State_All_Off              = ":ABORt"
    CMD_Set_Load_State_All_On               = ":RUN"
    CMD_Set_Resistance                      = "RESistance:L1 %.3f"
    CMD_Set_Resistance_Slew_Rate            = "RESistance:%s %.3f"
    CMD_Set_Static_Current                  = "CURRent:STATic:L1 %.3f"
    CMD_Set_Static_Current_Slew_Rate        = "CURRent:STATic:%s %.3f"

class Chroma_63630_80_60(DC_Load):
    Model_Name                              = "Chroma_63630_80_60"
    Current_Range                           = {"CCL": 0.6, "CCM": 6, "CCH": 60}
    CMD_Get_Load_State                      = "LOAD?"
    CMD_Measure_Voltage                     = "MEASure:VOLTage?"
    CMD_Measure_Current                     = "MEASure:CURRent?"
    CMD_Set_Mode                            = "MODE %s"
    CMD_Set_Channel                         = "CHANnel %d"
    CMD_Set_Dynamic_Current                 = "CURRent:DYNamic:L%d %.3f"
    CMD_Set_Dynamic_Current_Slew_Rate       = "CURRent:DYNamic:%s %.3f"
    CMD_Set_Dynamic_Current_Period          = "CURRent:DYNamic:T%d %f"
    CMD_Set_Load_Short_Off                  = "LOAD:SHORt OFF"
    CMD_Set_Load_Short_On                   = "LOAD:SHORt ON"
    CMD_Set_Load_State_Off                  = "Load OFF"
    CMD_Set_Load_State_On                   = "LOAD ON"
    CMD_Set_Load_State_All_Off              = ":ABORt"
    CMD_Set_Load_State_All_On               = ":RUN"
    CMD_Set_Resistance                      = "RESistance:STATic:L1 %.3f"
    CMD_Set_Resistance_Slew_Rate            = ""
    CMD_Set_Static_Current                  = "CURRent:STATic:L1 %.3f"
    CMD_Set_Static_Current_Slew_Rate        = "CURRent:STATic:%s %.3f"

class Chroma_63640_80_80(DC_Load):
    Model_Name                              = "Chroma_63640_80_80"
    Current_Range                           = {"CCL": 0.8, "CCM": 8, "CCH": 80}
    CMD_Get_Load_State                      = "LOAD?"
    CMD_Measure_Voltage                     = "MEASure:VOLTage?"
    CMD_Measure_Current                     = "MEASure:CURRent?"
    CMD_Set_Mode                            = "MODE %s"
    CMD_Set_Channel                         = "CHANnel %d"
    CMD_Set_Dynamic_Current                 = "CURRent:DYNamic:L%d %.3f"
    CMD_Set_Dynamic_Current_Slew_Rate       = "CURRent:DYNamic:%s %.3f"
    CMD_Set_Dynamic_Current_Period          = "CURRent:DYNamic:T%d %f"
    CMD_Set_Load_Short_Off                  = "LOAD:SHORt OFF"
    CMD_Set_Load_Short_On                   = "LOAD:SHORt ON"
    CMD_Set_Load_State_Off                  = "Load OFF"
    CMD_Set_Load_State_On                   = "LOAD ON"
    CMD_Set_Load_State_All_Off              = ":ABORt"
    CMD_Set_Load_State_All_On               = ":RUN"
    CMD_Set_Resistance                      = "RESistance:STATic:L1 %.3f"
    CMD_Set_Resistance_Slew_Rate            = ""
    CMD_Set_Static_Current                  = "CURRent:STATic:L1 % .3f"
    CMD_Set_Static_Current_Slew_Rate        = "CURRent:STATic:%s %.3f"
    
class KIKUSUI_PLZ334WL(DC_Load):
    Model_Name                              = "KIKUSUI_PLZ334WL"
    Current_Range                           = {"CC": 1, "CC": 10, "CC": 100}
    CMD_Get_Load_State                      = "LOAD?"
    CMD_Measure_Voltage                     = "MEASure:VOLTage?"
    CMD_Measure_Current                     = "MEASure:CURRent?"
    CMD_Set_Mode                            = "FUNCtion %s" #{"CC", "CV", "CP", "CR", "CCCV", "CRCV"}
    CMD_Set_Channel                         = ""
    CMD_Set_Dynamic_Current                 = ""
    CMD_Set_Dynamic_Current_Slew_Rate       = ""
    CMD_Set_Dynamic_Current_Period          = ""
    CMD_Set_Load_Short_Off                  = "INPut:SHORt OFF"
    CMD_Set_Load_Short_On                   = "INPut:SHORt ON"
    CMD_Set_Load_State_Off                  = "INPut OFF"
    CMD_Set_Load_State_On                   = "INPut ON"
    CMD_Set_Load_State_All_Off              = ":ABORt"
    CMD_Set_Load_State_All_On               = ""
    CMD_Set_Resistance                      = ""
    CMD_Set_Resistance_Slew_Rate            = ""
    CMD_Set_Static_Current                  = "CURRent %.3f"
    CMD_Set_Static_Current_Slew_Rate        = "CURRent:SLEW %.3f"