import sys
import serial
import datetime
import csv


COM = "COM6"
bitRate = 115200
valueNum = 23

ser = serial.Serial(COM,bitRate) #ポートの情報を記入
while(1):
    value =[]
    for num in range(0,valueNum):
        num += 1
        value.append(ser.readline().decode('utf-8').rstrip('\n'))
        print(value)
    with open('test.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(value)