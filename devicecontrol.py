import serial
#ser = serial.Serial('/dev/ttyACM0',9600, timeout= 1)
ser = serial.Serial('/dev/ttyACM0',115200, timeout= 1)
while 1:
#To display options
    print('-------MENU------\n------Fan Options ------\n 1 for PW_On \n 0 PW_off, \n 2 Speed \n------TV options-------- \n 3 PW_On/Off \n 4 CH_Up \n 5 CH_Dwn \n 6 VOL_up \n 7 VOL_Dwn\n------------------------\n')
    a = int(input('Enter 1 (Power ON) or 0 (Power OFF): '))
    print(a)
    if a == 1:
        ser.write(b'1')
        print('FAN ON')
    if a == 0:
        ser.write(b'0')
        print('FAN OFF')
    if a == 2:
        ser.write(b'2')
        print('Fan Speed Changed')
    if a == 0:
        ser.write(b'3')
        print('TV ON/OFF')
    if a == 1:
        ser.write(b'4')
        print('TV CH_UP')
    if a == 0:
        ser.write(b'5')
        print('TV CH_DWN')
    if a == 1:
        ser.write(b'6')
        print('TV VOL_UP')
    if a == 0:
        ser.write(b'7')
        print('TV VOL_DWN')
    #else:
        #print('Input Error!')
