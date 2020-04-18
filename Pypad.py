import buttons
from threading import Thread
from inputs import get_gamepad

### REFACTOR THIS SHIT

class __Input(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.A = 0
        self.B = 0
        self.X = 0
        self.Y = 0
        self.LBumper = 0
        self.RBumper = 0
        self.LThumb = 0
        self.RThumb = 0
        self.LTrigger = 0
        self.RTrigger = 0
        self.Select = 0
        self.Start = 0
        self.LStickX = 0
        self.LStickY = 0
        self.RStickX = 0
        self.RStickY = 0
        self.DPadUp = 0
        self.DPadDown = 0
        self.DPadLeft = 0
        self.DPadRight = 0


    def run(self):
        CENTER_MAX = 128 + 25
        CENTER_MIN = 128 - 25

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

        while True:
            for event in get_gamepad():
                if event.ev_type == "Key":
                   bttn = get_button(event.code)
                   bttn.set_state(event.state)

                elif event.ev_type == "Absolute":
                    analog = get_analog(event.code)

                    if CENTER_MIN <= event.state <= CENTER_MAX:
                        event.state = 0
                    
                    analog.set_state(event.state)


Input = __Input()

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
