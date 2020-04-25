import buttons
from threading import Thread
from inputs import get_gamepad

class __Input(Thread):
    def __init__(self):
        Thread.__init__(self)
        Thread.setDaemon(self, True)

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
            }
            return mapper.get(code)

        def get_trigger(code):
            mapper = {
                "ABS_Z" : buttons.L_TRIGGER,
                "ABS_RZ" : buttons.R_TRIGGER
            }
            return mapper.get(code)

        analogs = buttons.get_analogs()
        triggers = buttons.get_triggers()

        while True:
            for event in get_gamepad():
                analog = get_analog(event.code)
                bttn = get_button(event.code)
                trigger = get_trigger(event.code)

                if event.ev_type == "Key":
                    bttn.set_state(event.state)

                elif event.ev_type == "Absolute":
                    temp = event.state
                    if analog in analogs:
                        event.state /= 256
                        event.state -= .5
                        event.state *= 2
                        event.state = float("{:.1f}".format(event.state))
                        analog.set_state(event.state)
                    elif trigger in triggers:
                        trigger.set_state(temp)

                    
    def get_key(self, key):
        """Gets key input from gamepad

        Arguments:
            key String -- name of the button or code of the button. If argument is "Any" gets input from any key pressed.

        Returns:
            Integer -- returns button state. Either 1 or 0. 
        """
        keys = buttons.get_buttons()

        for button in keys:
            if button.get_name() == key or button.get_code() == key:
                return button.state
            
            if key == "Any" and button.state > 0:
                return 1

    def get_dpad(self, axis=None):
        """Gets input data from gamepad's dpad

        Keyword Arguments:
            axis String -- axis of interest. Available: Vertical or Horizontal

        Raises:
            KeyError: when given axis is not either Vertical or Horizontal

        Returns:
            Integer -- returns either -1 or 1
        """
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
        else: raise KeyError("Error!", axis ,"axis not found")
    
    def analog_input(self, side):
        """Gets input data from gamepad's analog sticks.

        Arguments:
            side String -- side of the gamepad. Available arguments: Right or Left

        Raises:
            KeyError: when argument passed is not either Left or Right

        Returns:
            Tuple -- tuple of values in range -1, 1 based on position of analog sticks inclusive. Neutral position is (0, 0) 
        """

        input_x = 0
        input_y = 0

        if side == "Right":
            input_x = buttons.R_STICKX.state
            input_y = buttons.R_STICKY.state
        elif side == "Left":
            input_x = buttons.L_STICKX.state
            input_y = buttons.L_STICKY.state
        else: raise KeyError("Error!", side, " analog Axis not found")

        return (input_x, input_y)


    def get_trigger(self, side):
        """Gets gamepad's trigger input data

        Arguments:
            side String -- side of the gamepad. Available arguments: Right or Left

        Raises:
            KeyError: when argument passed is not either Left or Right

        Returns:
            Integer -- returns integer in range 0 - 255 inclusive
        """
        if side == "Right":
            return buttons.R_TRIGGER.state
        elif side == "Left":
            return buttons.L_TRIGGER.state
        else: raise KeyError("Error!", side, " not found!")

    def listen(self):
        """Starts listening input data from the gamepad on separate thread.
        """
        self.start()



Input = __Input()