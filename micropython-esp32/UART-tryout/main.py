from machine import UART

uart2 = UART(2, tx=17, rx=16)
uart2.init(115200, bits=8, parity=None, stop=1)
uart2.read(10)       # read 10 characters, returns a bytes object
uart2.read()         # read all available characters
uart2.readline()     # read a line
uart2.readinto(buf)  # read and store into the given buffer
uart2.write('abc')   # write the 3 characters
