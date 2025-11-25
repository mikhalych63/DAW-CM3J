import evdev
import sys
import os
import time
import yaml
import glob
from camilladsp import CamillaClient

cdsp = CamillaClient("127.0.0.1",1234)
cdsp.connect()

encoder=evdev.InputDevice('/dev/input/event0')
encoder.grab()

active = cdsp.config.file_path()
configdir = active.split('camilladsp/configs/')[0] + 'camilladsp/configs/'

def main():

  for event in encoder.read_loop():
       config = glob.glob(configdir + '_*')
       cdspvolume = cdsp.volume.main()
       cdspmute = cdsp.mute.main()
       cdspvolumeold = cdspvolume
       if event.type == evdev.ecodes.EV_REL:
            attrib = evdev.categorize(event)
            if str(attrib.event.value) == '-1':
                if cdspvolume - 1 >= -99: #change to cdspvolume - 0.5 if you want 0.5 dB increments
                    cdsp.volume.set_main(cdspvolume - 1) # change to cdspvolume - 0.5 if you want 0.5 dB increments
                    cdspvolume = cdsp.volume.main()
                else:
                    cdsp.volume.set_main(-99)
                    cdspvolume = cdsp.volume.main()

            elif str(attrib.event.value) == '1':
                if cdspvolume + 1 < 0: #change to cdspvolume + 0.5 if you want 0.5 dB increments
                     cdsp.volume.set_main(cdspvolume + 1) #change to cdspvolume + 0.5 if you want 0.5 dB increments
                     cdspvolume = cdsp.volume.main()
                else:
                     cdsp.volume.set_main(0)
                     cdspvolume = cdsp.volume.main()


if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
