import smbus
from BitParser import parse_bits, MultiBitValueParser
import logging

logfile = "/opt/camilladsp/camilladsp.log"

logging.basicConfig(level=logging.INFO, filename=logfile, filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")
#Addresses of chips
ADDR0=0x6a
ADDR1=0x6b

#Registers

DC_LOAD_DIA1=0x0c
DC_LOAD_DIA2=0x0d
DC_LOAD_DIA3=0x0e
CH_STATE=0x0f
CH_FAULTS=0x10
GLOB_FAULTS1=0x11
GLOB_FAULTS2=0x12

#DC Load Diagnostic Report 1
dia1 = MultiBitValueParser ({"1000": "Short-To-GND",
                             "0100": "Short-to-power",
                             "0010": "Open load",
                             "0001": "Shorted load",
                             "0000": "OK"})
dc_load_dia1 = [ dia1, dia1, dia1, dia1, dia1, dia1, dia1, dia1 ] 

status = MultiBitValueParser ({ "00": "PLAY",
                                "01": "Hi-Z",
                                "10": "MUTE",
                                "11": "DC load diagnostics"})
ch_states = [ status, status, status, status, status, status, status, status, ]

ch_faults = [ "Ch1: Overcurrent",
              "Ch2: Overcurrent",
              "Ch3: Overcurrent",
              "Ch4: Overcurrent",
              "Ch1: DC fault",
              "Ch2: DC fault",
              "Ch3: DC fault",
              "Ch4: DC fault", ]
glob_faults1 = [ " ",
                 " ",
                 " ",
                 "Clock fault",
                 "PVDD overvoltage fault",
                 "VBAT overvoltage fault",
                 "PVDD undervoltage fault",
                 "VBAT undervoltage fault", ]
glob_faults2 = [ " ",
                 " ",
                 " ",
                 "Global overtemperature shutdown",
                 "Overtemperature shutdown on Ch1",
                 "Overtemperature shutdown on Ch2",
                 "Overtemperature shutdown on Ch3",
                 "Overtemperature shutdown on Ch4", ]

bus = smbus.SMBus(1)

#Print Hardware errors
data = bus.read_byte_data(ADDR0, DC_LOAD_DIA1)
if data > 0:
        ls="Chip A Ch1 Ch2: " + str(parse_bits(format(data, '02x'), dc_load_dia1))
        logging.info(ls)
data = bus.read_byte_data(ADDR0, DC_LOAD_DIA2)
#print(format(data, '02x'))
if data > 0:
        ls="Chip A Ch3 Ch4: " + str(parse_bits(format(data, '02x'), dc_load_dia1))
        logging.info(ls)

data = bus.read_byte_data(ADDR1, DC_LOAD_DIA1)
if data > 0:
        ls="Chip B Ch1 Ch2: " + str(parse_bits(format(data, 'x'), dc_load_dia1))
        logging.info(ls)

data = bus.read_byte_data(ADDR1, DC_LOAD_DIA2)
if data > 0:
        ls="Chip B Ch3 Ch4: " + str(parse_bits(format(data, 'x'), dc_load_dia1))
        logging.info(ls)

#Print states of channels
data = bus.read_byte_data(ADDR0, CH_STATE)
if data > 0:
        ls="States Chip A Ch1-4: " + str(parse_bits(format(data, 'x'), ch_states))
        logging.info(ls)
data = bus.read_byte_data(ADDR1, CH_STATE)
if data > 0:
        ls="States Chip B Ch1-4: " + str(parse_bits(format(data, 'x'), ch_states))
        logging.info(ls)

#Print channels fault
data = bus.read_byte_data(ADDR0, CH_FAULTS)
if data > 0:
        ls="Channels Faults Chip A: " + str(parse_bits(format(data, 'x'), ch_faults))
        logging.error(ls)
data = bus.read_byte_data(ADDR1, CH_FAULTS)
if data > 0:
        ls="Channels Faults Chip B: " + str(parse_bits(format(data, 'x'), ch_faults))
        logging.error(ls)

#Pring global faults
data = bus.read_byte_data(ADDR0, GLOB_FAULTS1)
if data > 0:
        ls="Global Faults1 Chip A: " + str(parse_bits(format(data, 'x'), glob_faults1))
        logging.error(ls)
data = bus.read_byte_data(ADDR1, GLOB_FAULTS1)
if data > 0:
        ls="Global Faults1 Chip B: " + str(parse_bits(format(data, 'x'), glob_faults1))
        logging.Error(ls)

data = bus.read_byte_data(ADDR0, GLOB_FAULTS2)
if data > 0:
        ls="Global Faults2 Chip A: " + str(parse_bits(format(data, 'x'), glob_faults2))
        logging.error(ls)
data = bus.read_byte_data(ADDR1, GLOB_FAULTS2)
if data > 0:
        ls="Global Faults2 Chip B: " + str(parse_bits(format(data, 'x'), glob_faults2))
        logging.error(ls)

bus.close()

