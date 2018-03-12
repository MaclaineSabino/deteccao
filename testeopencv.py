import cv2


imagem = cv2.imread("opencv-python.jpg")
imagemCinza =cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
cv2.imshow("original",imagem)
cv2.imshow("cinza",imagemCinza)
cv2.waitKey()