#!/bin/sh
if [ "$1" = "" ];
then
    vfos_home=`pwd`
else
    vfos_home=$1
fi
PROCESS_NUM=`ps -ef | grep "python $vfos_home/ServerMain" | grep -v "grep" | wc -l`  
if [ $PROCESS_NUM -gt 0 ]; 
then
    ps -ef |grep "python $vfos_home/ServerMain" |awk '{print $2}' |while read pid
    do
        kill -9 $pid
    done 
    echo "------------stopped------------"   
else
    echo "the service is already stopped!"
    exit 1
fi
