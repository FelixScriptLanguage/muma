import keyboard
def on_press(event):
    print(event.name)
keyboard.on_press(on_press)
keyboard.wait()