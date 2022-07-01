"""
 * @File       : INSTR.py
 * @Version    : V1.1.0
 * @Date       : July 01, 2022
 * @Brief      : Father class of Instrument.
 * @Author     : Rex Wang
 * @Last editor: Rex Wang
 * Copyright (C) 2021 Alpha & Omega Semiconductor Ltd. All rights reserved.
"""
import pyvisa as visa

INSTR_CNT = 0
OSC_MEASUREMENT = []

class DC_Source():
    Model_Name                       = ""
    CMD_Set_Output_Channel           = ""
    CMD_Set_Voltage                  = ""
    CMD_Set_Voltage_Limit_State_On   = ""
    CMD_Set_Voltage_Limit_State_Off  = ""
    CMD_Set_Voltage_Limit            = ""
    CMD_Set_Voltage_Slew_Rate        = ""
    CMD_Set_Current                  = ""
    CMD_Set_Current_Limit_State_On   = ""
    CMD_Set_Current_Limit_State_Off  = ""
    CMD_Set_Current_Limit            = ""
    CMD_Set_Current_Slew_Rate        = ""
    CMD_Set_Remote_Sense_On          = ""
    CMD_Set_Remote_Sense_Off         = ""

    CMD_Measure_Voltage              = ""
    CMD_Measure_Current              = ""
    CMD_Measure_Power                = ""

    CMD_Set_Output_State_On          = ""
    CMD_Set_Output_State_Off         = ""
    CMD_Get_Output_State             = ""
    CMD_Set_Output_Channel_State_On  = ""
    CMD_Set_Output_Channel_State_Off = ""
    CMD_Set_Output_Series_State_On   = ""
    CMD_Set_Output_Series_State_Off  = ""


    def __init__(self, instrument_address=None):
        global INSTR_CNT
        self.State = False
        self.Resource_Manager = visa.ResourceManager()
        if instrument_address != None:
            self.Instrument = self.Resource_Manager.open_resource(instrument_address)
            INSTR_CNT += 1

    def Config(self, channel = None, voltage_limit = None, voltage = None, current_limit = None, current = None,
               voltage_slew_rate = None, current_slew_rate = None, remote_state = None, series_state = None):
        if self.Model_Name == "Chroma_62000P_Series" or self.Model_Name == "Ametek_AST200_17AR" or self.Model_Name == "Keithley_2200_Series" or self.Model_Name == "Keithley_2260B_Series":
            channel = None

        if channel != None:
            self.Set_Output_Channel(channel)

        if voltage_limit != None:
            self.Set_Voltage_Limit_State(True, channel)
            self.Set_Voltage_Limit(voltage_limit, channel)

        if voltage != None:
            self.Set_Voltage(voltage, channel)

        if current_limit != None:
            self.Set_Current_Limit_State(True, channel)
            self.Set_Current_Limit(current_limit, channel)

        if current != None:
            self.Set_Current(current, channel)

        if voltage_slew_rate != None:
            self.Set_Voltage_Slew_Rate(voltage_slew_rate, channel)

        if current_slew_rate != None:
            self.Set_Current_Slew_Rate(current_slew_rate, channel)

        if remote_state != None:
            self.Set_Remote_Sense_State(True, channel)

        if series_state != None:
            self.Set_Output_Series_State(series_state)

    def Measure(self, item, channel = None):
        if self.Model_Name == "Chroma_62000P_Series" or self.Model_Name == "Ametek_AST200_17AR" or self.Model_Name == "Keithley_2200_Series" or self.Model_Name == "Keithley_2260B_Series":
            channel = None
        if item == "Voltage":
            return self.Measure_Voltage(channel)
        elif item == "Current":
            return self.Measure_Current(channel)
        elif item == "Power":
            return self.Measure_Power(channel)

    def Output_State(self, state, channel = None):
        if self.Model_Name == "Chroma_62000P_Series" or self.Model_Name == "Ametek_AST200_17AR" or self.Model_Name == "Keithley_2200_Series" or self.Model_Name == "Keithley_2260B_Series":
            channel = None
        if channel != None:
            self.Set_Output_Channel(channel)
        self.Set_Output_State(state, channel)
        self.Set_Output_Channel_State(state)

    def Reset(self):
        self.Instrument.write("*RST")

    def Set_Output_Channel(self, channel):
        if self.CMD_Set_Output_Channel:
            self.Instrument.write(self.CMD_Set_Output_Channel % (channel))

    def Set_Voltage(self, voltage, channel = None):
        if self.CMD_Set_Voltage:
            if channel != None:
                self.Instrument.write(self.CMD_Set_Voltage % (voltage, channel))
            else:
                self.Instrument.write(self.CMD_Set_Voltage % (voltage))

    def Set_Voltage_Limit_State(self, state, channel = None):
        if channel != None:
            if self.CMD_Set_Voltage_Limit_State_On and self.CMD_Set_Voltage_Limit_State_Off:
                if state:
                    self.Instrument.write(self.CMD_Set_Voltage_Limit_State_On % (channel))
                else:
                    self.Instrument.write(self.CMD_Set_Voltage_Limit_State_Off % (channel))
        else:
            if self.CMD_Set_Voltage_Limit_State_On and self.CMD_Set_Voltage_Limit_State_Off:
                if state:
                    self.Instrument.write(self.CMD_Set_Voltage_Limit_State_On)
                else:
                    self.Instrument.write(self.CMD_Set_Voltage_Limit_State_Off)

    def Set_Voltage_Limit(self, voltage_limit, channel = None):
        self.Set_Voltage_Limit_State(True)
        if self.CMD_Set_Voltage_Limit:
            if channel != None:
                self.Instrument.write(self.CMD_Set_Voltage_Limit % (voltage_limit, channel))
            else:
                self.Instrument.write(self.CMD_Set_Voltage_Limit % (voltage_limit))

    def Set_Current(self, current, channel = None):
        if self.CMD_Set_Current:
            if channel != None:
                self.Instrument.write(self.CMD_Set_Current % (current, channel))
            else:
                self.Instrument.write(self.CMD_Set_Current % (current))

    def Set_Current_Limit_State(self, state, channel = None):
        if channel != None:
            if self.CMD_Set_Current_Limit_State_On and self.CMD_Set_Current_Limit_State_Off:
                if state:
                    self.Instrument.write(self.CMD_Set_Current_Limit_State_On % (channel))
                else:
                    self.Instrument.write(self.CMD_Set_Current_Limit_State_Off % (channel))
        else:
            if self.CMD_Set_Current_Limit_State_On and self.CMD_Set_Current_Limit_State_Off:
                if state:
                    self.Instrument.write(self.CMD_Set_Current_Limit_State_On)
                else:
                    self.Instrument.write(self.CMD_Set_Current_Limit_State_Off)

    def Set_Current_Limit(self, current_limit, channel = None):
        if self.CMD_Set_Current_Limit:
            if channel != None:
                self.Instrument.write(self.CMD_Set_Current_Limit % (current_limit, channel))
            else:
                self.Instrument.write(self.CMD_Set_Current_Limit % (current_limit))

    def Set_Voltage_Slew_Rate(self, slew_rate, channel = None):
        if self.CMD_Set_Voltage_Slew_Rate:
            if channel != None:
                self.Instrument.write(self.CMD_Set_Voltage_Slew_Rate % (slew_rate, channel))
            else:
                self.Instrument.write(self.CMD_Set_Voltage_Slew_Rate % (slew_rate))

    def Set_Current_Slew_Rate(self, slew_rate, channel = None):
        if self.CMD_Set_Current_Slew_Rate:
            if channel != None:
                self.Instrument.write(self.CMD_Set_Current_Slew_Rate % (slew_rate, channel))
            else:
                self.Instrument.write(self.CMD_Set_Current_Slew_Rate % (slew_rate))

    def Set_Remote_Sense_State(self, state, channel = None):
        if channel != None:
            if self.CMD_Set_Remote_Sense_On and self.CMD_Set_Remote_Sense_Off:
                if state:
                    self.Instrument.write(self.CMD_Set_Remote_Sense_On % (channel))
                else:
                    self.Instrument.write(self.CMD_Set_Remote_Sense_Off % (channel))
        else:
            if self.CMD_Set_Remote_Sense_On and self.CMD_Set_Remote_Sense_Off:
                if state:
                    self.Instrument.write(self.CMD_Set_Remote_Sense_On)
                else:
                    self.Instrument.write(self.CMD_Set_Remote_Sense_Off)

    def Measure_Voltage(self, channel = None):
        if self.CMD_Measure_Voltage:
            if channel != None:
                return float(self.Instrument.query(self.CMD_Measure_Voltage % (channel)))
            else:
                return float(self.Instrument.query(self.CMD_Measure_Voltage))
        else:
            return 0

    def Measure_Current(self, channel = None):
        if self.CMD_Measure_Current:
            if channel != None:
                return float(self.Instrument.query(self.CMD_Measure_Current % (channel)))
            else:
                return float(self.Instrument.query(self.CMD_Measure_Current))
        else:
            return 0

    def Measure_Power(self, channel = None):
        if self.CMD_Measure_Power:
            if channel != None:
                return float(self.Instrument.query(self.CMD_Measure_Power % (channel)))
            else:
                return float(self.Instrument.query(self.CMD_Measure_Power))
        else:
            return 0

    def Set_Output_State(self, state, channel = None):
        if self.CMD_Set_Output_State_On and self.CMD_Set_Output_State_Off:
            if channel != None:
                if state:
                    self.Instrument.write(self.CMD_Set_Output_State_On % (channel))
                else:
                    self.Instrument.write(self.CMD_Set_Output_State_Off % (channel))
            else:
                if state:
                    self.Instrument.write(self.CMD_Set_Output_State_On)
                else:
                    self.Instrument.write(self.CMD_Set_Output_State_Off)

        #self.State = self.Get_Output_State()
        self.State = state

    def Set_Output_Channel_State(self, state):
        if self.CMD_Set_Output_Channel_State_On and self.CMD_Set_Output_Channel_State_Off:
            if state:
                self.Instrument.write(self.CMD_Set_Output_Channel_State_On)
            else:
                self.Instrument.write(self.CMD_Set_Output_Channel_State_Off)
        self.State = state

    def Set_Output_Series_State(self, state):
        if self.CMD_Set_Output_Series_State_On and self.CMD_Set_Output_Series_State_Off:
            if state:
                self.Instrument.write(self.CMD_Set_Output_Series_State_On)
            else:
                self.Instrument.write(self.CMD_Set_Output_Series_State_Off)

    def Get_Output_State(self, channel = None):
        if self.CMD_Get_Output_State:
            if channel != None:
                state = self.Instrument.query(self.CMD_Get_Output_State % channel)
            else:
                state = self.Instrument.query(self.CMD_Get_Output_State)
            if state == "ON" or state == "1\n":
                return True
            else:
                return False

    def Close(self):
        global INSTR_CNT
        self.Instrument.close()
        INSTR_CNT -= 1
        if INSTR_CNT == 0:
            self.Resource_Manager.close()

class DC_Load():

    CMD_Set_Mode                            = ""
    CMD_Set_Channel                         = ""
    CMD_Set_Static_Current                  = ""
    CMD_Set_Static_Current_Slew_Rate        = ""
    CMD_Set_Dynamic_Current                 = ""
    CMD_Set_Dynamic_Current_Slew_Rate       = ""
    CMD_Set_Dynamic_Current_Period          = ""
    CMD_Measure_Voltage                     = ""
    CMD_Measure_Current                     = ""
    CMD_Set_Load_State_On                   = ""
    CMD_Set_Load_State_Off                  = ""
    CMD_Set_Load_State_All_On               = ""
    CMD_Set_Load_State_All_Off              = ""
    
    CMD_Get_Load_State                      = ""

    def __init__(self, instrument_address=None):
        global INSTR_CNT
        self.State = False
        self.Resource_Manager = visa.ResourceManager()
        if instrument_address != None:
            self.Instrument = self.Resource_Manager.open_resource(instrument_address)
            INSTR_CNT += 1

    def Config(self, channel = None, mode = None, current1 = None, current2 = None, period1 = None, period2 = None,
                      static_rise_slew_rate = None, static_fall_slew_rate = None, dynamic_rise_slew_rate = None, dynamic_fall_slew_rate = None):
        if channel != None:
            self.Set_Channel(channel)
        if mode != None:
            self.Set_Mode(mode) #mode: {"CCL", "CCH", "CCDL", "CCDH", "CRL", "CRH", "CV"}
        if current1 != None:
            if mode == "CCL" or mode == "CCH":
                self.Set_Static_Current(current1)
            elif mode == "CRL":
                if current1 < 0.025:
                    current1 = 0.025
                if current1 > 100:
                    current1 = 100
                self.Set_Resistance(current1)
            elif mode == "CRH":
                if current1 < 1.25:
                    current1 = 1.25
                if current1 > 5000:
                    current1 = 5000
                self.Set_Resistance(current1)
            
        if static_rise_slew_rate != None:
            if mode == "CCL" or mode == "CCH":
                self.Set_Static_Current_Slew_Rate("Rise", static_rise_slew_rate)
            elif mode == "CRL" or mode == "CRH":
                self.Set_Resistance_Slew_Rate("Rise", static_rise_slew_rate)
        if static_fall_slew_rate != None:
            if mode == "CCL" or mode == "CCH":
                self.Set_Static_Current_Slew_Rate("Fall", static_fall_slew_rate)
            elif mode == "CRL" or mode == "CRH":
                self.Set_Resistance_Slew_Rate("Fall", static_fall_slew_rate)
        if current1 != None and current2 != None:
            self.Set_Dynamic_Current(current1, current2)
        if period1 != None and period2 != None:
            self.Set_Dynamic_Current_Period(period1, period2)
        if dynamic_rise_slew_rate != None:
            self.Set_Dynamic_Current_Slew_Rate("Rise", dynamic_rise_slew_rate)
        if dynamic_fall_slew_rate != None:
            self.Set_Dynamic_Current_Slew_Rate("Fall", dynamic_fall_slew_rate)

    def Measure(self, item, channel = None):
        if channel != None:
            self.Set_Channel(channel)
        if item == "Voltage":
            return self.Measure_Voltage()
        elif item == "Current":
            return self.Measure_Current()

    def Load_State(self, state, channel = None):
        if channel != None:
            self.Set_Channel(channel)
            if channel == "ALL":
                self.Set_Load_State_All(state)
            else:
                self.Set_Load_State(state)

    def Reset(self):
        self.Instrument.write("*RST")

    def Get_Load_State(self):
        if self.CMD_Get_Load_State:
            state = self.Instrument.query(self.CMD_Get_Load_State)
            if state == "1" or state == "ON":
                return True
            else:
                return False

    def Measure_Voltage(self):
        if self.CMD_Measure_Voltage:
            return float(self.Instrument.query(self.CMD_Measure_Voltage))

    def Measure_Current(self):
        if self.CMD_Measure_Current:
            return float(self.Instrument.query(self.CMD_Measure_Current))

    def Set_Mode(self, mode): 
        #6310A mode: {"CCL", "CCH", "CCDL", "CCDH", "CRL", "CRH", "CV"}
        #63600 mode: {"CCL", "CCM", "CCH", "CRL", "CRM", "CRH", "CVL", "CVM", "CVH", "CPL", "CPM", "CPH",
        #             "CZL", "CZM", "CZH", "CCDL", "CCDM","CCDH", "CCFSL", "CCFSM", "CCFSH", "TIML", "TIMM",
        #             "TIMH", "SWDL", "SWDM", "SWDH", "OCPL", "OCPM", "OCPH", "PROG", "MPPTL", "MPPTM", "MPPTH", "UDWL", "UDWM", "UDWH"}
        if self.CMD_Set_Mode:
            self.Instrument.write(self.CMD_Set_Mode % (mode))

    def Set_Channel(self, channel):
        if self.CMD_Set_Channel:
            self.Instrument.write(self.CMD_Set_Channel % (channel))

    def Set_Dynamic_Current(self, load1, load2):
        if self.CMD_Set_Dynamic_Current:
            self.Instrument.write(self.CMD_Set_Dynamic_Current % (1, load1))
            self.Instrument.write(self.CMD_Set_Dynamic_Current % (2, load2))
            #self.Set_Dynamic_Current(load1, load2)

    def Set_Dynamic_Current_Period(self, period1, period2):
        if self.CMD_Set_Dynamic_Current_Period:
            self.Instrument.write(self.CMD_Set_Dynamic_Current_Period % (1, period1))
            self.Instrument.write(self.CMD_Set_Dynamic_Current_Period % (2, period2))

    def Set_Dynamic_Current_Slew_Rate(self, slope, slew_rate):
        if self.CMD_Set_Dynamic_Current_Slew_Rate:
            self.Instrument.write(self.CMD_Set_Dynamic_Current_Slew_Rate % (slope, slew_rate))

    def Set_Load_Short_State(self, state):
        if self.CMD_Set_Load_Short_On and self.CMD_Set_Load_Short_Off:
            if state:
                self.Instrument.write(self.CMD_Set_Load_Short_On)
            else:
                self.Instrument.write(self.CMD_Set_Load_Short_Off)

    def Set_Load_State(self, state):
        if self.CMD_Set_Load_State_On and self.CMD_Set_Load_State_Off:
            if state:
                self.Instrument.write(self.CMD_Set_Load_State_On)
            else:
                self.Instrument.write(self.CMD_Set_Load_State_Off)
            self.State = state #self.Get_Load_State()

    def Set_Load_State_All(self, state):
        if self.CMD_Set_Load_State_All_On and self.CMD_Set_Load_State_All_Off:
            if state:
                self.Instrument.write(self.CMD_Set_Load_State_All_On)
            else:
                self.Instrument.write(self.CMD_Set_Load_State_All_Off)
            self.State = state #self.Get_Load_State()

    def Set_Resistance(self, resistance):
        if self.CMD_Set_Resistance:
            self.Instrument.write(self.CMD_Set_Resistance % (resistance))

    def Set_Resistance_Slew_Rate(self, slope, slew_rate):
        if self.CMD_Set_Resistance_Slew_Rate:
            self.Instrument.write(self.CMD_Set_Resistance_Slew_Rate % (slope, slew_rate))

    def Set_Static_Current(self, current):
        if self.CMD_Set_Static_Current:
            self.Instrument.write(self.CMD_Set_Static_Current % (current))

    def Set_Static_Current_Slew_Rate(self, slope, slew_rate):
        if self.CMD_Set_Static_Current_Slew_Rate:
            self.Instrument.write(self.CMD_Set_Static_Current_Slew_Rate % (slope, slew_rate))
        
    def Close(self):
        global INSTR_CNT
        self.Instrument.close()
        INSTR_CNT -= 1
        if INSTR_CNT == 0:
            self.Resource_Manager.close()

class Power_Meter():

    def __init__(self, instrument_address=None):
        global INSTR_CNT
        self.Resource_Manager = visa.ResourceManager()
        if instrument_address != None:
            self.Instrument = self.Resource_Manager.open_resource(instrument_address)
            INSTR_CNT += 1

    def Config(self, mode, voltage_range, current_range, average_state, average_type, average_count):
        self.Set_Mode(mode)
        self.Set_Voltage_Range(voltage_range)
        self.Set_Current_Range(current_range)
        self.Set_Numeric_Format("ASCii")
        self.Preset_Numeric_Item(1)

        self.Set_Display_Item(1, "U")
        self.Set_Display_Item(2, "I")
        self.Set_Display_Item(3, "P")
        self.Set_Display_Item(4, "ITHD")
        
        self.Set_Measure_Averaging(state = False)
        self.Set_Measure_Averaging(state = average_state, averaging_type = average_type, count = average_count)
    
    def Measure(self, item):
        if item == "Voltage":
            return self.Measure_Numeric_Item(1)
        elif item == "Current":
            return self.Measure_Numeric_Item(2)
        elif item == "Power":
            return self.Measure_Numeric_Item(3)

    def Reset(self):
        self.Instrument.write("*RST")

    def Set_Display_Item(self, index, item):
        if self.CMD_Set_Display_Item:
            self.Instrument.write(self.CMD_Set_Display_Item % (index, item))

    def Set_Mode(self, mode): #mode: {"RMS", "VMEan", "DC"}
        if self.CMD_Set_Mode:
            self.Instrument.write(self.CMD_Set_Mode % (mode))

    def Set_Voltage_Range(self, voltage_range):
        if self.CMD_Set_Voltage_Auto_Range:
            if voltage_range == "AUTO":
                self.Instrument.write(self.CMD_Set_Voltage_Auto_Range)
            else:
                self.Instrument.write(self.CMD_Set_Voltage_Range % (voltage_range))

    def Set_Current_Range(self, current_range):
        if self.CMD_Set_Current_Auto_Range:
            if current_range == "AUTO":
                self.Instrument.write(self.CMD_Set_Current_Auto_Range)
            else:
                self.Instrument.write(self.CMD_Set_Current_Range % (current_range))

    def Set_Measure_Averaging(self, state, averaging_type = None, count = None): #averaging_type: {"LINear", "EXPonent"}
        if self.CMD_Set_Measure_Averaging_State and self.CMD_Set_Measure_Averaging_Type and self.CMD_Set_Measure_Averaging_Count:
            if state:
                self.Instrument.write(self.CMD_Set_Measure_Averaging_State % ("ON"))
                self.Instrument.write(self.CMD_Set_Measure_Averaging_Type % (averaging_type))
                self.Instrument.write(self.CMD_Set_Measure_Averaging_Count % (count))
            else:
                self.Instrument.write(self.CMD_Set_Measure_Averaging_State % ("OFF"))

    def Set_Numeric_Format(self, data_format):
        if self.CMD_Set_Numeric_Format:
            self.Instrument.write(self.CMD_Set_Numeric_Format % (data_format))

    def Set_Numeric_Item(self, index, item):
        if self.CMD_Set_Numeric_Item:
            self.Instrument.write(self.CMD_Set_Numeric_Item % (index, item))

    def Preset_Numeric_Item(self, pattem):
        if self.CMD_Preset_Numeric_Item:
            self.Instrument.write(self.CMD_Preset_Numeric_Item % (pattem))

    def Clear_Numeric_Item(self, index):
        if self.CMD_Clear_Numeric_Item:
            self.Instrument.write(self.CMD_Clear_Numeric_Item % (index))

    def Measure_Numeric_Item(self, index):
        if self.CMD_Measure_Numeric_Item:
            measure_value = "NAN\n"
            while measure_value == "NAN\n":
                measure_value = self.Instrument.query(self.CMD_Measure_Numeric_Item % (index))
            return float(measure_value)

    def Close(self):
        global INSTR_CNT
        self.Instrument.close()
        INSTR_CNT -= 1
        if INSTR_CNT == 0:
            self.Resource_Manager.close()

class Oscilloscope():
    Model_Name                              = ""
    CMD_Clear_Sweeps                        = ""
    CMD_Get_Channel_Attenuation             = ""
    CMD_Get_Measurement_Statistics_Value    = ""
    VAR_Get_Measurement_Statistics_Value    = {}
    CMD_Get_Measurement_Value               = ""
    CMD_Get_Time_Scale                      = ""
    CMD_Get_Trigger_Channel                 = ""
    CMD_Get_Trigger_Type                    = ""
    CMD_Measurement_Clear                   = ""
    CMD_Measurement_Delete                  = ""
    CMD_Measurement_Gate_Start              = ""
    CMD_Measurement_Gate_Stop               = ""
    CMD_Measurement_Setting                 = ""
    CMD_Measurement_Statistics_State        = ""
    CMD_Print_Screen                        = "" 
    CMD_Print_Setting                       = ""
    CMD_Set_Acquire_mode                    = ""
    CMD_Set_Axis_Labels_State               = ""
    CMD_Set_Channel_Attenuation             = ""
    CMD_Set_Channel_Bandwidth_Limit         = ""
    CMD_Set_Channel_Coupling                = ""
    VAR_Set_Channel_Coupling                = {}
    CMD_Set_Channel_Label                   = ""
    CMD_Set_Channel_Label_State             = ""
    CMD_Set_Channel_Noise_Filter            = ""
    CMD_Set_Channel_Trace_State_Off         = ""
    CMD_Set_Channel_Trace_State_On          = ""
    CMD_Set_Channel_Voltage_Offset          = ""
    CMD_Set_Channel_Voltage_Position        = ""
    CMD_Set_Channel_Voltage_Scale           = ""
    CMD_Set_Cmd_Header                      = ""
    CMD_Set_Cmd_Verbose                     = ""
    CMD_Set_Display_Grid                    = ""
    VAR_Set_Display_Grid                    = {}
    CMD_Set_Display_State_Off               = ""
    CMD_Set_Display_State_On                = ""
    CMD_Set_Time_Scale                      = ""
    CMD_Set_Trigger_Channel                 = ""
    CMD_Set_Trigger_Coupling                = ""
    VAR_Set_Trigger_Coupling                = {}
    CMD_Set_Trigger_Delay                   = ""
    CMD_Set_Trigger_Level                   = ""
    CMD_Set_Trigger_Mode                    = ""
    CMD_Set_Trigger_Position                = ""
    CMD_Set_Trigger_Slope                   = ""
    VAR_Set_Trigger_Slope                   = {}
    CMD_Set_Trigger_Type                    = ""

    def __init__(self, instrument_address=None):
        global INSTR_CNT
        self.Resource_Manager = visa.ResourceManager()
        if instrument_address != None:
            self.Instrument = self.Resource_Manager.open_resource(instrument_address)
            self.Address = instrument_address
            INSTR_CNT += 1

    def Reset(self):
        channel_range = []
        self.Set_Cmd_Header("OFF")
        for channel in range(1, 4): 
            channel_range.append(self.Get_Channel_Range(channel = channel))
        self.Instrument.write("*RST")
        
        for channel in range(1, 4):
            self.Set_Channel_Range_Mode(channel = channel, range_mode = "MANual")
            self.Set_Channel_Range(channel = channel, channel_range = channel_range[channel - 1])

    def Config(self, display_grid = None, time_scale = None, timeout = None):
        self.Set_Display_State(True)
        self.Set_Axis_Labels_State(False)
        self.Set_Cmd_Header("OFF")
        if display_grid != None:
            self.Set_Display_Grid(display_grid) #display_grid: {"Overlay", "Stacked"}
        self.Set_Acquire_mode("HIRes") #{SAMple|PEAKdetect|HIRes|AVErage|ENVelope}
        if time_scale != None:
            self.Set_Time_Scale(time_scale)
        if timeout != None:
            self.Instrument.timeout = timeout
    def Channel_Config(self,
                       c1_state = None, c2_state = None, c3_state = None, c4_state = None,
                       c5_state = None, c6_state = None, c7_state = None, c8_state = None,
                       c1_scale = None, c2_scale = None, c3_scale = None, c4_scale = None,
                       c5_scale = None, c6_scale = None, c7_scale = None, c8_scale = None,
                       c1_coupling = None, c2_coupling = None, c3_coupling = None, c4_coupling = None,
                       c5_coupling = None, c6_coupling = None, c7_coupling = None, c8_coupling = None,
                       c1_bandwidth = None, c2_bandwidth = None, c3_bandwidth = None, c4_bandwidth = None,
                       c5_bandwidth = None, c6_bandwidth = None, c7_bandwidth = None, c8_bandwidth = None,
                       c1_filter = None, c2_filter = None, c3_filter = None, c4_filter = None,
                       c5_filter = None, c6_filter = None, c7_filter = None, c8_filter = None,
                       c1_offset = None, c2_offset = None, c3_offset = None, c4_offset = None,
                       c5_offset = None, c6_offset = None, c7_offset = None, c8_offset = None,
                       c1_position = None, c2_position = None, c3_position = None, c4_position = None,
                       c5_position = None, c6_position = None, c7_position = None, c8_position = None,
                       c1_label = None, c2_label = None, c3_label = None, c4_label = None,
                       c5_label = None, c6_label = None, c7_label = None, c8_label = None):
        
        channel_state = [c1_state, c2_state, c3_state, c4_state, c5_state, c6_state, c7_state, c8_state]
        for channel, state in enumerate(channel_state, start = 1):
            if state != None and state != "":
                if self.Model_Name == "Lecroy_HDO4034A" and channel > 4:
                    break
                self.Set_Channel_Trace_State(int(channel), state)
        
        channel_scale = [c1_scale, c2_scale, c3_scale, c4_scale, c5_scale, c6_scale, c7_scale, c8_scale]
        for channel, scale in enumerate(channel_scale, start = 1):
            if scale != None and scale != "":
                if self.Model_Name == "Lecroy_HDO4034A" and channel > 4:
                    break
                self.Set_Channel_Voltage_Scale(int(channel), scale)

        channel_coupling = [c1_coupling, c2_coupling, c3_coupling, c4_coupling, c5_coupling, c6_coupling, c7_coupling, c8_coupling]
        for channel, coupling in enumerate(channel_coupling, start = 1):
            if coupling != None and coupling != "":
                if self.Model_Name == "Lecroy_HDO4034A" and channel > 4:
                    break
                self.Set_Channel_Coupling(int(channel), coupling) #channel_coupling: {"AC", "DC", "DC50", "DCREJ", "GND", "IAC", "IDC"}

        channel_bandwidth = [c1_bandwidth, c2_bandwidth, c3_bandwidth, c4_bandwidth, c5_bandwidth, c6_bandwidth, c7_bandwidth, c8_bandwidth]
        for channel, bandwidth in enumerate(channel_bandwidth, start = 1):
            if bandwidth != None and bandwidth != "":
                if self.Model_Name == "Lecroy_HDO4034A" and channel > 4:
                    break
                self.Set_Channel_Bandwidth_Limit(int(channel), bandwidth)
        
        channel_filter = [c1_filter, c2_filter, c3_filter, c4_filter, c5_filter, c6_filter, c7_filter, c8_filter]
        for channel, c_filter in enumerate(channel_filter, start = 1):
            if c_filter != None and c_filter != "":
                if self.Model_Name == "Lecroy_HDO4034A" and channel > 4:
                    break
                self.Set_Channel_Noise_Filter(int(channel), c_filter)
        
        channel_offset = [c1_offset, c2_offset, c3_offset, c4_offset, c5_offset, c6_offset, c7_offset, c8_offset]
        for channel, offset in enumerate(channel_offset, start = 1):
            if offset != None and offset != "":
                if self.Model_Name == "Lecroy_HDO4034A" and channel > 4:
                    break
                if self.Model_Name == "Lecroy_HDO4034A":
                    offset = -offset
                self.Set_Channel_Voltage_Offset(int(channel), offset)
        
        channel_position = [c1_position, c2_position, c3_position, c4_position, c5_position, c6_position, c7_position, c8_position]
        for channel, position in enumerate(channel_position, start = 1):
            if position != None and position != "":
                if self.Model_Name == "Lecroy_HDO4034A" and channel > 4:
                    break
                self.Set_Channel_Voltage_Position(int(channel), position)

        channel_label = [c1_label, c2_label, c3_label, c4_label, c5_label, c6_label, c7_label, c8_label]
        for channel, label in enumerate(channel_label, start = 1):
            if label != None and label != "":
                if self.Model_Name == "Lecroy_HDO4034A" and channel > 4:
                    break
                self.Set_Channel_Label_State(channel, True)
                self.Set_Channel_Label(int(channel), label)

    def Trigger_Config(self, trigger_channel = None, trigger_coupling = None, trigger_delay = None, trigger_position = None, trigger_level = None,
                       trigger_slope = None, trigger_mode = None):

        if trigger_channel != None:
            self.Set_Trigger_Channel(trigger_channel)

        if trigger_coupling != None:
            self.Set_Trigger_Coupling(trigger_coupling = trigger_coupling) #trigger_coupling: {"DC", "HFREJ", "LFREJ", "AC", "NOISEREJ"}
        
        if trigger_delay != None:
            self.Set_Trigger_Delay(trigger_delay)

        if trigger_position != None:
            self.Set_Trigger_Position(trigger_position)

        if trigger_level != None:
            self.Set_Trigger_Level(trigger_level)
        
        if trigger_slope != None:
            self.Set_Trigger_Slope(trigger_slope) #trigger_slope: {"Fall", "Rise", "Either"}
        
        if trigger_mode != None:
            self.Set_Trigger_Mode(trigger_mode) #{"AUTO", "NORM", "SINGLE", "STOP"}

    def Clear_Sweeps(self):
        if self.CMD_Clear_Sweeps:
            self.Instrument.write(self.CMD_Clear_Sweeps)    

    def Get_Channel_Attenuation(self, channel):
        if self.CMD_Get_Channel_Attenuation:
            return int(self.Instrument.query(self.CMD_Get_Channel_Attenuation % (channel)))

    def Get_Channel_Range(self, channel):
        if self.CMD_Get_Channel_Range:
            return float(self.Instrument.query(self.CMD_Get_Channel_Range % channel)[:-1])

    def Get_Measurement_Statistics_Value(self, index, statistic_method): #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        statistic = self.VAR_Get_Measurement_Statistics_Value.get(statistic_method)
        if statistic == None:
            return 0
        if self.Model_Name == "Lecroy_HDO4034A":
            if type(index) == int:
                if index >= 1 and index <= 8:
                    statistic_list = list(self.Instrument.query(self.CMD_Get_Measurement_Statistics_Value % (index)).replace("\n", "").split(",")[4:])
                    statistic_dict = {}
                    for i in range(len(statistic_list) >> 1):
                        if statistic_list[i * 2 + 1] == "UNDEF":
                            statistic_list[i * 2 + 1] = 0
                        statistic_dict[statistic_list[i * 2]] = float(statistic_list[i * 2 + 1])
                    return statistic_dict[statistic]
            else:
                statistic_list = list(self.Instrument.query(self.CMD_Get_Measurement_Statistics_Value % (index)).split(",")[2:])
                statistic_dict = {}
                for i in range(len(statistic_list)):
                    statistic_dict["P%d" % (i + 1)] = statistic_list[i]
                return statistic_dict[statistic]
        elif self.Model_Name == "Tektronix_MSO58" or self.Model_Name == "Tektronix_DPO7054C":
            if statistic == None:
                return 0
            return float(self.Instrument.query(self.CMD_Get_Measurement_Statistics_Value % (index, statistic)))

    def Get_Measurement_Value(self, index, measurement):
        if self.Model_Name == "Lecroy_HDO4034A":
            measurement_list = {
                "Amplitude"         : "AMPL",
                "Base"              : "BASE",
                "Maximum"           : "MAX",
                "Mean"              : "MEAN",
                "Minimum"           : "MIN",
                "Peak to peak"      : "PKPK",
                "RMS"               : "RMS",
                "Std dev"           : "SDEV",
                "Top"               : "TOP",
    
                "Delay"             : "DLY",
                "Dperiod@level"     : "DPLEV",
                "Dtime@level"       : "DTLEV",
                "Duty cycle"        : "DUTY",
                "Duty cycle@level"  : "DULEV",
                "Edge@level"        : "EDLEV",
                "Fall time"         : "FALL",
                "Fall 80-20%"       : "FALL82",
                "Frequency"         : "FREQ",
                "Period"            : "PER",
                "Phase"             : "Phase",
                "Rise time"         : "RISE",
                "Rise 20-80%"       : "RISE28",
                "Skew"              : "SKEW",
                "Time@level"        : "TLEV",
                "Width"             : "WID",
                "WidthN"            : "WIDN",
                "None"              : "NULL"
            }
            mnemonic = measurement_list.get(measurement)
            data_str = self.Instrument.query(self.CMD_Get_Measurement_Value % (index, mnemonic)).split(",")[1]
            try:
                return float(data_str)
            except:
                return data_str
        elif self.Model_Name == "Tektronix_MSO58":
            pass

    def Get_Probe_Degauss_State(self, channel):
        if self.CMD_Get_Probe_Degauss_State:
            degauss_state = self.Instrument.query(self.CMD_Get_Probe_Degauss_State % (channel))
            self.Instrument.query("*OPC?")
            if self.Model_Name == "Lecroy_HDO4034A":
                if degauss_state == "0\n":
                    return True
                else:
                    return False
            elif self.Model_Name == "Tektronix_MSO58" or self.Model_Name == "Tektronix_DPO7054C":
                if degauss_state == "PASS\n":
                    return True
                else:
                    return False

    def Get_Time_Scale(self):
        if self.CMD_Get_Time_Scale:
            self.Set_Cmd_Header("OFF")
            return float(self.Instrument.query(self.CMD_Get_Time_Scale))
        return 0

    def Get_Trigger_Channel(self):
        if self.Model_Name == "Lecroy_HDO4034A":
            if self.CMD_Get_Trigger_Type:
                get_trigger_type = self.Instrument.query(self.CMD_Get_Trigger_Type)
                get_trigger_type_array = get_trigger_type.split(",")
                for index, item in enumerate(get_trigger_type_array):
                    if item == "SR":
                        if get_trigger_type_array[index + 1].startswith("C"):
                            return int(get_trigger_type_array[index + 1][1])
        elif self.Model_Name == "Tektronix_MSO58" or self.Model_Name == "Tektronix_DPO7054C":
            if self.CMD_Get_Trigger_Channel:
                get_trigger_channel = self.Instrument.query(self.CMD_Get_Trigger_Channel)
                if get_trigger_channel.startswith("CH"):
                    return int(get_trigger_channel[2])
        return 0

    def Get_Trigger_Slope(self):
        if self.CMD_Get_Trigger_Slope:
            if self.Model_Name == "Lecroy_HDO4034A":
                channel = self.Get_Trigger_Channel()
                slope = self.Instrument.query(self.CMD_Get_Trigger_Slope % (channel))
                
            elif self.Model_Name == "Tektronix_MSO58" or self.Model_Name == "Tektronix_DPO7054C":
                slope = self.Instrument.query(self.CMD_Get_Trigger_Slope)
            
            if slope == "RIS\n" or slope == "POS\n":
                return "RISE"
            else:
                return "FALL"
    def Measurement_Clear(self):
        if self.Model_Name == "Lecroy_HDO4034A":
            if self.CMD_Measurement_Clear:
                self.Instrument.write(self.CMD_Measurement_Clear)
        elif self.Model_Name == "Tektronix_MSO58":
            meas_list = self.Instrument.query("MEASUrement:LIST?")[:-1].split(",")
            for meas in meas_list:
                self.Instrument.write('MEASUREMENT:DELETE "%s"' % meas)
        elif self.Model_Name == "Tektronix_DPO7054C":
            for index in range(1, 9):
                self.Measurement_Setting(index, measurement = "None")

    def Measurement_Delete(self, index):
        if self.CMD_Measurement_Delete:
            self.Instrument.write(self.CMD_Measurement_Delete % (index))

    def Measurement_Gate(self, index, gate_start = None, gate_stop = None):
        if self.Model_Name == "Lecroy_HDO4034A":
            if self.CMD_Measurement_Gate_Start and self.CMD_Measurement_Gate_Stop:
                if gate_start != None:
                    self.Instrument.write(self.CMD_Measurement_Gate_Start % (index, gate_start))
                
                if gate_stop != None:
                    self.Instrument.write(self.CMD_Measurement_Gate_Stop % (index, gate_stop))
        elif self.Model_Name == "Tektronix_MSO58" :
            if gate_start != None and gate_stop != None:
                self.Instrument.write("MEASUrement:MEAS%d:GATing:GLOBal OFF" % (index))
                self.Instrument.write("MEASUREMENT:MEAS%d:GATING TIMe" % (index))
            else:
                self.Instrument.write("MEASUREMENT:GATING None")
            get_time_scale = self.Get_Time_Scale()
            if gate_start != None:
                gate_start_time = (gate_start - 5) * get_time_scale
                self.Instrument.write(self.CMD_Measurement_Gate_Start % (index, gate_start_time))
            
            if gate_stop != None:
                gate_stop_time = (gate_stop - 5) * get_time_scale
                self.Instrument.write(self.CMD_Measurement_Gate_Stop % (index, gate_stop_time))
            
        elif self.Model_Name == "Tektronix_DPO7054C":
            get_time_scale = self.Get_Time_Scale()
            self.Instrument.write("CURSOR:FUNCTION VBArs")
            if gate_start != None:
                gate_start_time = (gate_start - 5) * get_time_scale
                self.Instrument.write(self.CMD_Measurement_Gate_Start % (gate_start_time))
            
            if gate_stop != None:
                gate_stop_time = (gate_stop - 5) * get_time_scale
                self.Instrument.write(self.CMD_Measurement_Gate_Stop % (gate_stop_time))

            self.Instrument.write("MEASUREMENT:GATING CURSor")

    def Measurement_Setting(self, index, measurement,
                            source1 = 1,
                            source2 = 1,
                            unit1 = "V",
                            unit2 = "V",
                            level1 = None,
                            level2 = None,
                            slope1 = None,
                            slope2 = None,
                            hysteresis1 = None,
                            hysteresis2 = None,
                            frequency = None,
                            signaltype = None,
                            outputin = None,
                            referencetype = None,
                            source1_rise_high = None,
                            source1_rise_low = None,
                            source1_fall_high = None,
                            source1_fall_mid = None,
                            source1_fall_low = None,
                            source2_rise_high = None,
                            source2_rise_low = None,
                            source2_fall_high = None,
                            source2_fall_mid = None,
                            source2_fall_low = None,
                            gate_start = None,
                            gate_stop = None):
        if self.CMD_Measurement_Setting:
            if self.Model_Name == "Lecroy_HDO4034A":
                if unit1 == "%" or unit1 == "PERC" or unit1 == "PCT":
                    unit1 = "PCT"
                else:
                    unit1 = "V"
                if unit2 == "%" or unit2 == "PERC" or unit2 == "PCT":
                    unit2 = "PCT"
                else:
                    unit2 = "V"
                if slope1 != None:
                    if slope1 == 0:
                        slope1 = "NEG"
                    else:
                        slope1 = "POS"
                if slope2 != None:
                    if slope2 == 0:
                        slope2 = "NEG"
                    else:
                        slope2 = "POS"
                measurement_list = {
                    "Amplitude"         : "AMPL, C%d" % (source1),
                    "Base"              : "BASE, C%d" % (source1),
                    "Maximum"           : "MAX, C%d" % (source1),
                    "Mean"              : "MEAN, C%d" % (source1),
                    "Minimum"           : "MIN, C%d" % (source1),
                    "Peak to peak"      : "PKPK, C%d" % (source1),
                    "RMS"               : "RMS, C%d" % (source1),
                    "Std dev"           : "SDEV, C%d" % (source1),
                    "Top"               : "TOP, C%d" % (source1),
        
                    #"Delay"             : "DLY, %s" %(source),
                    #"Dperiod@level"     : "DPLEV, %s" %(source),
                    "Delay"             : "DTLEV, C%d, %s, %s %s, %s DIV, C%d, %s, %s %s, %s DIV" % (source1, slope1, level1, unit1, hysteresis1, source2, slope2, level2, unit2, hysteresis2),
                    "Duty cycle"        : "DUTY, C%d" % (source1),
                    #"Duty cycle@level"  : "DULEV, %s" % (source),
                    #"Edge@level"        : "EDLEV, %s, %s, %s" % (source, slope, level),
                    "Fall time"         : "FALL, C%d" % (source1),
                    "Fall 80-20%"       : "FALL82, C%d" % (source1),
                    "Frequency"         : "FREQ, C%d" % (source1),
                    "Period"            : "PER, C%d" % (source1),
                    "Phase"             : "Phase, C%d" % (source1),
                    "Rise time"         : "RISE, C%d" % (source1),
                    "Rise 20-80%"       : "RISE28, C%d" % (source1),
                    "Skew"              : "SKEW, C%d, %s, %s%s, %s, %s, %s%s, %s, %s" % (source1, slope1, level1, unit1, source2, slope2, level2, unit2, hysteresis1, hysteresis2),
                    #"Time@level"        : "TLEV, %s, %s, %s, %s" % (source, slope, level, hysteresis),
                    "Width"             : "WID, C%d" % (source1),
                    "WidthN"            : "WIDN, C%d" % (source1),
                    "None"              : "NULL, C%d" % (source1)
                }
                mnemonic = measurement_list.get(measurement)
                if mnemonic != None:
                    self.Instrument.write(self.CMD_Measurement_Setting % (index, mnemonic))
            elif self.Model_Name == "Tektronix_MSO58":
                measurement_list = {
                    "Amplitude"         : "AMPlITUDE",
                    "Base"              : "BASE",
                    "Maximum"           : "MAXIMUM",
                    "Mean"              : "MEAN",
                    "Minimum"           : "MINIMUM",
                    "Peak to peak"      : "PK2Pk",
                    "RMS"               : "RMS",
                    #"Std dev"           : "",
                    "Top"               : "TOP",
        
                    "Delay"             : "DELAY",
                    #"Dperiod@level"     : "",
                    #"Dtime@level"       : "",
                    "Duty cycle"        : "PDUTY",
                    #"Duty cycle@level"  : "",
                    #"Edge@level"        : "",
                    "Fall time"         : "FALLTIME",
                    #"Fall 80-20%"       : "",
                    "Frequency"         : "FREQUENCY",
                    "Period"            : "PERIOD",
                    "Phase"             : "PHASE",
                    "Rise time"         : "RISETIME",
                    #"Rise 20-80%"       : "",
                    "Skew"              : "SKEW",
                    "Width"             : "PWIDTH",
                    "WidthN"            : "NWIDTTH",
                    "Rise slew rate"    : "RISESLEWRATE",
                    "Fall slew rate"    : "FALLSLEWRATE"
                    #"None"              : ""
                }
                mnemonic = measurement_list.get(measurement)
                
                self.Instrument.write(self.CMD_Measurement_Setting % (index))
                if mnemonic != None:
                    self.Instrument.write("MEASUrement:MEAS%d:TYPE %s" % (index, mnemonic))
                if source1 != None:
                    self.Instrument.write("MEASUrement:MEAS%d:SOUrce1 CH%d" % (index, source1))
                if source2 != None:
                    self.Instrument.write("MEASUrement:MEAS%d:SOUrce2 CH%d" % (index, source2))
                
                
                if unit1 == "%" or unit1 == "PERC" or unit1 == "PCT":
                    source1_method = "PERCent"
                    if source1_fall_high != None or source1_fall_mid != None or source1_fall_low != None:
                        self.Instrument.write("MEASUrement:MEAS%d:REFLevels1:PERCent:TYPE CUSTom" % (index))
                else:
                    source1_method = "ABSolute"
                    if source1_fall_high != None or source1_fall_mid != None or source1_fall_low != None:
                        self.Instrument.write("MEASUrement:MEAS%d:REFLevels1:ABSolute:TYPE UNIQUE" % (index))
                self.Instrument.write("MEASUREMENT:MEAS%d:REFLevels1:METHOD %s" % (index, source1_method))
                
                if unit2 == "%" or unit2 == "PERC" or unit2 == "PCT":
                    source2_method = "PERCent"
                    if source2_fall_high != None or source2_fall_mid != None or source2_fall_low != None:
                        self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:PERCent:TYPE CUSTom" % (index))
                else:
                    source2_method = "ABSolute"
                    if source2_fall_high != None or source2_fall_mid != None or source2_fall_low != None:
                        self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:ABSolute:TYPE UNIQUE" % (index))
                self.Instrument.write("MEASUREMENT:MEAS%d:REFLevels2:METHOD %s" % (index, source2_method))
                
                if slope1 != None:
                    if slope1 == 0:
                        self.Instrument.write("MEASUrement:MEAS%d:FROMedge %s" % (index, "FALL"))
                    else:
                        self.Instrument.write("MEASUrement:MEAS%d:FROMedge %s" % (index, "RISE"))
                if slope2 != None:
                    if slope2 == 0:
                        self.Instrument.write("MEASUREMENT:MEAS%d:TOedge %s" % (index, "FALL"))
                    else:
                        self.Instrument.write("MEASUREMENT:MEAS%d:TOedge %s" % (index, "RISE"))
                self.Instrument.write("MEASUrement:MEAS%d:GLOBalref 0" % (index))

                if source1_rise_high != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels1:%s:RISEHigh %f" % (index, source1_method, source1_rise_high))
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels1:%s:FALLHigh %f" % (index, source1_method, source1_rise_high))
                if level1 != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels1:%s:RISEMid %f" % (index, source1_method, level1))
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels1:%s:FALLMid %f" % (index, source1_method, level1))
                if source1_rise_low != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels1:%s:RISELow %f" % (index, source1_method, source1_rise_low))
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels1:%s:FALLLow %f" % (index, source1_method, source1_rise_low))
                if source1_fall_high != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels1:%s:FALLHigh %f" % (index, source1_method, source1_fall_high))
                if source1_fall_mid != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels1:%s:FALLMid %f" % (index, source1_method, source1_fall_mid))
                if source1_fall_low != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels1:%s:FALLLow %f" % (index, source1_method, source1_fall_low))

                if source2_rise_high != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:RISEHigh %f" % (index, source2_method, source2_rise_high))
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:FALLHigh %f" % (index, source2_method, source2_rise_high))
                if level2 != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:RISEMid %f" % (index, source2_method, level2))
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:FALLMid %f" % (index, source2_method, level2))
                if source2_rise_low != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:RISELow %f" % (index, source2_method, source2_rise_low))
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:FALLLow %f" % (index, source2_method, source2_rise_low))
                if source2_fall_high != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:FALLHigh %f" % (index, source2_method, source2_fall_high))
                if source2_fall_mid != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:FALLMid %f" % (index, source2_method, source2_fall_mid))
                if source2_fall_low != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:FALLLow %f" % (index, source2_method, source2_fall_low))
                self.Measurement_Gate(index, gate_start, gate_stop)

            elif self.Model_Name == "Tektronix_DPO7054C":
                measurement_list = {
                    "Amplitude"         : "AMPlITUDE",
                    "Base"              : "LOW",
                    "Maximum"           : "MAXIMUM",
                    "Mean"              : "MEAN",
                    "Minimum"           : "MINIMUM",
                    "Peak to peak"      : "PK2Pk",
                    "RMS"               : "RMS",
                    #"Std dev"           : "",
                    "Top"               : "HIGH",
        
                    "Delay"             : "DELAY",
                    #"Dperiod@level"     : "",
                    #"Dtime@level"       : "",
                    "Duty cycle"        : "PDUTY",
                    #"Duty cycle@level"  : "",
                    #"Edge@level"        : "",
                    "Fall time"         : "FALL",
                    #"Fall 80-20%"       : "",
                    "Frequency"         : "FREQUENCY",
                    "Period"            : "PERIOD",
                    "Phase"             : "PHASE",
                    "Rise time"         : "RISe",
                    #"Rise 20-80%"       : "",
                    "Width"             : "PWIDTH",
                    "WidthN"            : "NWIDTH",
                    "None"              : "UNDEFINED"
                }
                mnemonic = measurement_list.get(measurement)
                
                self.Instrument.write(self.CMD_Measurement_Setting % (index))
                if mnemonic != None:
                    self.Instrument.write("MEASUrement:MEAS%d:TYPE %s" % (index, mnemonic))
                if source1 != None:
                    self.Instrument.write("MEASUrement:MEAS%d:SOUrce1 CH%d" % (index, source1))
                if source2 != None:
                    self.Instrument.write("MEASUrement:MEAS%d:SOUrce2 CH%d" % (index, source2))
                
                
                if unit1 == "%" or unit1 == "PERC" or unit1 == "PCT":
                    source1_method = "PERCent"
                    #if source1_fall_high != None or source1_fall_mid != None or source1_fall_low != None:
                    #    self.Instrument.write("MEASUrement:MEAS%d:REFLevels1:PERCent:TYPE CUSTom" % (index))
                else:
                    source1_method = "ABSolute"
                    #if source1_fall_high != None or source1_fall_mid != None or source1_fall_low != None:
                    #    self.Instrument.write("MEASUrement:MEAS%d:REFLevels1:ABSolute:TYPE UNIQUE" % (index))
                self.Instrument.write("MEASUREMENT:MEAS%d:REFLevel:METHOD %s" % (index, source1_method))
                
                #if unit2 == "%" or unit2 == "PERC" or unit2 == "PCT":
                    #source2_method = "PERCent"
                    #if source2_fall_high != None or source2_fall_mid != None or source2_fall_low != None:
                    #    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:PERCent:TYPE CUSTom" % (index))
                #else:
                    #source2_method = "ABSolute"
                    #if source2_fall_high != None or source2_fall_mid != None or source2_fall_low != None:
                    #    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:ABSolute:TYPE UNIQUE" % (index))
                #self.Instrument.write("MEASUREMENT:MEAS%d:REFLevel:METHOD %s" % (index, source2_method))
                
                if slope1 != None:
                    if slope1 == 0:
                        self.Instrument.write("MEASUrement:MEAS%d:DELAY:EDGE1 %s" % (index, "FALL"))
                    else:
                        self.Instrument.write("MEASUrement:MEAS%d:DELAY:EDGE1 %s" % (index, "RISE"))
                if slope2 != None:
                    if slope2 == 0:
                        self.Instrument.write("MEASUREMENT:MEAS%d:DELAY:EDGE2 %s" % (index, "FALL"))
                    else:
                        self.Instrument.write("MEASUREMENT:MEAS%d:DELAY:EDGE2 %s" % (index, "RISE"))
                #self.Instrument.write("MEASUrement:MEAS%d:GLOBalref 0" % (index))

                if source1_rise_high != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevel:%s:HIGH %f" % (index, source1_method, source1_rise_high))
                if level1 != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevel:%s:MID %f" % (index, source1_method, level1))
                if source1_rise_low != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevel:%s:LOW %f" % (index, source1_method, source1_rise_low))
                #if source1_fall_high != None:
                #    self.Instrument.write("MEASUrement:MEAS%d:REFLevels1:%s:FALLHigh %f" % (index, source1_method, source1_fall_high))
                #if source1_fall_mid != None:
                #    self.Instrument.write("MEASUrement:MEAS%d:REFLevels1:%s:FALLMid %f" % (index, source1_method, source1_fall_mid))
                #if source1_fall_low != None:
                #    self.Instrument.write("MEASUrement:MEAS%d:REFLevels1:%s:FALLLow %f" % (index, source1_method, source1_fall_low))

                """
                if source2_rise_high != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:RISEHigh %f" % (index, source2_method, source2_rise_high))
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:FALLHigh %f" % (index, source2_method, source2_rise_high))
                if level2 != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:RISEMid %f" % (index, source2_method, level2))
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:FALLMid %f" % (index, source2_method, level2))
                if source2_rise_low != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:RISELow %f" % (index, source2_method, source2_rise_low))
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:FALLLow %f" % (index, source2_method, source2_rise_low))
                if source2_fall_high != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:FALLHigh %f" % (index, source2_method, source2_fall_high))
                if source2_fall_mid != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:FALLMid %f" % (index, source2_method, source2_fall_mid))
                if source2_fall_low != None:
                    self.Instrument.write("MEASUrement:MEAS%d:REFLevels2:%s:FALLLow %f" % (index, source2_method, source2_fall_low))
                """
            self.Measurement_Gate(index, gate_start, gate_stop)

    def Measurement_Statistics_State(self, channel = None, state = None):
        if self.Model_Name == "Lecroy_HDO4034A" and state != None:
            self.Instrument.write(self.CMD_Measurement_Statistics_State % (state))
        elif self.Model_Name == "Tektronix_MSO58" and channel != None and state != None:
            self.Instrument.write(self.CMD_Measurement_Statistics_State % (channel, state))
        elif self.Model_Name == "Tektronix_DPO7054C" and state != None:
            if state == True:
                self.Instrument.write(self.CMD_Measurement_Statistics_State % ("ALL"))
            else:
                self.Instrument.write(self.CMD_Measurement_Statistics_State % ("OFF"))

    def Print_Screen(self, folder, file_name):
        if self.Model_Name == "Lecroy_HDO4034A":
            self.Instrument.write(self.CMD_Print_Screen)
            screen_data = self.Instrument.read_raw()
            png_file = open("%s/%s.png" %(folder, file_name), 'wb+')
            png_file.write(screen_data)
            png_file.close()
        elif self.Model_Name == "Tektronix_MSO58":
            self.Instrument.write("SAVE:IMAGE 'temp.png'")
            self.Instrument.query('*OPC?')
            self.Instrument.write("FILESystem:READFile 'temp.png'")
            imgData = self.Instrument.read_raw()
            png_file = open("%s/%s.png" % (folder, file_name), "wb+")
            png_file.write(imgData)
            png_file.close()
            self.Instrument.write("FILESYSTEM:DELETE 'temp.png'")
        elif self.Model_Name == "Tektronix_DPO7054C":
            self.Instrument.write("HARDCopy:PORT FILE")
            self.Instrument.write("HARDCopy:VIEW FULLSCREEN")
            self.Instrument.write("HARDCopy:FILEName 'temp'")
            self.Instrument.write("HARDCopy STARt")
            path = (self.Instrument.query("HARDCOPY:FILENAME?"))[1:-2] + ".png"
            print(path)
            self.Instrument.write("FILESystem:READFile '%s'" % path)
            imgData = self.Instrument.read_raw()
            png_file = open("%s/%s.png" % (folder, file_name), "wb+")
            png_file.write(imgData)
            png_file.close()
            self.Instrument.write("FILESYSTEM:DELETE '%s'" % path)

    def Print_Setting(self, image_format, background_color, destination, area, port_name):
        if self.CMD_Print_Setting:
            self.Instrument.write(self.CMD_Print_Setting % (image_format, background_color, destination, area, port_name))

    def Set_Acquire_mode(self, mode): #mode: {"SAMple", "PEAKdetect", "HIRes", "AVErage", "ENVelope"}
        if self.CMD_Set_Acquire_mode:
            self.Instrument.write(self.CMD_Set_Acquire_mode % (mode))

    def Set_Axis_Labels_State(self, state):
        if self.CMD_Set_Axis_Labels_State:
            if state:
                self.Instrument.write(self.CMD_Set_Axis_Labels_State % (1))
            else:
                self.Instrument.write(self.CMD_Set_Axis_Labels_State % (0))

    def Set_Channel_Attenuation(self, channel, attenuation):
        if self.CMD_Set_Channel_Attenuation:
            self.Instrument.write(self.CMD_Set_Channel_Attenuation % (channel, attenuation))

    def Set_Channel_Bandwidth_Limit(self, channel, bandwidth): #Unit: MHz
        if self.CMD_Set_Channel_Bandwidth_Limit:
            if self.Model_Name == "Lecroy_HDO4034A":
                if bandwidth > 20:
                    bandwidth = 20
            if self.Model_Name == "Tektronix_MSO58" or self.Model_Name == "Tektronix_DPO7054C":
                if bandwidth > 350:
                    bandwidth = 350
                bandwidth = bandwidth * 1000000
            self.Instrument.write(self.CMD_Set_Channel_Bandwidth_Limit % (channel, bandwidth))

    def Set_Channel_Coupling(self, channel, channel_coupling): #channel_coupling: {"AC", "DC", "DC50", "DCREJ", "GND", "IAC", "IDC"}
        coupling = self.VAR_Set_Channel_Coupling.get(channel_coupling)
        if self.CMD_Set_Channel_Coupling and coupling:
            self.Instrument.write(self.CMD_Set_Channel_Coupling % (channel, coupling))

    def Set_Channel_Label(self, channel, text):
        if self.CMD_Set_Channel_Label:
            try:
                self.Instrument.write(self.CMD_Set_Channel_Label % (channel, text))
            except:
                self.Instrument.write(self.CMD_Set_Channel_Label % (channel, ""))

    def Set_Channel_Label_State(self, channel, state):
        if self.CMD_Set_Channel_Label_State:
            self.Instrument.write(self.CMD_Set_Channel_Label_State % (channel, state))

    def Set_Channel_Noise_Filter(self, channel, noise_filter):
        if self.CMD_Set_Channel_Noise_Filter:
            if noise_filter >= 0 and noise_filter <= 3:
                noise_filter = int(noise_filter * 2)
                self.Instrument.write(self.CMD_Set_Channel_Noise_Filter % (channel, noise_filter))

    def Set_Channel_Range(self, channel, channel_range):
        if self.CMD_Set_Channel_Range:
            self.Instrument.write(self.CMD_Set_Channel_Range % (channel, channel_range))
    
    def Set_Channel_Range_Mode(self, channel, range_mode):
        if self.CMD_Set_Channel_Range_Mode:
            self.Instrument.write(self.CMD_Set_Channel_Range_Mode % (channel, range_mode))

    def Set_Channel_Trace_State(self, channel, state):  
        if self.CMD_Set_Channel_Trace_State_On and self.CMD_Set_Channel_Trace_State_Off:
            if state == True or state == "ON":
                self.Instrument.write(self.CMD_Set_Channel_Trace_State_On % (channel))
            else:
                self.Instrument.write(self.CMD_Set_Channel_Trace_State_Off % (channel))

    def Set_Channel_Voltage_Offset(self, channel, offset):
        if self.CMD_Set_Channel_Voltage_Offset:
            self.Instrument.write(self.CMD_Set_Channel_Voltage_Offset % (channel, offset))

    def Set_Channel_Voltage_Position(self, channel, position):
#        if self.CMD_Set_Channel_Voltage_Position:
#            self.Instrument.write(self.CMD_Set_Channel_Voltage_Position % (channel, position))

        if self.Model_Name == "Lecroy_HDO4034A":
            self.Set_Cmd_Header("OFF")
            current_scale = float(self.Instrument.query("C%d:VOLT_DIV?" % (channel)))
            set_scale = (position) * current_scale
            if position == 0:
                set_scale = 0
            self.Set_Channel_Voltage_Offset(channel, set_scale)
        elif self.Model_Name == "Tektronix_MSO58" or self.Model_Name == "Tektronix_DPO7054C":
            self.Instrument.write(self.CMD_Set_Channel_Voltage_Position % (channel, float(position)))

    def Set_Channel_Voltage_Scale(self, channel, div):
        if self.CMD_Set_Channel_Voltage_Scale:
            self.Instrument.write(self.CMD_Set_Channel_Voltage_Scale % (channel, div))

    def Set_Cmd_Header(self, mode):
        if self.Model_Name == "Lecroy_HDO4034A":
            if self.CMD_Set_Cmd_Header:
                self.Instrument.write(self.CMD_Set_Cmd_Header % (mode))
        elif self.Model_Name == "Tektronix_MSO58" or self.Model_Name == "Tektronix_DPO7054C":
            if self.CMD_Set_Cmd_Header and self.CMD_Set_Cmd_Verbose:
                if mode == "LONG":
                    if self.CMD_Set_Cmd_Header:
                        self.Instrument.write(self.CMD_Set_Cmd_Header % ("ON"))
                    if self.CMD_Set_Cmd_Verbose:
                        self.Instrument.write(self.CMD_Set_Cmd_Verbose % ("ON"))
                elif mode == "SHORT":
                     if self.CMD_Set_Cmd_Header:
                         self.Instrument.write(self.CMD_Set_Cmd_Header % ("ON"))
                     if self.CMD_Set_Cmd_Verbose:
                         self.Instrument.write(self.CMD_Set_Cmd_Verbose % ("OFF"))
                elif mode == "OFF":
                    if self.CMD_Set_Cmd_Header:
                        self.Instrument.write(self.CMD_Set_Cmd_Header % ("OFF"))
                    if self.CMD_Set_Cmd_Verbose:
                        self.Instrument.write(self.CMD_Set_Cmd_Verbose % ("OFF"))

    def Set_Display_Grid(self, display_grid): #display_grid: {"Overlay", "Stacked"}
        grid = self.VAR_Set_Display_Grid.get(display_grid)
        if self.CMD_Set_Display_Grid and grid:
            self.Instrument.write(self.CMD_Set_Display_Grid % (grid))

    def Set_Display_State(self, state):
        if self.CMD_Set_Display_State_On and self.CMD_Set_Display_State_Off:
            if state:
                self.Instrument.write(self.CMD_Set_Display_State_On)
            else:
                self.Instrument.write(self.CMD_Set_Display_State_Off)

    def Set_Probe_Degauss(self, channel):
        if self.CMD_Set_Probe_Degauss:
            self.Instrument.write(self.CMD_Set_Probe_Degauss % (channel))
            self.Instrument.query("*OPC?")
            self.Instrument.query("*OPC?")

    def Set_Time_Scale(self, div):
        if self.CMD_Set_Time_Scale:
            self.Instrument.write(self.CMD_Set_Time_Scale % (div))

    def Set_Trigger_Channel(self, channel):
        trigger_type = "EDGE" #Default: EDGE
        if self.CMD_Set_Trigger_Type:
            if self.Model_Name == "Lecroy_HDO4034A":
                self.Instrument.write(self.CMD_Set_Trigger_Type % (trigger_type, channel))
            elif self.Model_Name == "Tektronix_MSO58" or self.Model_Name == "Tektronix_DPO7054C":
                if self.CMD_Set_Trigger_Channel:
                    self.Instrument.write(self.CMD_Set_Trigger_Channel % (channel))
                self.Instrument.write(self.CMD_Set_Trigger_Type % (trigger_type))

    def Set_Trigger_Coupling(self, trigger_coupling): #trigger_coupling: {"DC", "HFREJ", "LFREJ", "AC", "NOISEREJ"}
        coupling = self.VAR_Set_Trigger_Coupling.get(trigger_coupling)
        if self.CMD_Set_Trigger_Coupling and coupling != None:
            if self.Model_Name == "Lecroy_HDO4034A":
                channel = self.Get_Trigger_Channel()
                self.Instrument.write(self.CMD_Set_Trigger_Coupling % (channel, coupling))
            elif self.Model_Name == "Tektronix_MSO58" or self.Model_Name == "Tektronix_DPO7054C":
                self.Instrument.write(self.CMD_Set_Trigger_Coupling % (coupling))

    def Set_Trigger_Delay(self, delay):
        if self.CMD_Set_Trigger_Delay:
            if self.Model_Name == "Tektronix_MSO58":
                self.Instrument.write("HORizontal:DELay:MODe ON")
            self.Instrument.write(self.CMD_Set_Trigger_Delay % (delay))

    def Set_Trigger_Level(self, level):
        if self.CMD_Set_Trigger_Level:
            if level == "AUTO":
                if self.Model_Name == "Lecroy_HDO4034A":
                    self.Instrument.write("vbs app.Acquisition.Trigger.Edge.FindLevel()")
                elif self.Model_Name == "Tektronix_MSO58":
                    self.Instrument.write("TRIGger:A SETLEVEL")
            else:
                channel = self.Get_Trigger_Channel()
                self.Instrument.write(self.CMD_Set_Trigger_Level % (channel, level))

    def Set_Trigger_Mode(self, mode):  #{"AUTO", "NORM", "SINGLE", "STOP"}
        if self.CMD_Set_Trigger_Mode:
            if self.Model_Name == "Lecroy_HDO4034A":
                self.Instrument.write(self.CMD_Set_Trigger_Mode % (mode))
            elif self.Model_Name == "Tektronix_MSO58" or self.Model_Name == "Tektronix_DPO7054C":
                if mode == "AUTO" or mode == "NORM":
                    self.Instrument.write("ACQuire:STOPAfter RUNSTOP")
                    self.Instrument.write("ACQUIRE:STATE 1")
                    self.Instrument.write(self.CMD_Set_Trigger_Mode % (mode))
                elif mode == "SINGLE":
                    self.Instrument.write("ACQuire:STOPAfter SEQuence")
                    self.Instrument.write("ACQUIRE:STATE 1")
                    self.Instrument.write(self.CMD_Set_Trigger_Mode % ("NORM"))
                elif mode == "STOP":
                    self.Instrument.write("ACQuire:STOPAfter RUNSTOP")
                    self.Instrument.write("ACQUIRE:STATE 0")

    def Set_Trigger_Position(self, position):
        if self.Model_Name == "Lecroy_HDO4034A":
            self.Set_Cmd_Header("OFF")
            current_scale = float(self.Instrument.query("TIME_DIV?"))
            trigger_delay = (position - 50) * current_scale / 10
            self.Set_Trigger_Delay(trigger_delay)
        if self.Model_Name == "Tektronix_MSO58":
            self.Instrument.write("HORizontal:DELay:MODe OFF")
            self.Instrument.write(self.CMD_Set_Trigger_Position % (position))

    def Set_Trigger_Slope(self, trigger_slope): #trigger_slope: {"Fall", "Rise", "Either"}
        slope = self.VAR_Set_Trigger_Slope.get(trigger_slope.capitalize())
        if self.CMD_Set_Trigger_Slope and slope:
            if self.Model_Name == "Lecroy_HDO4034A":
                channel = self.Get_Trigger_Channel()
                self.Instrument.write(self.CMD_Set_Trigger_Slope % (channel, slope))
            elif self.Model_Name == "Tektronix_MSO58" or self.Model_Name == "Tektronix_DPO7054C":
                self.Instrument.write(self.CMD_Set_Trigger_Slope % (slope))

    def Close(self):
        global INSTR_CNT
        self.Instrument.close()
        INSTR_CNT -= 1
        if INSTR_CNT == 0:
            self.Resource_Manager.close()

class Source_Meter():

    def __init__(self, instrument_address=None):
        global INSTR_CNT
        self.State = False
        self.Resource_Manager = visa.ResourceManager()
        if instrument_address != None:
            self.Instrument = self.Resource_Manager.open_resource(instrument_address)
            INSTR_CNT += 1

    def Reset(self):
        self.Instrument.write("*RST")

    def Config(self, source_mode = None, source_voltage_limit = None, source_voltage_range = None, source_voltage = None,
               sense_current_limit = None, sense_current_range = None, remote_state = None, beeper_state = False):
        if source_mode != None:
            self.Set_Source_Mode(source_mode) #{"VOLTage", "CURRent", "MEMory"}
        
        if source_voltage_limit != None:
            self.Set_Source_Voltage_Limit(source_voltage_limit)

        if source_voltage_range != None:
            self.Set_Source_Voltage_Range(source_voltage_range)

        if source_voltage != None:
            self.Set_Source_Voltage_Amplitude(source_voltage)

        if sense_current_limit != None:
            self.Set_Sense_Current_Limit(sense_current_limit)

        if sense_current_range != None:
            self.Set_Sense_Current_Range(sense_current_range)

        if remote_state != None:
            self.Set_Remote_Sense_State(remote_state)
        
        if beeper_state != None:
            self.Set_Beeper_State(beeper_state)
            
    def Measurement_Config(self, function = None, average_state = None, average_type = None, average_count = None, concurrent_state = None):
        if function != None:
            self.Set_Measurement_State(function, True) #{"VOLTage", "CURRent"}

        if average_state != None and average_type:
            self.Set_Sense_Average(average_state, average_type, average_count) #average_type: {"REPEAT", "MOVING"}

        if concurrent_state != None:
            self.Set_Concurrent_Measurement_State(concurrent_state)

    def Measure(self, item): #{"Voltage", "Current"}
        if item == "Voltage":
            return self.Measure_Voltage()

        elif item == "Current":
            return self.Measure_Current()

    def Get_Output_State(self):
        if self.CMD_Get_Output_State:
            state = self.Instrument.query(self.CMD_Get_Output_State)
            if state == "1":
                return True
            else:
                return False

    def Initiate_Measurement(self):
        if self.CMD_Initiate_Measurement:
            self.Instrument.write(self.CMD_Initiate_Measurement)

    def Measure_Voltage(self):
        if self.Model_Nmae == "Keithley_2400":
            return float(self.Instrument.query(":FETCH?").split(",")[0])
        elif self.Model_Nmae == "Keysight_E3632A":
            return float(self.Instrument.query("MEASure:VOLTage?"))

    def Measure_Current(self):
        if self.Model_Nmae == "Keithley_2400":
            return float(self.Instrument.query(":FETCH?").split(",")[1])
        elif self.Model_Nmae == "Keysight_E3632A":
            return float(self.Instrument.query("MEASure:CURRent?"))

    def Set_All_Measurement_State(self, state):
        if self.CMD_Set_All_Measurement_On and self.CMD_Set_All_Measurement_Off:
            if state:
                self.Instrument.write(self.CMD_Set_All_Measurement_On)
            else:
                self.Instrument.write(self.CMD_Set_All_Measurement_Off)

    def Set_Beeper_State(self, state):
        if self.CMD_Set_Beeper_State:
            if state == True:
                self.Instrument.write(self.CMD_Set_Beeper_State % (1))
            else:
                self.Instrument.write(self.CMD_Set_Beeper_State % (0))

    def Set_Arm_Count(self, count):
        if self.CMD_Set_Arm_Count_Infinite and self.CMD_Set_Arm_Count:
            if count == 0:
                self.Instrument.write(self.CMD_Set_Arm_Count_Infinite)
            else:
                self.Instrument.write(self.CMD_Set_Arm_Count % (count))

    def Set_Concurrent_Measurement_State(self, state):
        if self.CMD_Set_Concurrent_Measurement_State_On and self.CMD_Set_Concurrent_Measurement_State_Off:
            if state:
                self.Instrument.write(self.CMD_Set_Concurrent_Measurement_State_On)
            else:
                self.Instrument.write(self.CMD_Set_Concurrent_Measurement_State_Off)

    def Set_Idle(self):
        if self.CMD_Set_Idle:
            self.Instrument.write(self.CMD_Set_Idle)

    def Set_Measurement_State(self, function, state): #{"VOLTage", "CURRent"}
        if self.CMD_Set_Measurement_On and self.CMD_Set_Measurement_Off:
            if state:
                self.Instrument.write(self.CMD_Set_Measurement_On % (function))
            else:
                self.Instrument.write(self.CMD_Set_Measurement_Off % (function))

    def Set_Output_State(self, state):
        if self.CMD_Set_Output_State_On and self.CMD_Set_Output_State_Off:
            if state:
                self.Instrument.write(self.CMD_Set_Output_State_On)
            else:
                self.Instrument.write(self.CMD_Set_Output_State_Off)
            self.State = state

    def Set_Remote_Sense_State(self, state):
        if self.CMD_Set_Remote_Sense_On and self.CMD_Set_Remote_Sense_Off:
            if state:
                self.Instrument.write(self.CMD_Set_Remote_Sense_On)
            else:
                self.Instrument.write(self.CMD_Set_Remote_Sense_Off)

    def Set_Sense_Average(self, state, average_type = None, count = None): #average_type: {"REPEAT", "MOVING"}
        if self.CMD_Set_Sense_Averaging_State and self.CMD_Set_Sense_Averaging_Type and self.CMD_Set_Sense_Averaging_Count:
            if state:
                self.Instrument.write(self.CMD_Set_Sense_Averaging_State % (1))
                if average_type != None:
                    self.Instrument.write(self.CMD_Set_Sense_Averaging_Type % (average_type))
                if count != None:
                    self.Instrument.write(self.CMD_Set_Sense_Averaging_Count % (count))
            else:
                self.Instrument.write(self.CMD_Set_Sense_Averaging_State % (0))

    def Set_Sense_Current_Limit(self, current_limit):
        if self.CMD_Set_Sense_Current_Limit:
            self.Instrument.write(self.CMD_Set_Sense_Current_Limit % (current_limit))

    def Set_Sense_Current_Range(self, current_range):
        if self.CMD_Set_Sense_Current_Range_Auto_State and self.CMD_Set_Sense_Current_Range:
            if current_range == "AUTO":
                self.Instrument.write(self.CMD_Set_Sense_Current_Range_Auto_State % (1))
            else:
                self.Instrument.write(self.CMD_Set_Sense_Current_Range % (current_range))

    def Set_Sense_Voltage_Limit(self, voltage_limit):
        if self.CMD_Set_Sense_Voltage_Limit:
            self.Instrument.write(self.CMD_Set_Sense_Voltage_Limit % (voltage_limit))

    def Set_Sense_Voltage_Range(self, voltage_range):
        if self.CMD_Set_Sense_Voltage_Range_Auto_State and self.CMD_Set_Sense_Voltage_Range:
            if voltage_range == "AUTO":
                self.Instrument.write(self.CMD_Set_Sense_Voltage_Range_Auto_State % (1))
            else:
                self.Instrument.write(self.CMD_Set_Sense_Voltage_Range % (voltage_range))

    def Set_Source_Current_Amplitude(self, current):
        if self.CMD_Set_Source_Current_Amplitude:
            self.Instrument.write(self.CMD_Set_Source_Current_Amplitude % (current))

    def Set_Source_Current_Range(self, current_range):
        if self.CMD_Set_Source_Current_Range:
            self.Instrument.write(self.CMD_Set_Source_Current_Range % (current_range))

    def Set_Source_Mode(self, mode): #{"VOLTage", "CURRent", "MEMory"}
        if self.CMD_Set_Source_Mode:
            self.Instrument.write(self.CMD_Set_Source_Mode % (mode))

    def Set_Source_Voltage_Amplitude(self, voltage):
        if self.CMD_Set_Source_Voltage_Amplitude:
            self.Instrument.write(self.CMD_Set_Source_Voltage_Amplitude % (voltage))

    def Set_Source_Voltage_Limit(self, voltage_limit):
        if self.CMD_Set_Source_Voltage_Limit:
            self.Instrument.write(self.CMD_Set_Source_Voltage_Limit % (voltage_limit))

    def Set_Source_Voltage_Range(self, voltage_range):
        if self.CMD_Set_Source_Voltage_Range:
            self.Instrument.write(self.CMD_Set_Source_Voltage_Range % (voltage_range))

    def Close(self):
        global INSTR_CNT
        self.Instrument.close()
        INSTR_CNT -= 1
        if INSTR_CNT == 0:
            self.Resource_Manager.close()

class Load_Meter():

    def __init__(self, instrument_address=None):
        global INSTR_CNT
        self.State = False
        self.Resource_Manager = visa.ResourceManager()
        if instrument_address != None:
            self.Instrument = self.Resource_Manager.open_resource(instrument_address)
            INSTR_CNT += 1

    def Reset(self):
        self.Instrument.write("*RST")

    def Config(self, source_mode = None, source_voltage_limit = None, source_voltage_range = None, source_voltage = None,
               source_current_limit = None, source_current_range = None, source_current = None,
               sense_voltage_limit = None, sense_voltage_range = None, sense_current_limit = None, sense_current_range = None, remote_state = None, beeper_state = False):
        if source_mode != None:
            self.Set_Source_Mode(source_mode) #{"VOLTage", "CURRent", "MEMory"}
        
        if source_voltage_limit != None:
            self.Set_Source_Voltage_Limit(source_voltage_limit)

        if source_voltage_range != None:
            self.Set_Source_Voltage_Range(source_voltage_range)

        if source_voltage != None:
            self.Set_Source_Voltage_Amplitude(source_voltage)

        if source_current_limit != None:
            self.Set_Source_Current_Limit(source_current_limit)

        if source_current_range != None:
            self.Set_Source_Current_Range(source_current_range)

        if source_current != None:
            self.Set_Source_Current_Amplitude(source_current)

        if sense_voltage_limit != None:
            self.Set_Sense_Voltage_Limit(sense_voltage_limit)
        
        if sense_voltage_range != None:
            self.Set_Sense_Voltage_Range(sense_voltage_range)
        
        if sense_current_limit != None:
            self.Set_Sense_Current_Limit(sense_current_limit)

        if sense_current_range != None:
            self.Set_Sense_Current_Range(sense_current_range)

        if remote_state != None:
            self.Set_Remote_Sense_State(remote_state)
        
        if beeper_state != None:
            self.Set_Beeper_State(beeper_state)
            
    def Measurement_Config(self, function = None, average_state = None, average_type = None, average_count = None, concurrent_state = None):
        if function != None:
            self.Set_Measurement_State(function, True) #{"VOLTage", "CURRent"}

        if average_state != None and average_type:
            self.Set_Sense_Average(average_state, average_type, average_count) #average_type: {"REPEAT", "MOVING"}

        if concurrent_state != None:
            self.Set_Concurrent_Measurement_State(concurrent_state)

    def Measure(self, item): #{"Voltage", "Current"}
        if item == "Voltage":
            return self.Measure_Voltage()

        elif item == "Current":
            return self.Measure_Current()

    def Get_Output_State(self):
        if self.CMD_Get_Output_State:
            state = self.Instrument.query(self.CMD_Get_Output_State)
            if state == "1":
                return True
            else:
                return False

    def Initiate_Measurement(self):
        if self.CMD_Initiate_Measurement:
            self.Instrument.write(self.CMD_Initiate_Measurement)

    def Measure_Voltage(self):
        return float(self.Instrument.query(":FETCH?")[:-1].split(",")[0])

    def Measure_Current(self):
        return float(self.Instrument.query(":FETCH?")[:-1].split(",")[1])

    def Set_All_Measurement_State(self, state):
        if self.CMD_Set_All_Measurement_On and self.CMD_Set_All_Measurement_Off:
            if state:
                self.Instrument.write(self.CMD_Set_All_Measurement_On)
            else:
                self.Instrument.write(self.CMD_Set_All_Measurement_Off)

    def Set_Arm_Count(self, count):
        if self.CMD_Set_Arm_Count_Infinite and self.CMD_Set_Arm_Count:
            if count == 0:
                self.Instrument.write(self.CMD_Set_Arm_Count_Infinite)
            else:
                self.Instrument.write(self.CMD_Set_Arm_Count % (count))

    def Set_Beeper_State(self, state):
        if self.CMD_Set_Beeper_State:
            if state == True:
                self.Instrument.write(self.CMD_Set_Beeper_State % (1))
            else:
                self.Instrument.write(self.CMD_Set_Beeper_State % (0))

    def Set_Concurrent_Measurement_State(self, state):
        if self.CMD_Set_Concurrent_Measurement_State_On and self.CMD_Set_Concurrent_Measurement_State_Off:
            if state:
                self.Instrument.write(self.CMD_Set_Concurrent_Measurement_State_On)
            else:
                self.Instrument.write(self.CMD_Set_Concurrent_Measurement_State_Off)

    def Set_Idle(self):
        if self.CMD_Set_Idle:
            self.Instrument.write(self.CMD_Set_Idle)

    def Set_Measurement_State(self, function, state): #{"VOLTage", "CURRent"}
        if self.CMD_Set_Measurement_On and self.CMD_Set_Measurement_Off:
            if state:
                self.Instrument.write(self.CMD_Set_Measurement_On % (function))
            else:
                self.Instrument.write(self.CMD_Set_Measurement_Off % (function))

    def Set_Output_State(self, state):
        if self.CMD_Set_Output_State_On and self.CMD_Set_Output_State_Off:
            if state:
                self.Instrument.write(self.CMD_Set_Output_State_On)
            else:
                self.Instrument.write(self.CMD_Set_Output_State_Off)
            self.State = state

    def Set_Remote_Sense_State(self, state):
        if self.CMD_Set_Remote_Sense_On and self.CMD_Set_Remote_Sense_Off:
            if state:
                self.Instrument.write(self.CMD_Set_Remote_Sense_On)
            else:
                self.Instrument.write(self.CMD_Set_Remote_Sense_Off)

    def Set_Sense_Average(self, state, average_type = None, count = None): #average_type: {"REPEAT", "MOVING"}
        if self.CMD_Set_Sense_Averaging_State and self.CMD_Set_Sense_Averaging_Type and self.CMD_Set_Sense_Averaging_Count:
            if state:
                self.Instrument.write(self.CMD_Set_Sense_Averaging_State % (1))
                if average_type != None:
                    self.Instrument.write(self.CMD_Set_Sense_Averaging_Type % (average_type))
                if count != None:
                    self.Instrument.write(self.CMD_Set_Sense_Averaging_Count % (count))
            else:
                self.Instrument.write(self.CMD_Set_Sense_Averaging_State % (0))

    def Set_Sense_Current_Limit(self, current_limit):
        if self.CMD_Set_Sense_Current_Limit:
            self.Instrument.write(self.CMD_Set_Sense_Current_Limit % (current_limit))

    def Set_Sense_Current_Range(self, current_range):
        if self.CMD_Set_Sense_Current_Range_Auto_State and self.CMD_Set_Sense_Current_Range:
            if current_range == "AUTO":
                self.Instrument.write(self.CMD_Set_Sense_Current_Range_Auto_State % (1))
            else:
                self.Instrument.write(self.CMD_Set_Sense_Current_Range % (current_range))

    def Set_Sense_Voltage_Limit(self, voltage_limit):
        if self.CMD_Set_Sense_Voltage_Limit:
            self.Instrument.write(self.CMD_Set_Sense_Voltage_Limit % (voltage_limit))

    def Set_Sense_Voltage_Range(self, voltage_range):
        if self.CMD_Set_Sense_Voltage_Range_Auto_State and self.CMD_Set_Sense_Voltage_Range:
            if voltage_range == "AUTO":
                self.Instrument.write(self.CMD_Set_Sense_Voltage_Range_Auto_State % (1))
            else:
                self.Instrument.write(self.CMD_Set_Sense_Voltage_Range % (voltage_range))

    def Set_Source_Current_Amplitude(self, current):
        if self.CMD_Set_Source_Current_Amplitude:
            self.Instrument.write(self.CMD_Set_Source_Current_Amplitude % (current))

    def Set_Source_Current_Limit(self, current_limit):
        if self.CMD_Set_Source_Current_Limit:
            self.Instrument.write(self.CMD_Set_Source_Current_Limit % (current_limit))

    def Set_Source_Current_Range(self, current_range):
        if self.CMD_Set_Source_Current_Range:
            self.Instrument.write(self.CMD_Set_Source_Current_Range % (current_range))

    def Set_Source_Mode(self, mode): #{"VOLTage", "CURRent", "MEMory"}
        if self.CMD_Set_Source_Mode:
            self.Instrument.write(self.CMD_Set_Source_Mode % (mode))

    def Set_Source_Voltage_Amplitude(self, voltage):
        if self.CMD_Set_Source_Voltage_Amplitude:
            self.Instrument.write(self.CMD_Set_Source_Voltage_Amplitude % (voltage))

    def Set_Source_Voltage_Limit(self, voltage_limit):
        if self.CMD_Set_Source_Voltage_Limit:
            self.Instrument.write(self.CMD_Set_Source_Voltage_Limit % (voltage_limit))

    def Set_Source_Voltage_Range(self, voltage_range):
        if self.CMD_Set_Source_Voltage_Range:
            self.Instrument.write(self.CMD_Set_Source_Voltage_Range % (voltage_range))

    def Close(self):
        global INSTR_CNT
        self.Instrument.close()
        INSTR_CNT -= 1
        if INSTR_CNT == 0:
            self.Resource_Manager.close()

class Enable_Control():

    def __init__(self, instrument_address=None):
        global INSTR_CNT
        self.State = False
        self.Resource_Manager = visa.ResourceManager()
        if instrument_address != None:
            self.Instrument = self.Resource_Manager.open_resource(instrument_address)
            INSTR_CNT += 1

    def Reset(self):
        self.Voltage = 0
        self.Instrument.write("*RST")
        if self.Model_Name == "Keithley_2400":
            self.Instrument.write(":SOURce:FUNCtion:MODE VOLTage")
        elif self.Model_Name == "AFG31000_Series":
            self.Instrument.write("OUTPut1:IMPedance INFinity")
            self.Instrument.write("SOURce1:BURSt ON")
            self.Instrument.write("SOURce1:BURSt:NCYCles 1")
            self.Instrument.write("SOURce1:FUNCtion:SHAPe Pulse")
            self.Instrument.write("SOURce1:PULSe:PERiod 0.1")
            self.Instrument.write("SOURce1:VOLTage:LEVel:IMMediate:LOW 0V")
            self.Instrument.write("TRIGger:SOURce EXTernal")
            

    def Config(self, source_voltage_limit = None, source_voltage_range = None, voltage = None,
               sense_current_limit = None, sense_current_range = None, beeper_state = False):
        if source_voltage_limit != None:
            self.Set_Source_Voltage_Limit(source_voltage_limit)

        if source_voltage_range != None:
            self.Set_Source_Voltage_Range(source_voltage_range)

        if voltage != None:
            self.Set_Voltage(voltage)

        if sense_current_limit != None:
            self.Set_Sense_Current_Limit(sense_current_limit)

        if sense_current_range != None:
            self.Set_Sense_Current_Range(sense_current_range)
        
        if beeper_state != None:
            self.Set_Beeper_State(beeper_state)

    def Get_Output_State(self):
        if self.CMD_Get_Output_State:
            state = self.Instrument.query(self.CMD_Get_Output_State)
            if state == "1":
                return True
            else:
                return False

    def Initiate_Measurement(self):
        if self.CMD_Initiate_Measurement:
            self.Instrument.write(self.CMD_Initiate_Measurement)

    def Set_Arm_Count(self, count):
        if self.CMD_Set_Arm_Count_Infinite and self.CMD_Set_Arm_Count:
            if count == 0:
                self.Instrument.write(self.CMD_Set_Arm_Count_Infinite)
            else:
                self.Instrument.write(self.CMD_Set_Arm_Count % (count))

    def Set_Beeper_State(self, state):
        if self.CMD_Set_Beeper_State:
            if state == True:
                self.Instrument.write(self.CMD_Set_Beeper_State % (1))
            else:
                self.Instrument.write(self.CMD_Set_Beeper_State % (0))

    def Set_Idle(self):
        if self.CMD_Set_Idle:
            self.Instrument.write(self.CMD_Set_Idle)

    def Set_Output_State(self, state):
        if self.CMD_Output_State_On and self.CMD_Output_State_Off:
            if state:
                self.Instrument.write(self.CMD_Output_State_On)
            else:
                self.Instrument.write(self.CMD_Output_State_Off)
            self.State = state
            #self.State = self.Get_Output_State()
    
    def Set_Output_Level(self, level, high_voltage = 5, low_voltage = 0):
        if self.Model_Name == "AFG31000_Series":
            self.Set_Voltage(high_voltage)
            if level == "Low":
                self.Instrument.write("SOURce1:BURSt:IDLE START")
            else:
                self.Instrument.write("SOURce1:BURSt:IDLE END")
        else:
            if level == "Low":
                self.Set_Voltage(0)
            else:
                self.Set_Voltage(high_voltage)

    def Set_Sense_Current_Limit(self, current_limit):
        if self.CMD_Set_Sense_Current_Limit:
            self.Instrument.write(self.CMD_Set_Sense_Current_Limit % (current_limit))

    def Set_Sense_Current_Range(self, current_range):
        if self.CMD_Set_Sense_Current_Range:
            self.Instrument.write(self.CMD_Set_Sense_Current_Range % (current_range))

    def Set_Source_Voltage_Limit(self, voltage_limit):
        if self.CMD_Set_Source_Voltage_Limit:
            self.Instrument.write(self.CMD_Set_Source_Voltage_Limit % (voltage_limit))

    def Set_Source_Voltage_Range(self, voltage_range):
        if self.CMD_Set_Source_Voltage_Range:
            self.Instrument.write(self.CMD_Set_Source_Voltage_Range % (voltage_range))

    def Set_Voltage(self, voltage):
        if self.CMD_Set_Voltage:
            self.Instrument.write(self.CMD_Set_Voltage % (voltage))

    def Trigger(self):
        if self.CMD_Trigger:
            self.Instrument.write(self.CMD_Trigger)

    def Close(self):
        global INSTR_CNT
        self.Instrument.close()
        INSTR_CNT -= 1
        if INSTR_CNT == 0:
            self.Resource_Manager.close()

class DAQ():
    def __init__(self, instrument_address=None):
        global INSTR_CNT
        self.State = False
        self.Channel_List = {}
        self.Channel_Count = 0
        self.Measure_Data = []
        self.Resource_Manager = visa.ResourceManager()
        if instrument_address != None:
            self.Instrument = self.Resource_Manager.open_resource(instrument_address)
            INSTR_CNT += 1

    def Reset(self):
        self.Channel_List = {}
        self.Channel_Count = 0
        self.Instrument.write("*RST")

    def Config_vol(self, mode = None, mode_range = None, mode_resolution = None, channel = None):
        if self.CMD_Config_VMode:
            if self.Model_Name == "Keysight_DAQ970A":
                self.Instrument.write(self.CMD_Config_VMode % (mode, mode_range, mode_resolution, channel))
            elif self.Model_Name == "Keithley_DAQ6510":
                self.Instrument.write(self.CMD_Config_VMode % (mode, channel))
                self.Set_Sense_Range(mode_range)
                self.Route_Add(channel)

    # def Config_cur(self, mode, mode_range, mode_resolution, ch):
        # self.Instrument.write(self.CMD_Config_IMode % (mode, mode_range, mode_resolution, ch))

    #def Config_temp(self, mode = None, mode_range = None, mode_resolution = None, channel = None):
    #    if self.CMD_Config_TMode:
    #        self.Instrument.write(self.CMD_Config_TMode % (mode, mode_range, mode_resolution, channel))

    def Initiate_Measurement(self):
        if self.Model_Name == "Keithley_DAQ6510":
            self.Instrument.write("INIT")
            self.Instrument.write("*WAI")
            self.Measure_Data = self.Instrument.query("TRAC:DATA? 1, %d" % (self.Channel_Count))[:-1].split(",")

    def Measure_Voltage(self, mode = None, mode_range = None, mode_resolution = None, channel = None):
        if  self.CMD_Measure_Voltage:
            if self.Model_Name == "Keysight_DAQ970A":
                if mode_range != "AUTO":
                    mode_range = str(mode_range)
                if channel != None:
                    return float(self.Instrument.query(self.CMD_Measure_Voltage % (mode, mode_range, mode_resolution, channel)))
                else:
                    return 0
            elif self.Model_Name == "Keithley_DAQ6510":
                return float(self.Measure_Data[self.Channel_List[channel]])
                
                
    # def Measure_Current(self,mode, mode_range, mode_resolution, ch):
        # return float(self.Instrument.query(self.CMD_Measure_Current % (mode, mode_range, mode_resolution, ch)))

    #def Measure_Temp(self, mode, mode_type, ch):
    #    if self.CMD_Measure_Temp:
    #           return float(self.Instrument.query(self.CMD_Measure_Temp % (mode, mode_type, ch)))    

    def Route_Add(self, channel):
        if self.CMD_Route_Add:
            self.Instrument.write(self.CMD_Route_Add % (channel))
            self.Channel_List.update({channel:self.Channel_Count})
            self.Channel_Count += 1

    def Set_Sense_Range(self, sense_range):
        if self.CMD_Set_Sense_Range:
            self.Instrument.write(self.CMD_Set_Sense_Range % (sense_range))

    def Close(self):
        global INSTR_CNT
        self.Instrument.close()
        INSTR_CNT -= 1
        if INSTR_CNT == 0:
            self.Resource_Manager.close()

class DMM():
    def __init__(self, instrument_address=None):
        global INSTR_CNT
        self.State = False
        self.Resource_Manager = visa.ResourceManager()
        if instrument_address != None:
            self.Instrument = self.Resource_Manager.open_resource(instrument_address)
            INSTR_CNT += 1

    def Reset(self):
        self.Instrument.write("*RST")

    def Config_vol(self, mode, mode_range, mode_resolution):
        if self.CMD_Config_VMode:
            if mode_range != "AUTO":
                mode_range = str(mode_range)
            self.Instrument.write(self.CMD_Config_VMode % (mode, mode_range, mode_resolution))

    def Config_cur(self, mode, mode_range, mode_resolution):
        if self.CMD_Config_IMode:
            self.Instrument.write(self.CMD_Config_IMode % (mode, mode_range, mode_resolution))

    def Measure(self, item, mode):
        if item == "Voltage":
            self.Measure_Voltage(mode)
        elif item == "Current":
            self.Measure_Current(mode)

    def Measure_Voltage(self, mode):
        if  self.CMD_Measure_Voltage:
            return float(self.Instrument.query(self.CMD_Measure_Voltage % (mode)))

    def Measure_Current(self, mode):
        if self.CMD_Measure_Current:
            return float(self.Instrument.query(self.CMD_Measure_Current % (mode)))

    def Close(self):
        global INSTR_CNT
        self.Instrument.close()
        INSTR_CNT -= 1
        if INSTR_CNT == 0:
            self.Resource_Manager.close()

class DMM_2():
    def __init__(self, instrument_address=None):
        global INSTR_CNT
        self.State = False
        self.Resource_Manager = visa.ResourceManager()
        if instrument_address != None:
            self.Instrument = self.Resource_Manager.open_resource(instrument_address)
            INSTR_CNT += 1

    def Reset(self):
        self.Instrument.write("*RST")

    def Config_vol(self, mode, mode_range, mode_resolution):
        if self.CMD_Config_VMode:
            if mode_range != "AUTO":
                mode_range = str(mode_range)
            self.Instrument.write(self.CMD_Config_VMode % (mode, mode_range, mode_resolution))

    def Config_cur(self, mode, mode_range, mode_resolution):
        if self.CMD_Config_IMode:
            self.Instrument.write(self.CMD_Config_IMode % (mode, mode_range, mode_resolution))

    def Measure(self, item, mode):
        if item == "Voltage":
            self.Measure_Voltage(mode)
        elif item == "Current":
            self.Measure_Current(mode)

    def Measure_Voltage(self, mode):
        if  self.CMD_Measure_Voltage:
            return float(self.Instrument.query(self.CMD_Measure_Voltage % (mode)))

    def Measure_Current(self, mode):
        if self.CMD_Measure_Current:
            return float(self.Instrument.query(self.CMD_Measure_Current % (mode)))

    def Close(self):
        global INSTR_CNT
        self.Instrument.close()
        INSTR_CNT -= 1
        if INSTR_CNT == 0:
            self.Resource_Manager.close()

class Function_Generator():
    CMD_Set_Amplitude       = ""
    CMD_Set_Frequency       = ""
    CMD_Set_Function        = ""
    VAR_Set_Function        = {}
    CMD_Set_Offset          = ""
    CMD_Set_Output_State    = ""
    CMD_Set_Phase           = ""
    CMD_Set_Pulse_Duty      = ""
    CMD_Set_Ramp_Symmetry   = ""
    CMD_Set_Unit            = ""

    def __init__(self, instrument_address=None):
        global INSTR_CNT
        self.State = False
        self.Resource_Manager = visa.ResourceManager()
        if instrument_address != None:
            self.Instrument = self.Resource_Manager.open_resource(instrument_address)
            INSTR_CNT += 1

    def Reset(self):
        self.Instrument.write("*RST")

    def Set_Amplitude(self, channel, amplitude, unit):
        if self.CMD_Set_Amplitude:
            self.Instrument.write(self.CMD_Set_Amplitude % (channel, amplitude, unit))

    def Set_Frequency(self, channel, frequency):
        if self.CMD_Set_Frequency:
            self.Instrument.write(self.CMD_Set_Frequency % (channel, frequency))

    def Set_Function(self, channel, function): #function: {"DC", "SIN", "SQU", "RAMP", "PULSE"}
        function = self.VAR_Set_Function.get(function)
        if self.CMD_Set_Function:
            self.Instrument.write(self.CMD_Set_Function % (channel, function))

    def Set_Impedance(self, channel, impedance): #impedance = {<ohms>, "INFinity", "MINimum", "MAXimum"}
        if self.CMD_Set_Impedance:
            self.Instrument.write(self.CMD_Set_Impedance % (channel, impedance))

    def Set_Offset(self, channel, offset):
        if self.CMD_Set_Offset:
            self.Instrument.write(self.CMD_Set_Offset % (channel, offset))

    def Set_Output_State(self, channel, state):
        if self.CMD_Set_Output_State:
            self.Instrument.write(self.CMD_Set_Output_State % (channel, state))
        self.State = state

    def Set_Phase(self, channel, phase):
        if self.CMD_Set_Phase:
            self.Instrument.write(self.CMD_Set_Phase % (channel, phase))

    def Set_Pulse_Duty(self, channel, duty):
        if self.CMD_Set_Pulse_Duty:
            self.Instrument.write(self.CMD_Set_Pulse_Duty % (channel, duty))

    def Set_Ramp_Symmetry(self, channel, symmetry):
        if self.CMD_Set_Ramp_Symmetry:
            self.Instrument.write(self.CMD_Set_Ramp_Symmetry % (channel, symmetry))

    def Set_Unit(self, channel, unit): #{"VPP", "VRMS"}
        if self.CMD_Set_Unit:
            self.Instrument.write(self.CMD_Set_Unit % (channel, unit))

    def syn(self):
        pass
    
    def call_wave(self):
        pass

    def Close(self):
        global INSTR_CNT
        self.Instrument.close()
        INSTR_CNT -= 1
        if INSTR_CNT == 0:
            self.Resource_Manager.close()