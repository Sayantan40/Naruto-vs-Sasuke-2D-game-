from cx_Freeze import *
import sys
sys.argv.append("build")

from cx_Freeze import setup, Executable


build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}


base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Narutp shippuden",
        version = "0.1",
        description = "Naruto vs Saske game...Dattebayo",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Naruto.py", base=base, icon='pics\\Naruto.ico')])


