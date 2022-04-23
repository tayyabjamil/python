

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def findClickPositions(obj, screenshot):

    img_rgb = cv.imread('fireman.png', cv.IMREAD_GRAYSCALE)
    # img_gray = cv.cvtColor(img_rgb, 0)
    w = img_rgb.shape[1]
    h = img_rgb.shape[0]

    screen = cv.imread('game.jpg', cv.IMREAD_GRAYSCALE)
    # screen_grey = cv.cvtColor(screen, cv.IMREAD_GRAYSCALE)
    # screen_grey = cv.cvtColor(templete, 0)

    res = cv.matchTemplate(screen, img_rgb, cv.TM_CCOEFF_NORMED)
    threshold = 0.4
    loctions = np.where(res >= threshold)
    new = list(zip(*loctions[::1]))

    for loc in new:

        top_left = (int(loc[0]), int(loc[1]))
        bottom_right = (int(top_left[0]) + w, int(top_left[1]) + h)
        cv.rectangle(screen, top_left, bottom_right,
                     (0, 255, 0), cv.LINE_4)
    cv.imshow('res.png', screen)
