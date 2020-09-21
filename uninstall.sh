#!/bin/sh
if test -h /usr/bin/hs_app; then
	rm /usr/bin/hs_app
fi

if test -d /opt/hs_app;then
	rm -r /opt/hs_app
fi
