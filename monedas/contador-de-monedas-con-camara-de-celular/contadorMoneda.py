import cv2 as cv
import numpy as np


def ordernarPuntos(puntos):
    n_puntos = np.concatenate([
        puntos[0], puntos[1], puntos[2], puntos[3]]).tolist()
    y_order = sorted(n_puntos, key=lambda n_puntos: n_puntos[1])
    x_order = y_order[:2]
    x_order = sorted(x_order, key=lambda x_order: [0])
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key=lambda x2_order: x2_order[0])
    return[x_order[0], x_order[1], x2_order[0], x2_order[1]]


def alineamiento(imagen, alto, ancho):
    imagen_alineada = None
    gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    tipoUmbral, umbral = cv.threshold(gris, 100, 255, cv.THRESH_BINARY)
    cv.imshow("Umbral", umbral)
    contorno = cv.findContours(
        umbral, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contorno = sorted(contorno, key=cv.contourArea, reverse=True)[:1]
    for i in contorno:
        epsilon = 0.01 * cv.arcLength(i, True)
        aprox = cv.approxPolyDP(i, epsilon, True)
        if len(aprox) == 4:
            puntos = ordernarPuntos(aprox)
            puntos1 = np.float32(puntos)
            puntos2 = np.float32(
                [[0, 0], [ancho, 0], [0, alto], [ancho, alto]])
            M = cv.getPerspectiveTransform(puntos1, puntos2)
            imagen_alineada = cv.warpPerspective(imagen, M, (ancho, alto))
    return imagen_alineada


capturaVideo = cv.VideoCapture(0)
while True:
    tipoCamara, camara = capturaVideo.read()
    if tipoCamara == False:
        break
    imagen_A6 = alineamiento(camara, ancho=480, alto=677)
    if imagen_A6 is not None:
        puntos = []
        imagenGris = cv.cvtColor(imagen_A6, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(imagenGris, (5, 5), 1)
        _, umbral2 = cv.threshold(
            blur, 0, 255, cv.THRESH_OTSU+cv.THRESH_BINARY_INV)
        cv.imshow("umbral 2", umbral2)
        contorno2 = cv.findContours(
            umbral2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
        cv.drawContours(imagen_A6, contorno2, -1, (255, 0, 0), 2)
        suma1 = 0.0
        suma2 = 0.0
        for c_2 in contorno2:
            area = cv.contourArea(c_2)
            momentos = cv.moments(c_2)
            if (momentos["m00"] == 0):
                momentos["m00"] = 1.0
            x = int(momentos["m10"]/momentos["m00"])
            y = int(momentos["m01"]/momentos["m00"])
            if area < 9300 and area > 8000:
                font = cv.FONT_HERSHEY_SIMPLEX
                cv.putText(imagen_A6, "S/. 0.20", (x, y),
                           font, 0.75, (0, 255, 0), 2)
                suma1 = suma1+0.2
            if area < 7800 and area > 6500:
                font = cv.FONT_HERSHEY_SIMPLEX
                cv.putText(imagen_A6, "S/. 0.10", (x, y),
                           font, 0.75, (0, 255, 0), 2)
                suma2 = suma2+0.1
        total = suma1+suma2
        print("Sumatoria total en Centimos:", round(total, 2))
        cv.imshow("Imagen A6", imagen_A6)
        cv.imshow("camara", camara)
    if cv.waitKey(1) == ord('s'):
        break
capturaVideo.release()
cv.destroyAllWindows()
