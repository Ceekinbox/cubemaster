import serial
import time
import serial.tools.list_ports
import threading
import kociemba


class serialMain:
    def __init__(self):
        self.ser = None
        self.msg = b''
        self.last_msg = b''

    def search(self):
        ports = list(serial.tools.list_ports.comports(include_links=False))
        for port in ports:
            print(port)
        return ports

    def init(self, port, baudrate=115200, bytesize=8, parity='N', stopbits=1):
        self.ser = serial.Serial(port=port, baudrate=baudrate, bytesize=bytesize, parity=parity,stopbits=stopbits, timeout=1, rtscts=False)

    def close(self):
        self.ser.close()

    def open(self):
        if not self.isOpen():
            self.ser.open()
        self.ser.open()
        print("{} is opened.".format(self.ser.port))

    def isOpen(self):
        if self.ser.isOpen():
            print("{} is already opened.".format(self.ser.port))
        return self.ser.isOpen()

    def write_str(self, str0):
        str1 = bytes(str0, encoding="utf-8")
        send_len = self.ser.write(str1)
        return send_len

    def write_data(self, str0):
        str00 = str0 + '\x0d\x0a'
        return self.write_str(str00)


    def read(self):
        while True:
            read_msg = self.ser.read(1)
            if read_msg == b'\r':
                read_msg = self.ser.read(1)
                if read_msg == b'\n':
                    print('read_msg: {}'.format(self.msg))
                else:
                    print('read msg error!')
            else:
                self.msg = self.msg + read_msg

            time.sleep(0.0001)

#    def serial_creat_thread(self):
#        thread_read = threading.Thread(target=self.serial_read, daemon=True)
#        thread_read.start()
# print('thread created')


# 下面实现了一个简易的字符分析器，可将F F’ F2 转换成单个字母
# 调用SolveTrainslate 参数为源字符串
# 注意！ 源字符串必须为kociemba.solve()输出的，每步之间有空格分隔的格式，否则输出为空！！
# 注意！ 源字符串必须为kociemba.solve()输出的，每步之间有空格分隔的格式，否则输出为空！！
# 注意！ 源字符串必须为kociemba.solve()输出的，每步之间有空格分隔的格式，否则输出为空！！

theTransDict = {"F'": "Q", "F2": "W", "F": "F",
                "L'": "E", "L2": "T", "L": "L",
                "U'": "Y", "U2": "I", "U": "U",
                "D'": "O", "D2": "P", "D": "D",
                "B'": "A", "B2": "S", "B": "B",
                "R'": "G", "R2": "H", "R": "R"}
def isLetter(src):
    return src.isalpha()

def isNumber(src):
    if src == "'":
        return True
    else:
        return src.isdigit()

def isSpace(src):
    return src == ' '
def SolveTranslate(src):
    dst = ""
    temp = ""
    src += " "
    for s in src:
        if isLetter(s):
            temp += s
        elif isSpace(s):
            if temp != "":
                dst += theTransDict[temp]
                temp = ""
            continue
        elif isNumber(s):
            temp += s
    return dst


if __name__ == "__main__":
    a = 0
#   example:
#   usart1 = serialMain()
#   usart1.serial_init("COM1")
#   usart1.serial_start()
#   usart1.serial_write_data("Hello world!")
#   usart1.serial_close()

