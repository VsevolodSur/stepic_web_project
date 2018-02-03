#!/bin/sh

echo "Init script"
host=kurgan
homeipaddr=192.168.1.201
IPADDR=`ifconfig | grep addr: |grep -v "127.0.0.1" | awk '{ print substr($2, 6) }'`
HOSTNAME=`hostname`
WORKDIR=/home/box/web

if [ -L /etc/gunicorn.d/ask.py ]; then
	sudo rm /etc/gunicorn.d/ask.py
fi
if [ -L /etc/gunicorn.d/hello.py ]; then
	sudo rm /etc/gunicorn.d/hello.py
fi
if [ -L /etc/nginx/conf.d/test.conf ]; then
	sudo rm /etc/nginx/conf.d/test.conf
fi

if [ $HOSTNAME = $host ] && [ $IPADDR != $homeipaddr ]; then # on 636
	sed "s/${homeipaddr}/localhost/" ${WORKDIR}/etc/ask_cfg.py > ${WORKDIR}/etc/ask.py
	sed "s/${homeipaddr}/localhost/" ${WORKDIR}/etc/hello_cfg.py > ${WORKDIR}/etc/hello.py
	sed "s/${homeipaddr}/localhost/" ${WORKDIR}/etc/nginx_cfg.conf.py > ${WORKDIR}/etc/nginx.conf
elif [ $HOSTNAME = $host ] && [ $IPADDR = $homeipaddr ]; then # on 103
	cat ${WORKDIR}/etc/ask_cfg.py > ${WORKDIR}/etc/ask.py
	cat ${WORKDIR}/etc/hello_cfg.py > ${WORKDIR}/etc/hello.py
	cat ${WORKDIR}/etc/nginx_cfg.py > ${WORKDIR}/etc/nginx.conf
elif [ $HOSTNAME != $host ]; then #on terminal
	sed "s/${homeipaddr}/0.0.0.0/" ${WORKDIR}/etc/ask_cfg.py > ${WORKDIR}/etc/ask.py
	sed "s/${homeipaddr}/0.0.0.0/" ${WORKDIR}/etc/hello_cfg.py > ${WORKDIR}/etc/hello.py
	sed "s/${homeipaddr}/0.0.0.0/" ${WORKDIR}/etc/nginx_cfg.py > ${WORKDIR}/etc/nginx.conf
	sed -i -e "s/DEBUG = True/DEBUG = False/; s/ALLOWED_HOSTS = \[.*\]/ALLOWED_HOSTS = \[\x27${IPADDR}\x27\]/" ${WORKDIR}/ask/ask/settings.py	
else
	echo "Unknown host&ip" ${HOSTNAME} ${IPADDR}
	exit 1
fi

sudo ln -s /home/box/web/etc/ask.py /etc/gunicorn.d/ask.py
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/conf.d/test.conf

if [ -f /etc/nginx/conf.d/default.conf ]; then
    sudo mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.bak
fi
if [ -f /etc/nginx/sites-enabled/default ]; then
    sudo rm /etc/nginx/sites-enabled/default
fi

# ls -la /etc/gunicorn.d/hello.py /etc/nginx/conf.d/test.conf

sudo /etc/init.d/nginx restart

echo ${HOSTNAME} ${IPADDR}

