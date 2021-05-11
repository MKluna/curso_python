import cv2
import numpy as np

valorGauss = 3
valorKernel = 3

original = cv2.imread('monedas/contador-de-monedas/Monedas_arboles2.jpg')
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
gaus = cv2.GaussianBlur(gris, (valorGauss, valorGauss), 0)
canny = cv2.Canny(gaus, 60, 100)
kernel = np.ones((valorKernel, valorKernel), np.uint8)
cierre = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
contorno, jerarquia = cv2.findContours(
    cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(original, contorno, -1, (0, 0, 255), 2)

# Mostrar
cv2.imshow('imagen', original)
cv2.waitKey(0)
cv2.destroyAllWindows()
