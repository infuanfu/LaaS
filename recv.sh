#!/bin/sh
sudo python recv/recv.py | sudo LD_LIBRARY_PATH=/usr/local/lib PYSDL2_DLL_PATH=/usr/local/lib python mixer/mix.py
