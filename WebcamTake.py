import cv2

"Takes a picture using the first camera in the list of cameras connected to the computer"
cam = cv2.VideoCapture(0)

"Creates a window named 'test' that shows what the camera is seeing"
cv2.namedWindow("test")

img_counter = 0

while True:
    """The method read uses also 'cv2.VideoCapture', the first variable is 'self' and the second one is the 
    image per se, this is why the second stored variable is 'frame' as it is the image"""
    return_value, frame = cam.read()
    if not return_value:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    """The following code provides the logic to use the 'esc' and 'spacebar' keys to either close the window or 
    take another picture. In case we want to add more keys please refer to:
    'https://stackoverflow.com/questions/14494101/using-other-keys-for-the-waitkey-function-of-opencv'  """
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

"""This method ends ad close the running webcam"""
cam.release()

"""This method close the created window"""
cv2.destroyAllWindows()
