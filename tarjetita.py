import cv2

#leer imagen del poster
img = cv2.imread("poster.jpg")
#mostrar la imagen
cv2.imshow("Mostar imagen",img )



cv2.waitKey(0)
