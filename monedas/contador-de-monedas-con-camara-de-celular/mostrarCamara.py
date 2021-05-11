import cv2 as cv
capturarVideo = cv.VideoCapture(0)
if not capturarVideo.isOpened():
    print("No se encontro una camara")
    exit()

while True:
    tipoCamara, camara = capturarVideo.read()
    gris = cv.cvtColor(camara, cv.COLOR_BGR2GRAY)
    cv.imshow("Video", gris)
    if cv.waitKey(1) == ord("q"):
        break

capturarVideo.release()
cv.destroyAllWindows()
