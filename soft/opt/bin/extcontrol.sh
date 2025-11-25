#!/bin/bash
MUTE=1	#pin for mute operation
#POWEROFF=199	#pin for poweroff signal
#POWEROFF pin is assignet thru DeviceTree overlay - pin 12 !!
TIMEOUT=1200	#Delay before shutdown 20min
ZERO=0
#gpio mode $POWEROFF output
#gpio mode $MUTE input
#gpioset 0 $POWEROFF=1
to=$TIMEOUT
currstate="stopped"

while true;

do
mstate=$(gpioget 0 $MUTE)
#echo $mstate
    if [ "$mstate" == "1" ]; then
#	echo "Включаем"
	    if [ "$currstate" == "stopped" ]; then
	        currstate="playing"
	        mpc play
	    fi
        to=$TIMEOUT
	    sleep 1
    else
#	echo "Выключаем"
	    if [ "$currstate" == "playing" ]; then
	        currstate="stopped"
        	mpc pause
	    fi
	    if [ "$to" -gt "$ZERO" ]; then
	        let "to-=1"
	        sleep 1
	    else
	        echo "Shutdown..."
	        poweroff
	        exit 0
	    fi
    fi
done

exit 0
