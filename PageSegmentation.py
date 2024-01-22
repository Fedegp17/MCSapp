import cv2
import pytesseract

# Programa para reconocimiento de números - Versión segmentación
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Start variables for the height and the width
"Height - std values w = 30 , x = 50"
w = 30
x = 30
"Width - std values y = 110, z = 100"
y = 200
z = 130


# Functions used for this code
def identify_number_red(image, config):
    """This will allow us to transform the choosen image to one in a gray scale"""
    imagen_gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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
    texto = pytesseract.image_to_string(imagen_procesada, lang='eng', config=config)
    texto = int(texto)
    return texto


print("Vamos a delimitar el cuadrante\n")
flag_principal = True
while flag_principal:
    # First we load an image from our computer
    img = cv2.imread('Monitor.png')
    cv2.imshow("Monitor original", img)
    cv2.waitKey(0)

    monitor_cuadro = cv2.rectangle(img, (w, x), (y, z), (255, 0, 0), 1)
    cv2.imshow("Monitor delimitado", monitor_cuadro)
    cv2.waitKey(0)

    # Configurar altura del marco SUPERIOR
    print("Configuraremos la altura empezando por el MARCO SUPERIOR")
    opcion = int(input("¿Desea ajustar la altura? Elija 1 para si o 2 para no\n>>> "))
    if opcion == 1:
        flag2 = True
        while flag2:

            cv2.destroyAllWindows()
            img = cv2.imread('Monitor.png')
            monitor_cuadro = cv2.rectangle(img, (w, x), (y, z), (255, 0, 0), 1)
            cv2.imshow("Monitor delimitado", monitor_cuadro)

            k = cv2.waitKey(0)
            if k == 27:  # Esc key to stop
                flag2 = False
            elif k == 119:  # W key to go up
                x -= 10
                monitor_cuadro = cv2.rectangle(img, (w, x), (y, z), (255, 0, 0), 1)
            elif k == 115:  # S key to go down
                x += 10
                monitor_cuadro = cv2.rectangle(img, (w, x), (y, z), (255, 0, 0), 1)
    else:
        pass

    # Configurar altura del marco INFERIOR
    print("\nConfiguraremos ahora la altura del MARCO INFERIOR")
    opcion = int(input("¿Desea ajustar la altura? Elija 1 para si o 2 para no\n>>> "))
    if opcion == 1:
        flag3 = True
        while flag3:

            cv2.destroyAllWindows()
            img = cv2.imread('Monitor.png')
            monitor_cuadro = cv2.rectangle(img, (w, x), (y, z), (255, 0, 0), 1)
            cv2.imshow("Monitor delimitado", monitor_cuadro)

            k = cv2.waitKey(0)
            if k == 27:  # Esc key to stop
                flag3 = False
            elif k == 119:  # W key to go up
                z -= 10
                monitor_cuadro = cv2.rectangle(img, (w, x), (y, z), (255, 0, 0), 1)
            elif k == 115:  # S key to go down
                z += 10
                monitor_cuadro = cv2.rectangle(img, (w, x), (y, z), (255, 0, 0), 1)
    else:
        pass

    # Configurar altura del marco IZQUIERDO
    print("\nConfiguraremos ahora la altura del MARCO IZQUIERDO")
    opcion = int(input("¿Desea ajustar la altura? Elija 1 para si o 2 para no\n>>> "))
    if opcion == 1:
        flag4 = True
        while flag4:

            cv2.destroyAllWindows()
            img = cv2.imread('Monitor.png')
            monitor_cuadro = cv2.rectangle(img, (w, x), (y, z), (255, 0, 0), 1)
            cv2.imshow("Monitor delimitado", monitor_cuadro)

            k = cv2.waitKey(0)
            if k == 27:  # Esc key to stop
                flag4 = False
            elif k == 97:  # A key to go Left
                w -= 10
                monitor_cuadro = cv2.rectangle(img, (w, x), (y, z), (255, 0, 0), 1)
            elif k == 100:  # D key to go Right
                w += 10
                monitor_cuadro = cv2.rectangle(img, (w, x), (y, z), (255, 0, 0), 1)
    else:
        pass

    # Configurar altura del marco DERECHO
    print("\nConfiguraremos ahora la altura del MARCO IZQUIERDO")
    opcion = int(input("¿Desea ajustar la altura? Elija 1 para si o 2 para no\n>>> "))
    if opcion == 1:
        flag5 = True
        while flag5:

            cv2.destroyAllWindows()
            img = cv2.imread('Monitor.png')
            monitor_cuadro = cv2.rectangle(img, (w, x), (y, z), (255, 0, 0), 1)
            cv2.imshow("Monitor delimitado", monitor_cuadro)

            k = cv2.waitKey(0)
            if k == 27:  # Esc key to stop
                flag5 = False
            elif k == 97:  # A key to go Left
                y -= 10
                monitor_cuadro = cv2.rectangle(img, (w, x), (y, z), (255, 0, 0), 1)
            elif k == 100:  # D key to go Right
                y += 10
                monitor_cuadro = cv2.rectangle(img, (w, x), (y, z), (255, 0, 0), 1)
    else:
        pass

    flag_principal = False

img = cv2.imread('Monitor.png')
bpm_img = img[x: z, w: y]
cv2.imshow("BPM Image", bpm_img)
cv2.waitKey(0)

bpm = identify_number_red(bpm_img, '--psm 10')
print(f"\nThe desired integer is: {bpm}")

cv2.waitKey(0)
cv2.destroyAllWindows()
