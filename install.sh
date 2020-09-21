#!/bin/sh

if test -h /usr/bin/hs_app; then
	rm /usr/bin/hs_app
fi

if test -d /opt/hs_app; then
	rm -r /opt/hs_app
fi

cp hs_app.tar.gz /opt
tar -zxvf /opt/hs_app.tar.gz -C /opt
chmod +x /opt/hs_app/hs_app
ln -s /opt/hs_app/hs_app /usr/bin/hs_app
rm /opt/hs_app.tar.gz

