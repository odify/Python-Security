#!/bin/bash

# usage: online <protocols>
# example: online wifi bluetooth



CVARS=$@
for VAR in $CVARS; do
	if [[ ! -z `grep -ai "^wifi\$" <<< "$VAR"` ]]; then
		rfkill unblock wifi
		echo -e "Unblocked WiFi."
	elif [[ ! -z `grep -ai "^gps\$" <<< "$VAR"` ]]; then
		rfkill unblock gps
		echo -e "Unblocked GPS."
	elif [[ ! -z `grep -ai "^bluetooth\$" <<< "$VAR"` ]]; then
		rfkill unblock bluetooth
		echo -e "Unblocked Bluetooth."
	fi
done

if [[ -z $1 ]]; then
	rfkill unblock wifi
	rfkill unblock gps
	rfkill unblock bluetooth
	echo -e "Unblocked WiFi, GPS, Bluetooth."
fi
