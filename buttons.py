class __Button:

    def __init__(self, code, name):
        self.__code = code
        self.__name = name
        self.state = 0

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

    def set_state(self, state):
        self.state = state

class __Analog:

    def __init__(self, code, name):
        self.__code = code
        self.__name = name
        self.state = 0

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

    def set_state(self, state):
        self.state = state

class __Trigger:
    
    def __init__(self, code, name):
        self.__code = code
        self.__name = name
        self.state = 0

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

    def set_state(self, state):
        self.state = state


# Buttons
TRIANGLE = __Button("BTN_NORTH", "Triangle")
CIRCLE = __Button("BTN_EAST", "Circle")
CROSS = __Button("BTN_SOUTH", "Cross")
SQUARE = __Button("BTN_WEST", "Square")
SELECT = __Button("BTN_SELECT", "Select")
START = __Button("BTN_START", "Start")
D_UP = __Button("BTN_DPAD_UP", "D-pad Up")
D_DOWN = __Button("BTN_DPAD_DOWN", "D-pad Down")
D_LEFT = __Button("BTN_DPAD_LEFT", "D-pad Left")
D_RIGHT = __Button("BTN_DPAD_RIGHT", "D-pad Right")
PS_BTTN = __Button("BTN_MODE", "PS Button")
L1 = __Button("BTN_TL", "L1")
L2 = __Button("BTN_TL2", "L2")
L3 = __Button("BTN_THUMBL", "L3")
R1 = __Button("BTN_TR", "R1")
R2 = __Button("BTN_TR2", "R2")
R3 = __Button("BTN_THUMBR", "R3")

# Analogs
L_STICKX = __Analog("ABS_X", "Left Stick X")
L_STICKY = __Analog("ABS_Y", "Left Stick Y")
R_STICKY = __Analog("ABS_RY", "Right Stick X")
R_STICKX = __Analog("ABS_RX", "Right Stick Y")

# Triggers
R_TRIGGER = __Trigger("ABS_RZ", "Right Trigger")
L_TRIGGER = __Trigger("ABS_Z", "Left Trigger")

__all_triggers = [L_TRIGGER, R_TRIGGER]
__all_analogs = [L_STICKX, L_STICKY, R_STICKX, R_STICKY]
__all_buttons = [TRIANGLE, SQUARE, CROSS, CIRCLE, R1, R2, R3, D_DOWN, D_LEFT, D_RIGHT, D_UP, L1, L2, L3, SELECT, START, PS_BTTN]

def get_triggers():
    return __all_triggers
def get_analogs():
    return __all_analogs
def get_buttons():
    return __all_buttons