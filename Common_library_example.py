"""
 * @File       : Common_library_example.py
 * @Version    : V1.0.0
 * @Date       : 2022/04/27
 * @Brief      : Example
 * @Author     : Rex Wang
 * @Last editor: Rex Wang
 * Copyright (C) 2022 Alpha & Omega Semiconductor Ltd. All rights reserved.
"""
from time import sleep
import DC_Source_Model
import Source_Meter_Model
import Enable_Control_Model
import Load_Meter_Model
import DC_Load_Model
import DAQ_Model
import DMM_Model
import Function_Generator_Model
import Oscilloscope_Model
#aaacc

"""
DC_Source_Model example
"""
dc = DC_Source_Model.Chroma_62000P_Series(instrument_address = "GPIB0::1::INSTR")


dc.Config(channel = 1, voltage_limit = 15, voltage = 12, current_limit = 8, current = 4)
#If a function is required, the script is assigned the corresponding value
#If a function is not required, the script is assigned None or not assigned.

dc.Output_State(state = True, channel = 1)

sleep(3)

voltage = dc.Measure(item = "Voltage") #item: "Voltage", "Current", "Power"
current = dc.Measure(item = "Current") #item: "Voltage", "Current", "Power"

dc.Output_State(state = False, channel = 1)

print("DC Source: %.3fV, %.3fA" % (voltage, current))


"""
Source_Meter_Model example
"""
source_meter = Source_Meter_Model.Keithley_2400(instrument_address = "GPIB0::24::INSTR")

source_meter.Config(source_mode = "VOLTage", source_voltage_limit = 21, source_voltage = 5, sense_current_limit = 1, sense_current_range = 1, remote_state = True)

#function: {"VOLTage", "CURRent"}
#average_type: {"REPEAT", "MOVING"}
source_meter.Measurement_Config(function = "CURRent", average_state = True, average_type = "REPEAT", average_count = 10, concurrent_state = True)

source_meter.Set_Output_State(state = True)

source_meter.Set_Sense_Current_Range(current_range = "AUTO")

source_meter.Set_Sense_Average(state = False)
source_meter.Set_Sense_Average(state = True, average_type = "REPEAT", count = 10)

source_meter.Set_Arm_Count(count = 0)
source_meter.Initiate_Measurement()

sleep(3)

source_meter.Set_Idle()
source_meter.Set_Arm_Count(count = 1)
source_meter.Initiate_Measurement()

measure_vcc = source_meter.Measure_Voltage()
measure_icc = source_meter.Measure_Current()

source_meter.Set_Output_State(False)

print("Source meter: %.3fV, %.3fA" % (measure_vcc, measure_icc))

"""
Enable_Control_Model example
"""
enable_control = Enable_Control_Model.Keithley_2400(instrument_address = "GPIB0::23::INSTR")

enable_control.Config(source_voltage_limit = 21, source_voltage_range = 10, voltage = 5,
                      sense_current_limit = 1, sense_current_range = 1)

enable_control.Set_Output_State(True)

sleep(3)

enable_control.Set_Output_State(False)

"""
Load_Meter_Model example
"""
load_meter = Load_Meter_Model.Keithley_2400(instrument_address = "GPIB0::25::INSTR")

#source_mode: {"VOLTage", "CURRent", "MEMory"}
load_meter.Config(source_mode = "CURRent", source_current_range = 0.1, source_current = -0.001, sense_voltage_limit = 21,
                  sense_current_limit = 1, sense_voltage_range = 1, remote_state = True)

#function: {"VOLTage", "CURRent"}
#average_type: {"REPEAT", "MOVING"}
load_meter.Measurement_Config(function = "VOLTage", average_state = True, average_type = "REPEAT", average_count = 10, concurrent_state = True)

load_meter.Set_Output_State(state = True)

load_meter.Set_Arm_Count(count = 0)
load_meter.Initiate_Measurement()

sleep(3)

load_meter.Set_Idle()
load_meter.Set_Arm_Count(count = 1)
load_meter.Initiate_Measurement()

measure_vcc = load_meter.Measure_Voltage()
measure_icc = load_meter.Measure_Current()

load_meter.Set_Output_State(state = False)

print("Source meter: %.3fV, %.3fA" % (measure_vcc, measure_icc))

"""
DC_Load_Model example
"""
dc_load = DC_Load_Model.Chroma_6312A(instrument_address = "GPIB0::8::INSTR")

dc_load.Config(channel = 1, mode = "CCH", current1 = 1) #mode: {"CCL", "CCH", "CCDL", "CCDH", "CRL", "CRH", "CV"}
#dc_load.Config(channel = 1, mode = "CCDH", current1 = 1, current2 = 5, period1 = 0.001, period2 = 0.001) #mode: {"CCL", "CCH", "CCDL", "CCDH", "CRL", "CRH", "CV"}

dc_load.Set_Load_State(True)

sleep(3)

dc_load.Set_Load_State(False)

"""
DAQ_Model example
"""
daq = DAQ_Model.Keithley_DAQ6510(instrument_address = "GPIB0::18::INSTR")
daq.Reset() 
daq.Config_vol(mode = "DC", mode_range = 0.001, mode_resolution = 0.000001, channel = 111)

sleep(3)

voltage1 = daq.Measure_Voltage("DC", mode_range = 0.001, mode_resolution = 0.000001, channel = 111)

print(voltage1)

"""
DMM_Model example
"""
dmm = DMM_Model.Keysight_34461("GPIB0::2::INSTR")
dmm.Config_vol(mode = "DC", mode_range = 1, mode_resolution = 0.00001)

sleep(3)

dmm.Measure_Voltage(mode = "DC", mode_range = 1, mode_resolution = 0.0001)

"""
Function_Generator_Model example
"""
function_generator = Function_Generator_Model.AFG31000_Series(instrument_address = "GPIB0::3::INSTR")
function_generator.Reset()
function_generator.Set_Impedance(channel = 1, impedance = "INFinity") #impedance = {<ohms>, "INFinity", "MINimum", "MAXimum"}
function_generator.Set_Function(channel = 1, function = "DC") #function: {"DC", "SIN", "SQU", "RAMP", "PULSE"}
function_generator.Set_Offset(channel = 1, offset = 0)
function_generator.Set_Offset(channel = 1, offset = 5)
function_generator.Set_Output_State(channel = 1, state = True)

sleep(3)

function_generator.Set_Output_State(channel = 1, state = False)

"""
Oscilloscope_Model example
"""
oscilloscope = Oscilloscope_Model.Lecroy_HDO4034A(instrument_address = "GPIB0::6::INSTR")
oscilloscope.Reset()
        
#display_grid: {"Overlay", "Stacked"}
oscilloscope.Config(display_grid = "Overlay", time_scale = 0.001, timeout = 10000)

#cx_coupling: {"AC", "DC", "DC50", "DCREJ", "GND", "IAC", "IDC"}
oscilloscope.Channel_Config(c1_state = True, c2_state = True, c3_state = True, c4_state = True,
                            c1_scale = 5, c2_scale = 5, c3_scale = 1, c4_scale = 5,
                            c1_coupling = "DC", c2_coupling = "DC", c3_coupling = "DC", c4_coupling = "DC",
                            c1_bandwidth = 20, c2_bandwidth = 20, c3_bandwidth = 20, c4_bandwidth = 20,
                            c1_filter = 0, c2_filter = 0, c3_filter = 0, c4_filter = 0,
                            c1_position = 2, c2_position = 0, c3_position = -2, c4_position = -4,
                            c1_label = "Vcc", c2_label = "EN", c3_label = "Vout", c4_label = "PG")

#trigger_coupling: {"DC", "HFREJ", "LFREJ", "AC", "NOISEREJ"}
#trigger_slope: {"Fall", "Rise", "Either"}
oscilloscope.Trigger_Config(trigger_channel = 2, trigger_coupling = "DC", trigger_position = 50,
                            trigger_level = 2.5, trigger_slope = "Rise", trigger_mode = "NORM")

oscilloscope.Measurement_Clear()
oscilloscope.Measurement_Setting(1, measurement = "Mean", source1 = 1, unit1 = "%")
oscilloscope.Measurement_Setting(2, measurement = "Top", source1 = 2, unit1 = "%")
oscilloscope.Measurement_Setting(3, measurement = "Rise time", source1 = 3, unit1 = "%")
oscilloscope.Measurement_Setting(4, measurement = "Top", source1 = 3, unit1 = "%")
oscilloscope.Measurement_Setting(5, measurement = "Top", source1 = 4, unit1 = "%")

oscilloscope.Clear_Sweeps()

sleep(3) #waiting trigger

measure_parameter_1 = oscilloscope.Get_Measurement_Statistics_Value(1, "MEAN") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
measure_parameter_2 = oscilloscope.Get_Measurement_Statistics_Value(2, "MEAN") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
measure_parameter_3 = oscilloscope.Get_Measurement_Statistics_Value(3, "MEAN") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
measure_parameter_4 = oscilloscope.Get_Measurement_Statistics_Value(4, "MEAN") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}
measure_parameter_5 = oscilloscope.Get_Measurement_Statistics_Value(5, "MEAN") #statistic_method: {"LAST", "MEAN", "MIN", "MAX", "NUM"}

oscilloscope.Print_Setting(image_format = "PNG", background_color = "WHITE", destination = "REMOTE", area = "GRIDAREAONLY", port_name = "GPIB")

oscilloscope.Print_Screen(folder = "Test result/Image", file_name = "Test1")