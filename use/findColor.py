sg = PySimpleGUI
sg.theme('Default 1')
layout = [
    [sg.ColorChooserButton(button_text='选择'),sg.In(key='color')],
    [sg.B('确认')]
]

window = sg.Window('Choose a color', layout)

while True:
    event, values = window.read()
    if event == None:
        break
    elif event == '确认':
        key = values['color']
        send(key)
        break

window.close()
