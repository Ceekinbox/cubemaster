
import cv2
import threading
import sys
import time
import multiprocessing as mprssing
import numpy as np


def getContours(img, dst):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 检测外部轮廓
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 300:
            print(">300")
            cv2.drawContours(dst, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)  # xy对象的宽和高
    return x + w // 2, y


def findColors(image, myColors):
    myColors = [[2, 107, 0, 19, 255, 255],
                [133, 56, 0, 159, 156, 255],
                [57, 76, 0, 100, 255, 255]]  # 颜色列表
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])  # 下限
        upper = np.array(color[3:6])  # 上限
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask, image)
        cv2.circle(image, (x, y), 10, (255, 0, 0), cv2.FILLED)
        mask = cv2.inRange(imgHSV, lower, upper)

    return 0


def findColor(image, color):
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array(color[0:3])
    upper = np.array(color[3:6])
    mask = cv2.inRange(imgHSV, lower, upper)
    cv2.imshow("dst", mask)
    return mask

def cubeAffine(image, num):
    """
    功能描述：
    接口：image 输入的图片  num 为摄像头的位置 1就是只能拍一个面的摄像头 2就是两个面
        return dst 结果 为正方形
    修改记录：2023-4-2   创建函数
    """
    dst = 0
    return dst

if __name__ == "__main__":
    print("hi")
