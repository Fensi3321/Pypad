#   TRIANGLE => BTN_NORTH
#   CIRCLE => BTN_EAST     
#   CROSS => BTN_SOUTH
#   SQAURE => BTN_WEST  
#   SELECT => BTN_SELECT
#   START => BTN_START
#   D_UP => BTN_DPAD_UP
#   D_DOWN => BTN_DPAD_DOWN
#   D_RIGHT => BTN_DPAD_RIGHT
#   D_LEFT => BTN_DPAD_LEFT

#   L1 => BTN_TL
#   R1 => BTN_TR
#   R2 => BTN_TR2
#   R3 => BTN_THUMBR
#   L3 => BTN_THUMBL
#   L2 => BTN_TL2
#   PS_BTTN => BTN_BTN_MODE

# TRIGGER VALUE => ABS_Z / ABS_RZ

from inputs import get_gamepad

class Button:

    def __init__(self, code, name):
        self.__code = code
        self.__name = name

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

class Stick:

    def __init__(self,code ,code_vertical, code_horizontal, name, number_of_axes=2):
        self.__name = name

        if number_of_axes == 2:
            self.__axis = [None, None]    
            self.__axis[0] = code_vertical
            self.__axis[1] = code_horizontal
        elif number_of_axes == 1:
            self.__axis = code_vertical


    def get_code(self, axis):
        return self.__axis[axis]

    def get_name(self):
        return self.__name


# Buttons
TRIANGLE = Button("BTN_NORTH", "Triangle")
CIRCLE = Button("BTN_EAST", "Circle")
CROSS = Button("BTN_SOUTH", "Cross")
SQUARE = Button("BTN_WEST", "Square")
SELECT = Button("BTN_SELECT", "Select")
START = Button("BTN_START", "Start")
D_UP = Button("BTN_DPAD_UP", "D-pad Up")
D_DOWN = Button("BTN_DPAD_DOWN", "D-pad Down")
D_LEFT = Button("BTN_DPAD_LEFT", "D-pad Left")
D_RIGHT = Button("BTN_DPAD_RIGHT", "D-pad Right")
PS_BTTN = Button("BTN_MODE", "PS Button")
L1 = Button("BTN_TL", "L1")
L2 = Button("BTN_TL2", "L2")
L3 = Button("BTN_THUMBL", "L3")
R1 = Button("BTN_TR", "R1")
R2 = Button("BTN_TR2", "R2")
R3 = Button("BTN_THUMBR", "R3")

__all_buttons = [TRIANGLE, CIRCLE, CROSS, SQUARE, SELECT, START, D_UP, D_DOWN, D_LEFT, D_RIGHT, PS_BTTN, L1, L2, L3, R1, R2, R3]

def get_buttons():
    return __all_buttons


# Sticks
RIGTH_THUMB = Stick("ABS_RY", "ABS_RX", "Thumb Right", 2)
LEFT_THUMB = Stick("ABS_Y", "ABS_X", "Thumb Left", 2)
RIGHT_TRIGGER = Stick("ABS_RZ", None, "Right Trigger", 1)
LEFT_TRIGGER = Stick("ABS_Z", None, "Left Trigger", 1)

__all_sticks = [RIGTH_THUMB, LEFT_THUMB, RIGHT_TRIGGER, LEFT_TRIGGER]

def get_sticks():
    return __all_sticks
