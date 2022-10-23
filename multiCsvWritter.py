import sys
import time
import serial
import datetime
import csv


COM = "COM6"
positionTipes = 'pTipe1'
roadTipes = 'carpet'
runTimes = '1'
eightsensorPosition = 'frontR'
ninesensorPosition = 'backL'
bitRate = 115200
valueNum = 15
eightcsvFileName = positionTipes + '_' + roadTipes + '_' + runTimes  +  '_' +  eightsensorPosition+'.csv'
ninecsvFileName = positionTipes + '_' + roadTipes + '_' + runTimes  +  '_' +  ninesensorPosition+'.csv'
csvColumn = ['時刻(μs)','相対方位(w)','相対方位(x)','相対方位(y)','相対方位(z)','角速度(x)','角速度(y)','角速度(z)','加速度-重力加速度(x)','加速度-重力加速度(y)','加速度-重力加速度(z)','Sys','Gyro','Accel','Mag']

with open(eightcsvFileName, 'w',newline="") as f:
        writer = csv.writer(f)
        writer.writerow(csvColumn)
        
with open(ninecsvFileName, 'w',newline="") as f:
        writer = csv.writer(f)
        writer.writerow(csvColumn)


ser = serial.Serial(COM,bitRate) #ポートの情報を記入

while(1):
    eightvalue =[]
    ninevalue = []
    for num in range(0,valueNum):
        num += 1
        eightvalue.append(ser.readline().decode('utf-8').rstrip('\n'))
        print(eightvalue)
    for num in range(0,valueNum):
        num += 1
        ninevalue.append(ser.readline().decode('utf-8').rstrip('\n'))
        print(ninevalue)
    with open(eightcsvFileName, 'a',newline="") as f:
        writer = csv.writer(f)
        writer.writerow(eightvalue)
    with open(ninecsvFileName, 'a',newline="") as f:
        writer = csv.writer(f)
        writer.writerow(ninevalue)