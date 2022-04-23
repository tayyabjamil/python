from time import time
import cv2 as cv
import numpy as np
import pyautogui
from PIL import ImageGrab
loop_time = time()
while(True):
    screenshot = ImageGrab.grab()
    # screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
    cv.imshow('Screen Shot', screenshot)
    print('FPS {}'.format(1/(time()-loop_time)))
    loop_time = time()
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()
print('Done')
