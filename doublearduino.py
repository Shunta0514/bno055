import sys
import time
import serial
import datetime
import csv

comOne = "COM5"
comTWO = "COM6"
positionTipes = 'pTipe1'
roadTipes = 'carpet'
runTimes = '1'
sensorPositionONE = 'frontR'
sensorPositionTWO = 'backL'
bitRate = 115200
valueNum = 15
fileNameONE = positionTipes + '_' + roadTipes + '_' + runTimes  +  '_' +  sensorPositionONE+'.csv'
fileNameTWO = positionTipes + '_' + roadTipes + '_' + runTimes  +  '_' +  sensorPositionTWO+'.csv'
csvColumn = ['時刻(ms)','相対方位(w)','相対方位(x)','相対方位(y)','相対方位(z)','角速度(x)','角速度(y)','角速度(z)','加速度-重力加速度(x)','加速度-重力加速度(y)','加速度-重力加速度(z)','Sys','Gyro','Accel','Mag']

fileONE = open(fileNameONE, 'w',newline="")
writerONE = csv.writer(fileONE)
writerONE.writerow(csvColumn)
        
fileTWO = open(fileNameTWO, 'w',newline="")
writerTWO = csv.writer(fileTWO)
writerTWO.writerow(csvColumn)


serONE = serial.Serial(comOne,bitRate) #ポートの情報を記入
serTWO = serial.Serial(comTWO,bitRate)

count = 0
loop = 1
while(loop):
    count += 1
    valueONE =[]
    valueTWO = []
    for num in range(0,valueNum):
        num += 1
        valueONE.append(serONE.readline().decode('utf-8').rstrip('\n'))
        valueTWO.append(serTWO.readline().decode('utf-8').rstrip('\n'))
    print(valueONE)
    print(valueTWO)
    writerONE.writerow(valueONE)
    writerTWO.writerow(valueTWO)
    
    if(count == 1000):
        loop = 0

fileONE.close()
fileTWO.close()