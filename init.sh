#!/bin/sh

echo "init script"
if [ ! -L /etc/nginx/conf.d/test.conf ]; then
    sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/conf.d/test.conf 
fi
if [ -f /etc/nginx/conf.d/default.conf ]; then 
    sudo mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.bak
fi
if [ -f /etc/nginx/sites-enabled/default ]; then 
    sudo rm /etc/nginx/sites-enabled/default
fi
sudo /etc/init.d/nginx restart

