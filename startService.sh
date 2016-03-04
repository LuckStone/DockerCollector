#!/bin/sh
if [ "$1" = "" ]; 
then   
    vfos_home=`pwd`
else
    vfos_home=$1 
fi    
export PYTHONPATH=".:$vfos_home"
PROCESS_NUM=`ps -ef | grep "python $vfos_home/ServerMain" | grep -v "grep" | wc -l`  
if [ $PROCESS_NUM -gt 0 ]; 
then   
    echo "the Service is already running!"
    exit 1
else   
    if [ -f "$vfos_home/ServerMain.pyc" ]; then
        nohup python $vfos_home/ServerMain.pyc >$vfos_home/main.out & 
    else        
	nohup python $vfos_home/ServerMain.py >$vfos_home/main.out &
    fi
    echo "--------------started---------------"
    tailf $vfos_home/Trace/logs/operation.log
fi
