import numpy as np
import cv2

white = np.ones([150,200,1],'uint8')
white =  white *  ( 2**8 - 1 )
cv2.imshow("White",white)

cv2.waitKey(0)

cv2.destroyAllWindows()