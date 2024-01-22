import cv2
import pytesseract
import matplotlib

"""Created by: Ing. Antonio Gómez Ruiz
01/16/2024 """

"""Overall notes of the program:

How to take a picture using the webcam of the computer:
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)


Problems to use Pytesseract please refer to:
'https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i'


With this we can now the widht and heigh of the image after the image has been read
        rows, cols, _ = imagen.shape
        print(f'Los pixeles de filas son {rows} y de las columnas son {cols}')
After running this code, we now know that the image is 411 x 500 pxls


The 'PSM' is the page segmentation Modes of the Tesseract that can help us improve the accuracy of the OCR, please
refer to: 
https://pyimagesearch.com/2021/11/15/tesseract-page-segmentation-modes-psms-explained-how-to-improve-your-ocr-accuracy/
"""

# Programa para reconocimiento de números - Versión monitor médico
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Functions developed for this program
# This function should be used when trying to delete the red area of an image
def identify_number_red(img, x):
    """This will allow us to transform the choosen image to one in a gray scale"""
    imagen_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('imagen gris', imagen_gris)
    # cv2.waitKey(0)

    """Thresholding == 'umbral' o 'umbralización'
    The function threshold returns a tuple, and the funtion 'cv2.imshow' only shows 'arrays', therefore this is 
    solved by adding the '[1]' at the end of the method 'threshold'. In case further doubts show up, print the variable 
    type"""
    imagen_procesada = cv2.threshold(imagen_gris, 140, 255, cv2.THRESH_BINARY)[1]
    # cv2.imshow('imagen procesada', imagen_procesada)
    # cv2.waitKey(0)

    """With this section we use pytesseract to analyze the processed image and detect a number. We need to check 
    further in the 'config' section to get a better result accuracy depending on individual cases"""
    option1 = '-c tessedit_char_whitelist=0123456789 --psm 11 --oem 0'
    option2 = 'tesseract input_file output_file --oem 0 -c tessedit_char_whitelist=0123456789'
    texto = pytesseract.image_to_string(imagen_procesada, lang='eng', config=x)
    texto = int(texto)
    return texto


# This function should be used when trying to delete the blue area of an image
def identify_number_blue(img, x, y):
    """This will allow us to transform the choosen image to one in a gray scale"""
    imagen_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('imagen gris', imagen_gris)
    cv2.waitKey(0)

    """Thresholding == 'umbral' o 'umbralización'
    The function threshold returns a tuple, and the funtion 'cv2.imshow' only shows 'arrays', therefore this is 
    solved by adding the '[1]' at the end of the method 'threshold'. In case further doubts show up, print the variable 
    type"""
    """This values will retrieve only the 'red' area and delete the blue one"""
    imagen_procesada = cv2.threshold(imagen_gris, y, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('imagen procesada', imagen_procesada)
    cv2.waitKey(0)

    """With this section we use pytesseract to analyze the processed image and detect a number. We need to check 
    further in the 'config' section to get a better result accuracy depending on individual cases"""
    option1 = '-c tessedit_char_whitelist=0123456789 --psm 11 --oem 0'
    option2 = 'tesseract input_file output_file --oem 0 -c tessedit_char_whitelist=0123456789'
    texto = pytesseract.image_to_string(imagen_procesada, lang='eng', config=x)
    texto = int(texto)
    return texto


# This function should be used when trying to delete the yellow area of an image
def identify_number_yellow(img, x):
    """This will allow us to transform the choosen image to one in a gray scale"""
    imagen_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('imagen gris', imagen_gris)
    cv2.waitKey(0)

    """Thresholding == 'umbral' o 'umbralización'
    The function threshold returns a tuple, and the funtion 'cv2.imshow' only shows 'arrays', therefore this is 
    solved by adding the '[1]' at the end of the method 'threshold'. In case further doubts show up, print the variable 
    type"""
    """This values will retrieve only the 'red' area and delete the blue one"""
    imagen_procesada = cv2.threshold(imagen_gris, 130, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('imagen procesada', imagen_procesada)
    cv2.waitKey(0)

    """With this section we use pytesseract to analyze the processed image and detect a number. We need to check 
    further in the 'config' section to get a better result accuracy depending on individual cases"""
    option1 = '-c tessedit_char_whitelist=0123456789 --psm 11 --oem 0'
    option2 = 'tesseract input_file output_file --oem 0 -c tessedit_char_whitelist=0123456789'
    texto = pytesseract.image_to_string(imagen_procesada, lang='eng', config=x)
    texto = int(texto)
    return texto


"First we load the desired image"
imagen = cv2.imread('Monitor.png')

"""This will show in  window the image that we choose"""
cv2.imshow('imagen', imagen)
cv2.waitKey(0)

# Code used to ROI an image (select a Region Of Interest, or chop it)
"""As a reference 'imagen[height start: height end, width start, width end]"""
bpm_img = imagen[50: 100, 30: 110]
spo2_img = imagen[105: 150, 30: 110]
resp_img = imagen[155: 200, 30: 110]
pressure_systolic_img = imagen[205: 240, 20: 100]
pressure_diastolic_img = imagen[205: 240, 120: 170]
"""Important note; it is not possible to have the same window name on 2 windows"""
cv2.imshow("imgen cortada 1", bpm_img)
# cv2.imshow("imgen cortada 2", spo2_img)
# cv2.imshow("imgen cortada 3", resp_img)
# cv2.imshow("imgen cortada 4", pressure1_img)
# cv2.imshow("imgen cortada 5", pressure2_img)
# cv2.waitKey(0)

"""Call the functions to identify the numbers in the images and store them in variables"""
bpm = identify_number_red(bpm_img, '--psm 10')
spo2 = identify_number_red(spo2_img, '--psm 10')
resp = identify_number_red(resp_img, '--psm 10')
pressure_systolic = identify_number_red(pressure_systolic_img, '--psm 10')
pressure_diastolic = identify_number_red(pressure_diastolic_img, '--psm 10')

print(f'The Heart Rate is {bpm}\nThe SPO2 is {spo2}\nThe respiration per minute is {resp}\nThe '
      f'pressure is {pressure_systolic}/{pressure_diastolic}')

cv2.waitKey(0)
cv2.destroyAllWindows()
