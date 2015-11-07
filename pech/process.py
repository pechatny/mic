__author__ = 'Dmitry Pechatnikov'
class Process:
    def find_contours(image):
        (_, contours, hierarchy) = cv2.findContours(image, mode=cv2.cv.CV_RETR_EXTERNAL, method=cv2.cv.CV_CHAIN_APPROX_SIMPLE)
        return contours
