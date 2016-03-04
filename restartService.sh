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
    ps -ef |grep "python $vfos_home/ServerMain" |awk '{print $2}' |while read pid
    do
        kill -9 $pid
    done    
else
    echo "the service is stoped!"
fi
if [ -f "$vfos_home/ServerMain.pyc" ]; then
    nohup python $vfos_home/ServerMain.pyc >$vfos_home/main.out &
else
    nohup python $vfos_home/ServerMain.py >$vfos_home/main.out &
fi
echo "--------------restarted---------------"
tailf $vfos_home/Trace/logs/operation.log