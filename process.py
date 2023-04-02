import cv2
import threading
import sys
import time
import multiprocessing as mprssing
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 检测外部轮廓
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(type(area))
        if area > 300:
            print(">300")
            # cv2.drawContours(dst, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)  # xy对象的宽和高
    return x + w // 2, y


def findColors(image, myColors):
    """
    功能描述： 不要用这个函数，会产生错误的输出
    接口：不要用这个函数，会产生错误的输出
    修改记录：不要用这个函数，会产生错误的输出
    """
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

    mask = cv2.GaussianBlur(mask, (3, 3), 0)
    cv2.imshow("dst", mask)
    getContours(mask)
    return mask

def colorComposition():
    """
    功能描述： 输入一张图片 ，将六种色块重新染色后叠加显示
    接口：image 输入的图片
        return dst
    修改记录：2023-4-2   创建函数
    """

def darwRect(image, num):
    """
    功能描述： 画一个或两个四边形，标定魔方位置
    接口：image 输入的图片  num 为摄像头的位置 1就是只能拍一个面的摄像头 2就是两个面
        return dst
    修改记录：2023-4-2   创建函数
    """
    if num == 1:
        zero = image.shape[0:2]
        zero = [x / 2 for x in zero]
        length = 100
        x1, y1 = int(zero[1] - length), int(zero[0] - length)
        x2, y2 = int(zero[1] + length), int(zero[0] + length)
        image = cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 1)
        image = cv2.circle(image, (x1, y1), 2, (0, 255, 0), 1)
        image = cv2.circle(image, (x2, y1), 2, (0, 0, 255), 1)
        image = cv2.circle(image, (x1, y2), 2, (0, 255, 255), 1)
        dst = image
    else:
        dst = image
    return dst


def cubeAffine(image, num):
    """
    功能描述：根据输入的图片进行仿射变换
    接口：image 输入的图片  num 为摄像头的位置 1就是只能拍一个面的摄像头 2就是两个面
        return dst 结果 为正方形
    修改记录：2023-4-2   创建函数
    """
    #  1--2 [[1], [2],
    #  |  |  [3], [4]]
    #  3--4
    # 变换矩阵四点规律
    arraySrc = np.array([
        [92, 44], [292, 44],
        [92, 244], [292, 244]
    ], dtype="float32")
    arrayDst = np.array([
        [0, 0], [200, 0],
        [0, 200], [200, 200]
    ], dtype="float32")
    MP = cv2.getPerspectiveTransform(arraySrc, arrayDst)  # 计算投影变换矩阵 M
    warped = cv2.warpPerspective(image, MP, (200, 200))
    cv2.imshow("dst", warped)
    dst = warped
    return dst


if __name__ == "__main__":
    a = 0
