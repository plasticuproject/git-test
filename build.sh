#!/bin/sh

if test -d build; then
	rm -r build
fi

python setup.py build
cp install.sh build
cp uninstall.sh build
cd build
mkdir hs_app
cd exe.linux-x86_64-3.6
cp -r . ../hs_app
cd ../
tar -czvf hs_app.tar.gz hs_app
rm -r exe.linux-x86_64-3.6
cd ../

