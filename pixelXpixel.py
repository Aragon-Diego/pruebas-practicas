import numpy as np
import cv2
import random
m=cv2.imread("01.jpg")
h,w,bpp = np.shape(m)


for py in range(0,h):
    for px in range(0,w):
        if(m[py][px][0] >200):            
            m[py][px][0]=random.randint(0,255)
            m[py][px][1]=random.randint(0,255)
            m[py][px][2]=random.randint(0,255)

cv2.imshow('matrix', m)
cv2.waitKey(0)
cv2.imwrite('yourNewImage.jpg',m)