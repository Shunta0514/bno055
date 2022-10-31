import sys
import time
import msvcrt
import serial
import datetime
import csv
import os

if __name__ == '__main__':
    COM = "COM6"
    positionTipes = 'pTipe1'
    roadTipes = 'carpet'
    runTimes = '3'
    sensorPosition = 'front_R'
    bitRate = 115200
    valueNum = 15
    csvColumn = ['時刻(ms)','相対方位(w)','相対方位(x)','相対方位(y)','相対方位(z)','角速度(x)','角速度(y)','角速度(z)','加速度-重力加速度(x)','加速度-重力加速度(y)','加速度-重力加速度(z)','Sys','Gyro','Accel','Mag']
    csv_dir = './imu_raw_data/'
    os.makedirs(csv_dir, exist_ok=True)

    status = 'f'
    start_record = False
    data = 0
    value =[]
    count = 0
    ser = serial.Serial(COM,bitRate) #ポートの情報を記入

    
    while(1):
        #キーボード押下時の処理
        if msvcrt.kbhit():
            
            status = msvcrt.getch()
            status = status.decode()
            
            if status == 's':
                
                start_record = True
                
                now = datetime.datetime.now()
                csvFileName = csv_dir + now.strftime(('%Y%m%d_%H%M%S')) + '_' + sensorPosition + '_' +positionTipes + '_' + roadTipes + '_' + runTimes + '.csv'
                                
                csvf = open(csvFileName, 'w',newline="")
                fwriter = csv.writer(csvf)
                fwriter.writerow(csvColumn)
                
                print('記録開始')
            
            elif status == 'f':
                
                try:
                    csvf.close()
                    print('記録終了')
                except:
                    pass
        
        if status == 'f':
            pass
        
        elif status == 's':
            
            if start_record:
                empty = ser.readline()
                print("処理を開始")
                time.sleep(10)
                print("10秒待機しました。")
                start_record = False
                judge_record = False
                while(True):
                    data = float(ser.readline().decode('utf-8').rstrip('\n'))
                    print('data'+ str(data))
                    if float(data) > 1000:
                        judge_record = True
                    if judge_record:
                        for cnt in range(0,4):
                            ser.readline().decode('utf-8').rstrip('\n')
                        break
                      
            
            for data in range(0,valueNum):
                #print(ser.readline().decode('utf-8').rstrip('\n'))
                #if ser.readline().decode('utf-8').rstrip('\n') == '':
                    #value.append('NUN')
                    #pass
                #else:
                value.append(float(ser.readline().decode('utf-8').rstrip('\n')))
                count += 1
                print(value)
    
                
            fwriter.writerow(value)
            #初期化
            value = [] 
            
    
        