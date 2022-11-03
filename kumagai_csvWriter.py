import sys
import time
import msvcrt
import serial
import datetime
import csv
import os

def judge_time_data():
    
    while(True):
        
        try:
            data = float(ser.readline().decode('utf-8').rstrip('\r\n'))
            
            if data > 1000:
                
                return data
            
        except:
            pass

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
    data = 0
    value =[]
    DATA_LENGTH = 15
    count = 0
    ser = serial.Serial(COM,bitRate) #ポートの情報を記入
    
    while(1):
        #キーボード押下時の処理
        if msvcrt.kbhit():
            
            status = msvcrt.getch()
            
            if (status.decode() == 's') or (status.decode() == 'f'):
                status = status.decode()
            
            if status == 's':
                
                now = datetime.datetime.now()
                csvFileName = csv_dir + now.strftime(('%Y%m%d_%H%M%S')) + '_' + sensorPosition + '_' +positionTipes + '_' + roadTipes + '_' + runTimes + '.csv'
                                
                csvf = open(csvFileName, 'w',newline="")
                fwriter = csv.writer(csvf)
                fwriter.writerow(csvColumn)
                
                print('記録中：', csvFileName)
            
            elif status == 'f':
                
                try:
                    csvf.close()
                    print('記録終了')
                except:
                    pass
        
        if status == 'f':
            pass
        
        elif status == 's':
                
            try:
                
                time_data = judge_time_data()
                value.append(time_data)
                
                for data_num in range(DATA_LENGTH-1):
                    value.append(float(ser.readline().decode('utf-8').rstrip('\r\n')))
            
            except:
                print('読み込みエラー')
            
            print(value)
            fwriter.writerow(value)
            value = []