import time
import serial


ser = serial.Serial(
    port='/dev/serial0',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
counter=0


while 1:
    	ser.write(b'%d' % (counter++))
        time.sleep(0.05)