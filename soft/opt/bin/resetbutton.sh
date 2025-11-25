#!/bin/bash
RST=24	#pin for reset
TIMEOUT=5	#Delay 
ONE=1
to=0
currstate="off"

while true;

do
mstate=$(gpioget 1 $RST)
#echo $mstate
    if [ "$mstate" == "1" ]; then
#	echo "Rise"
        if [ "$currstate" == "off" ]; then
          currstate="on"
        fi
        let to+=1
        sleep 1
    else
#	echo "Fall"
	    if [ "$currstate" == "on" ]; then
	        currstate="off"
#        	echo $to
                if [ "$to" -ge "$TIMEOUT" ]; then
#                    echo "Reboot"
                    reboot
                else
#                    echo "Amp reset"
                    /opt/bin/tas6241.sh
                fi
                let to=0
            fi
    fi
done

exit 0
