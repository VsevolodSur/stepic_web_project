#!/bin/sh

echo "init script"
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/conf.d/test.conf 
if [ -f /etc/nginx/conf.d/default.conf ]; then 
    sudo mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.bak
fi
sudo /etc/init.d/nginx restart

