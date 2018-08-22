import sys

from cx_Freeze import setup, Executable

base = "Win32GUI"
#path_platforms = ( "..\..\..\PyQt4\plugins\platforms\qwindows.dll", "platforms\qwindows.dll" )
#build_options = {"includes" : [ "re", "atexit" ], "include_files" : [ path_platforms ]}

setup(
    name = "APNOZ",
    version = "2.2",
    description = "APNOZ",
    #options = {"build_exe" : build_options},
    executables = [Executable("main_window.py", base = base)]
    )
