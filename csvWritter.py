import sys
import time
import serial
import datetime
import csv


COM = "COM6"
positionTipes = 'pTipe1'
roadTipes = 'carpet'
runTimes = '3'
sensorPosition = 'front_R'
bitRate = 115200
valueNum = 15
csvFileName = positionTipes + '_' + roadTipes + '_' + runTimes  +  '_' +  sensorPosition+'.csv'
csvColumn = ['時刻(ms)','相対方位(w)','相対方位(x)','相対方位(y)','相対方位(z)','角速度(x)','角速度(y)','角速度(z)','加速度-重力加速度(x)','加速度-重力加速度(y)','加速度-重力加速度(z)','Sys','Gyro','Accel','Mag']

f = open(csvFileName, 'w',newline="")
writer = csv.writer(f)
writer.writerow(csvColumn)

ser = serial.Serial(COM,bitRate) #ポートの情報を記入
count = 0
loop = 1
while(loop):
    count += 1
    print(count)
    value =[]
    for num in range(0,valueNum):
        num += 1
        value.append(ser.readline().decode('utf-8').rstrip('\n'))
    print(value)
        
    writer.writerow(value)
    if(count > 400000):
        loop = 0
        
f.close()
    