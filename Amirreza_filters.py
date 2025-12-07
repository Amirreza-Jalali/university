import cv2 as cv
import numpy as np


img = cv.imread('/Users/apple/Desktop/images/BikesHelmets100.png')


mask1 = np.array(
   [[0 , -1, 0],
    [-1 , 4, -1],
    [0 , -1, 0]])

mask2 = np.array(
   [[-3 , 3, -3],
    [3  , 3,   3],
    [-3 , 3, -3]])

mask3 = np.array(
   [[-1 , 1, -1],
    [1 , 1, 1],
    [-1 , 1, -1]])

mask4 = np.array(
   [[-1 , -1, -1],
    [-1 , -1, -1],
    [-1 , -1, -1]])/-9


new_img1 = cv.filter2D(img, -1, mask1)
new_img2 = cv.filter2D(img, -1, mask2)
new_img3 = cv.filter2D(img, -1, mask3)
new_img4 = cv.filter2D(img, -1, mask4)


cv.imshow('original',img)
cv.imshow('img1',new_img1)
cv.imshow('img2',new_img2)
cv.imshow('img3',new_img3)
cv.imshow('img4',new_img4)



cv.waitKey(0)
cv.destroyAllWindows()