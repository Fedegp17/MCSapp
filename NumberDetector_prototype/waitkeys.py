import cv2

"""Created by: Ing. Antonio Gómez Ruiz
01/16/2024 """

"""Python script for recognizing the return value when a key is pressed while using the method 'cv2.waitKey()' of the
   cv2 library. With this code we can know the value and use more keys, for example to give instructions."""

# First we load an image from our computer
img = cv2.imread('Imagenes/Monitor.png')

flag = True
while flag:
    cv2.imshow('img', img)
    k = cv2.waitKey(1)
    if k == 27:    # Esc key to stop
        print(k)
        flag = False
    elif k == -1:  # normally -1 returned,so don't print it
        continue
    else:
        print(k)
