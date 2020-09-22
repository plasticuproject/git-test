#!/bin/sh

# Check if symbolic link to executable is installed and remove if so
if test -h /usr/bin/hs-app; then
	rm /usr/bin/hs-app
fi

# Check if application files are installed and remove if so
if test -d /opt/hs-app;then
	rm -r /opt/hs-app
fi
