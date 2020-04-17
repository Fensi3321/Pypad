import buttons
from inputs import get_gamepad

__btns = buttons.get_buttons()
__stcks = buttons.get_sticks()

### REFACTOR THIS SHIT

class Input:
    
    def __init__(self):
        self.current = 0
        self.previous = 0
        self.min_delta = 1


    def get_axis(self, axis):
        events = get_gamepad()


        for event in events:
            if axis == "LHORIZONTAL" and event.code == buttons.LEFT_THUMB.get_code(0):
                if event.state < 110:
                    return -1
                elif event.state > 135:
                    return 1
                else: return 0

            elif axis == "LVERTICAL" and event.code == buttons.LEFT_THUMB.get_code(1):
                if event.state < 110:
                    return -1
                elif event.state > 135:
                    return 1
                else: return 0
    
            elif axis == "RVERTICAL" and event.code == buttons.RIGTH_THUMB.get_code(1):
                if event.state < 110:
                    return -1
                elif event.state > 135:
                    return 1
                else: return 0

            elif axis == "RHORIZONTAL" and event.code == buttons.RIGTH_THUMB.get_code(0):
                if event.state < 110:
                    return -1
                elif event.state > 135:
                    return 1
                else: return 0
            
        return 0

GamePad = Input()
