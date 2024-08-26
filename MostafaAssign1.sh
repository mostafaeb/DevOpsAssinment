#!/bin/bash

# Cheking the script's input for IP(s).
if [ "$#" -eq 0 ]; then
	echo "Enter the IP address(es) like: \"$0 1.1.1.1\""
	exit 1
fi

# processing the IP addresses:
for ip in "$@"; do
	pingResult=$(ping -c4 "$ip" | grep "error")
	if [ ! -z "$pingResult" -a "$pingResult" != " " ]; then
		echo "For the IP address \"$ip\", the Destination Host/Net is Unreachable!"
		continue
	else
		packetLoss=$(ping -c4 "$ip" | grep "packet loss" | gawk -F'[, %]' '{print $8}')
	fi
echo "For the IP address \"$ip\", the rate of packet loss is: $packetLoss%"
done
