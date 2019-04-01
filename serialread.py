import time
import serial

ser = serial.Serial(
	port='/dev/serial0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
)
counter=0

while 1:
	if(ser.in_waiting > 0):
		x=ser.read(1)
		print(x)
