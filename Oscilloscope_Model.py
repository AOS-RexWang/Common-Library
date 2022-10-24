"""
 * @File       : Oscilloscope_Model.py
 * @Version    : V1.3.0
 * @Date       : Oct 24, 2022
 * @Brief      : Child class of Oscilloscope.
 * @Author     : Rex Wang
 * @Last editor: Rex Wang
 * Copyright (C) 2022 Alpha & Omega Semiconductor Ltd. All rights reserved.
"""

from Library.INSTR import Oscilloscope
from time import sleep

class Lecroy_HDO4034A(Oscilloscope):
    Channel_Number                          = 4
    Model_Name                              = "Lecroy_HDO4034A"
    CMD_Clear_Sweeps                        = "CLEAR_SWEEPS"
    CMD_Get_Channel_Attenuation             = "C%d:ATTENUATION?"
    CMD_Get_Channel_Range                   = ""
    CMD_Get_Cursor_AVPosition               = ""
    CMD_Get_Cursor_BVPosition               = ""
    CMD_Get_Cursor_Function                 = "CURSORS?"
    CMD_Get_Measurement_Statistics_Value    = "PARAMETER_STATISTICS? CUST, P%d"
    VAR_Get_Measurement_Statistics_Value    = {"LAST":"LAST", "MEAN":"AVG", "MIN":"LOW", "MAX":"HIGH", "NUM":"SWEEPS"}
    CMD_Get_Measurement_Value               = "C%d:PARAMETER_VALUE? %s"
    CMD_Get_Probe_Degauss_State             = "C%d:PROBE_DEGAUSS?"
    CMD_Get_Time_Scale                      = "TIME_DIV?"
    CMD_Get_Trigger_Channel                 = ""
    CMD_Get_Trigger_Slope                   = "C%d:TRIG_SLOPE?"
    CMD_Get_Trigger_Type                    = "TRIG_SELECT?"
    CMD_Measurement_Clear                   = "PARAMETER_CLR"
    CMD_Measurement_Delete                  = "PARAMETER_CUSTOM %d, NULL, C1"
    CMD_Measurement_Gate_Start              = "vbs app.Measure.P%d.GateStart = %.2f"
    CMD_Measurement_Gate_Stop               = "vbs app.Measure.P%d.GateStop = %.2f"
    CMD_Measurement_Setting                 = "PARAMETER_CUSTOM %d, %s"
    CMD_Measurement_Statistics_State        = "vbs app.Measure.StatsOn = %d"
    CMD_Print_Screen                        = "SCREEN_DUMP"
    CMD_Print_Setting                       = "HARDCOPY_SETUP DEV, %s, BCKG, %s, DEST, %s, AREA, %s, PORT, %s"
    CMD_Set_Acquire_mode                    = ""
    CMD_Set_Axis_Labels_State               = "vbs app.Display.AxisLabelsForTopTrace=%d"
    CMD_Set_Channel_Attenuation             = "C%d:ATTENUATION %d"
    CMD_Set_Channel_Bandwidth_Limit         = "BANDWIDTH_LIMIT C%d, %dMHZ"
    CMD_Set_Channel_Coupling                = "C%d:COUPLING %s"
    VAR_Set_Channel_Coupling                = {"AC":"A1M", "DC":"D1M", "DC50":"D50", "GND":"GND", "IAC":"AC", "IDC":"DC"} #channel_coupling: {"AC":"AC", "DC":"DC", "DC50":"D50", "DCREJ":"DCREJ", "GND":"GND", "IAC":Current"AC", "IDC":Current"DC"}
    CMD_Set_Channel_Label                   = 'vbs app.Acquisition.C%d.LabelsText = "%s"'
    CMD_Set_Channel_Label_State             = "vbs app.Acquisition.C%d.ViewLabels = %d"
    CMD_Set_Channel_Noise_Filter            = 'vbs app.Acquisition.Channels("C%d").EnhanceResType = %d'
    CMD_Set_Channel_Range                   = ""
    CMD_Set_Channel_Range_Mode              = ""
    CMD_Set_Channel_Trace_State_Off         = "C%d:TRACE OFF"
    CMD_Set_Channel_Trace_State_On          = "C%d:TRACE ON"
    CMD_Set_Channel_Voltage_Offset          = "C%d:OFFSET %f"
    CMD_Set_Channel_Voltage_Position        = ""
    CMD_Set_Channel_Voltage_Scale           = "C%d:VOLT_DIV %.3f"
    CMD_Set_Cmd_Header                      = "COMM_HEADER %s"
    CMD_Set_Cmd_Verbose                     = ""
    CMD_Set_Cursor_Function                 = "CURSORS %s"
    VAR_Set_Cursor_Function                 = {"SCREEN":"BREL", "WAVEFORM":"HREL", "VBArs":"", "HBArs":"VREL"}
    CMD_Set_Cursor_APosition                = "C%d:CRST HREF, %fDIV"
    CMD_Set_Cursor_ASource                  = ""
    CMD_Set_Cursor_AXPosition               = ""
    CMD_Set_Cursor_AYPosition               = ""
    CMD_Set_Cursor_BPosition                = "C%d:CRST HDIF, %fDIV"
    CMD_Set_Cursor_BSource                  = ""
    CMD_Set_Cursor_BXPosition               = ""
    CMD_Set_Cursor_BYPosition               = ""
    CMD_Set_Cursor_Split_Mode               = ""
    CMD_Set_Cursor_State_OFF                = ""
    CMD_Set_Cursor_State_ON                 = ""
    CMD_Set_Display_Grid                    = "GRID %s"
    VAR_Set_Display_Grid                    = {"Overlay":"SINGLE", "Stacked":"AUTO"}
    CMD_Set_Display_State_Off               = "DISPLAY OFF"
    CMD_Set_Display_State_On                = "DISPLAY ON"
    CMD_Set_Probe_Degauss                   = ""
    CMD_Set_Time_Scale                      = "TIME_DIV %.15f"
    CMD_Set_Trigger_Channel                 = ""
    CMD_Set_Trigger_Coupling                = "C%d:TRIG_COUPLING %s"
    VAR_Set_Trigger_Coupling                = {"DC":"DC", "HFREJ":"HFREJ", "LFREJ":"LFREJ", "AC":"AC"} #trigger_coupling: {"DC":"DC", "HFREJ":"HFREJ", "LFREJ":"LFREJ", "AC":"AC", "NOISEREJ":"NOISEREJ"}
    CMD_Set_Trigger_Delay                   = "TRIG_DELAY %.15f"
    CMD_Set_Trigger_Level                   = "C%d:TRIG_LEVEL %f"
    CMD_Set_Trigger_Mode                    = "TRIG_MODE %s"
    CMD_Set_Trigger_Position                = ""
    CMD_Set_Trigger_Slope                   = "C%d:TRIG_SLOPE %s"
    VAR_Set_Trigger_Slope                   = {"Fall":"NEG", "Rise":"POS", "Either":"EITHER"}
    CMD_Set_Trigger_Type                    = "TRIG_SELECT %s, SR, C%d"

    def Auto_Horizontal_Scale(self, channel, cycle, grid_limit, grid_position):
        self.Set_Channel_Voltage_Scale(channel, 5)
        self.Set_Channel_Voltage_Offset(channel, -20)
        last_measure_1 = self.Instrument.query("PARAMETER_CUSTOM? 1")
        last_measure_2 = self.Instrument.query("PARAMETER_CUSTOM? 2")
        last_measure_3 = self.Instrument.query("PARAMETER_CUSTOM? 3")
        self.Measurement_Setting(1, measurement = "Mean", source1 = channel, unit1 = "%")
        self.Measurement_Setting(2, measurement = "Peak to peak", source1 = channel, unit1 = "%")
        self.Measurement_Setting(3, measurement = "Period", source1 = channel, unit1 = "%")

        #trigger_coupling: {0:"DC", 1:"HFREJ", 2:"LFREJ", 3:"AC", 4:"NOISEREJ"}
        #trigger_slope: {0:"FALL", 1:"RISE", 2:"EITHER}
        self.Trigger_Config(trigger_channel = channel, trigger_mode = "AUTO")
        self.Clear_Sweeps()
        sleep(3)

        self.Instrument.write("vbs app.Acquisition.Trigger.Edge.FindLevel()")
        mean_value = float(self.Get_Measurement_Statistics_Value(1, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        peak_value = float(self.Get_Measurement_Statistics_Value(2, "MAX")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        #min_value = float(self.Get_Measurement_Statistics_Value(3, "MIN") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}

        for decimal in range(-2, 3):
            for base in 1,2,5:
                scale = float("%dE%d" % (base, decimal))
                
                #print(scale)
                #grid_limit = 4
                #grid_position = -2
                if round(grid_limit * scale, 5) > peak_value:

                    self.Set_Channel_Voltage_Scale(channel, scale)
                    self.Set_Channel_Voltage_Offset(channel, scale * grid_position - mean_value)
                    #self.Measurement_Setting(8, measurement = "Period", source = ("C%d" % channel))

                    status = int(self.Instrument.query("INR?"))
                    while status & 0x01 == 0:
                        status = int(self.Instrument.query("INR?"))
                    for decimal in range(-6, 1):
                        for base in 1,2,5:
                            time_scale = "%dE%d" % (base, decimal)
                            #self.Set_Trigger_Mode("STOP")
                            self.Set_Time_Scale(float(time_scale))
                            self.Instrument.write("*CLS")
                            #self.Set_Trigger_Mode("NORMAL")
                            status = int(self.Instrument.query("INR?"))
                            while status & 0x01 == 0:
                                status = int(self.Instrument.query("INR?"))
                            #sleep(1)
                            self.Clear_Sweeps()
                            sleep(1.5)

                            period_high_str = self.Get_Measurement_Statistics_Value(3, "MAX") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            mean_sweeps_str = self.Get_Measurement_Statistics_Value(1, "NUM") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            period_sweeps_str = self.Get_Measurement_Statistics_Value(3, "NUM") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            
                        if period_high_str != "UNDEF":
                            period_high_float = float(period_high_str)
                            mean_sweeps_float = int(float(mean_sweeps_str))
                            period_sweeps_float = int(float(period_sweeps_str))
                            if period_high_float > 0 and period_sweeps_float > mean_sweeps_float << 6:
                                
                                for decimal in range(-6, 1):
                                    for base in 1,2,5:
                                        time_scale = "%dE%d" % (base, decimal)
                                        time_limit = float(time_scale) * 10
                                        if period_high_float*cycle < time_limit and period_high_float*2 < time_limit:
                                            self.Set_Time_Scale(float(time_scale))
                                            self.Instrument.write("vbs app.Acquisition.Trigger.Edge.FindLevel()")
                                            self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_1)
                                            self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_2)
                                            self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_3)
                                            return
                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_1)
                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_2)
                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_3)
                    return
        return
        """
        self.Set_Channel_Voltage_Scale(channel, 50)
        self.Set_Channel_Voltage_Offset(channel, 0)
        last_measure_6 = self.Instrument.query("PARAMETER_CUSTOM? 6")
        last_measure_7 = self.Instrument.query("PARAMETER_CUSTOM? 7")
        last_measure_8 = self.Instrument.query("PARAMETER_CUSTOM? 8")
        self.Measurement_Setting(6, measurement = "Mean", source = ("C%d" % channel))
        self.Measurement_Setting(7, measurement = "Peak to peak", source = ("C%d" % channel))
        self.Measurement_Setting(8, measurement = "Minimum", source = ("C%d" % channel))
        
        self.Set_Trigger_Mode("AUTO")
        sleep(1)
        self.Set_Channel_Trigger_type(channel, trigger_type = "EDGE")
        self.Instrument.write("vbs app.Acquisition.Trigger.Edge.FindLevel()")
        self.Instrument.write("vbs app.Acquisition.C%d.FindScale" % (channel))
        #self.Set_Trigger_Mode("STOP")
        #self.Set_Trigger_Mode("AUTO")
        sleep(1)
        self.Instrument.write("*CLS")
        status = int(self.Instrument.query("INR?"))
        while status & 0x01 == 0:
            status = int(self.Instrument.query("INR?"))
            sleep(0.1)
        self.Clear_Sweeps()
        sleep(3)
        self.Instrument.write("vbs app.Acquisition.Trigger.Edge.FindLevel()")
        mean_value = float(self.Get_Measurement_Statistics_Value("AVG")["P6"])
        amplitude = float(self.Get_Measurement_Statistics_Value("HIGH")["P7"])
        min_value = float(self.Get_Measurement_Statistics_Value("LOW")["P8"])
        for decimal in range(-6, 3):
            for base in 1,2,5:
                scale = float("%dE%d" % (base, decimal))
                #print(scale)
                #grid_limit = 4
                #grid_position = -2
                if round(grid_limit * scale, 5) > amplitude:
                    self.Set_Channel_Voltage_Scale(channel, scale)
                    self.Set_Channel_Voltage_Offset(channel, scale * grid_position - (amplitude / 2) - min_value)
                    self.Measurement_Setting(8, measurement = "Period", source = ("C%d" % channel))

                    status = int(self.Instrument.query("INR?"))
                    while status & 0x01 == 0:
                        status = int(self.Instrument.query("INR?"))
                    for decimal in range(-6, 3):
                        for base in 1,2,5:
                            time_scale = "%dE%d" % (base, decimal)
                            #self.Set_Trigger_Mode("STOP")
                            self.Instrument.write("*CLS")
                            self.Set_Time_Scale(float(time_scale))
                            #self.Set_Trigger_Mode("NORMAL")
                            self.Clear_Sweeps()
                            sleep(5)
                            status = int(self.Instrument.query("INR?"))
                            while status & 0x01 == 0:
                                status = int(self.Instrument.query("INR?"))
                            period_str = self.Get_Measurement_Statistics_Value("AVG")["P8"]
                            if period_str != "UNDEF":
                                period_float = float(period_str)
                                if period_float > 0:
                                    for decimal in range(-14, 3):
                                        for base in 1,2,5:
                                            time_limit = "%dE%d" % (base, decimal-1)
                                            if period_float*cycle < float(time_limit) and period_float*2 < float(time_limit):
                                                self.Set_Time_Scale(float(time_limit))
                                                self.Instrument.write("vbs app.Acquisition.Trigger.Edge.FindLevel()")
                                                self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_8)
                                                return
                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_6)
                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_7)
                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_8)
                    return
        return
"""
    def Auto_Horizontal_Scale_Current(self, channel, cycle, grid_limit, grid_position, max_value, min_value):
        self.Set_Channel_Voltage_Scale(channel, 10)
        self.Set_Channel_Voltage_Offset(channel, 0)
        last_measure_1 = self.Instrument.query("PARAMETER_CUSTOM? 1")
        self.Measurement_Setting(1, measurement = "Period", source1 = channel, unit1 = "%")
        
        self.Trigger_Config(trigger_channel = channel, trigger_mode = "AUTO")
        sleep(1)
        amplitude = max_value - min_value
        for decimal in range(-2, 3):
            for base in 1,2,5:
                scale = float("%dE%d" % (base, decimal))
                if round(grid_limit * scale, 5) > amplitude:
                    self.Set_Channel_Voltage_Scale(channel, scale)
                    self.Set_Channel_Voltage_Offset(channel, scale * grid_position - (amplitude / 2) - min_value)

                    status = int(self.Instrument.query("INR?"))
                    while status & 0x01 == 0:
                        status = int(self.Instrument.query("INR?"))
                    for decimal in range(-6, 1):
                        for base in 1,2,5:
                            time_scale = "%dE%d" % (base, decimal)
                            #self.Set_Trigger_Mode("STOP")
                            self.Instrument.write("*CLS")
                            self.Config(time_scale = float(time_scale))
                            #self.Set_Trigger_Mode("NORMAL")
                            self.Clear_Sweeps()
                            sleep(1)
                            status = int(self.Instrument.query("INR?"))
                            while status & 0x01 == 0:
                                status = int(self.Instrument.query("INR?"))
                            period_str = self.Get_Measurement_Statistics_Value(1, "MEAN") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            
                        if period_str != "UNDEF":
                            period_float = float(period_str)
                            if period_float > 0:
                                for decimal in range(-14, 1):
                                    for base in 1,2,5:
                                        time_limit = "%dE%d" % (base, decimal-1)
                                        if period_float*cycle < float(time_limit) and period_float*2 < float(time_limit):
                                            self.Config(time_scale = float(time_limit)/10)
                                            self.Instrument.write("vbs app.Acquisition.Trigger.Edge.FindLevel()")
                                            self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_1)
                                            return
                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_1)
                    return
        return

    def Find_Scale(self):
        for channel in range(1,5):
            self.Instrument.write("vbs app.Acquisition.C%d.FindScale" % (channel))

    def Auto_Vertical_Scale(self, channel, mode = "AC", grid_limit = 1, grid_position = 0, vertical_scale = None):
        self.Set_Channel_Voltage_Scale(channel, 10)
        self.Set_Channel_Voltage_Offset(channel, -40)
        last_trigger = self.Instrument.query("TRIG_SELECT?")
        #last_measure_1 = self.Instrument.query("PARAMETER_CUSTOM? 1")
        last_measure_2 = self.Instrument.query("PARAMETER_CUSTOM? 2")
        last_measure_3 = self.Instrument.query("PARAMETER_CUSTOM? 3")
        
        self.Trigger_Config(trigger_channel = channel, trigger_mode = "AUTO")

        self.Instrument.write("vbs app.Acquisition.C%d.FindScale" % (channel))
        self.Instrument.write("*CLS")
        status = int(self.Instrument.query("INR?"))
        while status & 0x01 == 0:
            status = int(self.Instrument.query("INR?"))
        self.Instrument.write("vbs app.Acquisition.Trigger.Edge.FindLevel()")
        #return
        #self.Measurement_Setting(1, measurement = "Mean", source1 = channel, unit1 = "%")
        self.Measurement_Setting(2, measurement = "Mean", source1 = channel, unit1 = "%")
        self.Measurement_Setting(3, measurement = "Peak to peak", source1 = channel, unit1 = "%")

        self.Clear_Sweeps()
        sleep(3)

        mean_value = float(self.Get_Measurement_Statistics_Value(2, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        if mode == "AC":
            amplitude = float(self.Get_Measurement_Statistics_Value(3, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        else:
            amplitude = mean_value

        if vertical_scale == None:
            for decimal in range(-2, 3):
                for base in 1,2,5:
                    scale = float("%dE%d" % (base, decimal))
                    #print(scale)
                    if round(grid_limit * scale, 5) > amplitude:
                        self.Set_Channel_Voltage_Scale(channel, scale)
                        if mode == "AC":
                            self.Set_Channel_Voltage_Offset(channel, scale * grid_position - mean_value)
                        else:
                            self.Set_Channel_Voltage_Offset(channel, scale * grid_position)
                        self.Clear_Sweeps()
                        sleep(3)
                        mean_value = float(self.Get_Measurement_Statistics_Value(2, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                        if mode == "AC":
                            amplitude = float(self.Get_Measurement_Statistics_Value(3, "MAX")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                        else:
                            amplitude = mean_value
                        
                        for decimal in range(-2, 3):
                            for base in 1,2,5:
                                scale = float("%dE%d" % (base, decimal))
                                #print(scale)
                                if round(grid_limit * scale, 5) > amplitude:
                                    self.Set_Channel_Voltage_Scale(channel, scale)
                                    if mode == "AC":
                                        self.Set_Channel_Voltage_Offset(channel, scale * grid_position - mean_value)
                                    else:
                                        self.Set_Channel_Voltage_Offset(channel, scale * grid_position)
                                    self.Instrument.write("TRIG_SELECT %s" % last_trigger)
                                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_2)
                                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_3)
                                    return
        else:
            scale = vertical_scale
            #print(scale)
            if round(grid_limit * scale, 5) > amplitude:
                self.Set_Channel_Voltage_Scale(channel, scale)
                if mode == "AC":
                    self.Set_Channel_Voltage_Offset(channel, scale * grid_position - mean_value)
                else:
                    self.Set_Channel_Voltage_Offset(channel, scale * grid_position)
                self.Clear_Sweeps()
                sleep(3)
                mean_value = float(self.Get_Measurement_Statistics_Value(2, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                if mode == "AC":
                    amplitude = float(self.Get_Measurement_Statistics_Value(3, "MAX")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                else:
                    amplitude = mean_value
                
                scale = vertical_scale
                #print(scale)
                if round(grid_limit * scale, 5) > amplitude:
                    self.Set_Channel_Voltage_Scale(channel, scale)
                    if mode == "AC":
                        self.Set_Channel_Voltage_Offset(channel, scale * grid_position - mean_value)
                    else:
                        self.Set_Channel_Voltage_Offset(channel, scale * grid_position)
                    self.Instrument.write("TRIG_SELECT %s" % last_trigger)
                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_2)
                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_3)
                    return

        self.Instrument.write("TRIG_SELECT %s" % last_trigger)
        self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_2)
        self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_3)
        return
        
        #self.Instrument.query()
        mean = 0
        while mean == 0:
            mean = self.Get_Measurement_Value(channel, "Mean")
        maximum = self.Get_Measurement_Value(channel, "Maximum")
        minimum = self.Get_Measurement_Value(channel, "Minimum")

        sleep(5)
        self.Trigger_Config( trigger_mode = "STOP")
        self.Instrument.write("*CLS")
        self.Trigger_Config(trigger_mode = "AUTO")
        status = int(self.Instrument.query("INR?"))
        while status & 0x01 == 0:
            status = int(self.Instrument.query("INR?"))
        mean = 0
        while mean == 0:
            mean = self.Get_Measurement_Value(channel, "Mean")
        maximum = self.Get_Measurement_Value(channel, "Maximum")
        minimum = self.Get_Measurement_Value(channel, "Minimum")

        amplitude = maximum - minimum
        for decimal in range(-2, 2):
            for base in 1,2,5:
                scale = float("%dE%d" % (base, decimal))
                if round(grid_limit * scale, 5) > amplitude:
                    self.Set_Channel_Voltage_Scale(channel, scale)
                    self.Set_Channel_Voltage_Offset(channel, scale * grid_position - mean)
                    self.Instrument.write("vbs app.Acquisition.Trigger.Edge.FindLevel()")
                    self.Instrument.write("*CLS")
                    self.Set_Trigger_Mode("NORMAL")
                    while status & 0x01 == 0:
                        status = int(self.Instrument.query("INR?"))
                    if (self.Get_Measurement_Value(channel, "Maximum") < (grid_limit/2*scale+self.Get_Measurement_Value(channel, "Mean")) and self.Get_Measurement_Value(channel, "Minimum") > (-grid_limit/2*scale+self.Get_Measurement_Value(channel, "Mean"))):
                        return
        return

class Lecroy_44MXs_A(Oscilloscope):
    Channel_Number                          = 4
    Model_Name                              = "Lecroy_44MXs_A"
    CMD_Clear_Sweeps                        = "CLEAR_SWEEPS"
    CMD_Get_Channel_Attenuation             = "C%d:ATTENUATION?"
    CMD_Get_Channel_Range                   = ""
    CMD_Get_Cursor_AVPosition               = ""
    CMD_Get_Cursor_BVPosition               = ""
    CMD_Get_Cursor_Function                 = "CURSORS?"
    CMD_Get_Measurement_Statistics_Value    = "PARAMETER_STATISTICS? CUST, P%d"
    VAR_Get_Measurement_Statistics_Value    = {"LAST":"LAST", "MEAN":"AVG", "MIN":"LOW", "MAX":"HIGH", "NUM":"SWEEPS"}
    CMD_Get_Measurement_Value               = "C%d:PARAMETER_VALUE? %s"
    CMD_Get_Probe_Degauss_State             = "C%d:PROBE_DEGAUSS?"
    CMD_Get_Time_Scale                      = "TIME_DIV?"
    CMD_Get_Trigger_Channel                 = ""
    CMD_Get_Trigger_Slope                   = "C%d:TRIG_SLOPE?"
    CMD_Get_Trigger_Type                    = "TRIG_SELECT?"
    CMD_Measurement_Clear                   = "PARAMETER_CLR"
    CMD_Measurement_Delete                  = "PARAMETER_CUSTOM %d, NULL, C1"
    CMD_Measurement_Gate_Start              = "vbs app.Measure.P%d.GateStart = %.2f"
    CMD_Measurement_Gate_Stop               = "vbs app.Measure.P%d.GateStop = %.2f"
    CMD_Measurement_Setting                 = "PARAMETER_CUSTOM %d, %s"
    CMD_Measurement_Statistics_State        = "vbs app.Measure.StatsOn = %d"
    CMD_Print_Screen                        = "SCREEN_DUMP"
    CMD_Print_Setting                       = "HARDCOPY_SETUP DEV, %s, BCKG, %s, DEST, %s, AREA, %s, PORT, %s"
    CMD_Set_Acquire_mode                    = ""
    CMD_Set_Axis_Labels_State               = ""
    CMD_Set_Channel_Attenuation             = "C%d:ATTENUATION %d"
    CMD_Set_Channel_Bandwidth_Limit         = "BANDWIDTH_LIMIT C%d, %dMHZ"
    CMD_Set_Channel_Coupling                = "C%d:COUPLING %s"
    VAR_Set_Channel_Coupling                = {"AC":"A1M", "DC":"D1M", "DC50":"D50", "GND":"GND", "IAC":"AC", "IDC":"DC"} #channel_coupling: {"AC":"AC", "DC":"DC", "DC50":"D50", "DCREJ":"DCREJ", "GND":"GND", "IAC":Current"AC", "IDC":Current"DC"}
    CMD_Set_Channel_Label                   = 'vbs app.Acquisition.C%d.LabelsText = "%s"'
    CMD_Set_Channel_Label_State             = "vbs app.Acquisition.C%d.ViewLabels = %d"
    CMD_Set_Channel_Noise_Filter            = 'vbs app.Acquisition.Channels("C%d").EnhanceResType = %d'
    CMD_Set_Channel_Range                   = ""
    CMD_Set_Channel_Range_Mode              = ""
    CMD_Set_Channel_Trace_State_Off         = "C%d:TRACE OFF"
    CMD_Set_Channel_Trace_State_On          = "C%d:TRACE ON"
    CMD_Set_Channel_Voltage_Offset          = "C%d:OFFSET %f"
    CMD_Set_Channel_Voltage_Position        = ""
    CMD_Set_Channel_Voltage_Scale           = "C%d:VOLT_DIV %.3f"
    CMD_Set_Cmd_Header                      = "COMM_HEADER %s"
    CMD_Set_Cmd_Verbose                     = ""
    CMD_Set_Cursor_Function                 = "CURSORS %s"
    VAR_Set_Cursor_Function                 = {"SCREEN":"BREL", "WAVEFORM":"HREL", "VBArs":"", "HBArs":"VREL"}
    CMD_Set_Cursor_APosition                = "C%d:CRST HREF, %fDIV"
    CMD_Set_Cursor_ASource                  = ""
    CMD_Set_Cursor_AXPosition               = ""
    CMD_Set_Cursor_AYPosition               = ""
    CMD_Set_Cursor_BPosition                = "C%d:CRST HDIF, %fDIV"
    CMD_Set_Cursor_BSource                  = ""
    CMD_Set_Cursor_BXPosition               = ""
    CMD_Set_Cursor_BYPosition               = ""
    CMD_Set_Cursor_Split_Mode               = ""
    CMD_Set_Cursor_State_OFF                = ""
    CMD_Set_Cursor_State_ON                 = ""
    CMD_Set_Display_Grid                    = "GRID %s"
    VAR_Set_Display_Grid                    = {"Overlay":"SINGLE", "Stacked":"AUTO"}
    CMD_Set_Display_State_Off               = "DISPLAY OFF"
    CMD_Set_Display_State_On                = "DISPLAY ON"
    CMD_Set_Probe_Degauss                   = ""
    CMD_Set_Time_Scale                      = "TIME_DIV %.15f"
    CMD_Set_Trigger_Channel                 = ""
    CMD_Set_Trigger_Coupling                = "C%d:TRIG_COUPLING %s"
    VAR_Set_Trigger_Coupling                = {"DC":"DC", "HFREJ":"HFREJ", "LFREJ":"LFREJ", "AC":"AC"} #trigger_coupling: {"DC":"DC", "HFREJ":"HFREJ", "LFREJ":"LFREJ", "AC":"AC", "NOISEREJ":"NOISEREJ"}
    CMD_Set_Trigger_Delay                   = "TRIG_DELAY %.15f"
    CMD_Set_Trigger_Level                   = "C%d:TRIG_LEVEL %f"
    CMD_Set_Trigger_Mode                    = "TRIG_MODE %s"
    CMD_Set_Trigger_Position                = ""
    CMD_Set_Trigger_Slope                   = "C%d:TRIG_SLOPE %s"
    VAR_Set_Trigger_Slope                   = {"Fall":"NEG", "Rise":"POS", "Either":"EITHER"}
    CMD_Set_Trigger_Type                    = "TRIG_SELECT %s, SR, C%d"

    def Auto_Horizontal_Scale(self, channel, cycle, grid_limit, grid_position):
        self.Set_Channel_Voltage_Scale(channel, 5)
        self.Set_Channel_Voltage_Offset(channel, -20)
        last_measure_1 = self.Instrument.query("PARAMETER_CUSTOM? 1")
        last_measure_2 = self.Instrument.query("PARAMETER_CUSTOM? 2")
        last_measure_3 = self.Instrument.query("PARAMETER_CUSTOM? 3")
        self.Measurement_Setting(1, measurement = "Mean", source1 = channel, unit1 = "%")
        self.Measurement_Setting(2, measurement = "Peak to peak", source1 = channel, unit1 = "%")
        self.Measurement_Setting(3, measurement = "Period", source1 = channel, unit1 = "%")

        #trigger_coupling: {0:"DC", 1:"HFREJ", 2:"LFREJ", 3:"AC", 4:"NOISEREJ"}
        #trigger_slope: {0:"FALL", 1:"RISE", 2:"EITHER}
        self.Trigger_Config(trigger_channel = channel, trigger_mode = "AUTO")
        self.Clear_Sweeps()
        sleep(3)

        self.Instrument.write("vbs app.Acquisition.Trigger.Edge.FindLevel()")
        mean_value = float(self.Get_Measurement_Statistics_Value(1, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        peak_value = float(self.Get_Measurement_Statistics_Value(2, "MAX")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        #min_value = float(self.Get_Measurement_Statistics_Value(3, "MIN") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}

        for decimal in range(-2, 3):
            for base in 1,2,5:
                scale = float("%dE%d" % (base, decimal))
                
                #print(scale)
                #grid_limit = 4
                #grid_position = -2
                if round(grid_limit * scale, 5) > peak_value:

                    self.Set_Channel_Voltage_Scale(channel, scale)
                    self.Set_Channel_Voltage_Offset(channel, scale * grid_position - mean_value)
                    #self.Measurement_Setting(8, measurement = "Period", source = ("C%d" % channel))

                    status = int(self.Instrument.query("INR?"))
                    while status & 0x01 == 0:
                        status = int(self.Instrument.query("INR?"))
                    for decimal in range(-6, 1):
                        for base in 1,2,5:
                            time_scale = "%dE%d" % (base, decimal)
                            #self.Set_Trigger_Mode("STOP")
                            self.Set_Time_Scale(float(time_scale))
                            self.Instrument.write("*CLS")
                            #self.Set_Trigger_Mode("NORMAL")
                            status = int(self.Instrument.query("INR?"))
                            while status & 0x01 == 0:
                                status = int(self.Instrument.query("INR?"))
                            #sleep(1)
                            self.Clear_Sweeps()
                            sleep(1.5)

                            period_high_str = self.Get_Measurement_Statistics_Value(3, "MAX") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            mean_sweeps_str = self.Get_Measurement_Statistics_Value(1, "NUM") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            period_sweeps_str = self.Get_Measurement_Statistics_Value(3, "NUM") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            
                        if period_high_str != "UNDEF":
                            period_high_float = float(period_high_str)
                            mean_sweeps_float = int(float(mean_sweeps_str))
                            period_sweeps_float = int(float(period_sweeps_str))
                            if period_high_float > 0 and period_sweeps_float > mean_sweeps_float << 6:
                                
                                for decimal in range(-6, 1):
                                    for base in 1,2,5:
                                        time_scale = "%dE%d" % (base, decimal)
                                        time_limit = float(time_scale) * 10
                                        if period_high_float*cycle < time_limit and period_high_float*2 < time_limit:
                                            self.Set_Time_Scale(float(time_scale))
                                            self.Instrument.write("vbs app.Acquisition.Trigger.Edge.FindLevel()")
                                            self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_1)
                                            self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_2)
                                            self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_3)
                                            return
                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_1)
                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_2)
                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_3)
                    return
        return

    def Auto_Horizontal_Scale_Current(self, channel, cycle, grid_limit, grid_position, max_value, min_value):
        self.Set_Channel_Voltage_Scale(channel, 10)
        self.Set_Channel_Voltage_Offset(channel, 0)
        last_measure_1 = self.Instrument.query("PARAMETER_CUSTOM? 1")
        self.Measurement_Setting(1, measurement = "Period", source1 = channel, unit1 = "%")
        
        self.Trigger_Config(trigger_channel = channel, trigger_mode = "AUTO")
        sleep(1)
        amplitude = max_value - min_value
        for decimal in range(-2, 3):
            for base in 1,2,5:
                scale = float("%dE%d" % (base, decimal))
                if round(grid_limit * scale, 5) > amplitude:
                    self.Set_Channel_Voltage_Scale(channel, scale)
                    self.Set_Channel_Voltage_Offset(channel, scale * grid_position - (amplitude / 2) - min_value)

                    status = int(self.Instrument.query("INR?"))
                    while status & 0x01 == 0:
                        status = int(self.Instrument.query("INR?"))
                    for decimal in range(-6, 1):
                        for base in 1,2,5:
                            time_scale = "%dE%d" % (base, decimal)
                            #self.Set_Trigger_Mode("STOP")
                            self.Instrument.write("*CLS")
                            self.Config(time_scale = float(time_scale))
                            #self.Set_Trigger_Mode("NORMAL")
                            self.Clear_Sweeps()
                            sleep(1)
                            status = int(self.Instrument.query("INR?"))
                            while status & 0x01 == 0:
                                status = int(self.Instrument.query("INR?"))
                            period_str = self.Get_Measurement_Statistics_Value(1, "MEAN") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            
                        if period_str != "UNDEF":
                            period_float = float(period_str)
                            if period_float > 0:
                                for decimal in range(-14, 1):
                                    for base in 1,2,5:
                                        time_limit = "%dE%d" % (base, decimal-1)
                                        if period_float*cycle < float(time_limit) and period_float*2 < float(time_limit):
                                            self.Config(time_scale = float(time_limit)/10)
                                            self.Instrument.write("vbs app.Acquisition.Trigger.Edge.FindLevel()")
                                            self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_1)
                                            return
                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_1)
                    return
        return

    def Find_Scale(self):
        for channel in range(1,5):
            self.Instrument.write("vbs app.Acquisition.C%d.FindScale" % (channel))

    def Auto_Vertical_Scale(self, channel, mode = "AC", grid_limit = 1, grid_position = 0, vertical_scale = None):
        self.Set_Channel_Voltage_Scale(channel, 10)
        self.Set_Channel_Voltage_Offset(channel, -40)
        last_trigger = self.Instrument.query("TRIG_SELECT?")
        #last_measure_1 = self.Instrument.query("PARAMETER_CUSTOM? 1")
        last_measure_2 = self.Instrument.query("PARAMETER_CUSTOM? 2")
        last_measure_3 = self.Instrument.query("PARAMETER_CUSTOM? 3")
        
        self.Trigger_Config(trigger_channel = channel, trigger_mode = "AUTO")

        self.Instrument.write("vbs app.Acquisition.C%d.FindScale" % (channel))
        self.Instrument.write("*CLS")
        status = int(self.Instrument.query("INR?"))
        while status & 0x01 == 0:
            status = int(self.Instrument.query("INR?"))
        self.Instrument.write("vbs app.Acquisition.Trigger.Edge.FindLevel()")
        #return
        #self.Measurement_Setting(1, measurement = "Mean", source1 = channel, unit1 = "%")
        self.Measurement_Setting(2, measurement = "Mean", source1 = channel, unit1 = "%")
        self.Measurement_Setting(3, measurement = "Peak to peak", source1 = channel, unit1 = "%")

        self.Clear_Sweeps()
        sleep(3)

        mean_value = float(self.Get_Measurement_Statistics_Value(2, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        if mode == "AC":
            amplitude = float(self.Get_Measurement_Statistics_Value(3, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        else:
            amplitude = mean_value

        if vertical_scale == None:
            for decimal in range(-2, 3):
                for base in 1,2,5:
                    scale = float("%dE%d" % (base, decimal))
                    #print(scale)
                    if round(grid_limit * scale, 5) > amplitude:
                        self.Set_Channel_Voltage_Scale(channel, scale)
                        if mode == "AC":
                            self.Set_Channel_Voltage_Offset(channel, scale * grid_position - mean_value)
                        else:
                            self.Set_Channel_Voltage_Offset(channel, scale * grid_position)
                        self.Clear_Sweeps()
                        sleep(3)
                        mean_value = float(self.Get_Measurement_Statistics_Value(2, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                        if mode == "AC":
                            amplitude = float(self.Get_Measurement_Statistics_Value(3, "MAX")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                        else:
                            amplitude = mean_value
                        
                        for decimal in range(-2, 3):
                            for base in 1,2,5:
                                scale = float("%dE%d" % (base, decimal))
                                #print(scale)
                                if round(grid_limit * scale, 5) > amplitude:
                                    self.Set_Channel_Voltage_Scale(channel, scale)
                                    if mode == "AC":
                                        self.Set_Channel_Voltage_Offset(channel, scale * grid_position - mean_value)
                                    else:
                                        self.Set_Channel_Voltage_Offset(channel, scale * grid_position)
                                    self.Instrument.write("TRIG_SELECT %s" % last_trigger)
                                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_2)
                                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_3)
                                    return
        else:
            scale = vertical_scale
            #print(scale)
            if round(grid_limit * scale, 5) > amplitude:
                self.Set_Channel_Voltage_Scale(channel, scale)
                if mode == "AC":
                    self.Set_Channel_Voltage_Offset(channel, scale * grid_position - mean_value)
                else:
                    self.Set_Channel_Voltage_Offset(channel, scale * grid_position)
                self.Clear_Sweeps()
                sleep(3)
                mean_value = float(self.Get_Measurement_Statistics_Value(2, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                if mode == "AC":
                    amplitude = float(self.Get_Measurement_Statistics_Value(3, "MAX")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                else:
                    amplitude = mean_value
                
                scale = vertical_scale
                #print(scale)
                if round(grid_limit * scale, 5) > amplitude:
                    self.Set_Channel_Voltage_Scale(channel, scale)
                    if mode == "AC":
                        self.Set_Channel_Voltage_Offset(channel, scale * grid_position - mean_value)
                    else:
                        self.Set_Channel_Voltage_Offset(channel, scale * grid_position)
                    self.Instrument.write("TRIG_SELECT %s" % last_trigger)
                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_2)
                    self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_3)
                    return

        self.Instrument.write("TRIG_SELECT %s" % last_trigger)
        self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_2)
        self.Instrument.write("PARAMETER_CUSTOM %s" % last_measure_3)
        return
        
        #self.Instrument.query()
        mean = 0
        while mean == 0:
            mean = self.Get_Measurement_Value(channel, "Mean")
        maximum = self.Get_Measurement_Value(channel, "Maximum")
        minimum = self.Get_Measurement_Value(channel, "Minimum")

        sleep(5)
        self.Trigger_Config( trigger_mode = "STOP")
        self.Instrument.write("*CLS")
        self.Trigger_Config(trigger_mode = "AUTO")
        status = int(self.Instrument.query("INR?"))
        while status & 0x01 == 0:
            status = int(self.Instrument.query("INR?"))
        mean = 0
        while mean == 0:
            mean = self.Get_Measurement_Value(channel, "Mean")
        maximum = self.Get_Measurement_Value(channel, "Maximum")
        minimum = self.Get_Measurement_Value(channel, "Minimum")

        amplitude = maximum - minimum
        for decimal in range(-2, 2):
            for base in 1,2,5:
                scale = float("%dE%d" % (base, decimal))
                if round(grid_limit * scale, 5) > amplitude:
                    self.Set_Channel_Voltage_Scale(channel, scale)
                    self.Set_Channel_Voltage_Offset(channel, scale * grid_position - mean)
                    self.Instrument.write("vbs app.Acquisition.Trigger.Edge.FindLevel()")
                    self.Instrument.write("*CLS")
                    self.Set_Trigger_Mode("NORMAL")
                    while status & 0x01 == 0:
                        status = int(self.Instrument.query("INR?"))
                    if (self.Get_Measurement_Value(channel, "Maximum") < (grid_limit/2*scale+self.Get_Measurement_Value(channel, "Mean")) and self.Get_Measurement_Value(channel, "Minimum") > (-grid_limit/2*scale+self.Get_Measurement_Value(channel, "Mean"))):
                        return
        return


class Tektronix_MSO58(Oscilloscope):
    Channel_Number                          = 8
    Model_Name                              = "Tektronix_MSO58"
    CMD_Clear_Sweeps                        = "CLEAR"
    CMD_Get_Channel_Attenuation             = ""#"CH%d:PRObe:SET?"
    CMD_Get_Channel_Range                   = "CH%d:PRObe:FORCEDRange?"
    CMD_Get_Cursor_AVPosition               = "DISplay:WAVEView1:CURSor:CURSOR:WAVEform:AVPOSition?"
    CMD_Get_Cursor_BVPosition               = "DISplay:WAVEView1:CURSor:CURSOR:WAVEform:BVPOSition?"
    CMD_Get_Cursor_Function                 = "DISPLAY:WAVEVIEW1:CURSOR:CURSOR1:FUNCTION?"
    CMD_Get_Measurement_Statistics_Value    = "MEASUrement:MEAS%d:RESUlts:ALLAcqs:%s?"
    VAR_Get_Measurement_Statistics_Value    = {"LAST":"LAST", "MEAN":"MEAN", "MIN":"MINimum", "MAX":"MAXimum", "NUM":"POPUlation"}
    CMD_Get_Measurement_Value               = "MEASUrement:MEAS%d:RESUlts:CURRentacq:MEAN?"
    CMD_Get_Probe_Degauss_State             = "CH%d:PROBE:DEGAUSS:STATE?"
    CMD_Get_Time_Scale                      = "HORIZONTAL:MODE:SCALE?"
    CMD_Get_Trigger_Channel                 = "TRIGGER:A:EDGE:SOURCE?"
    CMD_Get_Trigger_Slope                   = "TRIGGER:A:EDGE:SLOPE?"
    CMD_Get_Trigger_Type                    = ""
    CMD_Measurement_Clear                   = "MEASUrement:DELETEALL"
    CMD_Measurement_Delete                  = 'MEASUREMENT:DELETE "MEAS%d"'
    CMD_Measurement_Mode                    = 'MEASUrement:GATing %s'#NONE|SCREEN|CURSor|LOGic|SEARch
    CMD_Measurement_Gate_Start              = "MEASUrement:MEAS%d:GATing:STARTtime %.15f"
    CMD_Measurement_Gate_Stop               = "MEASUrement:MEAS%d:GATing:ENDtime %.15f"
    CMD_Measurement_Setting                 = 'MEASUrement:ADDNew "MEAS%d"'
    CMD_Measurement_Statistics_State        = "MEASUrement:MEAS%d:DISPlaystat:ENABle %d"
    CMD_Measurement_Global_State            = "MEASUrement:MEAS%d:GLOBalref %d"
    CMD_Print_Screen                        = "SAVE:IMAGE 'temp.png'"
    CMD_Print_Setting                       = ""
    CMD_Set_Acquire_mode                    = "ACQuire:MODe %s" #{SAMple|PEAKdetect|HIRes|AVErage|ENVelope}
    CMD_Set_Axis_Labels_State               = ""
    CMD_Set_Channel_Attenuation             = ""#"CH%d:PRObe:SET 'ATTENUATION %dX'"
    CMD_Set_Channel_Bandwidth_Limit         = "CH%d:BANDWIDTH %d"
    CMD_Set_Channel_Coupling                = "CH%d:COUPLING %s"
    VAR_Set_Channel_Coupling                = {"AC":"AC", "DC":"DC", "DCREJ":"DCREJ", "IAC":"AC", "IDC":"DC"} #channel_coupling: {0:"AC", 1:"DC", 2:"D50", 3:"DCREJ", 4:"GND", 5:Current"AC", 6:Current"DC"}
    CMD_Set_Channel_Label                   = "CH%d:LABEL:NAME '%s'"
    CMD_Set_Channel_Label_State             = ""
    CMD_Set_Channel_Noise_Filter            = ""
    CMD_Set_Channel_Range                   = "CH%d:PRObe:FORCEDRange %d"
    CMD_Set_Channel_Range_Mode              = "CH%d:PROBECOntrol %s"#AUTO|MANual
    CMD_Set_Channel_Trace_State_Off         = "DISplay:GLObal:CH%d:STATE OFF"
    CMD_Set_Channel_Trace_State_On          = "DISplay:GLObal:CH%d:STATE ON"
    CMD_Set_Channel_Voltage_Offset          = "CH%d:OFFSET %f"
    CMD_Set_Channel_Voltage_Position        = "CH%d:POSition %f"
    CMD_Set_Channel_Voltage_Scale           = "CH%d:SCAle %.3f"
    CMD_Set_Cmd_Header                      = "HEADer %s"
    CMD_Set_Cmd_Verbose                     = "VERBose %s"
    CMD_Set_Cursor_Function                 = "DISPLAY:WAVEVIEW1:CURSOR:CURSOR1:FUNCTION %s"
    VAR_Set_Cursor_Function                 = {"SCREEN":"SCREEN", "WAVEFORM":"WAVEFORM", "VBArs":"VBArs", "HBArs":"HBArs"}
    CMD_Set_Cursor_APosition                = "DISplay:WAVEView1:CURSor:CURSOR1:%s:APOSition %.15f"
    CMD_Set_Cursor_ASource                  = "DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce CH%d"
    CMD_Set_Cursor_AXPosition               = "DISPLAY:WAVEVIEW1:CURSOR:CURSOR1:%s:AXPOSITION %.15f"
    CMD_Set_Cursor_AYPosition               = "DISPLAY:WAVEVIEW1:CURSOR:CURSOR1:%s:AYPOSITION %.15f"
    CMD_Set_Cursor_BPosition                = "DISplay:WAVEView1:CURSor:CURSOR1:%s:BPOSition %.15f"
    CMD_Set_Cursor_BSource                  = "DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce CH%d"
    CMD_Set_Cursor_BXPosition               = "DISPLAY:WAVEVIEW1:CURSOR:CURSOR1:%s:BXPOSITION %.15f"
    CMD_Set_Cursor_BYPosition               = "DISPLAY:WAVEVIEW1:CURSOR:CURSOR1:%s:BYPOSITION %.15f"
    CMD_Set_Cursor_Split_Mode               = "DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE %s"
    CMD_Set_Cursor_State_OFF                = "DISplay:WAVEView1:CURSor:CURSOR1:STATE OFF"
    CMD_Set_Cursor_State_ON                 = "DISplay:WAVEView1:CURSor:CURSOR1:STATE ON"
    CMD_Set_Display_Grid                    = "DISplay:WAVEView1:VIEWStyle %s"
    VAR_Set_Display_Grid                    = {"Overlay":"OVErlay", "Stacked":"STAcked"}
    CMD_Set_Display_State_Off               = ""
    CMD_Set_Display_State_On                = ""
    CMD_Set_Probe_Degauss                   = "CH%d:PRObe:DEGAUSS EXECute"
    CMD_Set_Time_Scale                      = "HORIZONTAL:MODE:SCALE %.15f"
    CMD_Set_Trigger_Channel                 = "TRIGGER:A:EDGE:SOURCE CH%d"
    CMD_Set_Trigger_Coupling                = "TRIGGER:A:EDGE:COUPLING %s"
    VAR_Set_Trigger_Coupling                = {"DC":"DC", "HFREJ":"HFREJ", "LFREJ":"LFREJ", "NOISEREJ":"NOISEREJ"} #trigger_coupling: {"DC":"DC", "HFREJ":"HFREJ", "LFREJ":"LFREJ", "AC":"AC", "NOISEREJ":"NOISEREJ"}
    CMD_Set_Trigger_Delay                   = "HORizontal:DELay:TIMe %.15f"
    CMD_Set_Trigger_Level                   = "TRIGGER:A:LEVEL:CH%d %f"
    CMD_Set_Trigger_Mode                    = "TRIGger:A:MODe %s"
    CMD_Set_Trigger_Position                = "HORizontal:POSition %d"
    CMD_Set_Trigger_Slope                   = "TRIGGER:A:EDGE:SLOPE %s"
    VAR_Set_Trigger_Slope                   = {"Fall":"FALL", "Rise":"RISE", "Either":"EITHER"}
    CMD_Set_Trigger_Type                    = "TRIGGER:A:TYPE %s"
    CMD_Set_Persistence_Type                = "DISplay:PERSistence %s"#{OFF|AUTO|INFPersist|INFInite|VARpersist|CLEAR}
    
    def Auto_Horizontal_Scale(self, channel, cycle, grid_limit, grid_position):
        self.Set_Channel_Voltage_Scale(channel, 5)
        self.Set_Channel_Voltage_Position(channel, -4)
        self.Measurement_Setting(51, measurement = "Mean", source1 = channel, unit1 = "%")
        self.Measurement_Setting(52, measurement = "Peak to peak", source1 = channel, unit1 = "%")
        self.Measurement_Setting(53, measurement = "Period", source1 = channel, unit1 = "%")

        #trigger_coupling: {0:"DC", 1:"HFREJ", 2:"LFREJ", 3:"AC", 4:"NOISEREJ"}
        #trigger_slope: {0:"FALL", 1:"RISE", 2:"EITHER}
        self.Trigger_Config(trigger_channel = channel, trigger_mode = "AUTO")
        self.Clear_Sweeps()
        sleep(3)

        mean_value = float(self.Get_Measurement_Statistics_Value(1, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        peak_value = float(self.Get_Measurement_Statistics_Value(2, "MAX")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        #min_value = float(self.Get_Measurement_Statistics_Value(3, "MIN") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}

        for decimal in range(-2, 3):
            for base in 1,2,5:
                scale = float("%dE%d" % (base, decimal))
                
                #print(scale)
                #grid_limit = 4
                #grid_position = -2
                if round(grid_limit * scale, 5) > peak_value:

                    self.Set_Channel_Voltage_Scale(channel, scale)
                    self.Set_Channel_Voltage_Position(channel, grid_position)
                    self.Set_Channel_Voltage_Offset(channel, mean_value)

                    self.Instrument.query("*OPC?")
                    
                    for decimal in range(-6, 1):
                        for base in 1,2,5:
                            time_scale = "%dE%d" % (base, decimal)
                            #self.Set_Trigger_Mode("STOP")
                            self.Set_Time_Scale(float(time_scale))
                            self.Instrument.write("*CLS")
                            #self.Set_Trigger_Mode("NORMAL")
                            self.Instrument.query("*OPC?")
                            #sleep(1)
                            self.Clear_Sweeps()
                            sleep(1.5)

                            period_high_str = self.Get_Measurement_Statistics_Value(53, "MAX") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            mean_sweeps_str = self.Get_Measurement_Statistics_Value(51, "NUM") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            period_sweeps_str = self.Get_Measurement_Statistics_Value(53, "NUM") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            
                        if period_high_str != "UNDEF":
                            period_high_float = float(period_high_str)
                            mean_sweeps_float = int(float(mean_sweeps_str))
                            period_sweeps_float = int(float(period_sweeps_str))
                            if period_high_float > 0 and period_sweeps_float > mean_sweeps_float << 6:
                                
                                for decimal in range(-6, 1):
                                    for base in 1,2,5:
                                        time_scale = "%dE%d" % (base, decimal)
                                        time_limit = float(time_scale) * 10
                                        if period_high_float*cycle < time_limit and period_high_float*2 < time_limit:
                                            self.Set_Time_Scale(float(time_scale))

                                            return

                    return
        return

    def Auto_Horizontal_Scale_Current(self, channel, cycle, grid_limit, grid_position, max_value, min_value):
        self.Set_Channel_Voltage_Scale(channel, 10)
        self.Set_Channel_Voltage_Offset(channel, 0)
        self.Measurement_Setting(51, measurement = "Period", source1 = channel, unit1 = "%")
        self.Measurement_Statistics_State(channel = 51, state = True)
        
        self.Trigger_Config(trigger_channel = channel, trigger_mode = "AUTO")
        sleep(1)
        amplitude = max_value - min_value
        for decimal in range(-2, 3):
            for base in 1,2,5:
                scale = float("%dE%d" % (base, decimal))
                if round(grid_limit * scale, 5) > amplitude:
                    self.Set_Channel_Voltage_Scale(channel, scale)
                    self.Set_Channel_Voltage_Position(channel, grid_position)
                    self.Trigger_Config(trigger_channel = 1, trigger_level = "AUTO")
                    self.Instrument.query("*OPC?")
                    
                    for decimal in range(-6, 1):
                        for base in 1,2,5:
                            time_scale = "%dE%d" % (base, decimal)
                            #self.Set_Trigger_Mode("STOP")
                            self.Instrument.write("*CLS")
                            self.Config(time_scale = float(time_scale))
                            #self.Set_Trigger_Mode("NORMAL")
                            self.Clear_Sweeps()
                            
                            period_num = self.Get_Measurement_Statistics_Value(51, "NUM") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            sleep(0.1)
                            self.Instrument.query("*OPC?")
                        if period_num > 0:
                            period_str = self.Get_Measurement_Statistics_Value(51, "MEAN") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            period_float = float(period_str)
                            if period_float > 0:
                                for decimal in range(-14, 1):
                                    for base in 1,2,5:
                                        time_limit = "%dE%d" % (base, decimal-1)
                                        if period_float*cycle < float(time_limit) and period_float*2 < float(time_limit):
                                            self.Config(time_scale = float(time_limit)/10)
                                            self.Instrument.query("*OPC?")
                                            self.Measurement_Delete(51)
                                            return
                    self.Instrument.query("*OPC?")
                    self.Measurement_Delete(51)
                    return
        self.Instrument.query("*OPC?")
        self.Measurement_Delete(51)
        return

    def Find_Scale(self):
        bandwidth = []
        for ch in range(1, self.Channel_Number + 1):
            bandwidth.append(float(self.Instrument.query("CH%d:BANdwidth?" % (ch))))
        self.Instrument.write("AUTOSet:ACQuisition:ENAble 0")
        self.Instrument.write("AUTOSet:HORizontal:ENAble 0")
        self.Instrument.write("AUTOSet:TRIGger:ENAble 0")
        self.Instrument.write("AUTOSet:VERTical:ENAble 1")
        self.Instrument.write("AUTOSet EXECute")
        self.Instrument.query("*OPC?")
        for ch in range(1, self.Channel_Number + 1):
            self.Instrument.write("CH%d:BANdwidth %.f" % (ch, bandwidth[ch-1]))
        
        self.Instrument.query("*OPC?")

    def Auto_Vertical_Scale(self, channel, mode = "AC", grid_limit = 1, grid_position = 0, vertical_scale = None):

        last_trigger = self.Get_Trigger_Channel()
        
        self.Trigger_Config(trigger_channel = channel, trigger_mode = "AUTO")

        self.Measurement_Setting(51, measurement = "Mean", source1 = channel, unit1 = "%")
        self.Measurement_Setting(52, measurement = "Peak to peak", source1 = channel, unit1 = "%")
        self.Measurement_Setting(53, measurement = "Minimum", source1 = channel, unit1 = "%")

        self.Clear_Sweeps()
        
        sleep(2)
        
        mean_value = float(self.Get_Measurement_Statistics_Value(51, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        min_value = float(self.Get_Measurement_Statistics_Value(53, "MIN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        if mode == "AC":
            amplitude = float(self.Get_Measurement_Statistics_Value(52, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        else:
            amplitude = mean_value

        if vertical_scale == None:
            for decimal in range(-2, 3):
                for base in 1,2,5:
                    scale = float("%dE%d" % (base, decimal))
                    #print(scale)
                    if round(grid_limit * scale, 5) > amplitude:
                        self.Set_Channel_Voltage_Scale(channel, scale)
                        if mode == "AC":
                            self.Set_Channel_Voltage_Offset(channel, min_value)
                            self.Set_Channel_Voltage_Position(channel, grid_position)
                        else:
                            self.Set_Channel_Voltage_Offset(channel, 0)
                            self.Set_Channel_Voltage_Position(channel, grid_position)
                        self.Clear_Sweeps()
                        sleep(3)
                        mean_value = float(self.Get_Measurement_Statistics_Value(51, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                        min_value = float(self.Get_Measurement_Statistics_Value(53, "MIN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                        if mode == "AC":
                            self.Set_Channel_Voltage_Offset(channel, mean_value)
                            self.Set_Channel_Voltage_Position(channel, grid_position)
                        else:
                            self.Set_Channel_Voltage_Offset(channel, 0)
                            self.Set_Channel_Voltage_Position(channel, grid_position)
                        self.Measurement_Delete(51)
                        self.Measurement_Delete(52)
                        self.Measurement_Delete(53)
                        return
        else:
            pass

        self.Measurement_Delete(51)
        self.Measurement_Delete(52)
        self.Measurement_Delete(53)
        return
        
        #self.Instrument.query()
        mean = 0
        while mean == 0:
            mean = self.Get_Measurement_Value(channel, "Mean")
        maximum = self.Get_Measurement_Value(channel, "Maximum")
        minimum = self.Get_Measurement_Value(channel, "Minimum")

        sleep(5)
        self.Trigger_Config( trigger_mode = "STOP")
        self.Instrument.write("*CLS")
        self.Trigger_Config(trigger_mode = "AUTO")
        status = int(self.Instrument.query("INR?"))
        while status & 0x01 == 0:
            status = int(self.Instrument.query("INR?"))
        mean = 0
        while mean == 0:
            mean = self.Get_Measurement_Value(channel, "Mean")
        maximum = self.Get_Measurement_Value(channel, "Maximum")
        minimum = self.Get_Measurement_Value(channel, "Minimum")

        amplitude = maximum - minimum
        for decimal in range(-2, 2):
            for base in 1,2,5:
                scale = float("%dE%d" % (base, decimal))
                if round(grid_limit * scale, 5) > amplitude:
                    self.Set_Channel_Voltage_Scale(channel, scale)
                    self.Set_Channel_Voltage_Offset(channel, scale * grid_position - mean)
                    self.Instrument.write("vbs app.Acquisition.Trigger.Edge.FindLevel()")
                    self.Instrument.write("*CLS")
                    self.Set_Trigger_Mode("NORMAL")
                    while status & 0x01 == 0:
                        status = int(self.Instrument.query("INR?"))
                    if (self.Get_Measurement_Value(channel, "Maximum") < (grid_limit/2*scale+self.Get_Measurement_Value(channel, "Mean")) and self.Get_Measurement_Value(channel, "Minimum") > (-grid_limit/2*scale+self.Get_Measurement_Value(channel, "Mean"))):
                        return
        return

class Tektronix_MSO54(Oscilloscope):
    Channel_Number                          = 4
    Model_Name                              = "Tektronix_MSO54"
    CMD_Clear_Sweeps                        = "CLEAR"
    CMD_Get_Channel_Attenuation             = ""#"CH%d:PRObe:SET?"
    CMD_Get_Channel_Range                   = "CH%d:PRObe:FORCEDRange?"
    CMD_Get_Cursor_AVPosition               = "DISplay:WAVEView1:CURSor:CURSOR:WAVEform:AVPOSition?"
    CMD_Get_Cursor_BVPosition               = "DISplay:WAVEView1:CURSor:CURSOR:WAVEform:BVPOSition?"
    CMD_Get_Cursor_Function                 = "DISPLAY:WAVEVIEW1:CURSOR:CURSOR1:FUNCTION?"
    CMD_Get_Measurement_Statistics_Value    = "MEASUrement:MEAS%d:RESUlts:ALLAcqs:%s?"
    VAR_Get_Measurement_Statistics_Value    = {"LAST":"LAST", "MEAN":"MEAN", "MIN":"MINimum", "MAX":"MAXimum", "NUM":"POPUlation"}
    CMD_Get_Measurement_Value               = "MEASUrement:MEAS%d:RESUlts:CURRentacq:MEAN?"
    CMD_Get_Probe_Degauss_State             = "CH%d:PROBE:DEGAUSS:STATE?"
    CMD_Get_Time_Scale                      = "HORIZONTAL:MODE:SCALE?"
    CMD_Get_Trigger_Channel                 = "TRIGGER:A:EDGE:SOURCE?"
    CMD_Get_Trigger_Slope                   = "TRIGGER:A:EDGE:SLOPE?"
    CMD_Get_Trigger_Type                    = ""
    CMD_Measurement_Clear                   = "MEASUrement:DELETEALL"
    CMD_Measurement_Delete                  = 'MEASUREMENT:DELETE "MEAS%d"'
    CMD_Measurement_Mode                    = 'MEASUrement:GATing %s'#NONE|SCREEN|CURSor|LOGic|SEARch
    CMD_Measurement_Gate_Start              = "MEASUrement:MEAS%d:GATing:STARTtime %.15f"
    CMD_Measurement_Gate_Stop               = "MEASUrement:MEAS%d:GATing:ENDtime %.15f"
    CMD_Measurement_Setting                 = 'MEASUrement:ADDNew "MEAS%d"'
    CMD_Measurement_Statistics_State        = "MEASUrement:MEAS%d:DISPlaystat:ENABle %d"
    CMD_Measurement_Global_State            = "MEASUrement:MEAS%d:GLOBalref %d"
    CMD_Print_Screen                        = "SAVE:IMAGE 'temp.png'"
    CMD_Print_Setting                       = ""
    CMD_Set_Acquire_mode                    = "ACQuire:MODe %s" #{SAMple|PEAKdetect|HIRes|AVErage|ENVelope}
    CMD_Set_Axis_Labels_State               = ""
    CMD_Set_Channel_Attenuation             = ""#"CH%d:PRObe:SET 'ATTENUATION %dX'"
    CMD_Set_Channel_Bandwidth_Limit         = "CH%d:BANDWIDTH %d"
    CMD_Set_Channel_Coupling                = "CH%d:COUPLING %s"
    VAR_Set_Channel_Coupling                = {"AC":"AC", "DC":"DC", "DCREJ":"DCREJ", "IAC":"AC", "IDC":"DC"} #channel_coupling: {0:"AC", 1:"DC", 2:"D50", 3:"DCREJ", 4:"GND", 5:Current"AC", 6:Current"DC"}
    CMD_Set_Channel_Label                   = "CH%d:LABEL:NAME '%s'"
    CMD_Set_Channel_Label_State             = ""
    CMD_Set_Channel_Noise_Filter            = ""
    CMD_Set_Channel_Range                   = "CH%d:PRObe:FORCEDRange %d"
    CMD_Set_Channel_Range_Mode              = "CH%d:PROBECOntrol %s"#AUTO|MANual
    CMD_Set_Channel_Trace_State_Off         = "DISplay:GLObal:CH%d:STATE OFF"
    CMD_Set_Channel_Trace_State_On          = "DISplay:GLObal:CH%d:STATE ON"
    CMD_Set_Channel_Voltage_Offset          = "CH%d:OFFSET %f"
    CMD_Set_Channel_Voltage_Position        = "CH%d:POSition %f"
    CMD_Set_Channel_Voltage_Scale           = "CH%d:SCAle %.3f"
    CMD_Set_Cmd_Header                      = "HEADer %s"
    CMD_Set_Cmd_Verbose                     = "VERBose %s"
    CMD_Set_Cursor_Function                 = "DISPLAY:WAVEVIEW1:CURSOR:CURSOR1:FUNCTION %s"
    VAR_Set_Cursor_Function                 = {"SCREEN":"SCREEN", "WAVEFORM":"WAVEFORM", "VBArs":"VBArs", "HBArs":"VREL"}
    CMD_Set_Cursor_APosition                = "DISplay:WAVEView1:CURSor:CURSOR1:%s:APOSition %.15f"
    CMD_Set_Cursor_ASource                  = "DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce CH%d"
    CMD_Set_Cursor_AXPosition               = "DISPLAY:WAVEVIEW1:CURSOR:CURSOR1:%s:AXPOSITION %.15f"
    CMD_Set_Cursor_AYPosition               = "DISPLAY:WAVEVIEW1:CURSOR:CURSOR1:%s:AYPOSITION %.15f"
    CMD_Set_Cursor_BPosition                = "DISplay:WAVEView1:CURSor:CURSOR1:%s:BPOSition %.15f"
    CMD_Set_Cursor_BSource                  = "DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce CH%d"
    CMD_Set_Cursor_BXPosition               = "DISPLAY:WAVEVIEW1:CURSOR:CURSOR1:%s:BXPOSITION %.15f"
    CMD_Set_Cursor_BYPosition               = "DISPLAY:WAVEVIEW1:CURSOR:CURSOR1:%s:BYPOSITION %.15f"
    CMD_Set_Cursor_Split_Mode               = "DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE %s"
    CMD_Set_Cursor_State_OFF                = "DISplay:WAVEView1:CURSor:CURSOR1:STATE OFF"
    CMD_Set_Cursor_State_ON                 = "DISplay:WAVEView1:CURSor:CURSOR1:STATE ON"
    CMD_Set_Display_Grid                    = "DISplay:WAVEView1:VIEWStyle %s"
    VAR_Set_Display_Grid                    = {"Overlay":"OVErlay", "Stacked":"STAcked"}
    CMD_Set_Display_State_Off               = ""
    CMD_Set_Display_State_On                = ""
    CMD_Set_Probe_Degauss                   = "CH%d:PRObe:DEGAUSS EXECute"
    CMD_Set_Time_Scale                      = "HORIZONTAL:MODE:SCALE %.15f"
    CMD_Set_Trigger_Channel                 = "TRIGGER:A:EDGE:SOURCE CH%d"
    CMD_Set_Trigger_Coupling                = "TRIGGER:A:EDGE:COUPLING %s"
    VAR_Set_Trigger_Coupling                = {"DC":"DC", "HFREJ":"HFREJ", "LFREJ":"LFREJ", "NOISEREJ":"NOISEREJ"} #trigger_coupling: {"DC":"DC", "HFREJ":"HFREJ", "LFREJ":"LFREJ", "AC":"AC", "NOISEREJ":"NOISEREJ"}
    CMD_Set_Trigger_Delay                   = "HORizontal:DELay:TIMe %.15f"
    CMD_Set_Trigger_Level                   = "TRIGGER:A:LEVEL:CH%d %f"
    CMD_Set_Trigger_Mode                    = "TRIGger:A:MODe %s"
    CMD_Set_Trigger_Position                = "HORizontal:POSition %d"
    CMD_Set_Trigger_Slope                   = "TRIGGER:A:EDGE:SLOPE %s"
    VAR_Set_Trigger_Slope                   = {"Fall":"FALL", "Rise":"RISE", "Either":"EITHER"}
    CMD_Set_Trigger_Type                    = "TRIGGER:A:TYPE %s"
    CMD_Set_Persistence_Type                = "DISplay:PERSistence %s"#{OFF|AUTO|INFPersist|INFInite|VARpersist|CLEAR}
    
    def Auto_Horizontal_Scale(self, channel, cycle, grid_limit, grid_position):
        self.Set_Channel_Voltage_Scale(channel, 5)
        self.Set_Channel_Voltage_Position(channel, -4)
        self.Measurement_Setting(51, measurement = "Mean", source1 = channel, unit1 = "%")
        self.Measurement_Setting(52, measurement = "Peak to peak", source1 = channel, unit1 = "%")
        self.Measurement_Setting(53, measurement = "Period", source1 = channel, unit1 = "%")

        #trigger_coupling: {0:"DC", 1:"HFREJ", 2:"LFREJ", 3:"AC", 4:"NOISEREJ"}
        #trigger_slope: {0:"FALL", 1:"RISE", 2:"EITHER}
        self.Trigger_Config(trigger_channel = channel, trigger_mode = "AUTO")
        self.Clear_Sweeps()
        sleep(3)

        mean_value = float(self.Get_Measurement_Statistics_Value(1, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        peak_value = float(self.Get_Measurement_Statistics_Value(2, "MAX")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        #min_value = float(self.Get_Measurement_Statistics_Value(3, "MIN") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}

        for decimal in range(-2, 3):
            for base in 1,2,5:
                scale = float("%dE%d" % (base, decimal))
                
                #print(scale)
                #grid_limit = 4
                #grid_position = -2
                if round(grid_limit * scale, 5) > peak_value:

                    self.Set_Channel_Voltage_Scale(channel, scale)
                    self.Set_Channel_Voltage_Position(channel, grid_position)
                    self.Set_Channel_Voltage_Offset(channel, mean_value)

                    self.Instrument.query("*OPC?")
                    
                    for decimal in range(-6, 1):
                        for base in 1,2,5:
                            time_scale = "%dE%d" % (base, decimal)
                            #self.Set_Trigger_Mode("STOP")
                            self.Set_Time_Scale(float(time_scale))
                            self.Instrument.write("*CLS")
                            #self.Set_Trigger_Mode("NORMAL")
                            self.Instrument.query("*OPC?")
                            #sleep(1)
                            self.Clear_Sweeps()
                            sleep(1.5)

                            period_high_str = self.Get_Measurement_Statistics_Value(53, "MAX") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            mean_sweeps_str = self.Get_Measurement_Statistics_Value(51, "NUM") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            period_sweeps_str = self.Get_Measurement_Statistics_Value(53, "NUM") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            
                        if period_high_str != "UNDEF":
                            period_high_float = float(period_high_str)
                            mean_sweeps_float = int(float(mean_sweeps_str))
                            period_sweeps_float = int(float(period_sweeps_str))
                            if period_high_float > 0 and period_sweeps_float > mean_sweeps_float << 6:
                                
                                for decimal in range(-6, 1):
                                    for base in 1,2,5:
                                        time_scale = "%dE%d" % (base, decimal)
                                        time_limit = float(time_scale) * 10
                                        if period_high_float*cycle < time_limit and period_high_float*2 < time_limit:
                                            self.Set_Time_Scale(float(time_scale))

                                            return

                    return
        return

    def Auto_Horizontal_Scale_Current(self, channel, cycle, grid_limit, grid_position, max_value, min_value):
        self.Set_Channel_Voltage_Scale(channel, 10)
        self.Set_Channel_Voltage_Offset(channel, 0)
        self.Measurement_Setting(51, measurement = "Period", source1 = channel, unit1 = "%")
        self.Measurement_Statistics_State(channel = 51, state = True)
        
        self.Trigger_Config(trigger_channel = channel, trigger_mode = "AUTO")
        sleep(1)
        amplitude = max_value - min_value
        for decimal in range(-2, 3):
            for base in 1,2,5:
                scale = float("%dE%d" % (base, decimal))
                if round(grid_limit * scale, 5) > amplitude:
                    self.Set_Channel_Voltage_Scale(channel, scale)
                    self.Set_Channel_Voltage_Position(channel, grid_position)
                    self.Trigger_Config(trigger_channel = 1, trigger_level = "AUTO")
                    self.Instrument.query("*OPC?")
                    
                    for decimal in range(-6, 1):
                        for base in 1,2,5:
                            time_scale = "%dE%d" % (base, decimal)
                            #self.Set_Trigger_Mode("STOP")
                            self.Instrument.write("*CLS")
                            self.Config(time_scale = float(time_scale))
                            #self.Set_Trigger_Mode("NORMAL")
                            self.Clear_Sweeps()
                            
                            period_num = self.Get_Measurement_Statistics_Value(51, "NUM") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            sleep(0.1)
                            self.Instrument.query("*OPC?")
                        if period_num > 0:
                            period_str = self.Get_Measurement_Statistics_Value(51, "MEAN") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                            period_float = float(period_str)
                            if period_float > 0:
                                for decimal in range(-14, 1):
                                    for base in 1,2,5:
                                        time_limit = "%dE%d" % (base, decimal-1)
                                        if period_float*cycle < float(time_limit) and period_float*2 < float(time_limit):
                                            self.Config(time_scale = float(time_limit)/10)
                                            self.Instrument.query("*OPC?")
                                            self.Measurement_Delete(51)
                                            return
                    self.Instrument.query("*OPC?")
                    self.Measurement_Delete(51)
                    return
        self.Instrument.query("*OPC?")
        self.Measurement_Delete(51)
        return

    def Find_Scale(self):
        bandwidth = []
        for ch in range(1, self.Channel_Number + 1):
            bandwidth.append(float(self.Instrument.query("CH%d:BANdwidth?" % (ch))))
        self.Instrument.write("AUTOSet:ACQuisition:ENAble 0")
        self.Instrument.write("AUTOSet:HORizontal:ENAble 0")
        self.Instrument.write("AUTOSet:TRIGger:ENAble 0")
        self.Instrument.write("AUTOSet:VERTical:ENAble 1")
        self.Instrument.write("AUTOSet EXECute")
        self.Instrument.query("*OPC?")
        for ch in range(1, self.Channel_Number + 1):
            self.Instrument.write("CH%d:BANdwidth %.f" % (ch, bandwidth[ch-1]))
        
        self.Instrument.query("*OPC?")

    def Auto_Vertical_Scale(self, channel, mode = "AC", grid_limit = 1, grid_position = 0, vertical_scale = None):

        last_trigger = self.Get_Trigger_Channel()
        
        self.Trigger_Config(trigger_channel = channel, trigger_mode = "AUTO")

        self.Measurement_Setting(51, measurement = "Mean", source1 = channel, unit1 = "%")
        self.Measurement_Setting(52, measurement = "Peak to peak", source1 = channel, unit1 = "%")
        self.Measurement_Setting(53, measurement = "Minimum", source1 = channel, unit1 = "%")

        self.Clear_Sweeps()
        
        sleep(2)
        
        mean_value = float(self.Get_Measurement_Statistics_Value(51, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        min_value = float(self.Get_Measurement_Statistics_Value(53, "MIN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        if mode == "AC":
            amplitude = float(self.Get_Measurement_Statistics_Value(52, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
        else:
            amplitude = mean_value

        if vertical_scale == None:
            for decimal in range(-2, 3):
                for base in 1,2,5:
                    scale = float("%dE%d" % (base, decimal))
                    #print(scale)
                    if round(grid_limit * scale, 5) > amplitude:
                        self.Set_Channel_Voltage_Scale(channel, scale)
                        if mode == "AC":
                            self.Set_Channel_Voltage_Offset(channel, min_value)
                            self.Set_Channel_Voltage_Position(channel, grid_position)
                        else:
                            self.Set_Channel_Voltage_Offset(channel, 0)
                            self.Set_Channel_Voltage_Position(channel, grid_position)
                        self.Clear_Sweeps()
                        sleep(3)
                        mean_value = float(self.Get_Measurement_Statistics_Value(51, "MEAN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                        min_value = float(self.Get_Measurement_Statistics_Value(53, "MIN")) #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
                        if mode == "AC":
                            self.Set_Channel_Voltage_Offset(channel, mean_value)
                            self.Set_Channel_Voltage_Position(channel, grid_position)
                        else:
                            self.Set_Channel_Voltage_Offset(channel, 0)
                            self.Set_Channel_Voltage_Position(channel, grid_position)
                        self.Measurement_Delete(51)
                        self.Measurement_Delete(52)
                        self.Measurement_Delete(53)
                        return
        else:
            pass

        self.Measurement_Delete(51)
        self.Measurement_Delete(52)
        self.Measurement_Delete(53)
        return
        
        #self.Instrument.query()
        mean = 0
        while mean == 0:
            mean = self.Get_Measurement_Value(channel, "Mean")
        maximum = self.Get_Measurement_Value(channel, "Maximum")
        minimum = self.Get_Measurement_Value(channel, "Minimum")

        sleep(5)
        self.Trigger_Config( trigger_mode = "STOP")
        self.Instrument.write("*CLS")
        self.Trigger_Config(trigger_mode = "AUTO")
        status = int(self.Instrument.query("INR?"))
        while status & 0x01 == 0:
            status = int(self.Instrument.query("INR?"))
        mean = 0
        while mean == 0:
            mean = self.Get_Measurement_Value(channel, "Mean")
        maximum = self.Get_Measurement_Value(channel, "Maximum")
        minimum = self.Get_Measurement_Value(channel, "Minimum")

        amplitude = maximum - minimum
        for decimal in range(-2, 2):
            for base in 1,2,5:
                scale = float("%dE%d" % (base, decimal))
                if round(grid_limit * scale, 5) > amplitude:
                    self.Set_Channel_Voltage_Scale(channel, scale)
                    self.Set_Channel_Voltage_Offset(channel, scale * grid_position - mean)
                    self.Instrument.write("vbs app.Acquisition.Trigger.Edge.FindLevel()")
                    self.Instrument.write("*CLS")
                    self.Set_Trigger_Mode("NORMAL")
                    while status & 0x01 == 0:
                        status = int(self.Instrument.query("INR?"))
                    if (self.Get_Measurement_Value(channel, "Maximum") < (grid_limit/2*scale+self.Get_Measurement_Value(channel, "Mean")) and self.Get_Measurement_Value(channel, "Minimum") > (-grid_limit/2*scale+self.Get_Measurement_Value(channel, "Mean"))):
                        return
        return


class Tektronix_DPO7054C(Oscilloscope):
    Channel_Number                          = 4
    Model_Name                              = "Tektronix_DPO7054C"
    CMD_Clear_Sweeps                        = "CLEAR"
    CMD_Get_Channel_Attenuation             = ""#"CH%d:PRObe:SET?"
    CMD_Get_Channel_Range                   = "CH%d:PRObe:FORCEDRange?"
    CMD_Get_Cursor_AVPosition               = ""
    CMD_Get_Cursor_BVPosition               = ""
    CMD_Get_Cursor_Function                 = ""
    CMD_Get_Measurement_Statistics_Value    = "MEASUrement:MEAS%d:%s?"
    VAR_Get_Measurement_Statistics_Value    = {"LAST":None, "MEAN":"MEAN", "MIN":"MINimum", "MAX":"MAXimum", "NUM":"COUNt"}
    CMD_Get_Measurement_Value               = "MEASUrement:IMMed:VALue?"
    CMD_Get_Probe_Degauss_State             = "CH%d:PROBE:DEGAUSS:STATE?"
    CMD_Get_Time_Scale                      = "HORIZONTAL:MODE:SCALE?"
    CMD_Get_Trigger_Channel                 = "TRIGGER:A:EDGE:SOURCE?"
    CMD_Get_Trigger_Slope                   = "TRIGGER:A:EDGE:SLOPE?"
    CMD_Get_Trigger_Type                    = ""
    CMD_Measurement_Clear                   = ""
    CMD_Measurement_Delete                  = ""
    CMD_Measurement_Gate_Start              = "CURSor:VBArs:POSITION1 %.15f"
    CMD_Measurement_Gate_Stop               = "CURSor:VBArs:POSITION2 %.15f"
    CMD_Measurement_Setting                 = 'MEASUrement:MEAS%d:STATE ON'
    CMD_Measurement_Statistics_State        = "MEASUrement:STATIstics:MODe %s"
    CMD_Print_Screen                        = "SAVE:IMAGE 'temp.png'"
    CMD_Print_Setting                       = ""
    CMD_Set_Acquire_mode                    = "ACQuire:MODe %s" #{SAMple|PEAKdetect|HIRes|AVErage|ENVelope}
    CMD_Set_Axis_Labels_State               = ""
    CMD_Set_Channel_Attenuation             = ""#"CH%d:PRObe:SET 'ATTENUATION %dX'"
    CMD_Set_Channel_Bandwidth_Limit         = "CH%d:BANDWIDTH %s"
    CMD_Set_Channel_Coupling                = "CH%d:COUPLING %s"
    VAR_Set_Channel_Coupling                = {"AC":"AC", "DC":"DC", "DCREJ":"DCREJect", "GND":"GND", "IAC":"AC", "IDC":"DC"} #channel_coupling: {0:"AC", 1:"DC", 2:"D50", 3:"DCREJ", 4:"GND", 5:Current"AC", 6:Current"DC"}
    CMD_Set_Channel_Label                   = "CH%d:LABEL:NAME '%s'"
    CMD_Set_Channel_Label_State             = ""
    CMD_Set_Channel_Noise_Filter            = ""
    CMD_Set_Channel_Range                   = "CH%d:PRObe:FORCEDRange %d"
    CMD_Set_Channel_Range_Mode              = "CH%d:PROBECOntrol %s"#AUTO|MANual
    CMD_Set_Channel_Trace_State_Off         = "SELECT:CH%d OFF"
    CMD_Set_Channel_Trace_State_On          = "SELECT:CH%d ON"
    CMD_Set_Channel_Voltage_Offset          = "CH%d:OFFSET %f"
    CMD_Set_Channel_Voltage_Position        = "CH%d:POSition %f"
    CMD_Set_Channel_Voltage_Scale           = "CH%d:SCAle %.3f"
    CMD_Set_Cmd_Header                      = "HEADer %s"
    CMD_Set_Cmd_Verbose                     = "VERBose %s"
    CMD_Set_Cursor_Function                 = ""
    CMD_Set_Cursor_APosition                = ""
    CMD_Set_Cursor_ASource                  = ""
    CMD_Set_Cursor_AXPosition               = ""
    CMD_Set_Cursor_AYPosition               = ""
    CMD_Set_Cursor_BPosition                = ""
    CMD_Set_Cursor_BSource                  = ""
    CMD_Set_Cursor_BXPosition               = ""
    CMD_Set_Cursor_BYPosition               = ""
    CMD_Set_Cursor_Split_Mode               = ""
    CMD_Set_Cursor_State_OFF                = ""
    CMD_Set_Cursor_State_ON                 = ""
    CMD_Set_Display_Grid                    = ""
    VAR_Set_Display_Grid                    = {}
    CMD_Set_Display_State_Off               = ""
    CMD_Set_Display_State_On                = ""
    CMD_Set_Probe_Degauss                   = "CH%d:PRObe:DEGAUSS EXECute"
    CMD_Set_Time_Scale                      = "HORIZONTAL:MODE:SCALE %.15f"
    CMD_Set_Trigger_Channel                 = "TRIGGER:A:EDGE:SOURCE CH%d"
    CMD_Set_Trigger_Coupling                = "TRIGGER:A:EDGE:COUPLING %s"
    VAR_Set_Trigger_Coupling                = {"DC":"DC", "HFREJ":"HFREJ", "LFREJ":"LFREJ", "AC":"AC", "NOISEREJ":"NOISEREJ"} #trigger_coupling: {"DC":"DC", "HFREJ":"HFREJ", "LFREJ":"LFREJ", "AC":"AC", "NOISEREJ":"NOISEREJ"}
    CMD_Set_Trigger_Delay                   = "HORizontal:DELay:TIMe %.15f"
    CMD_Set_Trigger_Level                   = "TRIGGER:A:LEVEL:CH%d %f"
    CMD_Set_Trigger_Mode                    = "TRIGger:A:MODe %s"
    CMD_Set_Trigger_Position                = "HORizontal:POSition %d"
    CMD_Set_Trigger_Slope                   = "TRIGGER:A:EDGE:SLOPE %s"
    VAR_Set_Trigger_Slope                   = {"Fall":"FALL", "Rise":"RISE", "Either":"EITHER"}
    CMD_Set_Trigger_Type                    = "TRIGGER:A:TYPE %s"
