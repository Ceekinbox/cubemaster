# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import cv2
import kociemba as koci
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QTimer
import sys
import ui

#           +--------+
#           |U1 U2 U3|
#           |U4 U5 U6|
#           |U7 U8 U9|
#  +--------+--------+--------+--------+
#  |L1 L2 L3|F1 F2 F3|R1 R2 R3|B1 B2 B3|
#  |L4 L5 L6|F4 F5 F6|R4 R5 R6|B4 B5 B6|
#  |L7 L8 L9|F7 F8 F9|R7 R8 R9|B7 B8 B9|
#  +--------+--------+--------+--------+
#           |D1 D2 D3|
#           |D4 D5 D6|
#           |D7 D8 D9|
#           +--------+

#           U*9 R*9 F*9 D*9 L*9 B*9

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

    print(koci.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD'))

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi("hi")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


    # 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
