import cv2
import pytesseract

"""Created by: Ing. Antonio Gómez Ruiz
01/16/2024 """

"""Overall notes of the program:

How to take a picture using the webcam of the computer:
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

Problems to use Pytesseract please refer to:
'https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i'
"""

# Programa para reconocimiento de números

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

"First we load the desired image"
imagen = cv2.imread('numeros.png')
"""With this we can now the widht and heigh of the image
        rows, cols, _ = imagen.shape
        print(f'Los pixeles de filas son {rows} y de las columnas son {cols}')
After running this code, we now know that the image is 675 x 1200 pxls """

"""This will show in  window the image that we choose"""
cv2.imshow('imagen', imagen)
cv2.waitKey(0)

imagen_cortada = imagen[0: 300, 0:600]
cv2.imshow('Imagen recortada', imagen_cortada)

cv2.waitKey(0)
cv2.destroyAllWindows()


def identify_number(img):
    """This will allow us to transform the choosen image to one in a gray scale"""
    imagen_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('imagen gris', imagen_gris)
    cv2.waitKey(0)

    """Thresholding == 'umbral' o 'umbralización'
    The function threshold returns a tuple, and the funtion 'cv2.imshow' only shows 'arrays', therefore this is 
    solved by adding the '[1]' at the end of the method 'threshold'. In case further doubts show up, print the variable 
    type"""
    imagen_procesada = cv2.threshold(imagen_gris, 80, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('imagen procesada', imagen_procesada)
    cv2.waitKey(0)

    """With this section we use pytesseract to analyze the processed image and detect a number. We need to check 
    further in the 'config' section to get a better result accuracy"""
    option1 = '-c tessedit_char_whitelist=0123456789 --psm 11 --oem 0'
    option2 = 'tesseract input_file output_file --oem 0 -c tessedit_char_whitelist=0123456789'
    texto = pytesseract.image_to_string(imagen_procesada, lang='eng', config='--psm 8')
    print(texto)


