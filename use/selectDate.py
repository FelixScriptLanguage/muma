sg = PySimpleGUI
sg.theme('Default 1')
layout = [
    [sg.CalendarButton(button_text='选择'),sg.In(key='color')],
    [sg.B('确认')]
]
window = sg.Window('Select Date', layout)

while True:
    event, values = window.read()
    if event == None:
        break
    elif event == '确认':
        key = values['color']
        send(key)
        break

window.close()