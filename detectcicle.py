#! /usr/bin/env python

import numpy as np
import cv2

cap = cv2.VideoCapture(1)

eye_cascade = cv2.CascadeClassifier('/usr/share/OpenCV/haarcascades/haarcascade_eye.xml')

while 1:
    ret, frame = cap.read()

    #frame = captura.copy()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    img_gray = cv2.medianBlur(gray,5)
    eyes = eye_cascade.detectMultiScale(frame, 1.3, 2)

    for (ex,ey,ew,eh) in eyes:
        #cv2.rectangle(frame,(ex+int(ew/4),ey+int(eh/4)),(ex+int(3*ew/4),ey+int(3*eh/4)),(0,255,0),2)

        eye_gray = gray[ey+int(eh/4):ey+int(3*eh/4), ex+int(ew/4):ex+int(3*ew/4)]
        eye_color = frame[ey+int(eh/4):ey+int(3*eh/4), ex+int(ew/4):ex+int(3*ew/4)]

        iris = cv2.HoughCircles(eye_gray, cv2.HOUGH_GRADIENT,2,100,param1=50,param2=30,minRadius=0,maxRadius=0)

        #print(iris)


        try:
            #iris = np.uint16(np.around(iris))
            iris = np.uint16(np.around(iris))
            if iris is not None:
                for (xi, yi, ri) in iris[0,:]:
                    #cv2.circle(eye_color,(xi,yi), ri,(0, 0, 255),2)
                    #cv2.rectangle(eye_color, (xi-ri, yi-ri), (xi+ri, yi+ri), (0,255,0), 2)
                    so_iris_color = eye_color[yi-ri:yi+ri, xi-ri:xi+ri]
                    so_iris_gray = eye_gray[yi-ri:yi+ri, xi-ri:xi+ri]

                    so_iris = cv2.HoughCircles(so_iris_gray, cv2.HOUGH_GRADIENT,2,100,param1=50,param2=30,minRadius=0,maxRadius=ri)
                    so_iris = np.uint16(np.around(so_iris))
                    if so_iris is not None:
                        for (xc, yc, rc) in so_iris[0,:]:
                            cv2.circle(so_iris_color,(xc,yc), rc,(255, 0, 0),2)

                            tramento = 0.5

                            R_iris = int(rc * tramento)

                            pupila_color = so_iris_color[yc-R_iris:yc+R_iris, xc-R_iris:xc+R_iris]

                            pupila_gray = so_iris_gray[yc-R_iris:yc+R_iris, xc-R_iris:xc+R_iris]


                            pupila = cv2.HoughCircles(pupila_gray, cv2.HOUGH_GRADIENT,2,100,param1=50,param2=30,minRadius=0,maxRadius=ri)
                            pupila= np.uint16(np.around(pupila))
                            if pupila is not None:
                                for (xp, yp, rp) in pupila[0,:]:
                                    cv2.circle(pupila_color, (xp, yp), rp, (255, 255, 255), 4)

        except Exception as error:
            print(error)

    cv2.imshow('VideoCaptura',frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
