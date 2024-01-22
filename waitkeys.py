import cv2

"""Python script for image segmentation or page segmentation for further OCR-Optic Character Recognition.
   Made by: Ing. Antonio Gómez Ruiz"""

# Variables


# First we load an image from our computer
img = cv2.imread('Monitor.png')


def segmentar():
    flag1 = True

    while flag1:
        cuadrantes = int(input("Por favor declare el número de cuadrantes que va a necesitar: "))
        print(f'Usted ha elejido {cuadrantes} cuadrantes')
        confirmar = int(input("Si está de acuerdo con la cantidad de cuadrantes tecleé 1, si desea cambiar el número "
                              "de cuadrantes tecleé 2: "))
        if confirmar == 1:
            return cuadrantes
        elif confirmar == 2:
            flag1 = True
        else:
            print("Esa no es una opción válida, por favor elija una opción válida")


def cuadros(num_cuadros):
    num_cuadrantes = (num_cuadros)


def main():
    print("Iniciaremos a segmentar la imagen: ")
    # num_cuadrantes = segmentar()
    print('-' * 8)
    bpm_img = img[w: x, y: z]
    print(bpm_img)


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


main()
