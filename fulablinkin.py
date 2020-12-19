import serial
ser = serial.Serial('/dev/ttyACM0',9600, timeout= 1)

while 1:
    a = int(input('Enter 0 or 1: '))
    print(a)
    if a == 1:
        ser.write(b'1')
        print('LED ON')
    if a == 0:
        ser.write(b'0')
        print('LED OFF')
    #else:
        #print('Input Error!')
