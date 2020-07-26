import numpy as np
import cv2

white = np.ones([150,200,3],'uint8')
white =  white *  ( 2**8 - 1 )

blue = white.copy()
blue[:,:]= (255,0,0)
cv2.imshow("Blue",blue)

cv2.waitKey(0)

cv2.destroyAllWindows()