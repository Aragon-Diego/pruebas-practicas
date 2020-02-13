import numpy as np
import cv2

img = np.zeros([500,500,3])

img[:,:,0] = np.ones([500,500])*32/255.0
img[:,:,1] = np.ones([500,500])*157/255.0
img[:,:,2] = np.ones([500,500])*255/255.0

cv2.imwrite('color_img.jpg', img)
cv2.imshow("image", img);
cv2.waitKey();