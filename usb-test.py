from inputs import get_gamepad
import buttons
import Pypad
import numpy as np 
import cv2 as cv 

GamePad = Pypad.Input
GamePad.start()

while True:
    events = get_gamepad()


    #print("RIGHT VERTICAL: ", gamepad.GamePad.get_axis("RVERTICAL"))
    #print("RIGHT HORIZONTAL", gamepad.GamePad.get_axis("RHORIZONTAL"))
    #print("LEFT HORIZONTAL",gamepad.GamePad.get_axis("LHORIZONTAL"))
    #print("LEFT VERTICAL", gamepad.GamePad.get_axis("LVERTICAL"))


    for event in events:
        if event.code == buttons.CIRCLE.get_code():
            exit(0)

    

