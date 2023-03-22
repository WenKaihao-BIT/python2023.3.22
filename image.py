import cv2



img=cv2.imread("img_2.png",0)
blur = cv2.GaussianBlur(img,(11,11),2)

canny = cv2.Canny(img, 150, 230)  # 调用Canny函数，指定最大和最小阈值，其中apertureSize默认为3。
cv2.imshow('Canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()