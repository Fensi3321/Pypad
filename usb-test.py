import Pypad

def test():
    Gamepad = Pypad.Input
    Gamepad.listen()

    while True:
        if Gamepad.get_key("Circle"):
            print(Pypad.buttons.CIRCLE.get_name(), " : ", Pypad.buttons.CIRCLE.state)
        else: print(Pypad.buttons.CIRCLE.get_name(), " : ", Pypad.buttons.CIRCLE.state)

if __name__ == "__main__":
    test()
