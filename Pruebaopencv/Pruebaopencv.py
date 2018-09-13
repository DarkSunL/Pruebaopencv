"""
Testing OpenCV (Webcam pc computer, img to b&n)

MRH
"""

import cv2
import numpy as np

l_blue = np.array([110,50,50])
u_blue = np.array([130,255,255])

def show_webcam(mirror=True):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, l_blue, u_blue)
            res = cv2.bitwise_and(img,img, mask= mask)
        cv2.imshow('Original', img)
        cv2.imshow('Blanco y negro', gray_image)
        cv2.imshow("Mascara", mask)
        cv2.imshow("Resultado", res)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()