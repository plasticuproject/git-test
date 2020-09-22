#!/bin/sh

# Check if symbolic link to executable is installed and remove if so
if test -h /usr/bin/hs-app; then
	rm /usr/bin/hs-app
fi

# Check if application files are installed and remove if so
if test -d /opt/hs-app; then
	rm -r /opt/hs-app
fi

# Install application files, create symbolic link to executable in PATH and clean up
cp hs-app.tar.gz /opt
tar -zxvf /opt/hs-app.tar.gz -C /opt
chmod +x /opt/hs-app/hs-app
ln -s /opt/hs-app/hs-app /usr/bin/hs-app
rm /opt/hs-app.tar.gz

