import cv2
classificador = cv2.CascadeClassifier('cascades\haarcascade_frontalface_default.xml') #cria um classificador

imagem = cv2.imread('pessoas\\pessoas1.jpg') #leitura da imagem
imagemCinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY) # transforma a imagem em cinza

facesDetectadas = classificador.detectMultiScale(imagemCinza) #chama o classificador e a variável guarda as faces detectadas
print(len(facesDetectadas)) # facesDectadas e uma matriz, no print ele está informando o tamanho dessa matriz

print(facesDetectadas) # na saída, temos na primeira linha posição X 93 posição Y 71, largura 100 e altura 100

for (x,y,l,a) in facesDetectadas: #vai percorrer a matriz pegandos os valores x,y,largura e altura

    print(x,y,l,a)
    cv2.rectangle(imagem,(x,y),(x+l,y+a),(0,0,255),2)#passa a imagem original, as cordenadas do início da detecção,a criação
    #das linhas acrescentando ao inicio da detecção a largura e altura, depois a cor do retangulo e o tamanho da borda

cv2.imshow("ImagemComFaces",imagem)
cv2.waitKey()



