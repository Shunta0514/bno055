import sys
import time
import serial
import datetime
import csv

def getdata(valueNum):
    value =[]
    for num in range(0,valueNum):
        num += 1
        value.append(ser.readline().decode('utf-8').rstrip('\n'))
    return value

COM = "COM6"
positionTipes = 'pTipe1'
roadTipes = 'carpet'
runTimes = '1'
sensorPosition1 = 'frontR'
sensorPosition2 = 'frontL'
bitRate = 115200
valueNum = 24
csvFileName1 = positionTipes + '_' + roadTipes + '_' + runTimes  +  '_' +  sensorPosition1+'.csv'
csvFileName2 = positionTipes + '_' + roadTipes + '_' + runTimes  +  '_' +  sensorPosition2+'.csv'
csvColumn = ['時刻(μs)','絶対方位(x)','絶対方位(y)','絶対方位(z)','角速度(x)','角速度(y)','角速度(z)','加速度-重力加速度(x)','加速度-重力加速度(y)','加速度-重力加速度(z)','磁場強度(x)','磁場強度(y)','磁場強度(z)','加速度(x)','加速度(y)','加速度(z)','重力加速度(x)','重力加速度(y)','重力加速度(z)','温度(℃)','Sys','Gyro','Accel','Mag']

with open(csvFileName1, 'w',newline="") as f:
        writer = csv.writer(f)
        writer.writerow(csvColumn)
with open(csvFileName2, 'w',newline="") as f:
        writer = csv.writer(f)
        writer.writerow(csvColumn)

ser = serial.Serial(COM,bitRate) #ポートの情報を記入

while(1):
    value1 = getdata(valueNum)
    value2 = getdata(valueNum)
    with open(csvFileName1, 'a',newline="") as f:
        writer = csv.writer(f)
        writer.writerow(value1)
    with open(csvFileName2, 'a',newline="") as f:
        writer = csv.writer(f)
        writer.writerow(value2)