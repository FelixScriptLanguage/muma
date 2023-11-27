cd = easygui.codebox(msg='Please enter the program')
send(cd)
try:
    exec(cd)
except Exception as a:
    easygui.msgbox(str(a))