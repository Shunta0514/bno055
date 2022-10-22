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
csvColumn = ['時刻(μs)','相対方位(w)','相対方位(x)','相対方位(y)','相対方位(z)','角速度(x)','角速度(y)','角速度(z)','加速度-重力加速度(x)','加速度-重力加速度(y)','加速度-重力加速度(z)','磁場強度(x)','磁場強度(y)','磁場強度(z)','加速度(x)','加速度(y)','加速度(z)','重力加速度(x)','重力加速度(y)','重力加速度(z)','Sys','Gyro','Accel','Mag']

with open(csvFileName, 'w',newline="") as f:
        writer = csv.writer(f)
        writer.writerow(csvColumn)

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