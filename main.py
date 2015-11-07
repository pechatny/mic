__author__ = 'Dmitry Pechatnikov'
import tkinter as tk

from PIL import Image, ImageTk
import cv2

from Config import Config

# import os

config = Config()


def find_contours(image):
    (_, contours, hierarchy) = cv2.findContours(image, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    return contours


def open_camera(cam_id=0):
    cap = cv2.VideoCapture(cam_id)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, float(config.height))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, float(config.width))
    cap.set(cv2.CAP_PROP_FPS, float(config.fps))
    return cap


def open_video(videoName=config.video_name):
    cap = cv2.VideoCapture(videoName)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, float(config.height))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, float(config.width))
    cap.set(cv2.CAP_PROP_FPS, float(config.fps))
    return cap


def process_image(frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        imgret, img = cv2.threshold(gray, 100, 254, 244)
        edged = cv2.Canny(img, 200, 100)
        return edged


def show_frame():
    ret, frame = cam.read()

    #left to right flip
    frame = cv2.flip(frame, 1)

    #processin frame from camera
    image = process_image(frame)

    contours = find_contours(image)

    cv2.drawContours(frame, contours, -1, (44, 155, 33), 3)

    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)


if __name__ == '__main__':
    # print(config.__dict__)
    # cam = cv2.VideoCapture('./data/test.wmv')
    cam = open_camera()
    # cam = open_video()

    root = tk.Tk()
    root.bind('<Escape>', lambda e: root.quit())
    lmain = tk.Label(root)
    lmain.pack()

    show_frame()
    root.mainloop()
    # while True:
    #     #read image from cam
    #     ret, frame = cam.read()
    #
    #     #left to right flip
    #     frame = cv2.flip(frame, 1)
    #
    #     #processin frame from camera
    #     image = process_image(frame)
    #
    #     contours = find_contours(image)
    #
    #     cv2.drawContours(frame, contours, -1, (44, 155, 33), 3)
    #
    #     cv2.imshow('video', frame)
    #     cv2.waitKey(44)
    #     # print(ret)
    #     if (0xFF & cv2.waitKey(5) == 27) or frame.size == 0:
    #         break
