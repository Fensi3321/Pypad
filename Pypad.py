import buttons
from threading import Thread
from inputs import get_gamepad

### REFACTOR THIS SHIT

class __Input(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):

        def get_button(code):
            code_to_bttn = {
                "BTN_NORTH" : buttons.TRIANGLE,
                "BTN_EAST" : buttons.CIRCLE,
                "BTN_SOUTH" : buttons.CROSS,
                "BTN_WEST" : buttons.SQUARE,
                "BTN_SELECT" : buttons.SELECT,
                "BTN_START" : buttons.START,
                "BTN_DPAD_UP" : buttons.D_UP,
                "BTN_DPAD_DOWN" : buttons.D_DOWN,
                "BTN_DPAD_RIGHT" : buttons.D_RIGHT,
                "BTN_DPAD_LEFT" : buttons.D_LEFT,
                "BTN_TL" : buttons.L1,
                "BTN_TL2" : buttons.L2,
                "BTN_THUMBL" : buttons.L3,
                "BTN_TR" : buttons.R1,
                "BTN_TR2" : buttons.R2,
                "BTN_THUMBR" : buttons.R3,
                "BTN_MODE" : buttons.PS_BTTN
            }
            return code_to_bttn.get(code)

        def get_analog(code):
            mapper = {
                "ABS_X" : buttons.L_STICKX,
                "ABS_Y" : buttons.L_STICKY,
                "ABS_RX" : buttons.R_STICKX,
                "ABS_RY" : buttons.R_STICKY,
                "ABS_Z" : buttons.L_TRIGGER,
                "ABS_RZ" : buttons.R_TRIGGER
            }
            return mapper.get(code)

        CENTER_MAX = 128 + 25
        CENTER_MIN = 128 - 25

        analogs = buttons.get_analogs()

        while True:
            for event in get_gamepad():
                if event.ev_type == "Key":
                    bttn = get_button(event.code)
                    bttn.set_state(event.state)

                elif event.ev_type == "Absolute":
                    analog = get_analog(event.code)

                    # hacky AF
                    event.state /= 255
                    event.state -= .5
                    event.state *= 2
                    event.state = float("{:.2f}".format(event.state))

                    analog.set_state(event.state)

    def get_key(self, key):
        keys = buttons.get_buttons()

        for button in keys:
            if button.get_name() == key or button.get_code() == key or button == key:
                return button.state
            
            if key == "Any" and button.state > 0:
                return 1

    def get_dpad(self, axis=None):
        # vertical
        d_up = self.get_key(buttons.D_UP)
        d_down = self.get_key(buttons.D_DOWN)

        # horizontal
        d_left = self.get_key(buttons.D_LEFT)
        d_right = self.get_key(buttons.D_RIGHT)

        if axis == "Horizontal":
            if d_right > 0:
                return 1
            if d_left > 0:
                return -1
            else: return 0

        if axis == "Vertical":
            if d_up > 0:
                return 1
            if d_down > 0:
                return -1
            else: return 0
        else: raise KeyError("Error! Axis not found")

    
    def analog_input(self, hand):

        input_x = 0
        input_y = 0

        if hand == "Right":
            input_x = buttons.R_STICKX.state
            input_y = buttons.R_STICKY.state
        elif hand == "Left":
            input_x = buttons.L_STICKX.state
            input_y = buttons.L_STICKY.state
        else: raise KeyError("Error! Analog Axis not found")

        print(input_x, input_y)

        return (input_x, input_y)    

    def listen(self):
        self.start()

        


Input = __Input()