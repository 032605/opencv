import cv2

image_path = './src/1.jpg'

# 이미지 읽기
image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

img2 = cv2.rectangle(image, (10,10),(20,20),(255,255,255),2)

cv2.imshow("orignal",image)
cv2.imshow("rectangle", img2)

cv2.waitKey(0)