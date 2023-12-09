#!/bin/bash


# check if python is installed 

# check if venv exists

# check if packages are installed 

python3 -m venv .venv
source .venv/bin/activate
pip3 install colored
python3 main.py