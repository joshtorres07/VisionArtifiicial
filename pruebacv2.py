import cv2
import numpy as np

h = 400
w = 600
im1 = np.ones((h,w),np.uint8) * 255
im2 = np.ones((h,w),np.uint8)
im3 = np.random.random((h,w))
im4 = np.random.randint(0,255,(h,w),np.uint8)
im5 = np.random.randint(0,255,(h,w,3),np.uint8)
im6 = np.random.random((h,w,3))

cv2.imshow("im1",im1)
cv2.imshow("im2",im2)
cv2.imshow("im3",im3)
cv2.imshow("im4",im4)
cv2.imshow("im5",im5)
cv2.imshow("im6",im6)

cv2.waitKey(0)
cv2.destroyAllWindows()