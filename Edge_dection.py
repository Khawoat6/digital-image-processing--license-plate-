import cv2
import numpy as np

img = cv2.imread("image1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Appy Gaussian blur to remove some noises
inoise = cv2.GaussianBlur(gray,(3,3),sigmaX=0)


#Canny edge detection
lowThresh = 50
upThresh = 100
out = cv2.Canny(inoise,lowThresh,upThresh)

'''
#Gradient X
gradX = cv2.Sobel(inoise,cv2.CV_16S,dx=1,dy=0)
#Gradient Y
gradY = cv2.Sobel(inoise,cv2.CV_16S,dx=0,dy=1)
#Convert Gradients to 8 bits
gradX = cv2.convertScaleAbs(gradX)
gradY = cv2.convertScaleAbs(gradY)
#Total Gradient (approximate)
#grad = abs(gradX) + abs(gradY)
out = cv2.addWeighted(gradX,1,gradY,1,0)


out = cv2.Laplacian(inoise,ddepth=cv2.CV_16S,ksize=3)
#Need to set depth to 16-bit signed integer because Laplacian can give negative intensity.
# Convert it to 8-bit image with absolute value.
out = cv2.convertScaleAbs(out)
'''


cv2.imshow("Origin",img)
cv2.imshow("Edge Detection - Laplacian",out)
cv2.waitKey()
cv2.destroyAllWindows()
