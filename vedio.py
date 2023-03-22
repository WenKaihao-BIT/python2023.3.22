import cv2
import numpy as np
img_path ='D:/WEN\data/2023-3-3/test.png'
img = cv2.imread(img_path)
cv2.imshow('myPicture',img)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",img_gray)
_, binary = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)
binary_G = cv2.GaussianBlur(binary, (11, 11), 15)
cv2.imshow("binary_G",binary_G)
# edges = cv2.Canny(binary_G,100, 150)
# cv2.imshow("edges",edges)
# minLineLength = 50  # 最低线段的长度，小于这个值的线段被抛弃
# maxLineGap = 10  # 线段中点与点之间连接起来的最大距离，在此范围内才被认为是单行
# lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi / 180, threshold=20, minLineLength=minLineLength, maxLineGap=maxLineGap)


# 获取轮廓  cv2.RETR_EXTERNAL   cv2.RETR_TREE
binary,contours,hierarchy=cv2.findContours(binary_G,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
# 画出轮廓
draw_img=img.copy()
# cv2.drawContours(draw_img,contours,-1,(0, 0, 255), -1)

for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)  # 求轮廓的面积，得到第几个轮廓的面积
    # print(area)
    if area>5000:
        cv2.drawContours(draw_img, contours, i, (0, 0, 255), -1)
        M = cv2.moments(contours[i])  # 求矩
        cx = int(M['m10'] / M['m00'])  # 求x坐标
        cy = int(M['m01'] / M['m00'])  # 求y坐标
        print(cx,cy)
        draw_img = cv2.circle(draw_img, (cx, cy), 2, (0, 255, 0), 4)  # 画出重心

imgs=np.hstack([img,draw_img])
cv2.imshow('imgs',imgs)

# for i in range(len(lines)):
#     x_1, y_1, x_2, y_2 = lines[i][0]
#     cv2.line(img, (x_1, y_1), (x_2, y_2), (0, 255, 0), 2)
# cv2.imshow('result',img)
cv2.waitKey()
cv2.destroyWindow('myPicture')


