"""Setup script"""
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
DIR = "assets"
BUILD_EXE_OPTIONS = {
    "packages": ["gi", "random", "playsound"],
    "include_files": DIR
}

# GUI applications require a different base on Windows (the default is for a
# console application).
BASE = None
if sys.platform == "win32":
    BASE = "Win32GUI"

setup(name="H's App",
      version="0.1",
      description="H's App",
      options={"build_exe": BUILD_EXE_OPTIONS},
      executables=[Executable("hs_app.py", base=BASE)])
