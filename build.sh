#!/bin/bash

PATH_KIEKER='/home/serafim/Desktop/kieker-lang-pack-python'
PATH_SPYDER='/home/serafim/Desktop/spyder'
PATH_COLLECTOR='/home/serafim/Desktop/collector-1.15-SNAPSHOT/bin/collector'
PATH_CONFIG='/home/serafim/Desktop/collector-1.15-SNAPSHOT/bin/config.txt'

cd $PATH_KIEKER
python3 -m build
pip install dist/kieker-monitoring-for-python-0.0.1.tar.gz


if [[ $1 == -nc ]]
then 

     gnome-terminal -- bash -c "nc -l 65432"

     cd $PATH_SPYDER
     python3 bootstrap.py 
    
elif [[ $1 == -kieker ]]
then
     gnome-terminal -- bash -c "${PATH_COLLECTOR} -c ${PATH_CONFIG}"
     echo"wait 45 seconds to let collector initialize properly"
     sleep 45s
     cd $PATH_SPYDER
     python3 bootstrap.py

else
	echo "Wrong command. Supported commands: [-nc],[-kieker]"
	echo "[-nc] debug using netcat"
	echo "[-kieker] debug using collector"
fi    

