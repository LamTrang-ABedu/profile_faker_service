#!/bin/bash
cd /opt/hopehub/profile_faker_service
git pull
pip3 install -r requirements.txt
pkill -f "5002"
nohup gunicorn -w 2 -b 0.0.0.0:5002 app:app > log.txt 2>&1 &