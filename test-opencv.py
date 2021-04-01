import cv2
import urllib3
import json
import base64

openApiURL = "http://aiopen.etri.re.kr:8000/FaceDeID"
accessKey = "2ce78d65-5d6b-4f40-ae0a-9c0e1b0112cb"
type = "1";     # 얼굴 비식별화 기능 "1"로 설정

image_path = "./src/6.jpg"

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

content = json.loads(response.data)

# 이미지 읽기
img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

for i in range(0,len(content["return_object"]["faces"])):
    img_x = int(content["return_object"]["faces"][i]["x"])
    img_y = int(content["return_object"]["faces"][i]["y"])
    img_width = int(content["return_object"]["faces"][i]["width"])
    img_height = int(content["return_object"]["faces"][i]["height"])
    text = str(img_x) + "," + str(img_y)
    # 검출된 객체 사각형 그리기 
    cv2.rectangle(img, (img_x,img_y),(img_x+img_width,img_y+img_height),(255,255,255),4)
    # 사각형 위에 텍스트 붙이기
    cv2.putText(img, text, (img_x, img_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
    # 크롭 이미지 저장
    image_crop = img[img_y : img_y + img_height, img_x : img_x + img_width]
    cv2.imwrite('./crop.jpg', image_crop)
    
    
    #cv2.putText(img, text,(img_x,img_y -10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255))
	# 사각형 위에 텍스트 붙이기
 	#cv2.putText(img, text,(img_x,img_y -10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
	# 크롭 이미지 저장
	#cropped_img = img[img_y: img_y + img_height, img_x : img_x + img_width ]
	#cv2.imwrite('./cropped_img.jpg',cropped_img)


# 구하는 방법
#cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)


cv2.imshow("rectangle", img)
cv2.waitKey(0)

# json 객체로 반환
#print("[responseCode] " + str(response.status))
#print("[responBody]")
#print(response.data)
