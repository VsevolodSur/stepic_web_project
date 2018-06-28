#!/bin/bash

function run_gunicorn () {
    echo "Start gunicorn processes..."

    gunicorn -c /etc/gunicorn.d/hello.py hello:app & 
    cd ask/
    gunicorn -c /etc/gunicorn.d/ask.py ask.wsgi:application &
}

function kill_gunicorn {
    echo "Kill gunicorn processes..."

    for pid in `ps -ef | grep gunicorn | grep -v grep | awk '{ print $2 }'`
    do
        echo " kill pid: " $pid
        kill -9 $pid
    done
}

case $1 in
    "start" )
    run_gunicorn
        ;;
    "stop" )
    kill_gunicorn
        ;;
    "restart" )
    kill_gunicorn
    run_gunicorn
    ;;
    * )
    echo "Format: $0 start|stop|restart"
    exit 1
    ;;
esac
