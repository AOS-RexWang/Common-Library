"""
 * @File       : DC_Load_Model.py
 * @Version    : V1.0.0
 * @Date       : April 27, 2022
 * @Brief      : Child class of DC Load.
 * @Author     : Rex Wang
 * @Last editor: Rex Wang
 * Copyright (C) 2021 Alpha & Omega Semiconductor Ltd. All rights reserved.
"""

from Library.INSTR import DC_Load

class Chroma_6312A(DC_Load):
    CMD_Set_Mode                            = "MODE %s"
    CMD_Set_Channel                         = "CHANnel %d"
    CMD_Set_Static_Current                  = "CURRent:STATic:L1 %.3f"
    CMD_Set_Static_Current_Slew_Rate        = "CURRent:STATic:%s %.3f"
    CMD_Set_Dynamic_Current                 = "CURRent:DYNamic:L%d %.3f"
    CMD_Set_Dynamic_Current_Slew_Rate       = "CURRent:DYNamic:%s %.3f"
    CMD_Set_Dynamic_Current_Period          = "CURRent:DYNamic:T%d %f"

    CMD_Measure_Voltage                     = "MEASure:VOLTage?"
    CMD_Measure_Current                     = "MEASure:CURRent?"

    CMD_Set_Load_State_On                   = "LOAD ON"
    CMD_Set_Load_State_Off                  = "Load OFF"
    CMD_Set_Load_State_All_On               = ":RUN"
    CMD_Set_Load_State_All_Off              = ":ABORt"
    
    CMD_Get_Load_State                      = "LOAD?"
