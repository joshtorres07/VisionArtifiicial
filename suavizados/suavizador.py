import cv2

import numpy as np
img = cv2.imread("josh.jpg")
kernel = np.ones((3,3), np.float32)/9

im1 = cv2.filter2D(img, -1, kernel)
im2 = cv2.blur(img,(11,11))
im3 = cv2.boxFilter(img,-1,(3,3), normalize=False)
im4 = cv2.GaussianBlur(img,(11,11),0.50)
im5 = cv2.medianBlur(img, 11)
im6 = cv2.bilateralFilter(img, 11, 50, 50)
im7 = img.copy()
im7[30:600, 30:600] = cv2.medianBlur(im7[30:600, 30:600],3)

cv2.imshow("filter2D.jpg", im1)
cv2.imshow("blur.jpg", im2)
cv2.imshow("boxFilter.jpg", im3)
cv2.imshow("GaussianBlur.jpg", im4)
cv2.imshow("medianBlur.jpg", im5)
cv2.imshow("bilateralFilter.jpg", im6)
cv2.imshow("Original", im7[0:700, 30:1600])

cv2.imwrite("filter2D.jpg", im1)
cv2.imwrite("blur.jpg", im2)
cv2.imwrite("boxFilter.jpg", im3)
cv2.imwrite("GaussianBlur.jpg", im4)
cv2.imwrite("medianBlur.jpg", im5)
cv2.imwrite("bilateralFilter.jpg", im6)
cv2.imwrite("Original.jpg", im7[30:600, 30:600])

cv2.waitKey(0)
cv2.destroyAllWindows()