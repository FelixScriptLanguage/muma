# -*- coding: utf-8 -*-
import os
while True:
    if input('enter "exit" to exit >>') == 'exit':
        os.system('taskkill /f /im python.exe')