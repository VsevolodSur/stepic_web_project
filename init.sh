#!/bin/sh

echo "Init script"

sed s/localhost/0.0.0.0/ etc/ask_cfg.py > etc/ask.py
if [ ! -L /etc/gunicorn.d/ask.py ]; then
    sudo ln -s /home/box/web/etc/ask.py /etc/gunicorn.d/ask.py
fi
sed s/localhost/0.0.0.0/ etc/hello_cfg.py > etc/hello.py
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

host="kurgan"
IPADDR=`ifconfig | grep addr: |grep -v "127.0.0.1" | awk '{ print substr($2, 6) }'`
HOSTNAME=`hostname`

if [ $HOSTNAME != $host ]; then
	sed -i -e "s/DEBUG = True/DEBUG = False/; s/ALLOWED_HOSTS = \[.*\]/ALLOWED_HOSTS = \[\x27${IPADDR}\x27\]/" ask/ask/settings.py
fi	

ls -la /etc/gunicorn.d/hello.py /etc/nginx/conf.d/test.conf

sudo /etc/init.d/nginx restart
echo "cd ask; gunicorn -c /etc/gunicorn.d/ask.py ask.wsgi:application"
echo "gunicorn -c /etc/gunicorn.d/hello.py hello:app"
echo ${IPADDR}

