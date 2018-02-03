#!/bin/sh

echo "Start gunicorn processes..."

gunicorn -c /etc/gunicorn.d/hello.py hello:app &
cd ask/ 
gunicorn -c /etc/gunicorn.d/ask.py ask.wsgi:application &



