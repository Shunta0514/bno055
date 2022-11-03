import sys
import time
import serial
import datetime
import csv
import os



COM = "COM6"
positionTipes = 'pTipe1'
roadTipes = 'carpet'
runTimes = '5'
Position = ['frontR','backL','frontL','backR','handle']
bitRate = 921600
valueNum = 15
csvFileName=[]
test_dir = './sensor_test/'
os.makedirs(test_dir, exist_ok=True)
for n in range(0,5):
    csvFileName.append(test_dir + positionTipes + '_' + roadTipes + '_' + runTimes  +  '_' + Position[n]+'.csv')
csvColumn = ['時刻(ms)','相対方位(w)','相対方位(x)','相対方位(y)','相対方位(z)','角速度(x)','角速度(y)','角速度(z)','加速度-重力加速度(x)','加速度-重力加速度(y)','加速度-重力加速度(z)','Sys','Gyro','Accel','Mag']
f0= open(csvFileName[0], 'w',newline="")
f0writer = csv.writer(f0)
f0writer.writerow(csvColumn)

f1= open(csvFileName[1], 'w',newline="")
f1writer = csv.writer(f1)
f1writer.writerow(csvColumn)

f2= open(csvFileName[2], 'w',newline="")
f2writer = csv.writer(f2)
f2writer.writerow(csvColumn)

f3= open(csvFileName[3], 'w',newline="")
f3writer = csv.writer(f3)
f3writer.writerow(csvColumn)

f4= open(csvFileName[4], 'w',newline="")
f4writer = csv.writer(f4)
f4writer.writerow(csvColumn)
 


ser = serial.Serial(COM,bitRate) #ポートの情報を記入
count = 0
loop = 1
while(loop):
    count += 1
    value0 =[]
    value1 = []
    value2 = []
    value3 = []
    value4 = []
    for num in range(0,valueNum):
        num += 1
        value0.append(ser.readline().decode('utf-8').rstrip('\n'))
    print(value0)
    
    for num in range(0,valueNum):
        num += 1
        value1.append(ser.readline().decode('utf-8').rstrip('\n'))
    print(value1)
    
    for num in range(0,valueNum):
        num += 1
        value2.append(ser.readline().decode('utf-8').rstrip('\n'))
    print(value2)
    
    for num in range(0,valueNum):
        num += 1
        value3.append(ser.readline().decode('utf-8').rstrip('\n'))
    print(value3)
    for num in range(0,valueNum):
        num += 1
        value4.append(ser.readline().decode('utf-8').rstrip('\n'))
    print(value4)
    f0writer.writerow(value0)
    f1writer.writerow(value1)
    f2writer.writerow(value2)
    f3writer.writerow(value3)
    f4writer.writerow(value4)
    
    if(count == 1000000):
        loop = 0

f0.close()
f1.close()
f2.close()
f3.close()
f4.close()