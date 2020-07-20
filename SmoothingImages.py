# Importing cv2 module
import cv2

img = cv2.imread('image1.jpg')

# blur
blurImg = cv2.blur(img,(10,10))
cv2.imshow('blurred image',blurImg)
cv2.waitKey(0)


# Averaging
avging = cv2.blur(img,(10,10))
cv2.imshow('Averaging',avging)
cv2.waitKey(0)

# Gaussian Blurring
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gausBlur = cv2.GaussianBlur(gray, (5,5),0)
cv2.imshow('Gaussian Blurring', gausBlur)
cv2.waitKey(0)

# Median blurring
medBlur = cv2.medianBlur(img,5)
cv2.imshow('Media Blurring', medBlur)
cv2.waitKey(0)

# Bilateral Filtering
bilFilter = cv2.bilateralFilter(img,9,75,75)
cv2.imshow('Bilateral Filtering', bilFilter)
cv2.waitKey(0)
cv2.destroyAllWindows()
