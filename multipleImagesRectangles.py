
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def findClickPositions(obj, screenshot):

    img_rgb = cv.imread(obj)
    img_gray = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    template = cv.imread(obj, 0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.95
    # loctionsnew = np.where(res >= threshold)
    locations = np.where(res >= threshold)
    locationsnew = list(zip(*locations[::-1]))

    rectangles = []

    if(len(locationsnew)):

        for loc in locationsnew:

            react = [int(loc[0]), int(loc[1]), w, h]
            rectangles.append(react)
            rectangles.append(react)

            line_color = (0, 255, 0)
            line_type = cv.LINE_4
            marker_color = (255, 0, 255)
            marker_type = cv.MARKER_CROSS
            rectanglesNew, weights = cv.groupRectangles(rectangles, 1, 0.5)

        # for pt in zip(*rectanglesNew[::-1]):
            if(len(rectanglesNew)):

                for (x, y, w, h) in rectanglesNew:

                    top_left = (x, y)
                    bottom_right = (x + w, y + h)
                    # Draw the box
                    cv.rectangle(screenshot, top_left, bottom_right, color=line_color,
                                 lineType=line_type, thickness=2)
            cv.imshow('res.png', screenshot)
