import sys
import time
import serial
import datetime
import csv


COM = "COM6"
positionTipes = 'pTipe1'
roadTipes = 'carpet'
runTimes = '1'
sensorPosition = 'frontR'
bitRate = 115200
valueNum = 24
csvFileName = positionTipes + '_' + roadTipes + '_' + runTimes  +  '_' +  sensorPosition+'.csv'

ser = serial.Serial(COM,bitRate) #ポートの情報を記入

while(1):
    value =[]
    for num in range(0,valueNum):
        num += 1
        value.append(ser.readline().decode('utf-8').rstrip('\n'))
        print(value)
    with open(csvFileName, 'a',newline="") as f:
        writer = csv.writer(f)
        writer.writerow(value)