import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)
path = "kelebek.jpg"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBugu = cv2.GaussianBlur(img,(5,5),5)
imgCanny = cv2.Canny(imgBugu,100,100)
imgGen = cv2.dilate(imgCanny,kernel,4)
imgDar = cv2.erode(imgGen,kernel,1)


cv2.imshow("original",img)
cv2.imshow("gray",imgGray)
cv2.imshow("bugulu",imgBugu)
cv2.imshow("canny",imgCanny)
cv2.imshow("genişletilmiş",imgGen)
cv2.imshow("daraltma",imgDar)

cv2.waitKey(0)
cv2.destroyAllWindows()