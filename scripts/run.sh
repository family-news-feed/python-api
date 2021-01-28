#!/usr/bin/env bash
python $( pwd )/src/manage.py runserver &
explorer http://localhost:8000/