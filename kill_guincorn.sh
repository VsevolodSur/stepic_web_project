#!/bin/sh

echo "Kill gunicorn processes..."

for pid in `ps -ef | grep gunicorn | grep -v grep | awk '{ print $2 }'` 
do
	echo " kill pid: " $pid
	kill -9 $pid
done


