# -*- coding: utf-8 -*-
import os
import threading
import time

f1 = threading.Thread(target=lambda : os.system('python 1.py'))
f2 = threading.Thread(target=lambda : os.system('python 2.py'))
f3 = threading.Thread(target=lambda : os.system('python 3.py'))
f1.start()
f2.start()
time.sleep(5)
f3.start()