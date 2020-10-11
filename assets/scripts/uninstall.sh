#!/bin/sh

# Check if symbolic link to executable is installed and remove if so
if test -h /usr/bin/hs_app; then
	rm /usr/bin/hs_app
fi

# Check if application files are installed and remove if so
if test -d /opt/hs_app;then
	rm -r /opt/hs_app
fi
