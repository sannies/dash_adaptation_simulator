dash_adaptation_simulator
=========================

Simulate bitrate switching algorithms based on real data traces

Requirements:
- matplotlib
- numpy

Windows Users:
--------------

pip can't install scipy and numpy
Download them here:

* NumPy: http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
* SciPy: http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy

and install in your venv (after executing Scripts/activate) by executing easy_install "c:\Users\sannies\Downloads\numpy-MKL-1.9.1.win-amd64-py3.4.exe"

Additionally you'll need TCL/TK. I had no luck with any version besides 8.6.1 (exactly this version!!!). Download here:

https://bitbucket.org/tombert/tcltk/downloads



Usage:
simulate.py -frates.hdx.csv
