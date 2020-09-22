# Just Playing with Python/Linux/GTK+

## Installing on Linux:
- Open a terminal and enter your Python 3.6+ virtual environment
- Execute `sudo apt-get install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0` to install the build dependencies and GTK
- Execute `pip install -r requirements.txt` to install Python dependencies

## Build and install executable:
- Change the working directory to where `build.sh` is located
- Execute `./build.sh` to build
- Execute `sudo cd build && ./install.sh` to install
- Execute `hs-app` to run
