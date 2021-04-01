import cv2
import urllib3
import json
import base64

openApiURL = "http://aiopen.etri.re.kr:8000/FaceDeID"
accessKey = "2ce78d65-5d6b-4f40-ae0a-9c0e1b0112cb"
type = "1";     # 얼굴 비식별화 기능 "1"로 설정

image_path = './src/1.jpg'

file = open(image_path, "rb")
imageContents = base64.b64encode(file.read()).decode("utf8")
file.close()

requestJson = {
	"access_key": accessKey,
	"argument": {
		"type": type,
		"file": imageContents
	}
}

http = urllib3.PoolManager()
response = http.request(
	"POST",
	openApiURL,
	headers={"Content-Type": "application/json; charset=UTF-8"},
	body=json.dumps(requestJson)
)

# 이미지 읽기
image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

img2 = cv2.rectangle(image, (10,10),(20,20),(255,255,255),2)

cv2.imshow("orignal",image)
cv2.imshow("rectangle", img2)

cv2.waitKey(0)

print("[responseCode] " + str(response.status))
print("[responBody]")
print(response.data)