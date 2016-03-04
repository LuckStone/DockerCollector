#! /bin/bash

export PYTHONPATH=`pwd`

if [[ "$1" = "" || "$1" = "-h" ]];
then
    python mongoimpl/install.py  -h 2>&1
else
    python mongoimpl/install.py  $1 2>&1
fi

 
