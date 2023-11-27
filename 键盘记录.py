# -*- coding: utf-8 -*-
ip = input('Specify IP (If empty, listen to all) >>')
while True:
    op = open('./kbd.txt', 'r').read()
    if ip.replace(' ','') == '':
        if op == '':
            continue
        print(op)
        open('./kbd.txt', 'w').write('')
    elif op.split(':')[0] == ip:
        if op == '':
            continue
        print(op)
        open('./kbd.txt', 'w').write('')