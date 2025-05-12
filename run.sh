#!/bin/bash
cd /opt/hopehub/profile_faker_service

# Cài thư viện (nếu cần)
/usr/bin/python3 -m pip install -r requirements.txt

# Chạy Flask app
/usr/bin/python3 app.py
