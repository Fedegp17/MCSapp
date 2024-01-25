import cv2
import pytesseract

"""Created by: Ing. Antonio Gómez Ruiz
01/24/2024 """

"""Overall Notes:
   This code is for testing how we can ask the user how many segments he wants to take from the image and to allow
   him to re-size each of those segments. Using this code logic we can create as much segments as de user needs
   and determine the size and location that each segment should have"""

# Start variables for the height and the width
"Height - std values w = 30 , x = 50"
w = 30
x = 30
"Width - std values y = 110, z = 100"
y = 200
z = 130

# Number recognition program - Page segmentation functionality
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

num_segmentos = 3
contador = 0
segmentos = []

img = cv2.imread('Imagenes/Monitor.png')
cv2.imshow("Monitor original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

while contador < num_segmentos:

    cuadro_monitor = cv2.rectangle(img, (w, x), (y, z), (255, 0, 0), 1)
    cv2.imshow(f"Monitor delimitado", cuadro_monitor)
    cv2.waitKey(0)

    img = cv2.imread('Imagenes/Monitor.png')

    segmentos.append(img[x: z, w: y])

    cv2.imshow(f"Monitor cortado {contador + 1}", segmentos[contador])
    cv2.waitKey(0)
    x += 20
    y += 20
    z += 20
    w += 20

    contador += 1
