#!/bin/bash
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt

cd "$(dirname "$0")"
export PYTHONPATH=$PYTHONPATH:pwd

python3 queries.py
