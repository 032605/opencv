import cv2

image_path = './src/1.jpg'

# 이미지 읽기
image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
cv2.imshow("title",image)
cv2.waitKey(0)