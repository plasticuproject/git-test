#!/bin/sh

# Check if symbolic link to executable is installed and remove if so
if test -h /usr/bin/hs_app; then
	rm /usr/bin/hs_app
fi

# Check if application files are installed and remove if so
if test -d /opt/hs_app; then
	rm -r /opt/hs_app
fi

# Install application files, create symbolic link to executable in PATH and clean up
cp hs_app.tar.gz /opt
tar -zxvf /opt/hs_app.tar.gz -C /opt
chmod +x /opt/hs_app/hs_app
ln -s /opt/hs_app/hs_app /usr/bin/hs_app
rm /opt/hs_app.tar.gz

