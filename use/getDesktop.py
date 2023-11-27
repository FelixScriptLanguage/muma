def desk():
    if platform.system() == "Darwin":
        return os.path.expanduser("~/Desktop/")
    elif platform.system() == "Windows":
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        return winreg.QueryValueEx(key, "Desktop")[0] + "\\"
    else:
        return os.path.expanduser("~/Desktop/")
send(desk())