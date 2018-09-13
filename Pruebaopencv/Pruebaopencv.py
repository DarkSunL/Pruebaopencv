"""
Testing OpenCV (Webcam pc computer, img to b&n)

MRH
"""

import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Configuracion Tono Azul")

cv2.createTrackbar("AL","Configuracion Tono Azul", 0,255,nothing)
cv2.createTrackbar("BL","Configuracion Tono Azul", 0,255,nothing)
cv2.createTrackbar("CL","Configuracion Tono Azul", 0,255,nothing)
cv2.createTrackbar("DL","Configuracion Tono Azul", 0,255,nothing)
cv2.createTrackbar("EL","Configuracion Tono Azul", 0,255,nothing)
cv2.createTrackbar("FL","Configuracion Tono Azul", 0,255,nothing)


def show_webcam(mirror=True):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror: 

            al = cv2.getTrackbarPos("AL","Configuracion Tono Azul")
            bl = cv2.getTrackbarPos("BL","Configuracion Tono Azul")
            cl = cv2.getTrackbarPos("CL","Configuracion Tono Azul")
            dl = cv2.getTrackbarPos("AL","Configuracion Tono Azul")
            el = cv2.getTrackbarPos("BL","Configuracion Tono Azul")
            fl = cv2.getTrackbarPos("CL","Configuracion Tono Azul") 
           
            l_blue[:]=[dl,el,fl]
            u_blue[:]=[al,bl,cl]

#            l_blue = np.array([al,bl,cl])
#            u_blue = np.array([dl,el,fl]) 

            img = cv2.flip(img, 1)
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, l_blue, u_blue)
            res = cv2.bitwise_and(img,img, mask= mask)

        cv2.imshow('Original', img)
 #      cv2.imshow('Blanco y negro', gray_image)
 #      cv2.imshow("Mascara", mask)
        cv2.imshow("Resultado", res)

        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()