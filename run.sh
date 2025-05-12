#!/bin/bash
cd /opt/hopehub/profile_faker_service
git pull
pip3 install -r requirements.txt
pkill -f "5002"
# Chạy Flask app
/usr/bin/python3 app.py