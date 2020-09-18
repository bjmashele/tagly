#!/usr/bin/env bash 

if [ ! -d "taglyenv" ]; then
    echo --------------------
    echo Creating virtualenv
    echo --------------------
    virtualenv taglyenv
fi
source taglyenv/bin/activate

pip install -r requirements.txt