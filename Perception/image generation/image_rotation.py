# import required libraries
import cv2

# load the input image
img = cv2.imread('/home/santo/Project/dataset/1.jpg')

# rotate the image by 180 degree clockwise
img_cw_180 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# display the rotated image
cv2.imshow("Image rotated by 90 degree", img_cw_180)
cv2.waitKey(0)
cv2.destroyAllWindows()