import cv2
import numpy as np
cd=cv2.imread('cog.jpeg')
hsv=cv2.cvtColor(cd,cv2.COLOR_BGR2HSV)

lower_range=np.array([0,70,50])
upper_range=np.array([10,255,255])

mask=cv2.inRange(hsv,lower_range,upper_range)
cv2.imwrite('mask.jpeg',mask)