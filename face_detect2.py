#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 15:40
# @Author  : Roohom
# @Site    : 
# @File    : face_detect2.py
# @Software: PyCharm
import cv2 as cv
camera=cv.VideoCapture(0) #获取摄像头设备
face_cascade=cv.CascadeClassifier(r"D:\opencv-4.3.0\data\haarcascades\haarcascade_lefteye_2splits.xml") #创建人脸级联分类器
eye_cascade=cv.CascadeClassifier(r'D:\opencv-4.3.0\data\haarcascades\haarcascade_lefteye_2splits.xml') #创建人眼级联分类器
cv.namedWindow('face and eye') #创建 一个名字为face and eye 的窗口
while True: #循环读取帧 并且显示在窗口上
    status,img=camera.read() #读取一帧
    grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY) #帧转RGB 灰度图像
    face=face_cascade.detectMultiScale(grey,1.03,4) #找出人脸 返回vector
    for (x,y,w,h) in face: #遍历每张人脸vector
        img=cv.rectangle(img,(x,y),(x+w,y+h),(255,255,255),1) #把人脸周围画白色框
        roi_grey=grey[y:y+h,x:x+w] #将人脸单独提出来
        cv.imwrite('roi_grey.jpg',roi_grey) #写出人脸 测试用
        eye=eye_cascade.detectMultiScale(roi_grey,1.03,5,0,(40,40)) # 从人脸部分遍历人眼
        for (ex,ey,ew,eh) in eye: #画框
            img=cv.rectangle(img,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(0,255,0),1)
    cv.imshow('face and eye',img)#显示
    cv.waitKey(1)#延迟1毫秒 避免卡顿






