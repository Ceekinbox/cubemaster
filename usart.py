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
if __name__ == "__main__":
    a = 0
    x = kociemba.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')
    print(type(x))
    print(x)
#   example:
#   usart1 = serialMain()
#   usart1.serial_init("COM1")
#   usart1.serial_start()
#   usart1.serial_write_data("Hello world!")
#   usart1.serial_close()

