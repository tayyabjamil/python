from time import time
import cv2 as cv
import numpy as np
import cv2 as cv

from windowCapture import windowCapture
from multipleImagesRectangles import findClickPositions
# windowCapture.listwindowNames()
# exit()
wincap = windowCapture(
    'File Explorer')


loop_time = time()
while(True):
    screenshot = wincap.get_screenshot()
    cv.imshow('Screen Shot', screenshot)
    print('FPS {}'.format(1 / (time() - loop_time)))
    findClickPositions('onedrive.png', screenshot)
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


# window_capture()

# cv.destroyAllWindows()
print('Done')
