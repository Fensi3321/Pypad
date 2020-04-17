from inputs import get_gamepad
import buttons

while True:
    events = get_gamepad()

    for event in events:
        for stick in buttons.get_sticks():
            if event.code == stick.get_code(0):
                print("Stick vertical: ", stick.get_name())
            elif event.code == stick.get_code(1):
                print("Stick horizontal: ", stick.get_name())
        
        for button in buttons.get_buttons():
            if event.code == button.get_code():
                print("Button: ", button.get_name())
