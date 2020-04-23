import Pypad
import buttons

import numpy as np 
import cv2 as cv 

GamePad = Pypad.Input
GamePad.listen()

pos_x = 320
pos_y = 320


while True:
    r_stick = GamePad.analog_input("Left")
    img = np.zeros((720, 1080, 3), np.uint8)


    x = r_stick[0]
    y = r_stick[1]

    x *= 10
    y *= 10

    x = int(x)
    y = int(y)


    cv.waitKey(1)

    cv.rectangle(img, (pos_x, pos_y), (pos_x + 20, pos_y + 20), (255, 0, 0), 3)
    cv.imshow("analog", img)

    pos_x += x
    pos_y += y

