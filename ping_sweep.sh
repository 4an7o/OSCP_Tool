#!/bin/bash

range=10.11.1.

for i in {1..254}
do
	# ping it, if return 64 bytes = success 
	#echo $range$i
	# ping -c 5 $range$i and show which one no packet loss
	echo "IP: "$range$i
	ping -c 3 -w 3 $range$i|grep "packet loss"|awk '{print $6" "$7" "$8}'
	printf "\n"
	
done