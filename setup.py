import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
DIR = "assets"
build_exe_options = {"packages": ["gi", "random", "playsound"], "include_files": DIR}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "H's App",
        version = "0.1",
        description = "H's App",
        options = {"build_exe": build_exe_options},
        executables = [Executable("hs_app.py", base=base)])
