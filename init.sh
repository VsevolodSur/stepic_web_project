#!/bin/sh

echo "Init script"

if [ ! -L /etc/gunicorn.d/hello.py ]; then
    sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
fi
if [ ! -L /etc/nginx/conf.d/test.conf ]; then
    sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/conf.d/test.conf
fi
if [ -f /etc/nginx/conf.d/default.conf ]; then
    sudo mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.bak
fi
if [ -f /etc/nginx/sites-enabled/default ]; then
    sudo rm /etc/nginx/sites-enabled/default
fi

ls -la /etc/gunicorn.d/hello.py /etc/nginx/conf.d/test.conf

sudo /etc/init.d/nginx restart
