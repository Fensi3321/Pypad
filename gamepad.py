import buttons
from inputs import get_gamepad

__btns = buttons.get_buttons()
__stcks = buttons.get_sticks()

class Input:
    
    def __init__(self):
        self.current = 0
        self.previous = 0
        self.min_delta = 3


    def get_axis(self, axis):
        events = get_gamepad()

        self.previous = self.current

        for event in events:
            if axis == "LHORIZONTAL" and event.code == buttons.LEFT_THUMB.get_code(0):
                self.current = event.state

                if self.current - self.previous >= self.min_delta:
                    return self.current

            elif axis == "LVERTICAL" and event.code == buttons.LEFT_THUMB.get_code(1):
                self.current = event.state

                if self.current - self.previous >= self.min_delta:
                    return self.current
    
            elif axis == "RVERTICAL" and event.code == buttons.RIGTH_THUMB.get_code(1):
                self.current = event.state

                if self.current - self.previous >= self.min_delta:
                    return self.current

            elif axis == "RHORIZONTAL" and event.code == buttons.RIGTH_THUMB.get_code(0):
                self.current = event.state

                if self.current - self.previous >= self.min_delta:
                    return self.current
            
        return 0

GamePad = Input()
