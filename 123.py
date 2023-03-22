import cv2


data=open('D:/PY_Project/python_2022_8_3/123.txt','r').readlines()
# print(data)
length =len(data)
i=0
for i in range(length):
    if data[i]=='PFB<D8>\n':
        print(data[i+1].split(' ')[0],end='\n')