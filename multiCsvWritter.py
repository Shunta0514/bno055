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
bitRate = 921600
valueNum = 15
eightcsvFileName = positionTipes + '_' + roadTipes + '_' + runTimes  +  '_' +  eightsensorPosition+'.csv'
ninecsvFileName = positionTipes + '_' + roadTipes + '_' + runTimes  +  '_' +  ninesensorPosition+'.csv'
csvColumn = ['時刻(ms)','相対方位(w)','相対方位(x)','相対方位(y)','相対方位(z)','角速度(x)','角速度(y)','角速度(z)','加速度-重力加速度(x)','加速度-重力加速度(y)','加速度-重力加速度(z)','Sys','Gyro','Accel','Mag']

Eif = open(eightcsvFileName, 'w',newline="")
Eifwriter = csv.writer(Eif)
Eifwriter.writerow(csvColumn)
        
Nif = open(ninecsvFileName, 'w',newline="")
Nifwriter = csv.writer(Nif)
Nifwriter.writerow(csvColumn)


ser = serial.Serial(COM,bitRate) #ポートの情報を記入
count = 0
loop = 1
while(loop):
    count += 1
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
    Eifwriter.writerow(eightvalue)
    Nifwriter.writerow(ninevalue)
    
    if(count == 1000):
        loop = 0

Eif.close()
Nif.close()