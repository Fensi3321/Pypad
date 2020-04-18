import Pypad
import buttons

import numpy as np 
import cv2 as cv 

GamePad = Pypad.Input
GamePad.listen()



posX = 20
posY = 20

while True:

    img = np.zeros((720, 720, 3), np.uint8)

    cv.waitKey(1)

    cv.rectangle(img, (posX, posY), (posX + 20, posY + 20), (255, 0, 0), 3)

    cv.imshow("img", img)


    input_x = GamePad.get_dpad(axis="Horizontal")
    input_y = GamePad.get_dpad(axis="Vertical")


    posX += input_x
    posY -= input_y



