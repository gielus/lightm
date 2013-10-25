#!/bin/bash

ROOTPATH=/usr/local/bin/lightm

if [ ! -d $ROOTPATH ]; then
	mkdir -p $ROOTPATH/web/cgi-bin
fi

if [ ! -d "/etc/lightm/" ]; then
	mkdir "/etc/lightm/"
fi

cp init-script /etc/init.d/lightm
update-rc.d lightm defaults

cp lightm-web.py $ROOTPATH
cp index.html $ROOTPATH/web
cp style.css $ROOTPATH/web
cp lightm.py $ROOTPATH/web/cgi-bin
cp cgi-bin/toggle.py $ROOTPATH/web/cgi-bin/


cp lights.conf /etc/lightm/lights.conf

