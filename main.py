# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from serial import Serial
import datetime

if __name__ == '__main__':
    s = Serial(port="/dev/ttyUSB0", baudrate=115200)
    while s.isOpen():
        try:
            print(datetime.datetime.now(), end="\t")
            print(s.readline().decode().splitlines()[0])
        except:
            s.close()
            break
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
