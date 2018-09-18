"""
Testing OpenCV (Webcam pc computer, img to b&n)

MRH
"""

import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Ajuste HSV")

cv2.createTrackbar("H Min","Ajuste HSV", 0,255,nothing)
cv2.createTrackbar("S Min","Ajuste HSV", 0,255,nothing)
cv2.createTrackbar("V Min","Ajuste HSV", 0,255,nothing)
cv2.createTrackbar("H Max","Ajuste HSV", 0,255,nothing)
cv2.createTrackbar("S Max","Ajuste HSV", 0,255,nothing)
cv2.createTrackbar("V Max","Ajuste HSV", 0,255,nothing)




def show_webcam(mirror=True):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror: 

            al = cv2.getTrackbarPos("H Min","Ajuste HSV")
            bl = cv2.getTrackbarPos("S Min","Ajuste HSV")
            cl = cv2.getTrackbarPos("V Min","Ajuste HSV")
            dl = cv2.getTrackbarPos("H Max","Ajuste HSV")
            el = cv2.getTrackbarPos("S Max","Ajuste HSV")
            fl = cv2.getTrackbarPos("V Max","Ajuste HSV") 
           

            l_blue = np.array((al,bl,cl),np.uint8)
            u_blue = np.array((dl,el,fl),np.uint8)
            #l_blue[:]=[dl,el,fl]
            #u_blue[:]=[al,bl,cl]



            img = cv2.flip(img, 1)
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, l_blue, u_blue)
            res = cv2.bitwise_and(img,img, mask= mask)

        cv2.imshow('Original', img)
 #      cv2.imshow('Blanco y negro', gray_image)
        cv2.imshow("Mascara", mask)
        cv2.imshow("Ajuste HSV", res)

        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()