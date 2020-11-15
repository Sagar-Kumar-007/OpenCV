import cv2
import numpy as np
img=cv2.imread('red.jpg')
dim=img.shape
img=cv2.resize(img,(int(img.shape[0]*0.3),int(img.shape[1]*0.1)))
pt1=np.float32([[10,10],[50,10],[10,50]])
pt2=np.float32([[210,10],[250,10],[210,50]])
pt3=np.float32([[210,110],[250,110],[210,150]])
M=cv2.getAffineTransform(pt1,pt2)
M_y=cv2.getAffineTransform(pt2,pt3)
new=cv2.warpAffine(img,M,(dim[0],dim[1]))
new_y=cv2.warpAffine(new,M_y,(dim[0],dim[1]))
cv2.imshow("Window",new_y)
cv2.waitKey(0)
cv2.destroyAllWindows()