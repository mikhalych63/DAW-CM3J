#!/bin/bash

#Define control pins
MUTE='1 25' #gpiochip 1 
STANDBY='1 22' #gpiochip 1
FAULT0='2 3' #gpiochip 2
FAULT1='0 18' #gpiochip 0
LOGFILE='/opt/camilladsp/camilladsp.log'

#Addresses of chips
ADDR0='0x6a'
ADDR1='0x6b'

#Registers

VOL0='0x05'
VOL1='0x06'
VOL2='0x07'
VOL3='0x08'
MODE_REG='0x00'
SAP_REG='0x03'
CH_STATE_REG='0x04'

DC_LOAD_DIA1='0x0c'
DC_LOAD_DIA2='0x0d'
DC_LOAD_DIA3='0x0e'
CH_STATE='0x0f'
CH_FAULTS='0x10'
GLOB_FAULTS1='0x11'
GLOB_FAULTS2='0x12'

WARN_REG='0x13'
PCR_REG='0x14'
MISC_CNT_REG3='0x21'
MISC_CNT_REG5='0x28'

#Set pins 67 and 18 as inputs (Error or Warning sigmals from TAS6424)
echo 67 > /sys/class/gpio/export
echo in > /sys/class/gpio/gpio67/direction
echo 18 > /sys/class/gpio/export
echo in > /sys/class/gpio/gpio18/direction

#Reset Chips
i2ctransfer -y 1 w2@$ADDR0 $MODE_REG 0x80
i2ctransfer -y 1 w2@$ADDR1 $MODE_REG 0x80

#Turn on TAS62424
gpioset $STANDBY=0
sleep 1
#Turn chip A channels 3 and 4 in Parallel BTL mode
#i2ctransfer -y 1 w2@$ADDR0 $MODE_REG 0x20
#i2ctransfer -y 1 w2@$ADDR1 $MODE_REG 0x80
gpioset $STANDBY=1

sleep 3

#Reset errors
i2ctransfer -y 1 w2@$ADDR0 $MISC_CNT_REG3 0x80
i2ctransfer -y 1 w2@$ADDR1 $MISC_CNT_REG3 0x80

#Set 48 kHz Sample Rate I2S
i2ctransfer -y 1 w2@$ADDR0 $SAP_REG 0x44
i2ctransfer -y 1 w2@$ADDR1 $SAP_REG 0x44

#Set 96 kHz Sample Rate I2S
#i2ctransfer -y 1 w2@$ADDR0 $SAP_REG 0x84
#i2ctransfer -y 1 w2@$ADDR1 $SAP_REG 0x84

#Turn on FAULT and WARN pins
#i2ctransfer -y 1 w2@$ADDR0 $PCR_REG 0xff
#i2ctransfer -y 1 w2@$ADDR1 $PCR_REG 0xff

i2ctransfer -y 1 w2@$ADDR0 $MISC_CNT_REG5 0x2a
i2ctransfer -y 1 w2@$ADDR1 $MISC_CNT_REG5 0x2a

#i2ctransfer -y 1 w2@$ADDR0 $MISC_CNT_REG3 0x00
#i2ctransfer -y 1 w2@$ADDR1 $MISC_CNT_REG3 0x00

i2ctransfer -y 1 w2@$ADDR0 $VOL0 0xdf
#i2ctransfer -y 1 w2@$ADDR1 $VOL0 0x8f
i2ctransfer -y 1 w2@$ADDR0 $VOL1 0xdf
#i2ctransfer -y 1 w2@$ADDR1 $VOL1 0x8f
i2ctransfer -y 1 w2@$ADDR0 $VOL2 0xdf
#i2ctransfer -y 1 w2@$ADDR1 $VOL2 0x8f
i2ctransfer -y 1 w2@$ADDR0 $VOL3 0xdf
#i2ctransfer -y 1 w2@$ADDR1 $VOL3 0x8f


#Turn Play mode
i2ctransfer -y 1 w2@$ADDR0 $CH_STATE_REG 0x00
i2ctransfer -y 1 w2@$ADDR1 $CH_STATE_REG 0x00

#Turn On Sound
gpioset $MUTE=1
/usr/bin/python3 /opt/bin/tas6424_log.py
