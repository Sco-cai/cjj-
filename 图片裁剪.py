# 帅到包
# 开发时间:2022-06-08  9:02
# Importing the cv2 library
import cv2
img=cv2.imread('0000.JPG')


cropped_image = img[0:760, 256:956] # Slicing to crop the image

# Display the cropped image
cv2.imshow("cropped", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
