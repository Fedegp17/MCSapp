import cv2
import pytesseract

"""Created by: Ing. Antonio Gómez Ruiz
01/21/2024 """

"""Overall Notes:
   This code allows the user to segment the image by choosing a rectangle of pixels in the loaded image. Once the
   rectangle has been determined, the program uses number recognition to try to find an integer in the choosen 
   rectangle"""

# Number recognition program - Page segmentation functionality
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


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


def segmentar():
    # Start variables for the height and the width
    """Height - std values w = 30 , x = 50  (chosen by me)"""
    w = 30
    x = 30
    "Width - std values y = 110, z = 100  (chosen by me)"
    y = 200
    z = 130

    """First the program reads the image and shows it to the user """
    img_segmentar = cv2.imread('Imagenes/Monitor.png')
    cuadro_monitor = cv2.rectangle(img_segmentar, (w, x), (y, z), (255, 0, 0), 1)
    cv2.imshow(f"Monitor delimitado", cuadro_monitor)
    cv2.waitKey(0)

    """This part of the code will help the user to delimit the higher segment line"""
    # Configurar altura del marco SUPERIOR
    print("Configuraremos la altura empezando por el MARCO SUPERIOR")
    print("Use la tecla 'W' para mover hacia ARRIBA y la tecla 'S' para mover hacia ABAJO. Al acabar"
          " presione 'ESC' para salir y continuar")
    opcion_segmentar = int(input("¿Desea ajustar la altura? Elija 1 para si o 2 para no\n>>> "))
    if opcion_segmentar == 1:
        flag1 = True
        while flag1:
            cv2.destroyAllWindows()
            img_segmentar = cv2.imread('Imagenes/Monitor.png')
            cuadro_monitor = cv2.rectangle(img_segmentar, (w, x), (y, z), (255, 0, 0), 1)
            cv2.imshow("Monitor delimitado", cuadro_monitor)

            k = cv2.waitKey(0)
            if k == 27:  # Esc key to stop
                flag1 = False
            elif k == 119:  # W key to go up
                x -= 10
            elif k == 115:  # S key to go down
                x += 10
            else:
                pass
    else:
        pass

    # Configurar altura del marco INFERIOR
    print("\nConfiguraremos ahora la altura del MARCO INFERIOR")
    print("Use la tecla 'W' para mover hacia ARRIBA y la tecla 'S' para mover hacia ABAJO. Al acabar"
          " presione 'ESC' para salir y continuar")
    opcion_segmentar = int(input("¿Desea ajustar la altura? Elija 1 para si o 2 para no\n>>> "))
    if opcion_segmentar == 1:
        flag2 = True
        while flag2:

            cv2.destroyAllWindows()
            img_segmentar = cv2.imread('Imagenes/Monitor.png')
            cuadro_monitor = cv2.rectangle(img_segmentar, (w, x), (y, z), (255, 0, 0), 1)
            cv2.imshow("Monitor delimitado", cuadro_monitor)

            k = cv2.waitKey(0)
            if k == 27:  # Esc key to stop
                flag2 = False
            elif k == 119:  # W key to go up
                z -= 10
            elif k == 115:  # S key to go down
                z += 10
            else:
                pass
    else:
        pass

    # Configurar altura del marco IZQUIERDO
    print("\nConfiguraremos ahora la altura del MARCO IZQUIERDO")
    print("Use la tecla 'D' para mover hacia la DERECHA y la tecla 'A' para mover hacia la IZQUIERDA. Al acabar"
          " presione 'ESC' para salir y continuar")
    opcion_segmentar = int(input("¿Desea ajustar la altura? Elija 1 para si o 2 para no\n>>> "))
    if opcion_segmentar == 1:
        flag3 = True
        while flag3:

            cv2.destroyAllWindows()
            img_segmentar = cv2.imread('Imagenes/Monitor.png')
            cuadro_monitor = cv2.rectangle(img_segmentar, (w, x), (y, z), (255, 0, 0), 1)
            cv2.imshow("Monitor delimitado", cuadro_monitor)

            k = cv2.waitKey(0)
            if k == 27:  # Esc key to stop
                flag3 = False
            elif k == 97:  # A key to go Left
                w -= 10
            elif k == 100:  # D key to go Right
                w += 10
            else:
                pass
    else:
        pass

    # Configurar altura del marco DERECHO
    print("\nConfiguraremos ahora la altura del MARCO DERECHO ")
    print("Use la tecla 'D' para mover hacia la DERECHA y la tecla 'A' para mover hacia la IZQUIERDA. Al acabar"
          " presione 'ESC' para salir y continuar")
    opcion_segmentar = int(input("¿Desea ajustar la altura? Elija 1 para si o 2 para no\n>>> "))
    if opcion_segmentar == 1:
        flag4 = True
        while flag4:

            cv2.destroyAllWindows()
            img_segmentar = cv2.imread('Imagenes/Monitor.png')
            cuadro_monitor = cv2.rectangle(img_segmentar, (w, x), (y, z), (255, 0, 0), 1)
            cv2.imshow("Monitor delimitado", cuadro_monitor)

            k = cv2.waitKey(0)
            if k == 27:  # Esc key to stop
                flag4 = False
            elif k == 97:  # A key to go Left
                y -= 10
            elif k == 100:  # D key to go Right
                y += 10
            else:
                pass
    else:
        pass

    img_segmentar = cv2.imread('Imagenes/Monitor.png')
    img_trim = img_segmentar[x: z, w: y]

    """Once the segment is ready we will return it so the program can save it"""
    return img_trim


def principal():
    # First we load an image from our computer
    img_principal = cv2.imread('Imagenes/Monitor.png')
    cv2.imshow("Monitor original", img_principal)
    cv2.waitKey(0)

    """Variables used for the function. The variable 'num_segmentos' is how many segments the user needs, and the 
    variable 'valores_cartesianos' are the coordinates of each segment, for example, coordinates of segment 1, then 
    of segment 2, etc. Once we need to pull all the segments chosen, we will recall each index which will pull the 
    coordinates values"""
    num_segmentos = 0
    contador = 0
    contador2 = 0
    valores_cartesianos = []

    flag6 = True
    while flag6:
        print("Saludos usuario, antes de realizar el reconocimiento de imagen, "
              "por favor escriba el numero de una de las siguientes opciones")
        opcion_prin = int(
            input("1 Realizar solo una segmentación de imagen\n2 Realizar multiples segmentaciones de imagen"
                  "\n>>> "))
        if opcion_prin == 1:
            num_segmentos = 1
            flag6 = False
        elif opcion_prin == 2:
            num_segmentos = int(input("Por favor ingrese el número de segmentaciones para la imagen: "))
            flag6 = False
        else:
            print("Esa no es una opción válida, por favor vuelva a elegir")

    """In this part, the function 'segmentar' will be working until all the segments coordinates had been defined. For 
    example if the user needs 4 segments, the function will execute 4 times."""
    cv2.destroyAllWindows()
    while contador < num_segmentos:
        print("-" * 5 + f" Comenzaremos con el segmento {contador + 1} " + "-" * 5)
        img_temp = segmentar()
        valores_cartesianos.append(img_temp)
        cv2.imshow(f"Monitor cortado {contador + 1}", valores_cartesianos[contador])
        cv2.waitKey()
        contador += 1

    "Once the user has re-sized all of the segments, the program will show all the resulted different segments "
    cv2.destroyAllWindows()
    cv2.imshow("Monitor Médico", img_principal)
    while contador2 < num_segmentos:
        cv2.imshow(f"Monitor cortado {contador2 + 1}", valores_cartesianos[contador2])
        contador2 += 1
    cv2.waitKey(0)


# Code used to allow the user to segment the image to its needs
principal()

cv2.waitKey(0)
cv2.destroyAllWindows()
