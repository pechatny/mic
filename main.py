__author__ = 'Dmitry Pechatnikov'
# import sys
from Config import Config
import cv2
import numpy as np
# import os


def find_contours(image):
        (_, contours, hierarchy) = cv2.findContours(image, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
        return contours

#TODO: camerainicialization

if __name__ == '__main__':
    config = Config()

    print(config.width)
    print(config.height)
    # cam = cv2.VideoCapture('./data/test.wmv')
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()

        imgret, img = cv2.threshold(frame, 100, 254, 244)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 200, 100)
        contours = find_contours(edged)

        cv2.drawContours(frame, contours, -1, (44, 155, 33), 3)
        # frame = frame
        cv2.imshow('video', frame)
        cv2.waitKey(44)
        print(ret)
        if (0xFF & cv2.waitKey(5) == 27) or frame.size == 0:
            break
