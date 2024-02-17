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

NOTE: Monzon´s webcam is 480x640

The 'PSM' is the page segmentation Modes of the Tesseract that can help us improve the accuracy of the OCR, please
refer to: 
https://pyimagesearch.com/2021/11/15/tesseract-page-segmentation-modes-psms-explained-how-to-improve-your-ocr-accuracy/
"""

# OCR program focused in recognition of numbers in a medical monitor
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


def identify_number2(img, x):
    """This will allow us to transform the choosen image to one in a gray scale"""
    imagen_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('imagen gris', imagen_gris)
    cv2.waitKey(0)

    """Thresholding == 'umbral' o 'umbralización'
    The function threshold returns a tuple, and the funtion 'cv2.imshow' only shows 'arrays', therefore this is 
    solved by adding the '[1]' at the end of the method 'threshold'. In case further doubts show up, print the variable 
    type"""
    imagen_procesada = cv2.threshold(imagen_gris, 220, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('imagen procesada', imagen_procesada)
    cv2.waitKey(0)

    """With this section we use pytesseract to analyze the processed image and detect a number. We need to check 
    further in the 'config' section to get a better result accuracy depending on individual cases"""
    option1 = '-c tessedit_char_whitelist=0123456789 --psm 11 --oem 0'
    option2 = 'tesseract input_file output_file --oem 0 -c tessedit_char_whitelist=0123456789'
    texto = pytesseract.image_to_string(imagen_procesada, lang='eng', config=x)
    texto = int(texto)
    return texto


"""First we load the desired image
imagen = cv2.imread('Imagenes/opencv_frame_0.png') """

"""Unlike the other scripts, this time we will be using the webcam to take pictures"""
cam = cv2.VideoCapture(0)

bandera_principal = True
while bandera_principal:

    """This will show in  window the image that we choose, and first we need to make sure that the webcam is sending
    an image"""
    return_value, frame = cam.read()
    if not return_value:
        print("failed to grab frame")
        bandera_principal = False

    bandera_secundaria = True

    """Once the webcam is sending an image, we will start the loop where it will be doing the number recognition"""
    cv2.imshow('imagen de la webcam', frame)
    print("Esta es la imagen actual captada por la webcam, presione cualquier tecla para iniciar el reconocimiento")
    cv2.waitKey(0)

    while bandera_secundaria:

        return_value, frame = cam.read()
        if not return_value:
            print("failed to grab frame")
            bandera_principal = False
            bandera_secundaria = False

        try:
            # Code used to ROI an image (select a Region Of Interest, or chop it)
            """As a reference 'imagen[height start: height end, width start, width end]"""
            bpm_img = frame[50: 100, 400: 465]
            spo2_img = frame[105: 160, 405: 465]
            resp_img = frame[160: 215, 405: 465]
            pressure_systolic_img = frame[210: 240, 140: 170]
            pressure_diastolic_img = frame[210: 240, 172: 205]
            """Important note; it is not possible to have the same window name on 2 windows"""
            # cv2.imshow("imgen cortada 1", bpm_img)
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
                  f'pressure is {pressure_systolic}/{pressure_diastolic}\n---------------\n')

        except:
            print("Error, no se pudo reconocer el número, intentando de nuevo")
